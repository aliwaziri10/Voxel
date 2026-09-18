#!/usr/bin/env python3
"""
humanizer.py - AI-tell scan + rewrite pass for Voxel manuscripts.

Design borrowed from (ideas only, no code copied — all original here):
  - Aaron-Bushnell/humanizer (43-pattern lint list, "content integrity gate")
  - Aboudjem/humanizer-skill (0-100 AI-tell score, banned-phrase list)
  - maximsmd/Humanizer (fact-preservation guardrails)

Runs fully offline for the SCAN step (regex/pattern matching, no network,
no API key needed — works on Zia's laptop with nothing installed but
Python). The REWRITE step reuses the same OpenRouter call already used by
content_provider.py, so no new dependency/API is introduced.

Usage as a library:
    from humanizer import scan, rewrite_pass

    report = scan(text)              # -> dict: score 0-100, hits list
    clean  = rewrite_pass(text)       # -> str, rewritten + fact-checked
"""

import re


# --- Pattern list (word/phrase level) --------------------------------------
# Trimmed, high-signal set. Not trying to match 55 patterns exactly — trying
# to catch the ones that actually showed up in Voxel's own Book 1 output
# (see HANDOFF.md "known AI tells" section).
#
# 2026-09-15: added "particular" per amity-falls-book-3/HANDOFF.md, which
# flagged it as the single most recurrent AI-tell across all three books,
# including reintroduction during word-count-fix expansion passes. Added
# "the specific" and "the kind of" phrase-level for the same reason — these
# are fine in occasional/varied use, only a real problem when repetitive
# within one chapter, so treat count > 1-2 in a single chapter as a flag,
# not any single occurrence.
#
# 2026-09-19: added "unwavering", "woven" after Book 3's PROOFREAD_REPORT.md
# showed both got through the humanizer untouched (see the score-threshold
# fix below — this is the OTHER half of that same fix: the words also
# weren't all on the list yet).

BANNED_WORDS = [
    "delve", "delving", "unlock", "unleash", "leverage", "harness",
    "robust", "showcase", "vibrant", "tapestry", "testament",
    "boasts", "landscape", "realm", "journey", "elevate", "seamless",
    "furthermore", "moreover", "notably", "in conclusion",
    "particular", "unwavering", "woven",
]

BANNED_PHRASES = [
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
]

# Structural tells: rule-of-three lists, uniform sentence rhythm.
TRICOLON_RE = re.compile(
    r"\b(\w+),\s+(\w+),\s+and\s+(\w+)\b", re.IGNORECASE
)


def scan(text):
    """Offline scan. Returns {'score': int 0-100 (0=clean), 'hits': [...]}."""
    hits = []
    lower = text.lower()

    for w in BANNED_WORDS:
        count = lower.count(w)
        if count:
            hits.append({"type": "banned_word", "pattern": w, "count": count})

    for p in BANNED_PHRASES:
        count = lower.count(p)
        if count:
            hits.append({"type": "banned_phrase", "pattern": p, "count": count})

    tricolons = TRICOLON_RE.findall(text)
    if tricolons:
        hits.append({"type": "tricolon_list", "count": len(tricolons)})

    # Sentence-length burstiness: real human prose varies a lot; flat AI
    # prose clusters tightly around one length.
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    lengths = [len(s.split()) for s in sentences if s.strip()]
    if len(lengths) >= 6:
        mean = sum(lengths) / len(lengths)
        variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
        stdev = variance ** 0.5
        if mean > 0 and (stdev / mean) < 0.35:
            hits.append({"type": "low_burstiness", "stdev_over_mean": round(stdev / mean, 2)})

    # Score: weighted hit count, capped at 100.
    score = min(100, sum(h.get("count", 1) * 4 for h in hits))
    return {"score": score, "hits": hits}


def has_banned_hit(report):
    """True if the scan found ANY banned_word or banned_phrase hit, even
    just one. Used alongside the score threshold: a single stock AI-tell
    word is a hard content rule (never acceptable in the manuscript), not
    a soft style score, so it must always trigger a rewrite regardless of
    how low that pushes the overall weighted score. This fixes the bug
    where a lone hit (score 4) never crossed the old default 8-point
    rewrite threshold and silently passed through untouched."""
    return any(h["type"] in ("banned_word", "banned_phrase") for h in report.get("hits", []))


def _extract_facts(text):
    """Pull out numbers and capitalized multi-word spans (proper-noun-ish),
    for the post-rewrite integrity check. Cheap and deliberately conservative
    — false positives (flags something that's fine) are OK, false negatives
    (misses a dropped fact) are not."""
    numbers = re.findall(r"\b\d[\d,]*\.?\d*\b", text)
    caps = re.findall(r"\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)\b", text)
    return set(numbers), set(caps)


def rewrite_pass(text, call_llm_fn):
    """
    Rewrite text to remove AI tells, then verify no numbers/proper nouns
    were dropped. call_llm_fn(system_prompt, user_content) must return a
    plain string (not JSON) — pass content_provider.call_raw.

    Returns (clean_text, integrity_ok, dropped_facts).
    """
    system_prompt = (
        "Rewrite the following text to remove AI-writing tells: banned "
        "stock words (delve, leverage, robust, showcase, tapestry, "
        "testament, journey, seamless, particular, unwavering, woven, "
        "etc.), banned stock "
        "phrases, rule-of-three list patterns, and uniform sentence "
        "rhythm. Vary sentence length naturally. Do NOT change the "
        "meaning, do NOT drop or alter any number, date, proper name, or "
        "specific detail. Return ONLY the rewritten text, no preamble, "
        "no markdown fences."
    )
    rewritten = call_llm_fn(system_prompt, text)

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
    min_score_to_rewrite OR it contains any banned_word/banned_phrase hit
    at all (see has_banned_hit) — a lone stock AI-tell word must never
    survive just because the overall score stayed low.
    """
    for page in pages:
        original = page.get("text", "")
        if not original.strip():
            continue
        report = scan(original)
        if report["score"] < min_score_to_rewrite and not has_banned_hit(report):
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
    mutating a page list. Same has_banned_hit override as above applies."""
    report = scan(text)
    if report["score"] < min_score_to_rewrite and not has_banned_hit(report):
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
