# Voxel - Handoff

Read this first if you are new to this repo (human or AI). Short on purpose:
current status, hard rules, and known problems only. Anything historical
lives in git history, not here. Last rewritten 2026-09-19.

## Status (2026-09-19)

- **Books 1-3 of the Amity Falls series are published on Amazon KDP (ebook
  and paperback)** - stated by Zia on 2026-09-19. The repo cannot confirm
  this (no ASINs or listing links are stored here).
  - Book 1: Where the Frost Doesn't Reach
  - Book 2: working title "What the Valley Still Owes" (confirm the final
    published title; the old notes only called it tentative)
  - Book 3: What the Blood Remembers
- **Published books are frozen.** Do not edit their chapters, and never pad
  them to a newer word-count standard.
- No book is currently in progress. Next work is Book 4 or a new title.
- Also built earlier: Luna and the Lost Star (picture book), made with the
  same pipeline.

## Read in this order

1. `PLAYBOOK.md` - every tool used to make Books 1-3, with the exact
   command, what it does, and how to use it for Book 4+.
2. `novels/EDITORIAL_CHARTER.md` - mandatory before touching ANY novel
   chapter. Roles, no-padding rule, sequential review, Book 4+ word floor
   (2,300 minimum, about 2,700 natural ceiling).
3. `README.md` and `ARCHITECTURE.md` - background only. Last reconciled
   2026-09-13 and NOT re-audited in this rewrite; verify before trusting.

## Which repo and which account

- Working copy: `aliwaziri10/Voxel`. The GitHub connector authenticates as
  `aliwaziri10`. Confirm with `get_me` at the start of every session.
- `Wazzaboyzz/Voxel` is the old upstream and is stale (last commit
  2026-09-14). Never work there.
- **The connector cannot write to `.github/workflows/` (403).** This is a
  GitHub App scope limit, not a repo setting. Workflow files must be pasted
  by Zia in GitHub's web editor:
  `https://github.com/aliwaziri10/Voxel/edit/main/.github/workflows/<file>.yml`
  Everything else (`.py`, `novels/`, `scripts/`, docs) writes fine via the API.
- `push_logger.py` exists only because of that limit: it is a manual step
  inside `voxel-book.yml` and `voxel-novel.yml`, and does not run on a plain
  push.

## Rules for anyone working here

- Zia is a non-coder working in a browser, often by voice dictation. Give
  file paths and URLs on their own lines. For manual pastes, give the full
  file, never "find this line and change it".
- Every status claim, including in this file, is a hypothesis until checked
  against the live repo (commit history, real file contents, real word
  counts).
- After pushing an edit, confirm it landed via the GitHub API. Fetching from
  `raw.githubusercontent.com` right after a push can return a cached copy.
- Several sessions or profiles may work at once. Re-fetch a file's live
  contents and SHA right before editing it.
- Add or update a test when changing shared code (`content_provider.py`,
  `image_provider.py`, `project_provider.py`, `humanizer.py`,
  `story_bible.py`). Do not claim a change works without running tests.

## Known problems (verified against live files, 2026-09-19)

Fix these before starting Book 4. Details and fixes are in `PLAYBOOK.md`.

1. **`scripts/proofread_novel.py` treats only Book 1 as published.** It
   still lists Book 2 and Book 3 as scannable and it auto-writes dash fixes
   into chapter files. Running it would modify published source text. Its
   default word floor (1,900 to 2,500) also differs from the Book 4+
   standard.
2. **`scripts/word_repetition_fixer.py` auto-writes dash fixes** into every
   file it scans. Run it only on unpublished drafts.
3. **Folder layout mismatch.** `voxel_cli.py novel` writes to
   `novels/<series>/<book-slug>/chapter_NN.md`. The existing books live in
   `novels/<book-slug>/chapters/chapter_NN.md`, which is what the `scripts/`
   tools expect. Reconcile before generating Book 4.
4. **No series memory is stored.** `story_bibles/` is not in the repo, so a
   new `novel` run would start with no canon from Books 1-3. The canon
   currently lives only in the old per-book handoff files and beat maps.
5. **Two manuscript-build routes.** Book 3's manuscript was built with
   Node's `docx` package (Garamond 12pt, justified, first-line indent, page
   numbers from chapter 1). `scripts/build_manuscript.py` is a separate
   python-docx script that does not do those things. Nobody has confirmed
   which route made the files uploaded to KDP.
6. **Stale files:** root `PROOFREAD_REPORT.md` (about 60 KB, from before the
   books were finished) and the per-book handoffs for Books 1 and 2 (long
   review logs). They are candidates for deletion or slimming.
7. **Untested end to end:** the sub-beat beat map (added 2026-09-18) and
   `voxel_cli.py images` (NVIDIA FLUX.1-Kontext). No book has been produced
   with either yet.
8. **Leftovers:** `generate_images.py` is a third, disconnected image path.
   `video_output.py` is not wired into `voxel_cli.py`. `build-book.yml`
   duplicates `voxel-book.yml`.
