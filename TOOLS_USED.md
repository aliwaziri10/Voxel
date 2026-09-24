# Tools used to write, proofread and publish the Amity Falls books

Compiled 2026-09-25 from the repo's code, workflows and docs. It lists what
the repo records, not a log of every session's tool calls (those are not kept).

## Writing
- `voxel_cli.py novel` - one-command chapter writer. Run from GitHub Actions
  workflow "Voxel Novel (one command)" (`voxel-novel.yml`, manual trigger,
  commits each chapter as it is written; commits show as `voxel-bot`).
- `content_provider.py` - text generation. First choice NVIDIA direct API
  (`nvidia/nemotron-3-super-120b-a12b`); fallback OpenRouter
  (`nvidia/nemotron-3-ultra-550b-a55b:free`) with up to 6 rotating keys.
- `content_provider.generate_beat_map()` - whole-book outline, 2-4 typed
  sub-beats per chapter.
- `story_bible.py` + `story_bibles/amity-falls.json` - series continuity memory.
- `humanizer.py` - AI-tell scan and rewrite pass on each chapter. Ideas taken
  from blader/humanizer, Nanako0129/sepia, zy-zmc/tianming-novel-ai-writer
  (ideas only, no runtime dependency).
- Claude sessions writing/fixing chapters by hand and pushing them through the
  GitHub connector (Book 1 was written this way; Book 4 fixes too).
- Templates: `novels/BOOK_CONFIG_TEMPLATE.json`, `novels/VOICE_GUIDE_TEMPLATE.md`.

## Proofreading
- `scripts/proofread_novel.py` + `proofread.yml` - word floor, AI-tell phrases,
  meta-leaks, duplicate sentences, dash auto-fix. Rewrites text only if auto_fix is on.
- `voxel_cli.py audit` + `voxel-audit.yml` - word count, em dashes, AI-tell
  score. Report only.
- `scripts/word_repetition_fixer.py` - scans "particular", "the specific",
  "the kind of", "some/something" hedges. Auto-fixes dashes.
- `scripts/manuscript_qa.py` - grammar via LanguageTool (needs Java), doubled
  words, US/UK spelling, hidden characters, docx checks, page count via
  LibreOffice + pdfinfo. Report only.
- `scripts/continuity_extract.py` - name variants and time references per chapter.
- `scripts/book4_fixes.json` - one-off exact-text fixes for Book 4.
- Manual: the strict chapter-by-chapter read from `novels/EDITORIAL_CHARTER.md`,
  checked against `CANON_NUMBERS.md`, `PROOFED_LOG.md` and each `beat_map.md`.
- Claude bash: `curl` the raw chapter files, `wc -w`, `grep` full-book banned-word sweep.
- Tracked tells: "particular", "the specific", "the kind of", em dash,
  "some/something" hedge.

## Build and publish
- `scripts/pipeline.py` (stage state machine), `scripts/book_config.py`,
  `scripts/kdp_metadata.py`.
- `scripts/build_manuscript.py` - .docx (python-docx). Book 3 used a Node
  `docx` script that is not in the repo.
- `scripts/build_cover.py` - cover PDF (Pillow) using the KDP Cover Calculator template.
- `PRE_PUBLISH_CHECKLIST.md` (Books 1 and 2). KDP upload is manual by design.

## Images (picture books, not the novels)
- `image_provider.py` (Google Gemini image), Cloudflare FLUX fallback,
  `nvidia_image_provider.py` (FLUX.1 dev / Kontext), Canva for "Luna and the Lost Star".

## Claude's own tools in sessions
- GitHub connector: get_me, get_file_contents, create_or_update_file,
  push_files. search_code is unreliable (indexing lag).
- Claude cannot run GitHub Actions or edit `.github/workflows/`; Zia does that.
- Web search for market research (genre decision) and a survey of ~20 GitHub
  book-pipeline repos (`novels/PIPELINE_SPEC.md`).

## Known gaps
- `scripts/pipeline.py` `LOCKED_BOOK_IDS` does not yet include Book 4.
- `word_repetition_fixer.py` and `manuscript_qa.py` have no published-book block.
