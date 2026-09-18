# Voxel Novel Pipeline — State Machine

This documents the mechanical orchestration layer added on top of
`EDITORIAL_CHARTER.md`. It applies to **Book 4 of the Amity Falls Series
and every future novel only.**

## Permanently out of scope

Book 1 (*Where the Frost Doesn't Reach*), Book 2, and Book 3 (*What the
Blood Remembers*) of the Amity Falls Series are published. This
pipeline — `scripts/pipeline.py`, `scripts/book_config.py`,
`scripts/kdp_metadata.py` — will refuse to run against them. This is
enforced in code (`LOCKED_BOOK_IDS` in `pipeline.py`), not just a
convention. Nobody touches them, nothing corrects them, nothing
rebuilds them.

## The stages

Defined in `scripts/book_config.py`'s `STAGES` list, in this fixed
order. A book's `book_config.json` records exactly one current stage;
`pipeline.py` will not skip or reorder them.

1. **outline** — `beat_map.md` exists (produced manually / via
   `voxel_cli.py`'s beat-map step, outside this pipeline).
2. **drafting** — chapter files exist in the book's `chapters/` dir.
3. **editorial_review** — the strict sequential continuity/voice/canon
   read, plus the banned-word and hedge sweeps, per
   `EDITORIAL_CHARTER.md`. **This is never automated.** `pipeline.py`
   only checks that the manual gates below are set to `true`:
   - `continuity_voice_canon_review_complete`
   - `banned_word_sweep_complete`
   - `hedge_sweep_complete`

   Do the real work first, log it in that book's `HANDOFF.md` the same
   way Books 1-3 were logged, *then* set the gate.
4. **mechanical_qa** — runs `scripts/manuscript_qa.py`. Advances only
   if the report has zero `CONFIRMED-FIX` items outstanding.
5. **manuscript_build** — runs `scripts/build_manuscript.py` to
   produce the `.docx`.
6. **cover_build** — runs `scripts/build_cover.py`. Requires front/back
   art asset paths already in `book_config.json`'s `cover` section —
   this pipeline does not generate art.
7. **kdp_metadata** — runs `scripts/kdp_metadata.py`, which writes
   `KDP_METADATA.md` from the config's `kdp` section. Any missing field
   (description, keywords, categories, price, etc.) is reported as an
   `OPEN ITEM`, never guessed at. Advances only once the report is clean.
8. **ready_for_upload** — final Publisher-role gates:
   `name_collision_audit_complete`, `real_person_name_check_complete`,
   `back_cover_blurb_approved`, `cover_image_approved`,
   `kdp_metadata_approved`.
9. **published**.

## Per-book config

Copy `novels/BOOK_CONFIG_TEMPLATE.json` to
`novels/<book-id>/book_config.json` for each new title. It holds trim
size, word-count floor/ceiling, series/author/publisher, current stage,
and the manual gate flags — so onboarding Book 5, 6, etc. means filling
in one JSON file, not editing scripts.

## Running it

```
python scripts/pipeline.py novels/<book-id>/book_config.json --status
python scripts/pipeline.py novels/<book-id>/book_config.json --advance
```

`--status` is read-only. `--advance` attempts the current stage's
mechanical work (if any), and only moves `stage` forward in the config
if that stage's checks/gates pass. Every successful advance appends a
line to that book's `HANDOFF.md`, matching the existing logging
convention.

## What this deliberately does not do

- It does not replace the sequential editorial read — see charter.
- It does not generate KDP description/keywords/categories/price —
  those are supplied by Zia in `book_config.json`.
- It does not generate cover art — only composites art you already have
  (via `build_cover.py`).
- It does not run against Books 1-3, ever, regardless of config content.
