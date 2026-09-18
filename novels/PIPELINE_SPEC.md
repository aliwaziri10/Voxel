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
   (description, keywords, categories, price, AI-disclosure text, etc.)
   is reported as an `OPEN ITEM`, never guessed at. Advances only once
   the report is clean.
8. **ready_for_upload** — final Publisher-role gates:
   `name_collision_audit_complete`, `real_person_name_check_complete`,
   `back_cover_blurb_approved`, `cover_image_approved`,
   `kdp_metadata_approved`, `ai_disclosure_included`.
9. **published**.

## Per-book config

Copy `novels/BOOK_CONFIG_TEMPLATE.json` to
`novels/<book-id>/book_config.json` for each new title. It holds trim
size, word-count floor/ceiling, series/author/publisher, current stage,
the voice guide path, and the manual gate flags — so onboarding Book 5,
6, etc. means filling in one JSON file, not editing scripts.

## Voice guide

Copy `novels/VOICE_GUIDE_TEMPLATE.md` to `novels/<book-id>/VOICE_GUIDE.md`
alongside the book config. It's a standing, single-file record of that
book's locked filler/tell-word rules and narrator-voice notes — the same
kind of rule Book 3's editorial passes found and fixed chapter by chapter
(e.g. the "kind of" filler convention), but written once instead of
staying scattered across commit messages. A rule only gets promoted from
one book's `VOICE_GUIDE.md` into the series-wide `EDITORIAL_CHARTER.md`
after it holds across 2+ books — one book's pattern isn't a series rule
yet.

## AI disclosure (KDP requirement)

Amazon KDP requires books with AI-assisted content to (1) carry a
disclosure notice on the copyright page and (2) be declared as such in
the KDP backend upload form. Missing this risks the KDP account, not
just the one title. `ready_for_upload` will not clear until
`ai_disclosure_included` is set to `true` in `manual_gates`, and
`kdp_metadata.py` requires `kdp.ai_disclosure_text` (the exact wording
used) to be filled in before its report is clean.

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
- It does not generate KDP description/keywords/categories/price/AI-
  disclosure wording — those are supplied by Zia in `book_config.json`.
- It does not generate cover art — only composites art you already have
  (via `build_cover.py`).
- It does not run against Books 1-3, ever, regardless of config content.
- It does not attempt to automate the actual KDP upload. Amazon has no
  public API for author-account actions; the only way to script an
  upload is browser automation against KDP's web UI, which is fragile
  (session cookies, rate limits, UI drift) and risks the account for
  little benefit at this publishing volume. Upload stays manual.

## External research

Before building this, ~20 public GitHub repos in the "AI book
pipeline" / "KDP automation" space were surveyed (search terms: "kdp
publishing automation", "book writing pipeline AI agent"), with full
READMEs read on the five most substantive:
`zhamanov-seabus/books-pipeline`, `hannsxpeter/scriveno`,
`joshyattridge/amazon-kdp-skill`, `jirbis/ai-book-pipeline`,
`drkameleon/kdp-pricegen`. Most of this space is thin, single-author,
low-star hobby tooling. Three ideas were judged genuinely worth
adapting and are reflected above:

1. Named human-approval gates tied explicitly to protecting effort/spend
   (`books-pipeline`) — already partly present via `manual_gates`, kept.
2. A standing per-book voice/style file loaded into every editorial pass,
   instead of rules staying scattered across history (`scriveno`) — added
   as `VOICE_GUIDE_TEMPLATE.md` above.
3. The AI-disclosure requirement for KDP uploads (`books-pipeline`) —
   added as a hard gate above.

Not adopted: `scriveno`'s 127-command, 50-work-type framework (built for
a generic audience, not this two-series operation) and any form of
browser-automated KDP upload (see "What this deliberately does not do").
