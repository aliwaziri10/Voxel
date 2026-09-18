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
"""

import os
import json

import requests


OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"

# Direct NVIDIA NIM endpoint (build.nvidia.com), OpenAI-compatible.
# NVIDIA_MODEL can be overridden via env var if this default is renamed/
# retired - check https://build.nvidia.com for the current model catalog
# and matching model id if generation starts failing with a 404.
NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
NVIDIA_MODEL = os.environ.get("NVIDIA_MODEL", "nvidia/llama-3.1-nemotron-70b-instruct")


def _active_provider():
    """NVIDIA direct takes priority when its key is present, since it's a
    paid/direct key with no OpenRouter free-tier rate limits."""
    if NVIDIA_API_KEY:
        return NVIDIA_URL, NVIDIA_MODEL, NVIDIA_API_KEY
    if OPENROUTER_API_KEY:
        return OPENROUTER_URL, OPENROUTER_MODEL, OPENROUTER_API_KEY
    return None, None, None


def _require_key():
    if not NVIDIA_API_KEY and not OPENROUTER_API_KEY:
        raise RuntimeError(
            "No LLM API key is set. Export ONE of these before running:\n"
            "  export NVIDIA_API_KEY=your_key_here      (direct, no rate limit)\n"
            "  export OPENROUTER_API_KEY=your_key_here  (free tier, rate limited)"
        )


def _post(system_prompt, user_content, timeout):
    _require_key()
    url, model, key = _active_provider()
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
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


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
    be genuine and chapter-specific, never invented filler to hit a count.

    Returns a list of exactly `chapter_count` dicts:
      {"chapter": int, "sub_beats": [{"type": str, "detail": str}, ...]}
    "type" is one of SUB_BEAT_TYPES. "detail" is 1-3 sentences of
    concrete content for that sub-beat (not vague - say what actually
    happens/shifts/is revealed).
    """
    system_prompt = (
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
        "last chapter."
    )
    user_content = f"Book: {book}\nChapters required: {chapter_count}\nBrief:\n{brief}"
    if continuity_block:
        user_content = f"{continuity_block}\n\n{user_content}"
    beats = _call_nemotron(system_prompt, user_content, timeout=180)

    if not isinstance(beats, list) or len(beats) != chapter_count:
        raise RuntimeError(
            f"Beat map generation returned {len(beats) if isinstance(beats, list) else 'non-list'} "
            f"entries, expected exactly {chapter_count}. Raw: {beats}"
        )
    return beats


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
        "em-dash overuse."
    )
    user_content = f"Chapter {chapter_number} brief:\n{chapter_brief}"
    if continuity_block:
        user_content = f"{continuity_block}\n\n{user_content}"
    return call_raw(system_prompt, user_content, timeout=240)
