# Proof of Home canon: status

A pure slow-burn cozy fantasy romance. This folder replaced an earlier draft plan built around a council vote and a loaf count. Zia rejected that plot (no politics, law, counting, ledgers or balances) and the old folder `novels/next-series-canon/` was deleted on 2026-10-17.

The book's own working files are in `novels/proof-of-home/` (see its `HANDOFF.md` for current state and next steps).

## What is here (confirmed, built and checked)
- `canon_data.py`: the single source of truth. 32 chapters, kiss in chapter 27. Its asserts run on import.
- `build_canon.py`: run `python3 build_canon.py` in this folder to generate `CANON.md` and `chapter_briefs/ch01.md` to `ch32.md`. Generated files are not committed; regenerate them.
- `build_bible.py`: run `python3 build_bible.py` in this folder to generate `story_bibles/larkmere.json` and `novels/proof-of-home/beat_map.md`. Both generated files are committed. Re-run and re-save them after any canon change.
- `canon_scenes.py`: scene-level canon for the chapters.

## Decisions made by Zia
- First kiss at roughly 80 to 85 percent of the book.
- Constant restrained physical closeness before the kiss: narrow spaces, crowds, bodies pressed, both holding back. Sensual, never explicit.
- No exact dates, weekdays or numeric ages. Time is shown by season, light, weather and the bread.
- Heroine name changed from Zoya to Sarah. Mariam is an acceptable alternative.
- The longing must keep increasing until the very end and only culminate in the final chapter.
- 32 chapters, same tempo throughout.

## Changes made 2026-10-16
- Jack's niece renamed from Wren to Nell. Wren is already the heroine of another Voxel series, and the beat-map protocol says no name may be reused across books.
- Chapters 28 to 32 reworked so the kiss in 27 does not release the longing. 28: the town never leaves them alone. 29: she stops them herself at his cottage because she will not give all of herself until she knows she can stay. 30: the lowest and hungriest point, a desperate kiss on the dock and he pulls away. 31: she says she is staying, they hold the last of the wanting for morning. 32: the full release at the last lantern, in plain light.
- Rule and touch-ladder text changed from "tenderness after the kiss" to "the wanting only grows".
- `build_bible.py` written and fixed so chapters 27 and 32 do not carry a "why they cannot act" line. Story bible and beat map generated and committed.
- `book_config.json`, `VOICE_GUIDE.md` and `HANDOFF.md` added in `novels/proof-of-home/`.

## Decided by Claude, for Zia to overrule
- Standalone single book. The plan is a complete story with one ending. More books in Larkmere are a later decision.

## Not decided yet
- Pen name, genre label, series name and town name are proposals only (`Elif Kessler` is in the config as a proposal).
- Name check: done both ways on 2026-10-17 against the other books' chapter text as well as their bibles. One overlap, the first name Sarah in the frozen Amity Falls book 4. Details and the open decision are in `novels/proof-of-home/HANDOFF.md`.

## Known limit
- Claude's connector is refused (403) when creating files under `.github/workflows/`, so the planned auto-rebuild workflow could not be added. Regeneration is manual.

## Progress
- Chapters 1 to 23 are written and stamped in `novels/proof-of-home/PROOFREAD_TRACKER.md`. Chapters 24 to 32 are written by hand, one at a time, per the method in `HANDOFF.md`. The generation workflow produced poor chapters and is no longer the way this book is written.
