#!/usr/bin/env python3
"""
proofreader.py - grammar/punctuation flagging + date/math consistency
checking for Voxel manuscripts. Separate from humanizer.py on purpose:
humanizer.py checks for AI-writing STYLE tells (does this sound like an
LLM wrote it); this file checks for CORRECTNESS (is it grammatically
right, are commas/full stops/italics used consistently, do the dates and
ages actually add up across chapters). A chapter can pass one check and
fail the other - they are different failure modes and are kept as two
scripts so a run of one never silently substitutes for the other.

Built 2026-09-25 per Zia, in response to the specific pattern that caused
Book 4's date/continuity mixups: the fact existed in CANON_NUMBERS.md, but
nothing ever cross-checked it against what a chapter actually stated, so
drift only ever got caught by a human happening to notice. This file's
date_consistency_check() closes that gap mechanically, and it does NOT
try to parse relative dates out of prose ("three days after the
Reckoning") - that is unreliable regex/NLP work and would create false
confidence. Instead every chapter file carries a small, non-reader-facing
metadata header stating its own in-world date explicitly (see
CHAPTER_DATE_HEADER_RE below), and this script compares that header
against the beat map's locked date for the same chapter number and
against the book's CANON_NUMBERS.md. A metadata header is a simple,
reliable string/number to diff; prose is not.

Like humanizer.py's rewrite_pass, nothing in this file auto-fixes
anything. Grammar/punctuation issues and date mismatches are both
FLAGGED ONLY, for a human (or the next stamped sequential review pass
per EDITORIAL_CHARTER.md) to resolve - silently "correcting" a date
mismatch is worse than the original bug, since the script has no way to
know which of two conflicting dates is actually right.

Usage as a library:
    from proofreader import grammar_scan, date_consistency_check

    report = grammar_scan(chapter_text, call_llm_fn)
    # -> {'flags': [{'type': str, 'quote': str, 'note': str}, ...]}

    result = date_consistency_check(chapter_text, chapter_number, beat_map,
                                     canon_numbers_text)
    # -> {'chapter_date': str or None, 'mismatches': [...]}
"""

import re


# --- Chapter metadata header -------------------------------------------------
# Every chapter file should open with a small HTML-comment header (invisible
# to an e-reader, harmless if a raw .md file is read as prose) stating the
# chapter's own in-world date, e.g.:
#   <!-- chapter_date: 14 Emberfall, Year 3 of the Reckoning Accord -->
# This is written by whoever drafts the chapter, taken directly from the
# beat map's locked date for that chapter (see generate_beat_map's new
# "chapter_date" field in content_provider.py). It is metadata, not prose -
# never delete it when editing a chapter, and never let a rewrite pass
# (humanizer.py) touch it, since rewrite_pass only operates on the prose
# body a caller passes in.
CHAPTER_DATE_HEADER_RE = re.compile(
    r"<!--\s*chapter_date:\s*(.+?)\s*-->", re.IGNORECASE
)


def extract_chapter_date(chapter_text):
    """Returns the chapter's stated in-world date from its metadata header,
    or None if the header is missing. A missing header is itself worth
    flagging (see date_consistency_check) - it means this chapter was
    drafted before this convention existed, or someone forgot it."""
    match = CHAPTER_DATE_HEADER_RE.search(chapter_text)
    return match.group(1).strip() if match else None


def date_consistency_check(chapter_text, chapter_number, beat_map, canon_numbers_text=""):
    """
    Mechanical (no LLM) cross-check of one chapter's stated date against:
      1. The beat map's locked date for this chapter number (if the beat
         map entry has a "chapter_date" field - see content_provider.py).
      2. A plain substring check against canon_numbers_text, if given -
         this only catches an EXACT date string that appears in the
         chapter but conflicts with a date the same chapter number is
         expected to carry; it does not try to do calendar arithmetic.

    Returns {'chapter_date': str or None, 'mismatches': [...]}. An empty
    mismatches list with chapter_date=None means "nothing to check yet,
    add the header" - that is itself worth surfacing to whoever reviews
    this chapter, not silently skipped.
    """
    chapter_date = extract_chapter_date(chapter_text)
    mismatches = []

    if chapter_date is None:
        mismatches.append({
            "type": "missing_date_header",
            "note": f"Chapter {chapter_number} has no <!-- chapter_date: ... "
                     "--> header. Add one matching the beat map's locked "
                     "date for this chapter before this chapter is marked "
                     "reviewed - this is exactly the gap that let dates "
                     "drift silently in earlier books.",
        })
        return {"chapter_date": None, "mismatches": mismatches}

    beat_entry = next(
        (b for b in beat_map if b.get("chapter") == chapter_number), None
    )
    if beat_entry is None:
        mismatches.append({
            "type": "no_beat_map_entry",
            "note": f"No beat map entry found for chapter {chapter_number} - "
                     "cannot verify its date against the plan.",
        })
    else:
        locked_date = beat_entry.get("chapter_date")
        if locked_date and locked_date.strip() != chapter_date.strip():
            mismatches.append({
                "type": "date_beat_map_mismatch",
                "chapter_stated": chapter_date,
                "beat_map_locked": locked_date,
                "note": f"Chapter {chapter_number} states '{chapter_date}' "
                         f"but the beat map locks this chapter's date as "
                         f"'{locked_date}'. Resolve which is correct before "
                         "proceeding - do not guess.",
            })

    if canon_numbers_text and chapter_date not in canon_numbers_text:
        mismatches.append({
            "type": "date_not_in_canon",
            "chapter_stated": chapter_date,
            "note": f"'{chapter_date}' does not appear anywhere in "
                     "CANON_NUMBERS.md. Either this is a new date that "
                     "needs to be added there, or it's a typo/drift from "
                     "an existing locked date - check by hand.",
        })

    return {"chapter_date": chapter_date, "mismatches": mismatches}


# --- Grammar / punctuation (LLM flag-only pass) ------------------------------
_GRAMMAR_SYSTEM_PROMPT = """\
You are a meticulous copy editor. Read the chapter text below and find
GENUINE grammar, punctuation, and mechanical errors only - not style
preferences, not word choice, not anything already covered by an
AI-writing-tell checker elsewhere in this pipeline. Specifically check:

- Grammar: subject-verb agreement, tense consistency within a scene
  (an unmarked tense shift mid-scene is an error; a deliberate flashback
  is not), dangling/misplaced modifiers, sentence fragments used as an
  error rather than a deliberate stylistic beat.
- Commas: missing comma before a coordinating conjunction joining two
  independent clauses, comma splices, missing comma after an introductory
  clause, incorrectly comma-separated restrictive clauses.
- Full stops / sentence boundaries: run-on sentences, missing terminal
  punctuation.
- Italics: inconsistent use for internal thought, invented in-world terms,
  or emphasis - e.g. a term italicized on first use but not on later uses,
  or the reverse, within the same chapter.
- Dialogue punctuation: comma vs period before a closing quote when a
  dialogue tag follows, missing or misplaced quotation marks.

Do NOT flag: word choice, stock-phrase/AI-tell issues (a separate tool
already checks those), plot/continuity issues (a separate tool already
checks those), or a deliberate sentence fragment/run-on used as a clear
stylistic choice in dialogue or tense internal narration.

Return ONLY a JSON array, no markdown fences, no preamble. Each item:
  {"type": "grammar"|"comma"|"full_stop"|"italics"|"dialogue_punctuation",
   "quote": "the exact short span of text containing the error (under 20 words)",
   "note": "one sentence: what's wrong and the fix"}
Return an empty array [] if you find nothing genuine. Do not invent issues
to have something to report.
"""


def grammar_scan(chapter_text, call_llm_fn):
    """
    LLM-based flag-only grammar/punctuation pass. call_llm_fn(system_prompt,
    user_content) must return a plain string - pass content_provider.call_raw,
    same as humanizer.rewrite_pass does.

    Returns {'flags': [...]}. Never auto-fixes - same reasoning as
    humanizer.py's rewrite_pass integrity gate and date_consistency_check
    above: a flag needs a human or a stamped sequential review pass to
    resolve, not a silent auto-correction that might be wrong.
    """
    import json

    raw = call_llm_fn(_GRAMMAR_SYSTEM_PROMPT, chapter_text)
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.strip("`")
        if raw.lower().startswith("json"):
            raw = raw[4:].strip()

    try:
        flags = json.loads(raw)
        if not isinstance(flags, list):
            raise ValueError("Expected a JSON array")
    except (json.JSONDecodeError, ValueError) as e:
        return {"flags": [], "error": f"Could not parse grammar-scan response: {e}. Raw: {raw[:300]}"}

    return {"flags": flags}


def full_proofread(chapter_text, chapter_number, beat_map, call_llm_fn, canon_numbers_text=""):
    """
    Convenience wrapper: runs both checks and returns a combined report.
    Does not run humanizer.py's AI-tell scan - call that separately, it's
    a different tool for a different failure mode. Meant to be called
    per-chapter alongside humanizer.humanize_text, not as a replacement
    for the sequential stamped review pass in EDITORIAL_CHARTER.md - this
    is the mechanical pre-check that pass reads before starting.
    """
    grammar = grammar_scan(chapter_text, call_llm_fn)
    dates = date_consistency_check(chapter_text, chapter_number, beat_map, canon_numbers_text)
    return {
        "chapter": chapter_number,
        "grammar_flags": grammar.get("flags", []),
        "grammar_scan_error": grammar.get("error"),
        "chapter_date": dates["chapter_date"],
        "date_mismatches": dates["mismatches"],
    }
