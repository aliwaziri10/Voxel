# Voxel - Handoff

Read this first if you are new to this repo (human or AI). Short on purpose:
current status, hard rules, and open problems only. History lives in git.
Last corrected 2026-09-19 (late) after re-reading the newest commits.

## Status (2026-09-19)

- **Books 1-3 of the Amity Falls series are published on Amazon KDP (ebook
  and paperback).** Stated by Zia: Book 1 went live 2026-09-12, Books 2 and
  3 on 2026-09-19. No ASINs or links are stored in the repo.
  - Book 1: Where the Frost Doesn't Reach
  - Book 2: working title "What the Valley Still Owes" (confirm the final
    published title)
  - Book 3: What the Blood Remembers
- **Published books are frozen.** Never edit, pad, rebuild or scan them.
- **Book 4 is in production planning, run by another session.** Per commits
  on 2026-09-19: title locked as "The Secret She Kept Forever"; lead couple
  Wren and Theo; the real story bible is `novels/amity-falls-book-4/
  architecture.md` plus `story_bibles/amity-falls.json` (the file the
  pipeline actually reads, populated with Books 1-3 continuity and Book 4
  plot facts). A live 60-chapter beat-map run was made and hit a
  chapter-count bug that was then patched (retry on wrong count).
  Zia's genre decision stands: small-town slow-burn romance finale, closed
  door, happy ending, no rituals.
- **As of the last check there is NO Book 4 chapter text in the repo**
  (no `chapters/` folder). Nothing can be proofread until chapter text is
  committed or pasted.
- The old planning draft I wrote earlier was deleted as stale (commit
  `146d999`). It ignored the real bible. Do not resurrect it.
- Book 1 had no sales in its first week. Marketing Books 1-3 still matters
  more than a fourth book.
- Also built earlier: Luna and the Lost Star (picture book).

## Read in this order

1. `novels/amity-falls-book-4/architecture.md` and
   `story_bibles/amity-falls.json` - the Book 4 bible and its live
   continuity guardrails.
2. `GENRE_DECISION.md` - genre research and round 2 plan (some of its
   pipeline advice is now overtaken by the real bible work).
3. `CLAUDE_HANDOFF_2026-09-18.md` - the proofreading/tooling audit.
4. `novels/PIPELINE_SPEC.md` - the Book 4+ state machine.
5. `PLAYBOOK.md` - tool commands. Its cautions about the proofread
   blocklist and folder layout are fixed; trust this file.
6. `novels/EDITORIAL_CHARTER.md` - mandatory before touching ANY novel
   chapter (no padding; Book 4+ floor 2,300 words).
7. `PROJECT_ISOLATION_RULES.md` exists only in `Wazzaboyzz/Voxel`. It bars
   mixing picture-book and novel rules. Read it before editing shared code.

## Which repo and which account

- Working copy: `aliwaziri10/Voxel`. The connector authenticates as
  `aliwaziri10`; confirm with `get_me` each session.
- `Wazzaboyzz/Voxel` is the upstream and holds files this fork lacks:
  `PROJECT_ISOLATION_RULES.md`, `OWNERSHIP.md`, `generate_character_sheet.py`,
  and much larger `image_provider.py` and `story_bible.py` (sizes differ
  from the fork's). The two repos have diverged; do not assume they match.
- **Both repos were public when last checked and hold the full text of the
  published books.** Zia wants this closed. Not done yet.
- **The connector cannot write to `.github/workflows/` (403).** Zia must
  paste workflow changes in the web editor.

## Rules for anyone working here

- Zia is a non-coder working in a browser, often by voice dictation. Give
  paths and URLs on their own lines; for manual pastes give the full file.
- Treat every status claim, including this file's, as unverified until
  checked against live files and commits. Read the newest commits before
  claiming anything is missing.
- Re-fetch a file's live contents and SHA right before editing it; several
  sessions work at once. Confirm pushes landed via the API.
- Add or update a test when changing shared code. Do not claim a change
  works without running it.
- Do not add a book to the published or unpublished lists on inference.

## Open problems

1. **`scripts/word_repetition_fixer.py` has no published-book block** and
   rewrites dashes unconditionally. Run it only on copies of Book 4 text.
2. **Book 4 chapter text is not in the repo** (see Status).
3. **Two manuscript-build routes** (Node `docx` for Book 3 versus
   `scripts/build_manuscript.py`); which made the KDP files is unconfirmed.
4. **Untested end to end:** the sub-beat beat map, `pipeline.py`,
   `kdp_metadata.py`, `voxel_cli.py images`.
5. **Fork versus upstream drift** (see above).
6. **Old per-book handoffs are long logs;** keep the canon before deleting.
7. **Possible name problems in published books** (Ambrose Kell vs Ambrose
   Whitlock, Castellano vs Castellan). Book 4's bible now carries these as
   guardrails. Do not edit published text.
8. **Leftovers:** `generate_images.py`, unwired `video_output.py`,
   redundant `build-book.yml`.

## Not yet reviewed

Older commits before 2026-09-15 20:19 UTC, and: `architecture.md` for Book
4, `story_bibles/amity-falls.json`, `pipeline.py`, `book_config.py`,
`humanizer.py` (rewritten 2026-09-19, now has `test_humanizer.py`),
`README.md`, `ARCHITECTURE.md`, the seven workflows.
