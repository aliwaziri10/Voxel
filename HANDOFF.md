# Voxel - Handoff

Read this first. Last rewritten 2026-09-21 (verified live against `main` at
commit `89e5405`). Read `novels/EDITORIAL_CHARTER.md` before touching any
chapter.

Rule zero: verify against live files before saying anything is missing or
done. Before saying a file "does not exist", check `main` and the branches
`book4-progress-saving` and `book4-pipeline-fixes`. A `raw.githubusercontent.com`
read right after a push can be stale; read by commit SHA instead
(`.../Voxel/<commit-sha>/path`).

## WHERE EVERYTHING LIVES

Repo: `aliwaziri10/Voxel` (connector account is `aliwaziri10`). Upstream
`Wazzaboyzz/Voxel` is stale, do not use it.

Published books (frozen, on `main`, never edited or scanned):
- `novels/where-the-frost-doesnt-reach/chapters/` (Book 1, 45 chapters)
- `novels/amity-falls-book-2/chapters/` (Book 2)
- `novels/amity-falls-book-3/chapters/` (Book 3)

Book 4 "The Secret She Kept Forever" is on `main`:
- `novels/amity-falls-book-4/chapters/chapter_01.md` to `chapter_45.md`
  (all 45 exist; the book is complete)
- `novels/amity-falls-book-4/architecture.md` (story bible, ending confirmed)
- `novels/amity-falls-book-4/PRE_PUBLISH_AUDIT_2026-09-21.md` (the list of
  timeline and canon contradictions this handoff works from)
- `novels/amity-falls-book-4/PROOFREAD_REPORT.md` (written by the workflow)
- `novels/amity-falls-book-4/amity-falls-book-4_full_manuscript.md` (compiled
  copy, rebuilt by the proofread script)
- `scripts/book4_fixes.json` (exact-text fixes the proofread script applies;
  see "How fixes are applied")
- There is no book-level `HANDOFF.md` for Book 4. This file is the handoff.

Repo-wide docs on `main`: `PLAYBOOK.md`, `GENRE_DECISION.md`,
`CLAUDE_HANDOFF_2026-09-18.md`, `novels/PIPELINE_SPEC.md`.

Other new title: `novels/kindling-line-book-1/` (romantasy series, started
2026-09-21; architecture and book config only).

## Book 4 proofreading state (2026-09-21)

CONFIRMED live:
- 45 chapters, about 145,450 words. Em dashes: 0 in every chapter.
- Batch 1 fixes are APPLIED: the workflow run committed `7bfb33d` at 06:14 UTC
  and all 47 entries in `scripts/book4_fixes.json` are present in the chapters
  (checked by exact text).
- Pre-publish audit (`7350cac`): NOT ready to publish yet. Prose is clean;
  timeline and canon are not. Batch 1 fixed part of that list (below).

WORD COUNTS ARE APPROVED (Zia, 2026-09-21): short and long chapters in Book 4
stay exactly as they are. Do NOT flag them, do NOT pad them, do NOT list them
as open work. `scripts/proofread_novel.py` (commit `89e5405`) no longer
reports Book 4 word counts at all. The same commit lets chapter 8's
deliberately repeated Drake letter pass the duplicate-sentence check. Dry run
on the live chapters: 0 hard violations, exit code 0.

### Canon lock (decisions made 2026-09-21; reversible via git)

Fixed by the bible (`story_bibles/amity-falls.json`) and Books 1 to 3:
- Present day is autumn 2024. Drake's clock is about 30 days, so the book is
  one autumn (October into November).
- Harriet Marsh, born 1949 (75 now), lost 1997 to 2007 (ages 48 to 58).
  Drake's first attempt was 2005 (nineteen years ago), inside that decade.
- Theo born 1997. Harriet's husband Thomas died 2003, during the lost decade.
- Ring ritual (Book 3): 2023. Denise was freed by the split-the-weight ritual
  (Book 2), March 2022, ending 50 years of renewals (1972 to 2022).
- Millbrook is a two-hour drive from the valley.
- Adelaide's surname is Whitlock (Book 2). Denise Voss was 31 in 1981 (Book 2).
- Ambrose Whitlock died in 1945 (Book 3, chapter 5). His failed attempt to end
  the bargain is 1889 (chapter 3).
- Yusuf is the current Warden only since Denise was freed; the role was vacant
  after the previous Warden died in 1987.
- Drake is arrested in chapter 41, not before.

### Worklist, in order (strict chapter order inside each batch)

Batch 1: DONE and verified (above).

Batch 2, needs one decision before editing (Whitlock era). The book treats
Ambrose Whitlock as both an 1870 to 1901 Warden and a modern man alive in
2003 to 2009. Published Book 3 says he died in 1945, so the modern one cannot
be Ambrose. Recommended: keep Ambrose as the early-1900s figure and make the
modern "A.W." a descendant. Places: chapter 5 (journal signed A.W., "died in
2009", box sealed 2005, Adelaide called Ambrose's mother), chapter 37 ("Warden
of the first debt in 2003"), chapter 42 ("tried to end the bargain in 1923"
versus 1889 in chapter 3), 1847 and 1863 entries signed by Whitlock in
chapters 2, 4, 6 and 9, chapter 15 (Harriet's husband speaking of Whitlock in
the 1970s), chapter 19 (Whitlock's archive holding a 1974 record).

Batch 3, seasons and countdown: seasons wander (chapter 5 late summer, 8
January to February, 16 spring, 17 August, 28 April, 36 September to
October); Drake's clock reads 30 days, 4 days, 2 weeks, 12 days, 9 days, 6
and 10 days; deadline "the solstice" (chapter 8) versus "summer solstice"
(chapter 26).

Batch 4, canon: the ring versus split-the-weight ritual is mixed up in
chapter 39 ("ten volunteers split the weight of Denise's debt"); Drake's
claim in chapter 30 (Thomas Marsh's debt) is never answered outright, though
chapter 41 shows the extraction files; Harriet's family (granddaughter, "a
daughter who never existed", "grandmother of one"); Drake's collapse (chapter
22 substitution versus chapter 45 falsified trust record; FBI and state
police versus Millbrook Sheriff); Castellan (chapter 2 family in the 1860s,
chapter 22 clerk from 1981; Book 3 has Castellan as a young ring volunteer).

Author decisions, not errors: no proposal scene in chapter 44 (the beat map
called for one); chapter 45 recaps the romance stages as a summary paragraph;
real places (Harrisburg, Delaware, Ohio, Wilmington) inside a fictional
county. Chapter 8 repeats the same journal entry twice by design.

Not done: the Charter's strict sequential manual read of all 45 chapters, and
a check of Book 4 against the full text of Books 1 to 3 beyond the anchors
above. `architecture.md` still has a word-floor contradiction with the locked
2,500 to 4,500 range; word counts are approved as they stand, so leave it.

### How fixes are applied

`scripts/book4_fixes.json` is `{"chapter_NN.md": [[old, new], [old, new,
"all"]]}`. An entry applies only if `old` appears exactly once (or, with
`"all"`, at least once). Already-applied entries are skipped silently. Test
every new entry against the live chapter text before pushing. To apply: run
`proofread.yml` with `book=all-unpublished` and `auto_fix` on, then re-fetch
the chapters and confirm.

## Rules for anyone working here

- Zia is a non-coder working in a browser, often by voice. Paths and URLs
  go in their own code blocks; manual pastes are the whole file.
- The connector cannot write to `.github/workflows/`; Zia pastes workflow
  edits.
- Verify against live files and ALL branches before claiming anything is
  missing or done. Re-fetch a file's SHA right before editing; several
  sessions work at once.
- Published books are never edited, scanned with auto-fix, or padded.
- Never push a placeholder as file content. After any push, re-fetch and
  compare.
