# Voxel Playbook - tools and workflow for Book 4 and beyond

What was used to make the Amity Falls books, exactly how to run each tool,
and what to watch out for. Every command below was read from the live code
on 2026-09-19. "Used on Books 1-3" means the commit history or a book
handoff says so; "not yet run" means no evidence of a real run.

Rules for editing chapters are NOT here. They live in
`novels/EDITORIAL_CHARTER.md`, which always wins.

## The pipeline at a glance

1. Seed the series canon (gap - see step 0)
2. Plan the book: whole-book beat map with sub-beats
3. Draft chapters
4. Mechanical checks (scripts)
5. Human editorial pass (the part scripts cannot do)
6. Build the manuscript file
7. Build the cover
8. Pre-publish checklist, then manual KDP upload

## Step 0 - Seed the series canon (do this first, once)

Problem: `voxel_cli.py novel` reads series memory from
`story_bibles/<series>.json` through `story_bible.py`. That folder is not in
the repo, so Book 4 would start blind. Canon for Books 1-3 exists only in
`novels/amity-falls-book-2/HANDOFF.md` ("Established canon"),
`novels/amity-falls-book-3/HANDOFF.md` ("Locked facts", "Story summary"),
`novels/where-the-frost-doesnt-reach/architecture.md`, and each book's
beat map. Consolidate that into one series-canon file and register Books 1-3
in the story bible before generating anything.

## Step 1 - Plan: whole-book beat map

- Tool: `content_provider.generate_beat_map()`, run automatically inside
  `voxel_cli.py novel`.
- Since 2026-09-18 it plans 2 to 4 typed sub-beats per chapter: plot,
  relationship micro-beat, character interior, world/stakes, texture or
  callback. This is the charter's fix for thin chapters.
- If a beat map already exists for the same book title and chapter count, it
  is reused (resumed run) instead of regenerated.
- Status: not yet run end to end on a real book.

## Step 2 - Draft chapters

Command (run from a local clone, needs `OPENROUTER_API_KEY`):

    python voxel_cli.py novel --series amity-falls --book "Amity Falls Book 4" --chapters 45 --brief "..."

- Defaults: `--min-words 2300 --max-words 2700` (charter standard for Book 4+).
- Each chapter goes through `humanizer.py` (removes AI-tell phrasing; a
  single banned word now always triggers a rewrite; it keeps the original
  text if a rewrite would drop a fact).
- A chapter under the floor is only reported. It is never auto-expanded.
  An earlier "retry and expand" loop was reverted because it is padding.
- Add `--commit` to git add/commit/push using your own local git login.
- Watch out: output goes to `novels/<series>/<book-slug>/chapter_NN.md`, but
  existing books use `novels/<book-slug>/chapters/`. Fix the mismatch first.

## Step 3 - Mechanical checks

| Tool | Command | What it does | Writes files? |
|---|---|---|---|
| `voxel_cli.py audit` | `python voxel_cli.py audit --book "Amity Falls Book 4" --min-words 2300 --max-words 2700` | Word count, em-dash count, AI-tell score per chapter; writes `chapters_audit_report.md` | Report only |
| `scripts/proofread_novel.py` | `BOOK=amity-falls-book-4 python scripts/proofread_novel.py` | Word floor, banned phrases, overused words, repeated openers, rhythm, duplicate sentences, filenames; stamps the book's HANDOFF | YES: auto-fixes dashes in chapters |
| `scripts/word_repetition_fixer.py` | `python3 scripts/word_repetition_fixer.py --dir novels/<book>/chapters` | One-pass scan for "particular", "the specific", "the kind of", "some/something" hedges with line context | YES: auto-fixes dashes |
| `scripts/continuity_extract.py` | `python scripts/continuity_extract.py` | Pulls name variants, time references, opening/closing lines per chapter into `CONTINUITY_EXTRACT.md` | Report only |
| `scripts/manuscript_qa.py` | `python scripts/manuscript_qa.py --chapters novels/<book>/chapters --docx manuscript.docx` | Em dashes, doubled words, invisible characters, US/UK spelling mix, grammar (LanguageTool, needs Java), literal asterisks in the docx, page count via LibreOffice | Report only |

Cautions, all verified in the code:

- `proofread_novel.py` still lists Book 1 only as published and Books 2 and
  3 as scannable. Before any use, edit `PUBLISHED_BLOCKLIST` and
  `UNPUBLISHED_BOOKS`, and set `WORD_MIN`/`WORD_MAX` to 2300/2700 for Book 4.
- The "some/something" pattern is a candidate finder, not a verdict. It also
  matches someone, somehow, somewhat, and every plain "some". An earlier
  count of "17-32 per chapter" was pure noise; the real figure was about 0-2
  per chapter. Judge each hit in context.
- Scripts cannot judge continuity, timeline math, voice, or canon. Only the
  sequential human read can. In Book 2 it alone caught a "four weeks" vs
  "six weeks" wedding-timeline error repeated in two chapters, and in Book 3
  a countdown error and a line that contradicted a character's promise.

## Step 4 - Human editorial pass

Follow `novels/EDITORIAL_CHARTER.md` exactly. The short version:

- Strict numeric order, never worst-first.
- Read the chapter, the beat map, and the canon before judging.
- Fix in the chapter file itself, then stamp the chapter in the book's
  handoff log (date plus session label). One or two lines per chapter.
- Re-scan for ALL banned terms after ANY edit.
- Put a claim line at the top of the log when starting a batch, because
  several sessions can run at once.
- Keep the book handoff short. Book 2's grew to 34 KB because of logs.

## Step 5 - Build the manuscript (.docx)

Two routes exist. Pick one on purpose and keep it in the repo.

- Route A, `scripts/build_manuscript.py`:

      python scripts/build_manuscript.py --chapters novels/<book>/chapters --out manuscript.docx --title "..." --series "The Amity Falls Series" --book-number 4 --author "Elif Kessler" --trim 6x9 --year 2026

  Sets exact KDP trim, converts markdown italics to real italics (no literal
  asterisks), adds title and copyright pages. It does NOT set Garamond,
  justification, first-line indent, or page numbering from chapter 1.
- Route B, Node `docx` package, the route Book 3's handoff describes: 6x9,
  Garamond 12pt, justified, first-line indent, "CHAPTER <NUMBER>" headings,
  page numbers from 1 on the first chapter page, front matter with series
  list. That code is not in the repo. Recommended: port these formatting
  rules into Route A so one script produces the final file.
- Always render to PDF and check a few pages by eye, then run
  `manuscript_qa.py` with `--docx`.

## Step 6 - Build the cover

    python scripts/build_cover.py --template kdp_template.png --front front_art.png --back back_art.png --title "..." --series "The Amity Falls Series" --book-number 4 --blurb blurb.txt --full-width-in <inches> --spine-width-in <inches> --out cover_final.pdf

- Inputs you must supply: the KDP Cover Calculator template PNG, front art,
  back art, blurb text, and the full-width and spine-width numbers from the
  calculator.
- It samples the spine colour from the front art, draws rotated spine text,
  adds the blurb, leaves a blank white barcode box, and writes a PDF plus a
  preview JPG. It downloads fonts on first run.
- Cover art itself is made outside this repo. `voxel_cli.py images`
  (NVIDIA FLUX.1-Kontext, one reference photo to many images) exists but has
  never been run; treat the first run as a test.

## Step 7 - Pre-publish checklist and KDP upload

- Books 1 and 2 each have a `PRE_PUBLISH_CHECKLIST.md`. Copy that structure
  for Book 4.
- Items Book 3 still listed as open before upload: name-collision audit,
  real-person name check, back-cover blurb, cover image.
- KDP upload itself is manual. No upload automation exists by design.
- After publishing, record the title, publish date and listing links in the
  book's handoff, then freeze the book: add it to `PUBLISHED_BLOCKLIST` in
  `scripts/proofread_novel.py`.

## Other tools in the repo

- `voxel_cli.py book`: picture books (manuscript, humanizer, illustrations,
  print-ready interior and cover PDFs, `project.json`). Used for Luna and
  the Lost Star.
- `build_book.py`, `make_lesson.py`: the older picture-book and lesson-deck
  generators that `voxel_cli.py` wraps.
- `content_provider.py`, `image_provider.py`, `project_provider.py`,
  `story_bible.py`, `humanizer.py`: shared modules, with tests in
  `test_*.py`. `humanizer.py`, `story_bible.py`, `voxel_cli.py` and
  `nvidia_image_provider.py` have no tests.
- Workflows (`.github/workflows/`): `voxel-novel.yml`, `voxel-book.yml`,
  `voxel-audit.yml`, `proofread.yml`, `test.yml`, `test-image-secret.yml`,
  `build-book.yml` (redundant). Per Book 2's old notes `proofread.yml` was
  paused; not re-verified. Claude cannot edit these files, Zia pastes them.

## Environment variables

`OPENROUTER_API_KEY` (novel and book text), `GEMINI_API_KEY` (book
illustrations), `NVIDIA_API_KEY` (images command, or NVIDIA text).
