# Voxel — Handoff

## READ-BEFORE-WRITE RULE (added 2026-09-22, do not remove or soften)
**Before touching ANY chapter, you must read ALL FIVE of these files in
full, in this order, not just this one:**
1. This file (`HANDOFF.md`) — orientation only.
2. `novels/EDITORIAL_CHARTER.md` — methodology, applies to every Voxel book.
3. `novels/amity-falls-book-4/PROOFED_LOG.md` — live source of truth,
   read the STAMP at the top first, it supersedes older sections below it.
4. `novels/amity-falls-book-4/CANON_NUMBERS.md`
5. `novels/amity-falls-book-4/DATES_BIBLE.md`

**Do this even if you are resuming mid-task and think you already know the
state.** The specific failure this rule exists to stop: on 2026-09-22, one
session read only this file's summary and ch.3, concluded "Ambrose is
correct, Josiah is a naming error," and pushed a revert across 6 chapters.
It had not read `CANON_NUMBERS.md` (which says Josiah is a real, distinct
person) or `DATES_BIBLE.md` (which says the same, in different and also
unverified detail) or ch.9 in full (which independently tells a whole
parallel story about Josiah with its own dates). Reading only one of these
four sources produces a confident, wrong answer — this has now happened
at least three times on this exact question. The fix is not "read ch.3
carefully," it's "read all four sources every time before concluding
anything," because the conflict lives in the disagreement BETWEEN them,
not inside any single one.

If, after reading all four, you find a NEW disagreement between two of
these files (not just chapter text vs. one file — file vs. file), do not
pick a winner. Stamp `PROOFED_LOG.md` with the conflict, cite the exact
line from each file, and leave the chapters and both files untouched
until Zia decides. Silently trusting the more recently-edited file, or
the one that "sounds more confident," is exactly the pattern that created
the current mess (see PROOFED_LOG.md's STAMP 2).

Rule zero (unchanged): verify against live `main` before claiming anything
is missing, done, or true. Read by commit SHA right after a push
(`raw.githubusercontent.com/aliwaziri10/Voxel/<sha>/<path>`) since a plain
`main` fetch can be briefly stale. Never trust a HANDOFF, log, or bible
claim over what the live chapter file actually says — every one of these
files has been wrong before, including this one, more than once.

## Where everything lives

Repo: `aliwaziri10/Voxel`. Upstream `Wazzaboyzz/Voxel` is stale, don't use it.

Published (frozen, never edited/scanned): `novels/where-the-frost-doesnt-reach/`,
`novels/amity-falls-book-2/`, `novels/amity-falls-book-3/` — all on `main`.

Book 4, "The Secret She Kept Forever," on `main`:
- `novels/amity-falls-book-4/chapters/chapter_01.md` .. `chapter_45.md` (complete)
- `novels/amity-falls-book-4/PROOFED_LOG.md` — **read this for current state,
  open questions, and what's decided vs. still needs Zia. Read the STAMP
  at the very top first — older sections below it may be superseded.**
- `novels/amity-falls-book-4/CANON_NUMBERS.md` — dates/ages/names reference.
  **As of 2026-09-22 this file disagrees with `DATES_BIBLE.md` on Josiah's
  identity — see PROOFED_LOG.md STAMP 2. Do not treat either as settled
  until that's resolved.**
- `novels/amity-falls-book-4/DATES_BIBLE.md` — separate dates/facts
  reference, overlaps with CANON_NUMBERS.md but was written independently
  and is not fully reconciled with it. Read both, not just one.
- `novels/amity-falls-book-4/architecture.md`, `PRE_PUBLISH_AUDIT_2026-09-21*.md`,
  `PROOFREAD_REPORT.md`, `amity-falls-book-4_full_manuscript.md`
- `scripts/book4_fixes.json`, `scripts/proofread_novel.py` (mechanical fixer;
  see the log for how exact-text fixes are applied — old/new pairs, applies
  once, skips silently if already applied)
- `story_bibles/amity-falls.json`

Other: `novels/kindling-line-book-1/` (separate romantasy series, don't mix
with Amity Falls).

## Current state (see PROOFED_LOG.md for full detail — this is a summary)

Sequential real read: chapters 1–26 done. 27–45 not yet read. Several
mechanical fixes applied and verified live (ages, names, an em dash, a
truncated sentence).

**Josiah vs. Ambrose Whitlock: NOT RESOLVED. Live text is currently mixed
and that is CORRECT for now — do not "fix" it either direction.** Ch.2, 6,
7, 12, 13, 15 currently say Josiah. Ch.3, 5, 14, 19, 21 say Ambrose. Ch.9
names both, as two different people, generations apart. This has been
decided wrong at least three times already by sessions that read only a
subset of the five files above — see PROOFED_LOG.md's STAMP 2 for the full
trail, including the two real options (A: one person, naming error; B: two
people, intended parallel) that need Zia's decision, not another guess.
**Do not add or remove a single "Josiah" or "Ambrose" reference anywhere
in the book until that decision is made and stamped.**

Five other structural questions were flagged for Zia; he delegated the
call, and those decisions are in the log along with two open items: Q21
(superseded into the Josiah/Ambrose framing above) and Q22 (Martha
Whitlock's relation to Ambrose in ch.22, still unfixed, still needs Zia).

## Rules for anyone working here

- **Read all five files listed at the top before touching a chapter.**
  See the READ-BEFORE-WRITE RULE above — this is the single most important
  rule in this file and the one most often skipped.
- Zia is a non-coder, browser-only, often by voice. Small steps, code
  blocks for anything copyable, decide technical calls yourself rather than
  asking him to check things — except genuine two-way canon conflicts like
  Josiah/Ambrose, which are his call, not a technical decision.
- Before asserting any canon fact ("X tried the bargain," "Y is Z's
  grandmother"), read the actual chapter text yourself, AND check it
  against both CANON_NUMBERS.md and DATES_BIBLE.md. This project's biggest
  recurring failure mode is confidently repeating an earlier session's
  conclusion, or a single file's claim, without cross-checking every
  source — this has happened at least three times now on the same
  question (Elena Castellano, and Josiah/Ambrose, twice). A prior fix
  landing in 6 chapters is not evidence it was right; it's evidence a
  prior session was confident.
- Published books are never edited, scanned, or padded.
- Never push a placeholder as content. After any push, re-fetch and compare.
- Never claim a fix is applied without reading it back from the repo.
- Update `PROOFED_LOG.md`, not this file, with new findings. Keep this file
  short — it should describe where to look, not carry the facts themselves.
