#!/usr/bin/env python3
"""
humanizer.py - AI-tell scan + rewrite pass for Voxel manuscripts.

2026-09-19 rewrite: replaced the flat banned-word list with a categorized,
strength-ranked pattern set. Ideas ported (no code copied, all original
here) from researching two external, MIT-licensed projects during a
session with Zia:
  - github.com/blader/humanizer - 25 patterns grouped into 5 categories,
    ranked by strength/frequency, sourced from Wikipedia's "Signs of AI
    writing" project. Key idea adopted: some patterns are strong enough to
    flag on a single sighting; others ("weak alone") only matter when
    several co-occur in one passage, because a careful writer may use any
    one of them deliberately.
  - github.com/Nanako0129/sepia - narrative-architecture-level tells
    (citing StoryScope, arXiv:2604.03136: structure alone detects AI
    fiction at 93% F1 even after surface-level rewrites). Implemented
    2026-09-19 (later same day) as scan_narrative() below - see that
    function's docstring for scope and honest limitations.
  - github.com/zy-zmc/tianming-novel-ai-writer - per-chapter structured
    "what changed" declaration validated before a chapter lands. Not a
    prose-tell tool; relevant to story_bible.py instead, not this file.

Decision (Zia, 2026-09-19): port the ideas into Voxel's own Python, not
depend on the external skills at runtime. This file has no dependency on
any of the three projects above.

2026-09-19 (later same day) review pass, requested by Zia ("refine it to
the maximum"): the file shipped with two checks documented in
_PATTERN_REFERENCE (the text sent to the rewrite LLM) - em-dash overuse
and stacked qualifiers - that the offline scan() never actually
implemented. Added both below (see EMDASH_RE, STACKED_QUALIFIER_RE).
Also expanded STRONG_WORDS/STRONG_PHRASES with additional entries from
Wikipedia's "Signs of AI writing" list that Book 1-3's own tells didn't
happen to surface but are common enough to be worth catching pre-emptively
in Book 4. Added scan_narrative() for the structure-level check flagged
as a follow-up in HANDOFF.md - see its docstring for what it does and does
NOT do; it is intentionally conservative and separate from scan(), never
auto-invoked, because it operates on a whole chapter's shape rather than
a page's prose and its heuristics are far less validated than the
word/phrase list above.

Sanity-checked (read-only, no edits) 2026-09-19 against the published
Book 2 finale chapter: scored 12/100 with only one weak signal
(repeated_openings) and no false strong-tier hits across ~2,600 words of
real, previously-edited prose - the calibration target for this file.

2026-10-29 spec update (per Zia, after a cross-review with ChatGPT): the
REWRITE step now follows the frozen HUMANIZER STEP specification
(HUMANIZER_SPEC below) instead of the old fix-on-sight list. It is a
conservative proofreading layer: change only what a specific check flags,
smallest possible edit, and when uncertain keep the author's text. The
offline scan() is unchanged, so it still decides which pages go to the
rewrite step and what scripts/humanizer_pass.py reports. The rewrite step
now also produces a change log (see rewrite_pass_logged). The spec is
frozen: add checks only when a real test example shows a failure the
existing rules cannot handle.

Runs fully offline for the SCAN step (regex/pattern matching, no network,
no API key needed - works on Zia's laptop with nothing installed but
Python). The REWRITE step reuses the same OpenRouter call already used by
content_provider.py (call_llm_fn), so no new dependency/API is introduced.
It is now TWO calls instead of one: a draft rewrite, then a self-critique
pass that checks the draft against the full pattern list (including the
semantic patterns the offline scan can't see) and produces the final text.
This doubles rewrite-step API cost per flagged page/chapter - acceptable
because rewrites are already the minority case (only pages/chapters that
scan dirty get rewritten at all).

Usage as a library (unchanged from before this rewrite):
    from humanizer import scan, rewrite_pass, scan_narrative

    report = scan(text)                    # -> dict: score 0-100, hits list
    clean  = rewrite_pass(text, call_llm_fn)   # -> (text, ok, dropped)
    struct = scan_narrative(chapter_text)  # -> dict: flags list (see docstring)
"""

import re


# --- Pattern list -----------------------------------------------------------
# Two tiers:
#   STRONG  - a single sighting is worth flagging/fixing on its own.
#   WEAK    - only counts when 2+ weak hits appear in the same text, since a
#             careful writer may use any one of these on purpose. Modeled on
#             blader/humanizer's "weak alone" category, not copied from it.
#
# Kept everything Voxel had already confirmed as a real, recurring tell in
# its own books (see prior HANDOFF.md notes): "particular"/"the specific"
# (Book 3's most recurrent tell, including reintroduction during word-count
# expansion passes), "unwavering", "woven" (slipped through the old
# threshold). Added categories the old list had no equivalent for at all:
# hedges ("some/something ___", separately flagged in Book 3's own hedge
# sweep already done by hand - now catchable automatically), staged
# rhetorical moves, and forced-triad lists (already had a regex, kept).
#
# 2026-09-19 review pass: added a further batch from Wikipedia's "Signs of
# AI writing" that hadn't shown up in Books 1-3 specifically but are common
# enough in LLM output generally to be worth catching before Book 4 drafts,
# rather than waiting to confirm them as a Voxel-specific tell by hand
# first. Kept the existing list's items exactly as-is (still confirmed
# real), only added to it.

STRONG_WORDS = [
    "delve", "delving", "unlock", "unleash", "leverage", "harness",
    "robust", "showcase", "vibrant", "tapestry", "testament",
    "boasts", "landscape", "realm", "journey", "elevate", "seamless",
    "furthermore", "moreover", "notably",
    "particular", "unwavering", "woven",
    # added 2026-09-19 review pass:
    "multifaceted", "underscore", "underscores", "underscoring",
    "profound", "poignant", "palpable", "resonate", "resonates",
    "navigate", "navigating", "intricate", "nuanced", "cutting-edge",
    "game-changer", "unprecedented", "pivotal", "invaluable",
    "meticulous", "meticulously", "bustling", "myriad",
]

STRONG_PHRASES = [
    "in today's fast-paced world",
    "in the world of",
    "unlock the potential of",
    "it's important to note that",
    "at the end of the day",
    "when it comes to",
    "plays a crucial role",
    "stands as a testament",
    "the specific",
    "the kind of",
    "not just x but y",  # placeholder never matches; real check is regex below
    "in conclusion",
    # added 2026-09-19 review pass:
    "in the realm of",
    "in an increasingly",
    "no discussion would be complete without",
    "let's dive in",
    "in summary",
    "a rich tapestry of",
    "a testament to",
    "serves as a reminder",
    "it goes without saying",
    "the fact of the matter is",
]

# "Not X, it's Y" / "not just X, it's Y" - staged contrast instead of a
# direct statement. Strong on its own (blader/humanizer pattern #1).
NOT_X_BUT_Y_RE = re.compile(
    r"\b(?:it'?s|this is|that'?s)\s+not\s+(?:just\s+)?[\w '-]{2,40},?\s+"
    r"(?:it'?s|but)\s+", re.IGNORECASE
)

# Vague hedge: "some/something ___" used as a placeholder rather than a real
# referent. Confirmed by Book 3's own manual hedge-sweep as a genuine,
# recurring problem distinct from the word-level tells above. Weak alone -
# "someone", "somewhere", "somehow" and concrete uses ("some of the
# soldiers") are excluded; only the bare vague-noun pattern counts, and even
# then only when it recurs.
HEDGE_RE = re.compile(
    r"\bsome(?:thing)?\s+(?:small|strange|quiet|odd|deep|dark|old|tired|"
    r"fragile|fleeting|unspoken|unnamed|kind\s+of)\b", re.IGNORECASE
)

# Forced rule-of-three list (kept from the prior version).
TRICOLON_RE = re.compile(
    r"\b(\w+),\s+(\w+),\s+and\s+(\w+)\b", re.IGNORECASE
)

# Em-dash overuse. Added 2026-09-19 review pass: this was already promised
# in _PATTERN_REFERENCE (sent to the rewrite LLM) but never actually
# checked by the offline scan - a real gap, since it meant the SCORE never
# reflected em-dash overuse even though the rewrite prompt claimed to care
# about it. Counts em dashes (—) and the double-hyphen stand-in (--) some
# drafts use. Weak alone per the same reasoning as blader/humanizer: one or
# two em dashes in a chapter is normal punctuation, not a tell; the tell is
# using it as the DEFAULT connector in place of periods/commas/"and".
EMDASH_RE = re.compile(r"—|--")

# Stacked qualifiers - "could potentially possibly", "might perhaps",
# "seemed to almost". Added 2026-09-19 review pass, same gap as em-dash:
# promised in _PATTERN_REFERENCE, never implemented. Strong on its own when
# it appears at all - unlike em dashes or hedges, a stack of 2+ hedging
# qualifiers in a row is not something a deliberate human stylist does on
# purpose; it is close to always an LLM hedging artifact.
STACKED_QUALIFIER_RE = re.compile(
    r"\b(?:could|might|may|seemed?\s+to)\s+"
    r"(?:potentially|possibly|perhaps|maybe|almost|somewhat)\s+"
    r"(?:potentially|possibly|perhaps|maybe|almost|somewhat)?\b",
    re.IGNORECASE
)


# Repeated sentence openings - weak alone; three or more sentences in a row
# opening with the same first word is the threshold (a careful writer
# repeats a subject on purpose sometimes; a run of 3+ rarely is).
def _repeated_openings(sentences):
    openings = [s.strip().split(" ", 1)[0].lower() for s in sentences if s.strip()]
    run = 1
    best = 1
    for i in range(1, len(openings)):
        if openings[i] == openings[i - 1] and openings[i]:
            run += 1
            best = max(best, run)
        else:
            run = 1
    return best


def scan(text):
    """Offline scan. Returns {'score': int 0-100 (0=clean), 'hits': [...]}.

    Strong hits count individually. Weak hits are collected separately and
    only added to the hit list (and score) once 2 or more distinct weak
    patterns are present - a single weak-alone signal is not flagged, per
    the strength-ranking idea above.
    """
    hits = []
    weak_hits = []
    lower = text.lower()

    for w in STRONG_WORDS:
        count = lower.count(w)
        if count:
            hits.append({"type": "strong_word", "pattern": w, "count": count})

    for p in STRONG_PHRASES:
        if p == "not just x but y":
            continue
        count = lower.count(p)
        if count:
            hits.append({"type": "strong_phrase", "pattern": p, "count": count})

    not_x_but_y = NOT_X_BUT_Y_RE.findall(text)
    if not_x_but_y:
        hits.append({"type": "not_x_but_y", "count": len(not_x_but_y)})

    tricolons = TRICOLON_RE.findall(text)
    if tricolons:
        hits.append({"type": "tricolon_list", "count": len(tricolons)})

    hedges = HEDGE_RE.findall(text)
    if len(hedges) >= 2:
        hits.append({"type": "vague_hedge", "count": len(hedges)})
    elif hedges:
        weak_hits.append({"type": "vague_hedge", "count": len(hedges)})

    # Stacked qualifiers - strong on its own (see STACKED_QUALIFIER_RE note).
    stacked = STACKED_QUALIFIER_RE.findall(text)
    if stacked:
        hits.append({"type": "stacked_qualifier", "count": len(stacked)})

    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    word_count = max(1, len(text.split()))

    max_repeat = _repeated_openings(sentences)
    if max_repeat >= 3:
        hits.append({"type": "repeated_openings", "count": max_repeat})
    elif max_repeat == 2:
        weak_hits.append({"type": "repeated_openings", "count": max_repeat})

    # Em-dash overuse - scaled to length so this is consistent across a
    # single page and a full chapter, BUT gated by a minimum raw count
    # first. Rate-only scaling breaks on short text: a single dash in a
    # 40-word paragraph scales to a huge per-500-word rate despite being
    # completely normal punctuation. Require at least 3 raw occurrences
    # before the rate threshold is even considered, same shape as the
    # hedge/tricolon checks above which key off raw counts, not a rate.
    emdash_count = len(EMDASH_RE.findall(text))
    emdash_rate = emdash_count / (word_count / 500)
    if emdash_count >= 3 and emdash_rate > 4:
        hits.append({"type": "emdash_overuse", "count": emdash_count, "rate_per_500w": round(emdash_rate, 1)})
    elif emdash_count >= 2 and emdash_rate > 2:
        weak_hits.append({"type": "emdash_overuse", "count": emdash_count, "rate_per_500w": round(emdash_rate, 1)})

    # Sentence-length burstiness: real human prose varies a lot; flat AI
    # prose clusters tightly around one length. Kept as weak alone - this
    # alone was never a reliable standalone signal.
    lengths = [len(s.split()) for s in sentences if s.strip()]
    if len(lengths) >= 6:
        mean = sum(lengths) / len(lengths)
        variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
        stdev = variance ** 0.5
        if mean > 0 and (stdev / mean) < 0.35:
            weak_hits.append({"type": "low_burstiness", "stdev_over_mean": round(stdev / mean, 2)})

    if len(weak_hits) >= 2:
        hits.extend(weak_hits)

    # Score: weighted hit count, capped at 100.
    score = min(100, sum(h.get("count", 1) * 4 for h in hits))
    return {"score": score, "hits": hits}


def has_strong_hit(report):
    """True if the scan found ANY strong-tier hit (strong_word,
    strong_phrase, not_x_but_y, tricolon_list, stacked_qualifier,
    emdash_overuse, or a weak-tier pattern that crossed into the hit list
    because 2+ weak signals co-occurred). Used alongside the score
    threshold: a single stock AI-tell word is a hard content rule (never
    acceptable in the manuscript), not a soft style score, so it must
    always trigger a rewrite regardless of how low that pushes the overall
    weighted score."""
    strong_types = {
        "strong_word", "strong_phrase", "not_x_but_y", "tricolon_list",
        "stacked_qualifier", "emdash_overuse",
    }
    return any(h["type"] in strong_types for h in report.get("hits", []))


# Backward-compat alias - voxel_cli.py and scripts/ call this name.
has_banned_hit = has_strong_hit


def _extract_facts(text):
    """Pull out numbers and capitalized multi-word spans (proper-noun-ish),
    for the post-rewrite integrity check. Cheap and deliberately conservative
    - false positives (flags something that's fine) are OK, false negatives
    (misses a dropped fact) are not."""
    numbers = re.findall(r"\b\d[\d,]*\.?\d*\b", text)
    caps = re.findall(r"\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)\b", text)
    return set(numbers), set(caps)


# --- Frozen HUMANIZER STEP specification (2026-10-29) --------------------------
# Final spec agreed with Zia after a cross-review with ChatGPT. It is FROZEN:
# do not add checks unless a real testing example shows a specific failure the
# existing rules cannot handle. This text is sent to the rewrite model as-is.
HUMANIZER_SPEC = r"""
HUMANIZER STEP (FROZEN SPECIFICATION, for proofreading novel text)

GOAL: This is a conservative proofreading layer. Do not make the prose "more human", more polished, or more literary. Detect a specific formulaic AI habit, make the smallest possible correction, and leave the rest of the author's writing alone, including intentional imperfections and stylistic quirks.

PART A: CLEANUP (always do, no judgment needed)
A1. Remove leftover template text, drafting instructions, AI disclaimers, and "As an AI" lines. Be strict.
A2. Remove stray bold, bullets, emojis, and title-case headings that do not belong in a manuscript. Keep them where the story needs them (letters, messages, documents, chapter headings).

PART B: PATTERN CHECKS
Act when a pattern repeats or looks accidental. A single natural occurrence is usually fine. Each check lists the default action.
B1. Inflated importance: do not automatically remove phrases such as "a pivotal moment". Flag abstract significance language only when it replaces something the prose could show more concretely, or adds no meaningful information. Default: swap for one concrete detail, or cut.
B2. Forced closure: a closing line that only explains what the scene already showed. Default: delete it. Keep reflective endings the author chose on purpose.
B3. Unnecessary transition scaffolding: the problem is unnecessary scaffolding, not words such as "meanwhile" themselves. Flag "moreover", "furthermore", "meanwhile", "as a result", "in that moment", "with that in mind" when the sequence is already obvious. Keep a connector when it is natural to the narrator's voice or genuinely needed for clarity. Default: cut or use a plain connector.
B4. Symmetrical constructions: "not only X but also Y", "It wasn't X. It was Y.", "Not because X, but because Y.", "He didn't X; he Y." Default: rewrite only the repeated ones.
B5. Empty generic attribution ("some say", "many believe") that only adds fake authority. Default: make it specific or cut it. Keep when it stands for rumor, folklore, or public opinion.
B6. Redundant explanation: a sentence that explains the meaning or emotion of an action or line of dialogue that already carried it (observation, then interpretation, then emotional conclusion). Default: delete the explaining sentence. Keep direct emotional narration if it is the author's style.
B7. Stock phrasing: do not replace stock imagery merely because it occurs more than once. Flag repeated stock imagery (heartbeat, silence, chills, widened eyes) when it becomes conspicuous, interchangeable, or formulaic. Replace only the genuinely unnecessary occurrences, with a specific detail.
B8. Habitual hedging: repeated "seemed to", "appeared to", "almost", "somehow", "in a way". Default: cut the habitual ones. Keep genuine uncertainty that belongs to the POV character.
B9. Stacked decorative metaphors: several polished images where one concrete image would do. Default: keep the strongest one. Keep distinctive author metaphors.
B10. POV slips: information or interpretation the viewpoint character could not know. Keep this conservative. Normally flag for the author; do not silently rewrite.
B11. Dialogue: do not impose the model's idea of how a character should speak. Flag questionable dialogue for the author (explaining what would be left unsaid, answering too perfectly, stating what behavior already shows, identical speech rhythms), unless the problem is clearly redundant explanation covered by another check. Make a direct edit only when the violation is unambiguous.
B12. Character reference switching: unnatural swapping between a name and labels ("the woman", "the man", "the brunette"), or repeated names where a pronoun is natural. Default: fix only the unnatural ones.
B13. Paragraph-level repetition: require evidence of an actual repeated structure across multiple sentences or paragraphs before intervening. Do not rewrite deliberately minimalist, repetitive, or rhythmic prose merely because it differs from generic prose conventions. Default: flag the passage.

PART C: RULES
WHEN UNCERTAIN, PRESERVE THE AUTHOR'S TEXT. False positives are more damaging than missed humanization opportunities.

C1. Change only what a check flags. Do not use a general instruction like "make it sound more human".
C2. Every edit must name the check that triggered it. If no check applies, leave the text unchanged.
C3. Make the smallest possible edit. Do not rewrite nearby sentences to make them "flow better".
C4. Keep the author's vocabulary, diction, voice, plot, and names.
C5. Preserve deliberate quirks: repetition, fragments, odd punctuation, slang, dialect, bluntness, melodrama, unusual metaphors.
C6. Never add imperfections, slang, fragments, mistakes, or randomness to look less AI-generated.
C7. Edit locally, at the sentence or the smallest passage needed, not the whole paragraph or scene.
C8. A "no change" result is allowed. Do not modify every paragraph.
C9. "AI-like" is not the same as "bad writing". Do not improve style that is only plain or imperfect.
C10. For every change, show:
Original: [exact original text]
New: [exact revised text]
Check: [check number]
C11. List flagged passages that were deliberately left unchanged under "Kept on purpose", with the reason they were preserved. Do not claim to know the author's intention unless the text or instructions establish it. When uncertain, say that the passage was preserved because the evidence for changing it was insufficient.
C12. No stacked edits: if a passage triggers multiple checks, do not perform a chain of increasingly invasive rewrites. Apply the minimum necessary correction, then reassess the result. Do not let several individually minor checks collectively transform the author's paragraph.
C13. Confidence threshold: when there is reasonable uncertainty about whether something is an AI/formulaic habit or an intentional stylistic choice, leave the text unchanged and report it as preserved. False positives are worse than missed humanization opportunities.

FREEZE: Do not add checks unless a real testing example demonstrates a specific failure that the existing rules cannot handle.
"""


# Repo tells: the pre-existing Voxel list that the offline scan() looks for.
# Kept so the rewrite model knows what the scan flagged, but under the frozen
# spec these are INPUTS to judgment, not fix-on-sight rules (spec C13, and the
# Editorial Charter's "do not mechanically delete every instance of a flagged
# word without reading context").
_PATTERN_REFERENCE = """\
REPO TELLS (the offline scan flags these on a single sighting; they are not
extra checks. Per C13, change one only when it clearly reads as a tell in
context, and keep it when it is the author's voice. If an edit is justified
only by this list, write "Check: REPO TELL" in the change log):

- Stock AI vocabulary: delve, leverage, harness, robust, showcase, vibrant,
  tapestry, testament, boasts, landscape, realm, journey, elevate,
  seamless, furthermore, moreover, notably, particular, unwavering, woven,
  multifaceted, underscore, profound, poignant, palpable, resonate,
  navigate, intricate, nuanced, cutting-edge, game-changer, unprecedented,
  pivotal, invaluable, meticulous, bustling, myriad.
- Stock phrases: "it's important to note that", "at the end of the day",
  "when it comes to", "plays a crucial role", "stands as a testament",
  "the specific", "the kind of", "in conclusion", "in the realm of",
  "no discussion would be complete without", "in summary",
  "a rich tapestry of", "serves as a reminder", "it goes without saying".
- Staged contrast instead of a direct statement: "It's not just X, it's Y."
- Vague hedges used as a placeholder rather than a real, concrete detail:
  "some small, frightened part of him", "something in his chest tightened."
  Name the actual thing.
- Stacked qualifiers in a row: "could potentially possibly", "might
  perhaps almost". State the uncertainty once, plainly, or not at all.
- Em dash used as the default connector in place of periods, commas, or
  "and" - more than about 4 per 500 words reads as a tic, not a style.

Weak signals the scan also reports (repeated sentence openings, uniform
sentence rhythm, occasional em dashes, plain three-item lists): do NOT edit
for any of these alone. See B13, C5 and C6.
"""

_LOG_DELIM = "=====CHANGE LOG====="

_OUTPUT_FORMAT = (
    "OUTPUT FORMAT (follow exactly): first the complete revised text, with "
    "every sentence you did not change left exactly as written. Then, on its "
    "own line, the marker " + _LOG_DELIM + " and after it the change log. "
    "The log has one entry per edit in the form:\n"
    "Original: [exact original text]\n"
    "New: [exact revised text]\n"
    "Check: [check number such as B6, or REPO TELL]\n"
    "followed by a final section headed Kept on purpose, listing flagged "
    "passages you left unchanged, each with the reason. If you changed "
    "nothing, return the text unchanged, then the marker, then the single "
    "line No changes. No markdown fences and no preamble."
)


def _split_log(raw):
    """Split a model reply into (text, change_log) on the change-log marker.
    If the marker is missing the whole reply is the text and the log is empty
    (same as the behavior before the change log existed)."""
    if raw is None:
        return "", ""
    if _LOG_DELIM in raw:
        body, log = raw.split(_LOG_DELIM, 1)
        return body.strip(), log.strip()
    return raw, ""


def rewrite_pass_logged(text, call_llm_fn):
    """
    Apply the frozen HUMANIZER STEP spec to text, then verify no numbers or
    proper nouns were dropped. call_llm_fn(system_prompt, user_content) must
    return a plain string (not JSON) - pass content_provider.call_raw.

    Two calls:
      1. Draft: apply the spec (smallest possible edits, with a change log).
      2. Review: check the draft against the spec, restore the original
         wording for any edit that is not justified by a specific check
         (spec C2, C3, C12, C13), and produce the final text and log.

    Returns (clean_text, integrity_ok, dropped_facts, change_log).
    """
    draft_system_prompt = (
        "You are applying the HUMANIZER STEP specification below to the text "
        "the user sends. Follow it exactly. It is a conservative proofreading "
        "layer, not a rewrite: change only what a specific check flags, make "
        "the smallest possible edit, and when uncertain leave the author's "
        "text unchanged.\n\n"
        + HUMANIZER_SPEC + "\n" + _PATTERN_REFERENCE
        + "\nDo NOT change the meaning. Do NOT drop or alter any number, "
        "date, proper name, or specific detail. Do NOT shorten the text to "
        "fit a word count and do NOT lengthen it. Do NOT vary sentence "
        "length for its own sake.\n\n"
        + _OUTPUT_FORMAT
    )
    draft_raw = call_llm_fn(draft_system_prompt, text)
    draft_text, _draft_log = _split_log(draft_raw)

    if not draft_text.strip():
        return text, False, {"numbers": [], "names": [], "empty_output": True}, ""

    critique_system_prompt = (
        "You already applied the HUMANIZER STEP specification below to a "
        "passage. Now review your own draft against it. Undo any edit that "
        "is not justified by a specific check (C2), that is larger than "
        "needed (C3), that is part of a chain of edits changing the "
        "author's paragraph (C12), or where it is uncertain whether the "
        "original was a formulaic habit or the author's choice (C13). "
        "Restore the original wording for those. Add a new edit only when a "
        "clear, unambiguous violation of a check remains.\n\n"
        + HUMANIZER_SPEC + "\n" + _PATTERN_REFERENCE
        + "\nOriginal text (to restore wording from and to check facts "
        "against):\n---\n" + text + "\n---\n\n"
        "Do NOT change the meaning. Do NOT drop or alter any number, date, "
        "proper name, or specific detail from the original. Do NOT shorten "
        "the text to fit a word count.\n\n"
        + _OUTPUT_FORMAT
        + " The change log must describe the differences between the "
        "ORIGINAL text and your final text."
    )
    final_raw = call_llm_fn(critique_system_prompt, draft_text)
    rewritten, change_log = _split_log(final_raw)

    if not rewritten.strip():
        return text, False, {"numbers": [], "names": [], "empty_output": True}, ""

    before_nums, before_caps = _extract_facts(text)
    after_nums, after_caps = _extract_facts(rewritten)

    dropped = {
        "numbers": sorted(before_nums - after_nums),
        "names": sorted(before_caps - after_caps),
    }
    integrity_ok = not dropped["numbers"] and not dropped["names"]

    return rewritten, integrity_ok, dropped, change_log


def rewrite_pass(text, call_llm_fn):
    """Backward-compatible wrapper: same (clean_text, integrity_ok,
    dropped_facts) return as before the change log was added. Use
    rewrite_pass_logged to also get the change log."""
    clean, ok, dropped, _log = rewrite_pass_logged(text, call_llm_fn)
    return clean, ok, dropped


def humanize_manuscript(pages, call_llm_fn, min_score_to_rewrite=8):
    """
    Takes Voxel's page list (list of dicts with a 'text' key, as produced by
    content_provider.generate_manuscript or a novel chapter split into
    pages) and runs scan+rewrite per page. Only rewrites pages that
    actually scan dirty, to save API calls. Mutates and returns the same
    list, adding '_humanizer' metadata per page for the project.json
    record.

    A page is rewritten if EITHER its weighted score crosses
    min_score_to_rewrite OR it contains any strong-tier hit at all (see
    has_strong_hit) - a lone stock AI-tell word must never survive just
    because the overall score stayed low.
    """
    for page in pages:
        original = page.get("text", "")
        if not original.strip():
            continue
        report = scan(original)
        if report["score"] < min_score_to_rewrite and not has_strong_hit(report):
            page["_humanizer"] = {"scanned": True, "rewritten": False, "score_before": report["score"]}
            continue

        clean, ok, dropped, change_log = rewrite_pass_logged(original, call_llm_fn)
        if ok:
            page["text"] = clean
            page["_humanizer"] = {
                "scanned": True, "rewritten": True,
                "score_before": report["score"],
                "score_after": scan(clean)["score"],
            }
            if change_log:
                page["_humanizer"]["change_log"] = change_log
        else:
            page["_humanizer"] = {
                "scanned": True, "rewritten": False,
                "score_before": report["score"],
                "integrity_gate_failed": True, "dropped": dropped,
            }
    return pages


def humanize_text(text, call_llm_fn, min_score_to_rewrite=8):
    """Same idea as humanize_manuscript but for a single long text blob
    (a novel chapter), returning (final_text, meta_dict) instead of
    mutating a page list. Same has_strong_hit override as above applies."""
    report = scan(text)
    if report["score"] < min_score_to_rewrite and not has_strong_hit(report):
        return text, {"scanned": True, "rewritten": False, "score_before": report["score"]}

    clean, ok, dropped, change_log = rewrite_pass_logged(text, call_llm_fn)
    if ok:
        meta = {
            "scanned": True, "rewritten": True,
            "score_before": report["score"], "score_after": scan(clean)["score"],
        }
        if change_log:
            meta["change_log"] = change_log
        return clean, meta
    return text, {
        "scanned": True, "rewritten": False, "score_before": report["score"],
        "integrity_gate_failed": True, "dropped": dropped,
    }


# --- Narrative-architecture-level scan (2026-09-19, follow-up per HANDOFF.md) ---
#
# HONEST SCOPE NOTE: everything above operates at the word/sentence level -
# it catches individual tells but, per the StoryScope research cited at the
# top of this file (arXiv:2604.03136), structure-level patterns survive
# surface rewrites almost completely (93% F1 detection even after a full
# prose rewrite). This function is a first, DELIBERATELY CONSERVATIVE pass
# at three of those structural patterns, implemented as cheap heuristics on
# whatever text is given (works on a page or a full chapter, but is most
# meaningful on a full chapter or scene, since these are shape-level
# patterns, not line-level ones).
#
# Sanity-checked (read-only, no edits) 2026-09-19 against the published
# Book 2 finale chapter: flagged one instance (growth_arc_closer) across
# ~2,600 words of real, previously-edited prose - a single flag on a real,
# well-edited chapter is expected and fine; the design goal is that a
# careful human chapter shouldn't light up with many flags at once.
#
# This is NOT a validated detector. It is a set of flags for a human (or a
# subsequent LLM critique pass) to actually look at - false positives are
# expected and acceptable; this must never auto-rewrite or auto-reject a
# chapter on its own. It is intentionally NOT wired into humanize_text/
# humanize_manuscript above - per HANDOFF.md, Book 4 has no chapters
# written yet, so there is nothing real to validate this against, and
# auto-gating chapter output on unvalidated heuristics would be worse than
# not checking at all. Call this separately, read the flags, decide by eye.
NEAT_RESOLUTION_RE = re.compile(
    r"\b(?:finally|at last|in the end)\s+(?:understood|accepted|realized|"
    r"found peace|let go|made peace)\b", re.IGNORECASE
)

BODILY_ONLY_EMOTION_RE = re.compile(
    r"\b(?:chest|throat|stomach)\s+(?:tightened|clenched|ached|twisted)\b",
    re.IGNORECASE
)

GROWTH_ARC_CLOSER_RE = re.compile(
    r"\b(?:had grown|was no longer the (?:person|man|woman) "
    r"(?:who|that))\b", re.IGNORECASE
)


def scan_narrative(chapter_text):
    """Conservative, unvalidated heuristic flags for chapter/scene-shape
    level AI tells (see module-level note above for scope and honest
    limitations). Returns {'flags': [...]} - never a score, never a
    pass/fail, because these heuristics have not been calibrated against
    Voxel's own books the way the word-level scan() has.

    Three checks, each independently common in LLM-generated fiction per
    the sepia/StoryScope research cited above:
      - neat_resolution: an ending beat resolved via a stated realization/
        acceptance rather than dramatized action or dialogue.
      - bodily_only_emotion: emotion rendered ONLY as a physical sensation
        cliche (chest tightened / throat ached), with no other register
        used anywhere in the passage.
      - growth_arc_closer: a stock "had grown/was no longer who they were"
        arc-closing line.

    A chapter can legitimately contain any ONE of these once - human
    fiction uses them too. The flag is meant to prompt a human read of the
    specific passage, not an automatic verdict. Do not treat a nonzero flag
    count as equivalent to a scan() strong hit; it is a much weaker signal.
    """
    flags = []

    neat = NEAT_RESOLUTION_RE.findall(chapter_text)
    if neat:
        flags.append({
            "type": "neat_resolution",
            "count": len(neat),
            "note": "Ending resolved by stated realization/acceptance rather "
                     "than dramatized action or dialogue - check if this beat "
                     "is earned by a scene, or just asserted.",
        })

    bodily = BODILY_ONLY_EMOTION_RE.findall(chapter_text)
    if bodily:
        flags.append({
            "type": "bodily_only_emotion",
            "count": len(bodily),
            "note": "Emotion rendered as a physical-sensation cliche. Fine "
                     "once; several instances with no other register (no "
                     "dialogue, no action, no interiority) is the actual tell.",
        })

    growth = GROWTH_ARC_CLOSER_RE.findall(chapter_text)
    if growth:
        flags.append({
            "type": "growth_arc_closer",
            "count": len(growth),
            "note": "Stock 'had grown / was no longer who they were' "
                     "arc-closing line. Check if the growth was shown "
                     "earlier in the chapter or only stated here.",
        })

    return {"flags": flags}
