# Voxel - Handoff

Read this first. Last rewritten 2026-09-20 (end of a very long session).
Rule zero for any session or profile: before saying a file "does not
exist", check ALL THREE branches listed below. Two sessions already wasted
time because Book 4's chapters were on a branch, not on main.

## WHERE EVERYTHING LIVES

Repo: `aliwaziri10/Voxel` (the working copy; connector account is
`aliwaziri10`). Upstream `Wazzaboyzz/Voxel` is stale, do not use it.
Branches: `main`, `book4-progress-saving`, `book4-pipeline-fixes`.

Published books (frozen, on `main`):
- `novels/where-the-frost-doesnt-reach/chapters/` (Book 1, 45 chapters)
- `novels/amity-falls-book-2/chapters/` (Book 2)
- `novels/amity-falls-book-3/chapters/` (Book 3)
- Per-book handoffs, beat maps and checklists sit beside each folder.
- Book 1's story bible is `novels/where-the-frost-doesnt-reach/architecture.md`.

Book 4 "The Secret She Kept Forever" (in progress, mostly on a BRANCH):
- Branch `book4-progress-saving` is the live one. It holds:
  - `novels/amity-falls-book-4/chapters/chapter_01.md` to `chapter_12.md`
    (only chapters 1-5, 7, 9, 11, 12 exist; 6, 8, 10 are missing)
  - `story_bibles/amity-falls.json`, the bible the pipeline reads — as of
    2026-09-20 13:56 this now holds the REVIEWED 45-chapter beat map
    (Constance corrected to Harriet everywhere) and the meta-leak guard
    is already live in `voxel_cli.py` on this branch. This happened
    BEFORE Zia's sign-off on `BEAT_MAP_45_DRAFT.md` — see next steps.
  - `novels/amity-falls-book-4/CHAPTER_REVIEW_2026-09-20.md` (verdict per
    chapter, the leak root cause)
  - `novels/amity-falls-book-4/CANON_CONFLICTS.md` (contradictions, pending
    fixes)
  - `novels/amity-falls-book-4/BEAT_MAP_45_DRAFT.md` (the plan that was
    pushed live into the bible above — treat as ALREADY APPLIED, not just
    a draft awaiting approval)
  - `novels/amity-falls-book-4/architecture.md` (narrative bible; the
    pipeline does NOT read it)
- `main` has only `architecture.md` and the OLD bible for Book 4.
- Branch `book4-pipeline-fixes` has 2 code fixes not on main or on
  `book4-progress-saving` (a KeyError fix and a corrected file push). Not
  reviewed or merged into either.
- The workflow `voxel-novel.yml` runs from `book4-progress-saving`.

Repo-wide docs on `main`: `PLAYBOOK.md` (tool commands), `GENRE_DECISION.md`,
`CLAUDE_HANDOFF_2026-09-18.md`, `novels/PIPELINE_SPEC.md`,
`novels/EDITORIAL_CHARTER.md`.

## Status (2026-09-20)

- Books 1-3 are published on KDP (ebook and paperback): Book 1 on
  2026-09-12, Books 2 and 3 on 2026-09-19. Book 1 had no sales in week one.
- Book 4 is a romance finale (slow burn, closed door, happy ending). Lead
  couple Wren Castellano and Theo Marsh. Zia decided: 45 chapters, every
  chapter 2,500 to 4,500 words, none below 2,500.
- Chapter 1 is proofread and fixed. Chapters 2, 3, 5, 9, 11, 12 need full
  rewrites (leaks and canon conflicts); chapter 4 needs a canon rewrite;
  chapter 7 needs real content to reach the floor. NONE of these existing
  chapters have been regenerated yet — the meta-leak guard only protects
  chapters written from here on; it does not retroactively fix these.
- The other chapters contain leaks such as "Book 3" said in dialogue, and
  bible notes pasted as prose. Cause: the bible was written as author notes.
  Fixed in the JSON on 2026-09-20; the old chapters are not repaired.

## Locked canon (Book 4)

- Theo's grandmother: alive, lost about ten years of memory (the decade
  before 2007) in Drake's first attempt in Millbrook 19 years ago. The
  bible now correctly says "Harriet" (the earlier "Constance" name
  collided with a published character and has been corrected).
- Wren's mother is alive and lives in the valley; her father left; her
  grandmother (a Finder) is dead. Wren has not yet paid a large memory debt.
- Drake is arrested by ordinary law. Dev's evidence work breaks his
  leverage. Yusuf backs Wren at once. Priya and Dev are siblings, no
  romance ever. Use full names Ambrose Kell and Ambrose Whitlock; keep
  Wren Castellano distinct from the minor character Castellan.

## Next steps, in order (do one at a time)

1. Zia reviews what already happened without waiting for approval: the
   45-chapter beat map (`BEAT_MAP_45_DRAFT.md`) is already live in
   `story_bibles/amity-falls.json` on `book4-progress-saving`, and the
   meta-leak guard is already live in `voxel_cli.py` there too. If Zia
   wants changes to the beat map, edit the bible directly rather than
   re-approving the draft file — the draft has already been applied.
2. Rewrite chapters 4, 5, 11, then 2, 3, 9, 12. Proofread 7. Re-run the
   tools after each: `humanizer.scan`, `scripts/proofread_novel.py`,
   `word_repetition_fixer.py`, `manuscript_qa.py`, plus a manual read.
3. Generate missing chapters 6, 8, 10. OpenRouter's free tier (50
   requests a day) is used up, and resets daily at 05:30 IST; adding
   credit is Zia's call.
4. Zia pastes workflow edits (`git pull --rebase` before push; env
   `WORD_MIN=2500 WORD_MAX=4500`; generator flags `--min-words 2500
   --max-words 4500`). The connector cannot write to `.github/workflows/`.
5. Merge `book4-pipeline-fixes`'s 2 unreviewed code fixes (KeyError,
   corrected file push) into `book4-progress-saving` before relying on
   them — they are not there yet.
6. Merge the branch to `main`, after reformatting the bible JSON so it can
   merge without conflict.

## Open risks

- Both repos were public last time checked and hold the published books.
  Zia wants this closed (private repo).
- `scripts/word_repetition_fixer.py` rewrites dashes unconditionally; run
  it only on copies of unpublished text.
- Two manuscript build routes exist (Node docx for Book 3, `scripts/
  build_manuscript.py`); which made the KDP files is unconfirmed.
- Untested end to end: sub-beat beat map, `pipeline.py`, `kdp_metadata.py`,
  `voxel_cli.py images`.

## Rules for anyone working here

- Zia is a non-coder working in a browser, often by voice. Paths and URLs
  go in their own code blocks; manual pastes are the whole file.
- Verify against live files and ALL branches before claiming anything is
  missing or done. Check names against every published chapter (grep) before
  inventing them.
- Published books are never edited, scanned with auto-fix, or padded.
- Re-fetch a file's SHA right before editing; several sessions work at once.
