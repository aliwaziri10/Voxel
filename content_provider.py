#!/usr/bin/env python3
"""
content_provider.py - single shared entry point for all LLM-based content
generation across Voxel. Every script that needs an outline (slide deck),
a manuscript (page-by-page book), or a novel chapter calls into this
module instead of rolling its own HTTP call + JSON parsing.

This is Phase 1 of ARCHITECTURE.md: removing duplicated content-generation
code from make_lesson.py, build_book.py, and generate_images.py.

Phase 8 addendum (one-command publishing pipeline, see HANDOFF.md):
added generate_novel_chapter() and call_raw() for prose-chapter generation
(novels aren't a fixed-field JSON list like picture-book pages), used by
voxel_cli.py and humanizer.py.

Phase 8b addendum: added direct NVIDIA API support as an alternative to
OpenRouter. If NVIDIA_API_KEY is set, it's used (direct NVIDIA NIM
endpoint, no OpenRouter middleman/rate limits). Otherwise falls back to
OPENROUTER_API_KEY exactly as before - existing workflows/notebooks that
only set OPENROUTER_API_KEY keep working unchanged.

Phase 9 addendum: added generate_beat_map(), a chapter-by-chapter outline
generated ONCE up front for a novel, before any prose is written. Fixes
the "loses the plot over 45 chapters" gap - previously each chapter only
got the same top-level brief plus "continue naturally from last chapter",
with nothing tracking where the plot needs to go next. See story_bible.py
for where the beat map is stored and voxel_cli.py cmd_novel for how it's
used.

2026-09-19 fix (superseded same day, see next entry): first attempt added
a bare min/max word target to generate_novel_chapter()'s prompt, and
voxel_cli.py paired it with a retry loop that told the model to "expand"
a short chapter. That retry-and-expand approach is padding by another
name and directly violates novels/EDITORIAL_CHARTER.md's no-padding rule
("never inflate a one-beat chapter to hit a word target") - it was
reverted the same session before ever being run against a real book.

2026-09-19 fix (corrected): the charter's actual answer to short/thin
chapters is upstream, not downstream - plan 2-4 real sub-beats per
chapter BEFORE drafting (see the charter's "sub-beat planning method",
added 2026-09-16), not stretch a thin draft after the fact. generate_
beat_map() now asks for a list of typed sub-beats per chapter instead of
one flat "beat" string, and generate_novel_chapter() states the floor
honestly (no fake "hard requirement" language) while explicitly warning
against padding. This also moved the default word range from an
invented 2000-2300 to the charter's actual Book-4-onward standard,
2300-2700 - the earlier default didn't match the one real standing
number in the repo. Per the charter, none of this is retroactive to
Book 2 or Book 3, which are locked and done.

2026-09-20 fix: generate_beat_map() used to raise immediately if the
model's returned chapter count didn't exactly match what was asked for -
confirmed live against a real 60-chapter Book 4 run, where the model
returned 59 entries and the whole run died on one missing chapter after
successfully planning the other 59. This is a mechanical/structural
retry (getting an array to the right length), not a creative-content
retry like the reverted word-count "expand" loop above - it does not
touch prose or padding, so it does not conflict with the charter's
no-padding rule. generate_beat_map() now retries up to 2 additional
times, telling the model exactly how many chapters it returned last
time and how many are required, before giving up.

2026-09-20 fix: a live Book 4 run crashed on chapter 2's humanizer pass
with a bare `KeyError: 'choices'` out of _post() - the HTTP call returned
2xx but the JSON body had no "choices" key. _post() now checks for that
and raises/retries with the provider's real message instead of a bare
KeyError. CONFIRMED live on the next run: the provider body was
{'message': 'Upstream error from Nvidia: Service temporarily
overloaded', 'code': 503, 'metadata': {'error_type':
'provider_overloaded'}}.

2026-09-20 fix (this change): the same live run then died at chapter 13
with `429 Client Error: Too Many Requests` from OpenRouter. The earlier
retry only covered the "200 with no choices" case; a real HTTP 429 (or
5xx, timeout, or dropped connection) went straight through
raise_for_status() and killed the run. _post() now retries ALL of those,
waiting the provider's Retry-After time when it sends one and otherwise
backing off 60s, 120s, 180s... up to 300s, for up to _MAX_ATTEMPTS
tries. It also prints the provider's actual response text, so the real
reason is visible next time. Second problem found in the same run:
chapter 6 was saved at 467 words, cut off mid-sentence. A model reply
that stops because it hit its length limit (finish_reason "length") is
now treated as a failed call and retried, and if it is still cut off on
the last attempt the call raises instead of quietly returning half a
chapter. All of this is mechanical HTTP-level handling. It never touches
prose, word counts, or padding, so it does not conflict with the
charter's no-padding rule.

2026-09-20 fix (multi-key rotation): OpenRouter's free tier caps each
account/key at roughly 50 requests/day, which a single 45-chapter novel
run can exceed on its own (beat map + 2 calls/chapter + humanizer). Zia
can create multiple free OpenRouter accounts, each with its own key.
_post() now tries an ordered list of providers - NVIDIA direct first (no
daily cap, if NVIDIA_API_KEY is set), then OPENROUTER_API_KEY,
OPENROUTER_API_KEY_2, OPENROUTER_API_KEY_3, and so on for however many
are set as env vars/secrets (no fixed limit - it reads them in order
until a number is missing). An HTTP 429 (quota/rate exceeded) now moves
immediately to the next provider in the list instead of sleeping and
retrying the SAME key - waiting does not fix a daily quota. The chosen
provider is remembered (module-level) for the rest of this process, so
later calls in the same run do not keep re-trying an already-exhausted
key from the top. A 5xx/timeout/"200 with no choices"/cut-off reply is
still retried on the SAME provider first (these usually recover), and
only counts as that provider failing once its own retries are used up.
If every provider in the list is exhausted, the run raises a clear error
naming how many providers were tried, instead of hanging on a single
key's backoff for minutes with no path to success.
"""

import os
import json
import time

import requests


NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "")

# Direct NVIDIA NIM endpoint (build.nvidia.com), OpenAI-compatible.
# NVIDIA_MODEL can be overridden via env var if this default is renamed/
# retired - check https://build.nvidia.com for the current model catalog
# and matching model id if generation starts failing with a 404.
NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
NVIDIA_MODEL = os.environ.get("NVIDIA_MODEL", "nvidia/llama-3.1-nemotron-70b-instruct")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"


def _load_openrouter_keys():
    """Reads OPENROUTER_API_KEY, then OPENROUTER_API_KEY_2, _3, _4... in
    order, stopping at the first one that is not set. Each is a separate
    free OpenRouter account/key, each with its own ~50-requests/day cap -
    see the 2026-09-20 multi-key rotation note in the module docstring.
    No fixed maximum: add OPENROUTER_API_KEY_6, _7, etc. as env vars/
    secrets and they are picked up automatically, no code change needed."""
    keys = []
    primary = os.environ.get("OPENROUTER_API_KEY", "")
    if primary:
        keys.append(primary)
    i = 2
    while True:
        key = os.environ.get(f"OPENROUTER_API_KEY_{i}", "")
        if not key:
            break
        keys.append(key)
        i += 1
    return keys


OPENROUTER_API_KEYS = _load_openrouter_keys()
# Kept for backward compatibility with any other module that reads this
# name directly; OPENROUTER_API_KEYS (the full list) is what _post() uses.
OPENROUTER_API_KEY = OPENROUTER_API_KEYS[0] if OPENROUTER_API_KEYS else ""


def _build_providers():
    """Ordered provider list: NVIDIA direct first (if set - no daily cap),
    then one entry per OpenRouter key found, in the order they were set.
    _post() walks this list, moving to the next entry whenever one hits
    HTTP 429 (its rate/quota limit) instead of waiting on it."""
    providers = []
    if NVIDIA_API_KEY:
        providers.append({
            "label": "NVIDIA direct", "url": NVIDIA_URL,
            "model": NVIDIA_MODEL, "key": NVIDIA_API_KEY,
        })
    for i, key in enumerate(OPENROUTER_API_KEYS, start=1):
        providers.append({
            "label": f"OpenRouter key {i}", "url": OPENROUTER_URL,
            "model": OPENROUTER_MODEL, "key": key,
        })
    return providers


_PROVIDERS = _build_providers()
# Which provider _post() starts from. Sticky across calls within one run
# (one `python voxel_cli.py ...` process) so that once a key is found to
# be exhausted, later chapters in the same run do not waste a call
# re-trying it from the top - they pick up from the last provider that
# actually worked.
_active_provider_index = 0

# Retry policy for TRANSIENT failures on the current provider (momentary
# unavailability, dropped connections, replies cut off by the length
# limit, a "200 with no choices" body) - see 2026-09-20 fix notes above.
# A 429 (rate/quota exceeded) does NOT use this - see _post(): it moves
# to the next provider immediately instead, since waiting does not fix a
# daily quota. Not used for anything that would touch prose content or
# chapter length.
_MAX_ATTEMPTS = 4
_RETRY_BACKOFF_SECONDS = 5           # for "200 with no choices" and cut-off replies
_RATE_LIMIT_BACKOFF_SECONDS = 30     # for 5xx / timeouts, multiplied by attempt
_RATE_LIMIT_MAX_WAIT_SECONDS = 120   # never wait longer than this between tries on ONE provider
_SERVER_ERROR_STATUS_CODES = (500, 502, 503, 504)


def _require_key():
    if not _PROVIDERS:
        raise RuntimeError(
            "No LLM API key is set. Set at least one of these before running:\n"
            "  NVIDIA_API_KEY                 (direct, no daily cap)\n"
            "  OPENROUTER_API_KEY             (free tier, ~50 requests/day)\n"
            "  OPENROUTER_API_KEY_2, _3, ...  (extra free OpenRouter accounts - "
            "tried in order once an earlier one hits its daily cap)"
        )


def _wait_seconds_for(response, attempt):
    """How long to wait before retrying a 5xx/timeout on the SAME
    provider: the provider's own Retry-After header if it sent a usable
    one, else 30s x attempt, capped at 120s."""
    if response is not None:
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                return min(max(int(float(retry_after)), 1), _RATE_LIMIT_MAX_WAIT_SECONDS)
            except ValueError:
                pass
    return min(_RATE_LIMIT_BACKOFF_SECONDS * attempt, _RATE_LIMIT_MAX_WAIT_SECONDS)


def _post(system_prompt, user_content, timeout):
    """Tries each provider in _PROVIDERS, starting at _active_provider_index.
    On a given provider: network errors, 5xx, a cut-off ("length")
    reply, and a 200-with-no-"choices" body are retried on THAT SAME
    provider up to _MAX_ATTEMPTS times (these are usually transient and
    a different key would not help). An HTTP 429 (that provider's own
    rate/quota limit) or a non-2xx that isn't a 5xx (e.g. a bad/expired
    key) moves immediately to the NEXT provider instead - no point
    waiting on a quota that will not reset for hours. Once a provider
    succeeds, _active_provider_index is left there for future calls in
    this run. Raises only once every provider in the list has failed."""
    global _active_provider_index
    _require_key()
    provider_count = len(_PROVIDERS)

    last_error = None
    for providers_tried in range(provider_count):
        provider = _PROVIDERS[_active_provider_index]
        url, model, key, label = (provider["url"], provider["model"],
                                   provider["key"], provider["label"])

        provider_failed = False
        for attempt in range(1, _MAX_ATTEMPTS + 1):
            is_last_attempt_on_provider = attempt == _MAX_ATTEMPTS

            try:
                response = requests.post(
                    url,
                    headers={
                        "Authorization": f"Bearer {key}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": model,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_content},
                        ],
                    },
                    timeout=timeout,
                )
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                last_error = f"{label}: {type(e).__name__}: {e}"
                wait = _wait_seconds_for(None, attempt)
                print(f"[content_provider] {label}, attempt {attempt}/{_MAX_ATTEMPTS}: "
                      f"network problem ({last_error}). "
                      + ("Moving to next provider." if is_last_attempt_on_provider
                         else f"Waiting {wait}s, then retrying same provider..."))
                if is_last_attempt_on_provider:
                    provider_failed = True
                    break
                time.sleep(wait)
                continue

            if response.status_code == 429:
                # This provider's own rate/quota limit. Waiting minutes
                # does not fix a daily cap - switch keys now.
                last_error = f"{label}: HTTP 429 (rate/quota exceeded): {response.text[:200]}"
                print(f"[content_provider] {label} hit its rate limit (429). "
                      "Switching to the next provider...")
                provider_failed = True
                break

            if response.status_code in _SERVER_ERROR_STATUS_CODES:
                last_error = f"{label}: HTTP {response.status_code}: {response.text[:300]}"
                wait = _wait_seconds_for(response, attempt)
                print(f"[content_provider] {label}, attempt {attempt}/{_MAX_ATTEMPTS}: {last_error} "
                      + ("Moving to next provider." if is_last_attempt_on_provider
                         else f"Waiting {wait}s, then retrying same provider..."))
                if is_last_attempt_on_provider:
                    provider_failed = True
                    break
                time.sleep(wait)
                continue

            if not response.ok:
                # A non-2xx that isn't 429/5xx - typically a bad/expired
                # key or a malformed request on THIS provider. Don't burn
                # retries on it; just move to the next provider.
                last_error = (f"{label}: HTTP {response.status_code} for {url}. "
                               f"Response text: {response.text[:500]}")
                print(f"[content_provider] {label}: {last_error} Moving to next provider.")
                provider_failed = True
                break

            body = response.json()

            if "choices" in body and body["choices"]:
                choice = body["choices"][0]
                text = ((choice.get("message") or {}).get("content") or "").strip()
                finish_reason = choice.get("finish_reason")

                if finish_reason == "length":
                    # The model ran out of room and stopped mid-sentence. A
                    # half chapter must never be saved as a finished one.
                    last_error = f"{label}: reply was cut off by the length limit (finish_reason 'length')"
                    print(f"[content_provider] {label}, attempt {attempt}/{_MAX_ATTEMPTS}: {last_error}. "
                          + ("Moving to next provider." if is_last_attempt_on_provider else "Retrying same provider..."))
                    if is_last_attempt_on_provider:
                        provider_failed = True
                        break
                    time.sleep(_RETRY_BACKOFF_SECONDS * attempt)
                    continue

                if finish_reason not in (None, "stop"):
                    print(f"[content_provider] NOTE: {label} finish_reason was '{finish_reason}' (not 'stop').")
                return text

            # Some providers (notably OpenRouter free-tier models under
            # rate limiting or transient unavailability) return HTTP 200
            # with an error payload instead of a completion. Surface the
            # real message and retry on the SAME provider first.
            error_detail = body.get("error", body)
            last_error = f"{label}: {error_detail}"
            print(
                f"[content_provider] {label}, attempt {attempt}/{_MAX_ATTEMPTS}: provider "
                f"returned 200 with no 'choices' key. Error detail: {error_detail} "
                + ("Moving to next provider." if is_last_attempt_on_provider else "Retrying same provider...")
            )
            if is_last_attempt_on_provider:
                provider_failed = True
                break
            time.sleep(_RETRY_BACKOFF_SECONDS * attempt)

        if provider_failed:
            _active_provider_index = (_active_provider_index + 1) % provider_count
            if providers_tried < provider_count - 1:
                print(f"[content_provider] Now trying: {_PROVIDERS[_active_provider_index]['label']} "
                      f"({providers_tried + 2}/{provider_count})...")

    raise RuntimeError(
        f"All {provider_count} provider(s)/key(s) failed. Last error: {last_error}"
    )


def _call_nemotron(system_prompt, user_content, timeout=120):
    raw_text = _post(system_prompt, user_content, timeout)

    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")
        if raw_text.lower().startswith("json"):
            raw_text = raw_text[4:].strip()

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise RuntimeError(
            f"Model did not return valid JSON. Raw response was:\n{raw_text}"
        ) from e


def call_raw(system_prompt, user_content, timeout=120):
    """
    Plain-text (non-JSON) LLM call. Exposed for humanizer.rewrite_pass and
    generate_novel_chapter, which need free-form prose back, not a JSON
    object.
    """
    return _post(system_prompt, user_content, timeout)


def generate_outline(topic):
    """
    Slide-deck outline for make_lesson.py / generate_images.py.
    Returns a list of slide dicts: title, body, narration, mood, image_prompt.
    """
    system_prompt = (
        "You are a lesson-deck writer. Given a topic, produce a JSON array "
        "of 6-10 slide objects for a classroom teaching deck. Return ONLY "
        "valid JSON, no markdown fences, no preamble. Each object must have "
        "exactly these keys:\n"
        '  "title": short slide title (few words)\n'
        '  "body": array of 2-5 short bullet point strings for the slide\n'
        '  "narration": 1-3 sentences the teacher/narrator would say aloud '
        "for this slide, plain spoken language\n"
        '  "mood": one or two words describing the background music mood '
        '(e.g. "calm focused", "upbeat playful", "serious neutral")\n'
        '  "image_prompt": a short visual description (5-15 words) of what '
        "should be illustrated for this slide, concrete and specific, "
        "no abstract concepts - describe an actual scene or object\n"
        "The first slide should be a title/intro slide. The last slide should "
        "be a short recap/summary slide."
    )
    return _call_nemotron(system_prompt, f"Topic: {topic}")


def generate_manuscript(concept, page_count, continuity_block=""):
    """
    Page-by-page book manuscript for build_book.py.
    Returns a list of page dicts: page_number, text, image_prompt.

    continuity_block: optional text from story_bible.continuity_prompt_block()
    to keep a sequel's characters/style/plot consistent with prior books.
    """
    system_prompt = (
        f"You are a children's book author and illustrator's art director. "
        f"Given a book concept, produce a JSON array of exactly {page_count} "
        f"page objects. Return ONLY valid JSON, no markdown fences, no "
        f"preamble. Each object must have exactly these keys:\n"
        '  "page_number": integer, 1-indexed\n'
        '  "text": the text for this page (can be an empty string for '
        "pages meant to be pure illustration, e.g. coloring book pages)\n"
        '  "image_prompt": a concrete, specific visual description '
        "(10-25 words) of the illustration for this page - describe an "
        "actual scene, character pose, or object, not an abstract idea\n"
        "If the concept describes a coloring book, text should be empty "
        "or a very short caption, and image_prompt should describe a "
        "clean line-art scene suitable for coloring. If it's a story, "
        "text should carry the narrative forward page by page and "
        "image_prompt should illustrate that page's specific moment. "
        "Avoid AI-writing tells: no rule-of-three lists, no stock phrases, "
        "vary sentence length naturally, write like a human author."
    )
    user_content = f"Book concept: {concept}"
    if continuity_block:
        user_content = f"{continuity_block}\n\n{user_content}"
    return _call_nemotron(system_prompt, user_content, timeout=180)


# Sub-beat types from novels/EDITORIAL_CHARTER.md's "sub-beat planning
# method" (added 2026-09-16). A well-built chapter draws on 2-4 of these,
# not just the first - this is what a chapter's real content should be
# built from, instead of stretching one thin plot event to hit a length.
SUB_BEAT_TYPES = [
    "plot_beat",           # the thing the chapter exists to do
    "relationship_micro_beat",  # something shifts between two characters
    "interior_beat",       # POV character learns/admits something about themselves
    "stakes_beat",         # the ticking clock/danger gets more concrete
    "callback_beat",       # a small, earned connection to earlier chapters/voice
]


def generate_beat_map(book, chapter_count, brief, continuity_block=""):
    """
    Phase 9. Generates the FULL chapter-by-chapter outline for a novel in
    one call, before any prose is written. This is what keeps a 45-chapter
    novel from losing the plot: instead of each chapter only knowing "the
    overall brief" plus "what came directly before", every chapter is
    handed its own specific outline from a plan written with the whole
    book in view up front.

    2026-09-19: each chapter's outline is now a list of 2-4 typed
    sub-beats (see SUB_BEAT_TYPES / EDITORIAL_CHARTER.md), not one flat
    "beat" string. This is the actual fix for chapters reading thin or
    needing padding: a chapter drafted from one plot event only ever
    has one plot event's worth of real content. A chapter drafted from
    2-4 genuine sub-beats has real material to reach a natural length
    without stretching sentences. The charter is explicit that a
    genuinely one-beat chapter should just stay short rather than be
    inflated - this function's instruction reflects that: sub-beats must
    be genuine and chapter-specific, never invented filler to hit a
    count.

    2026-09-20: retries up to 2 additional times if the model returns the
    wrong number of chapter entries (confirmed live: a 60-chapter request
    once came back with 59). This is a structural retry only - it asks
    the model to correct an array length, never to pad or alter chapter
    content, so it does not conflict with the charter's no-padding rule.

    Returns a list of exactly `chapter_count` dicts:
      {"chapter": int, "sub_beats": [{"type": str, "detail": str}, ...]}
    "type" is one of SUB_BEAT_TYPES. "detail" is 1-3 sentences of
    concrete content for that sub-beat (not vague - say what actually
    happens/shifts/is revealed).
    """
    base_system_prompt = (
        "You are a novel outliner planning an entire book before a single "
        f"chapter is drafted. Given a book title, a brief, and a required "
        f"chapter count, produce a JSON array of exactly {chapter_count} "
        "chapter-outline objects, one per chapter, in reading order. "
        "Return ONLY valid JSON, no markdown fences, no preamble. Each "
        "object must have exactly these keys:\n"
        '  "chapter": integer, 1-indexed, matching its position\n'
        '  "sub_beats": an array of 2-4 sub-beat objects for this '
        "chapter. Each sub-beat object has exactly two keys: "
        '"type" (one of: ' + ", ".join(SUB_BEAT_TYPES) + ') and '
        '"detail" (1-3 concrete sentences - not vague, say what actually '
        "happens/shifts/is revealed). Always include the plot_beat for "
        "this chapter. Choose 1-3 more from the remaining types that "
        "genuinely fit this chapter's content - do not force a type that "
        "has nothing real to attach to; a chapter that only has one "
        "genuine sub-beat should have sub_beats be a one-item array "
        "rather than padding with an invented, weak entry.\n"
        "The chapters together must form one coherent through-line for "
        "the whole book: a clear setup, rising complications, a "
        "mid-point turn, escalation, and a resolution that lands by the "
        "final chapter. No chapter's content may contradict an earlier "
        "chapter's or any established plot fact given below. Pace events "
        "across the full chapter count - do not resolve the main "
        "conflict early and coast, and do not cram the ending into the "
        "last chapter.\n"
        f"CRITICAL: the returned JSON array must contain EXACTLY "
        f"{chapter_count} objects, no more, no fewer. Before returning, "
        f"count the objects in your array and confirm the count is "
        f"exactly {chapter_count}.\n"
        "Never write \"Book 1\", \"Book 2\", \"Book 3\", \"Book 4\", any "
        "book number, \"series\", \"protagonist\", \"arc\", or anything "
        "about an author's plan inside any sub-beat's \"detail\" text - "
        "every detail must read as an in-world fact or event, never as a "
        "note to the author."
    )
    user_content = f"Book: {book}\nChapters required: {chapter_count}\nBrief:\n{brief}"
    if continuity_block:
        user_content = f"{continuity_block}\n\n{user_content}"

    max_attempts = 3
    last_beats = None
    last_count = None
    for attempt in range(1, max_attempts + 1):
        system_prompt = base_system_prompt
        if attempt > 1:
            system_prompt += (
                f"\n\nPREVIOUS ATTEMPT FAILED: you returned {last_count} "
                f"chapter objects instead of exactly {chapter_count}. Do not "
                f"repeat that mistake. Return a complete array of exactly "
                f"{chapter_count} chapter objects this time, numbered 1 "
                f"through {chapter_count} with no gaps and no duplicates."
            )
        beats = _call_nemotron(system_prompt, user_content, timeout=180)

        if isinstance(beats, list) and len(beats) == chapter_count:
            return beats

        last_beats = beats
        last_count = len(beats) if isinstance(beats, list) else "non-list"
        print(f"[voxel] Beat map attempt {attempt}/{max_attempts} returned "
              f"{last_count} entries, expected exactly {chapter_count}. "
              + ("Retrying..." if attempt < max_attempts else "Giving up."))

    raise RuntimeError(
        f"Beat map generation returned {last_count} entries after "
        f"{max_attempts} attempts, expected exactly {chapter_count}. "
        f"Raw (last attempt): {last_beats}"
    )


def generate_novel_chapter(chapter_number, chapter_brief, continuity_block="",
                            min_words=2300, max_words=2700):
    """
    One prose chapter for a novel-length work (e.g. Amity Falls series).
    Unlike generate_manuscript, this returns plain prose text, not JSON,
    since a novel chapter isn't a fixed-field list.

    chapter_brief here should be the rendered sub-beats for this chapter
    (see generate_beat_map / story_bible.get_chapter_beat), not just the
    book-level brief - callers should pass that text, so the chapter has
    concrete, multi-part direction instead of one vague instruction.

    min_words/max_words: the length range to state honestly in the
    prompt. Defaults are novels/EDITORIAL_CHARTER.md's actual Book-4-
    onward standard (2300 floor, up to ~2700 ceiling) - NOT retroactive
    to Book 2/3, which are locked at their own already-completed floors.
    This is stated as a floor to write toward via genuine sub-beat
    content, never as license to pad: a chapter whose real content is
    thin should come in short rather than be stretched, per the charter's
    explicit no-padding rule.
    """
    system_prompt = (
        "You are a novelist continuing an existing series. Write chapter "
        f"{chapter_number} in full prose, matching the tone and voice of "
        "the existing chapters. Write the actual chapter text, several "
        f"pages long, with a floor of about {min_words} words and a "
        f"natural ceiling around {max_words} words. This is a target to "
        "reach through genuine content, NOT license to pad: dramatize "
        "each sub-beat given below as its own real moment (its own "
        "scene beat, its own piece of dialogue or interiority) rather "
        "than stretching a single event with extra adjectives, longer "
        "clauses, or restated description. If this chapter's brief "
        "genuinely only supports one sub-beat, write it at whatever "
        "length is honest and do not inflate it. Do not include a "
        "chapter title header unless the brief asks for one. Cover "
        "every sub-beat listed in the chapter brief below - each one "
        "reflects a whole-book outline, so skipping one will break "
        "later chapters that depend on it. Avoid AI-writing tells: no "
        "rule-of-three lists, no stock phrases like 'a testament to' or "
        "'in the tapestry of', no words like 'particular', 'unwavering', "
        "'woven', or 'seamless', vary sentence length naturally, no "
        "em-dash overuse. Never write \"Book 1\", \"Book 2\", \"Book 3\", "
        "\"Book 4\", any book number, the word \"series\", \"protagonist\", "
        "\"arc\", or anything about an author's plan, anywhere in the "
        "chapter - not in narration, not in a character's dialogue or "
        "thoughts. The characters live in this world and never refer to "
        "it as a book."
    )
    user_content = f"Chapter {chapter_number} brief:\n{chapter_brief}"
    if continuity_block:
        user_content = f"{continuity_block}\n\n{user_content}"
    return call_raw(system_prompt, user_content, timeout=240)
