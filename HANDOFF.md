# Voxel - Handoff

Read this first if you are new to this repo (human or AI). Short on purpose:
current status, hard rules, and open problems only. History lives in git.
Last corrected 2026-09-19 after reviewing the commit log (latest 200
commits, through 2026-09-19 01:54 UTC) and the live files listed below.

## Status (2026-09-19)

- **Books 1-3 of the Amity Falls series are published on Amazon KDP (ebook
  and paperback).** Stated by Zia: Book 1 went live 2026-09-12, Books 2 and
  3 on 2026-09-19. No ASINs or links are stored in the repo.
  - Book 1: Where the Frost Doesn't Reach
  - Book 2: working title "What the Valley Still Owes" (confirm the final
    published title)
  - Book 3: What the Blood Remembers
- **Published books are frozen.** Never edit, pad, rebuild or scan them.
- **No book is in progress.** Book 1 had no sales in its first week.
  Genre direction for the next book is NOT decided: see `GENRE_DECISION.md`.
- Also built earlier: Luna and the Lost Star (picture book).

## Read in this order

1. `GENRE_DECISION.md` - genre research, ranked options, draft contract,
   and what round 2 must do. Nothing gets written before this is settled.
2. `CLAUDE_HANDOFF_2026-09-18.md` - the proofreading/tooling audit: the
   five QA tools and what each one can and cannot edit.
3. `novels/PIPELINE_SPEC.md` - the Book 4+ state machine
   (`scripts/pipeline.py`, `book_config.py`, `kdp_metadata.py`), the
   AI-disclosure gate and `VOICE_GUIDE_TEMPLATE.md`.
4. `PLAYBOOK.md` - tool-by-tool commands. Two of its cautions are now
   fixed (see problems 1 and 3 below); trust this file over it.
5. `novels/EDITORIAL_CHARTER.md` - mandatory before touching ANY novel
   chapter (no padding; Book 4+ floor 2,300 words, ceiling about 2,700).
6. `README.md`, `ARCHITECTURE.md` - background only, not re-audited.

## Which repo and which account

- Working copy: `aliwaziri10/Voxel`. The connector authenticates as
  `aliwaziri10`; confirm with `get_me` each session.
- `Wazzaboyzz/Voxel` is the stale upstream (last commit 2026-09-14). Do not
  work there.
- **Both repos were public when last checked (2026-09-19) and hold the full
  text of the published books.** Zia wants this closed. Not done yet.
  GitHub often blocks making a fork of a public repo private; if the option
  is greyed out, create a new private repo and move the files.
- **The connector cannot write to `.github/workflows/` (403).** A GitHub
  App scope limit. Zia must paste workflow changes in the web editor.
  Everything else writes fine via the API.

## Rules for anyone working here

- Zia is a non-coder working in a browser, often by voice dictation. Give
  paths and URLs on their own lines; for manual pastes give the full file.
- Treat every status claim, including this file's, as unverified until
  checked against live files and commits.
- Re-fetch a file's live contents and SHA right before editing it; several
  sessions may work at once. Confirm pushes landed via the API.
- Add or update a test when changing shared code. Do not claim a change
  works without running it.
- Do not add a book to the published or unpublished lists on inference.
  Only on Zia's direct confirmation.

## Open problems (checked against the commit log, 2026-09-19)

Fixed since the earlier version of this list:
- `proofread_novel.py` now blocks all three published books (commit
  `25e8230`); `auto_fix` is off by default in `proofread.yml`.
- `manuscript_qa.py` has the same published-book block (`cdfa51f`).
- `voxel_cli.py novel` now writes to `novels/<book-slug>/chapters/`
  (`fceda1c`). Untested end to end.
- The stale root `PROOFREAD_REPORT.md` was deleted (`6358b59`).

Still open, most urgent first:
1. **`scripts/word_repetition_fixer.py` has no published-book block** and
   rewrites dashes unconditionally. The last unprotected tool that can
   change chapter text. `voxel-audit.yml` also has no block (report only).
2. **No genre contract or story bible stage.** `pipeline.py` starts at
   `outline`, so nothing fixes the genre or series canon before drafting.
   Also `story_bibles/` is not in the repo, so `voxel_cli.py novel` has no
   memory of Books 1-3. Plan: see `GENRE_DECISION.md`.
3. **Two manuscript-build routes.** Book 3 was built with Node `docx`
   (Garamond, justified, first-line indent). `scripts/build_manuscript.py`
   (used by `pipeline.py`) does not do that formatting. Which one made the
   KDP files is unconfirmed.
4. **Untested end to end:** the sub-beat beat map, `pipeline.py`,
   `kdp_metadata.py`, `voxel_cli.py images`. No test exists for
   `humanizer.py`, `story_bible.py`, `voxel_cli.py` or `pipeline.py`.
5. **`humanizer.py` was just rewritten in the GitHub web editor**
   (`34bcf7d`, 2026-09-19 01:54) with categorized, strength-ranked
   patterns. The session note that asked Zia to choose between porting the
   patterns and calling external skills was never answered; the commit
   looks like option (a). Unreviewed and untested.
6. **Old per-book handoffs are long review logs** (Book 2 was 33 KB and
   Book 1 18 KB when last checked). The series canon inside them must be
   kept, condensed into one canon file, before anything is deleted.
7. **Leftovers:** `generate_images.py` is a third image path,
   `video_output.py` is unwired, `build-book.yml` duplicates
   `voxel-book.yml`.

## Not yet reviewed (be honest about this)

The commit log before 2026-09-15 20:19 UTC (page 3 onward) and these files
were not opened in the last review: `pipeline.py`, `book_config.py`,
`kdp_metadata.py`, `BOOK_CONFIG_TEMPLATE.json`, `VOICE_GUIDE_TEMPLATE.md`,
the new `humanizer.py` and `content_provider.py`, `story_bible.py`,
`README.md`, `ARCHITECTURE.md`, the seven workflows and the Book 1/2
handoffs.
