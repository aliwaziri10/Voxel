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


_PATTERN_REFERENCE = """\
Categories of AI-writing tells to check for (fix any that are present; a
careful human writer sometimes uses one of the "weak alone" ones on
purpose, so only change it if it actually reads as a tell in context):

STRONG (fix on sight):
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
- Forced rule-of-three lists where the meaning doesn't need exactly three
  items.
- Vague hedges used as a placeholder rather than a real, concrete detail:
  "some small, frightened part of him", "something in his chest tightened."
  Name the actual thing.
- Stacked qualifiers in a row: "could potentially possibly", "might
  perhaps almost". State the uncertainty once, plainly, or not at all.
- Em dash used as the default connector in place of periods, commas, or
  "and" - more than about 4 per 500 words reads as a tic, not a style.

WEAK ALONE (fix only if several of these cluster in one passage):
- Repeated sentence openings (3+ sentences in a row starting the same way).
- Uniform sentence rhythm / low variance in sentence length.
- Occasional (not overused) em dashes are fine; only the overuse pattern
  above is a tell.
- Passive voice with a missing actor where naming the actor would help.
"""


def rewrite_pass(text, call_llm_fn):
    """
    Rewrite text to remove AI tells, then verify no numbers/proper nouns
    were dropped. call_llm_fn(system_prompt, user_content) must return a
    plain string (not JSON) - pass content_provider.call_raw.

    Two calls instead of one:
      1. Draft rewrite against the full pattern reference.
      2. Self-critique: check the draft against the same reference and
         produce a final version, catching anything the first pass missed
         or introduced.

    Returns (clean_text, integrity_ok, dropped_facts).
    """
    draft_system_prompt = (
        "Rewrite the following text to remove AI-writing tells.\n\n"
        + _PATTERN_REFERENCE
        + "\nDo NOT change the meaning, do NOT drop or alter any number, "
        "date, proper name, or specific detail. Vary sentence length "
        "naturally. Return ONLY the rewritten text, no preamble, no "
        "markdown fences."
    )
    draft = call_llm_fn(draft_system_prompt, text)

    critique_system_prompt = (
        "You already rewrote a passage to remove AI-writing tells. Check "
        "your own draft against the same pattern list below - some tells "
        "are easy to miss on a first pass, and a rewrite can introduce new "
        "ones (e.g. a fresh stock phrase, a new forced triad).\n\n"
        + _PATTERN_REFERENCE
        + "\nOriginal text (for fact-checking only - do not reintroduce its "
        "phrasing):\n---\n" + text + "\n---\n\n"
        "Produce the final version of the draft below. Do NOT change the "
        "meaning, do NOT drop or alter any number, date, proper name, or "
        "specific detail from the original. Return ONLY the final text, no "
        "preamble, no markdown fences, no commentary about what you "
        "changed."
    )
    rewritten = call_llm_fn(critique_system_prompt, draft)

    before_nums, before_caps = _extract_facts(text)
    after_nums, after_caps = _extract_facts(rewritten)

    dropped = {
        "numbers": sorted(before_nums - after_nums),
        "names": sorted(before_caps - after_caps),
    }
    integrity_ok = not dropped["numbers"] and not dropped["names"]

    return rewritten, integrity_ok, dropped


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

        clean, ok, dropped = rewrite_pass(original, call_llm_fn)
        if ok:
            page["text"] = clean
            page["_humanizer"] = {
                "scanned": True, "rewritten": True,
                "score_before": report["score"],
                "score_after": scan(clean)["score"],
            }
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

    clean, ok, dropped = rewrite_pass(text, call_llm_fn)
    if ok:
        return clean, {
            "scanned": True, "rewritten": True,
            "score_before": report["score"], "score_after": scan(clean)["score"],
        }
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
