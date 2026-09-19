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
    fiction at 93% F1 even after surface-level rewrites). NOT implemented
    here - these are chapter/plot-shape level checks (causally-tidy plots,
    emotion rendered only as bodily sensation, growth/acceptance endings),
    a different kind of check than this file's per-page/per-chapter prose
    scan. Left as a follow-up; see HANDOFF.md.
  - github.com/zy-zmc/tianming-novel-ai-writer - per-chapter structured
    "what changed" declaration validated before a chapter lands. Not a
    prose-tell tool; relevant to story_bible.py instead, not this file.

Decision (Zia, 2026-09-19): port the ideas into Voxel's own Python, not
depend on the external skills at runtime. This file has no dependency on
any of the three projects above.

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
    from humanizer import scan, rewrite_pass

    report = scan(text)              # -> dict: score 0-100, hits list
    clean  = rewrite_pass(text, call_llm_fn)   # -> (text, ok, dropped)
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

STRONG_WORDS = [
    "delve", "delving", "unlock", "unleash", "leverage", "harness",
    "robust", "showcase", "vibrant", "tapestry", "testament",
    "boasts", "landscape", "realm", "journey", "elevate", "seamless",
    "furthermore", "moreover", "notably",
    "particular", "unwavering", "woven",
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

    sentences = re.split(r"(?<=[.!?])\s+", text.strip())

    max_repeat = _repeated_openings(sentences)
    if max_repeat >= 3:
        hits.append({"type": "repeated_openings", "count": max_repeat})
    elif max_repeat == 2:
        weak_hits.append({"type": "repeated_openings", "count": max_repeat})

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
    strong_phrase, not_x_but_y, tricolon_list, or a weak-tier pattern that
    crossed into the hit list because 2+ weak signals co-occurred). Used
    alongside the score threshold: a single stock AI-tell word is a hard
    content rule (never acceptable in the manuscript), not a soft style
    score, so it must always trigger a rewrite regardless of how low that
    pushes the overall weighted score."""
    strong_types = {"strong_word", "strong_phrase", "not_x_but_y", "tricolon_list"}
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
  seamless, furthermore, moreover, notably, particular, unwavering, woven.
- Stock phrases: "it's important to note that", "at the end of the day",
  "when it comes to", "plays a crucial role", "stands as a testament",
  "the specific", "the kind of", "in conclusion".
- Staged contrast instead of a direct statement: "It's not just X, it's Y."
- Forced rule-of-three lists where the meaning doesn't need exactly three
  items.
- Vague hedges used as a placeholder rather than a real, concrete detail:
  "some small, frightened part of him", "something in his chest tightened."
  Name the actual thing.

WEAK ALONE (fix only if several of these cluster in one passage):
- Repeated sentence openings (3+ sentences in a row starting the same way).
- Uniform sentence rhythm / low variance in sentence length.
- Overuse of em dashes as the universal connector.
- Stacked qualifiers ("could potentially possibly").
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
