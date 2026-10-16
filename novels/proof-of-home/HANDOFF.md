# Proof of Home - HANDOFF

Read `novels/EDITORIAL_CHARTER.md` first, always, before this file or any chapter. This file defers to it.

Repo: `aliwaziri10/Voxel` (not `Wazzaboyzz/Voxel`, which is a different, unrelated repo).
Pipeline stage: **outline** (see `book_config.json`).
Zia works in the browser only. Test runs go through GitHub Actions, never a local terminal.

## What this book is

A pure slow-burn cozy fantasy romance. Sarah Quill, a baker whose bread carries what she feels, and Jack Mercer, the ferryman, in the lakeside town of Larkmere. 32 chapters, Sarah in odd chapters and Jack in even, close third person, past tense. First kiss in chapter 27. The longing keeps rising after the kiss and is released only in chapter 32. Standalone for now; more books in Larkmere is a later decision.

Single source of truth: `novels/proof-of-home-canon/canon_data.py`. Never edit the generated files by hand. Change the canon, then regenerate.

## CONFIRMED (verified live on 2026-10-16)

- Canon scripts are in the repo: `canon_data.py`, `build_canon.py`, `build_bible.py`, `STATUS.md` in `novels/proof-of-home-canon/`.
- `build_bible.py` was fixed so chapters 27 (first kiss) and 32 (final release) no longer carry the "why they cannot act" line. It is the only script change this session.
- Generated and saved: `story_bibles/larkmere.json` and `novels/proof-of-home/beat_map.md`. Both were regenerated from the fixed script and the saved copies were checked byte for byte against the generated ones. 32 chapters, no em dashes, no Wren, no Zoya.
- `book_config.json` and `VOICE_GUIDE.md` are saved in `novels/proof-of-home/`. The config loads with the project's own loader.
- No chapter has been drafted. There is no `chapters/` folder yet.

## To regenerate after any canon change

Run from `novels/proof-of-home-canon/`: `python3 build_canon.py` then `python3 build_bible.py`. Then save `story_bibles/larkmere.json` and `novels/proof-of-home/beat_map.md` to the repo.

## KNOWN LIMITS

- The connector that saves files here is refused (403) when it tries to create anything under `.github/workflows/`. So the planned auto-rebuild workflow (`build-proof-of-home.yml`) cannot be added by Claude. Regeneration is manual, as above. Zia could add that workflow file himself in the browser if he wants it.
- The name check was done against the two older story bibles only. The chapter text of the other books was not searched. A manual check of the other books' chapters is still open (gate `name_collision_audit_complete`).

## OPEN DECISIONS (for Zia)

- Pen name: `Elif Kessler` is in the config as a proposal only. Not decided.
- Genre label and the town name (Larkmere, lake Larkmere Water) are working names only.
- Series name "Larkmere" in the config is a working name.

## NEXT STEPS, in order

1. Confirm what the "Voxel Novel (one command)" workflow (`voxel-novel.yml`) needs as inputs and that it picks up `story_bibles/larkmere.json` and `novels/proof-of-home/beat_map.md`.
2. Zia starts that workflow by hand from the Actions tab to draft chapters. Chapters are written in strict numeric order.
3. After drafting: strict sequential editorial read per the charter, banned-word and hedge sweeps, then the gates in `book_config.json`.

## HYPOTHESIS (not yet verified)

- That the workflow reuses the beat map when its chapter count matches the number of chapters requested (stated in the `build_bible.py` header, not yet seen in a real run).
