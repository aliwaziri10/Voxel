# Voxel - Handoff

Read this first. Last rewritten 2026-09-21 (verified live against `main`).
Rule zero: verify against live files before saying anything is missing or
done. Before saying a file "does not exist", check `main` and the branches
`book4-progress-saving` and `book4-pipeline-fixes`.

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
- `novels/amity-falls-book-4/PROOFREAD_REPORT.md` (written by the workflow)
- `novels/amity-falls-book-4/amity-falls-book-4_full_manuscript.md` (compiled
  copy; rebuilt by the proofread script, see below)
- There is no book-level `HANDOFF.md` for Book 4. This file is the handoff.

Repo-wide docs on `main`: `PLAYBOOK.md`, `GENRE_DECISION.md`,
`CLAUDE_HANDOFF_2026-09-18.md`, `novels/PIPELINE_SPEC.md`,
`novels/EDITORIAL_CHARTER.md` (read before touching any chapter).

Other new title: `novels/kindling-line-book-1/` (romantasy series, started
2026-09-21; architecture and book config only).

## Book 4 proofreading state (2026-09-21)

CONFIRMED live:
- Book 4 is complete: 45 chapters, about 140,000 words.
- Em dashes: 0 in all 45 chapters (workflow run of `proofread.yml` with
  `book=all-unpublished`, `auto_fix` on, commit `8d7749f`). Em dashes became
  ` - ` in 30 chapters; chapters 2 and 18 had been fixed earlier.
- Two en dashes remain on purpose: `1847–Present` (ch.38) and `1900–Present`
  (ch.43). They are number ranges, not dashes.
- `amity-falls-book-4_full_manuscript.md` was overwritten with the text
  `FILE_CONTENT_PLACEHOLDER` by commit `71b2378` (2026-09-21 03:41 UTC).
  The chapter files were not affected.

PUSHED, NOT YET RUN (commit `83c0e2d`, `scripts/proofread_novel.py`):
- Rewords the AI-tell phrases ("particular", "the kind of", "woven",
  "eyes widened", "the specific") at exact known spots in 17 chapters.
- Rebuilds the full manuscript from the 45 chapter files and stages it.
- Book 4 floor 2,500 and ceiling 4,500 words (the workflow inputs would
  otherwise use 1,900 and 2,500).
- Duplicate-sentence hard check now applies to sentences of 60+ characters.
- Tested on a local copy of all 45 chapters before pushing.
- To apply: run `proofread.yml` again with `book=all-unpublished` and
  `auto_fix` on.

STILL OPEN after that run:
- Word-count floor (2,500): chapters 1 (2,301w), 14 (2,214w), 17 (1,561w),
  18 (1,531w), 20 (1,920w), 37 (1,949w), 44 (2,325w), 45 (1,623w). Needs new
  sub-beats per the Charter, never padding.
- Chapter 5 is 6,602 words, over the 4,500 ceiling.
- Chapter 8 repeats the same journal entry twice by design (a silent read,
  then a recorded read). Left as is; it will stay flagged.
- Continuity read (Charter): strict sequential manual read of all 45
  chapters has not been done. The mechanical script cannot do it.
- `architecture.md` open items: word-floor contradiction between it and the
  Charter (locked decision is 2,500 to 4,500); Ambrose/Castellan naming.

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
