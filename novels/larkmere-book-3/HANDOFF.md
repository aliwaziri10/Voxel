# Larkmere Book 3: KEEL AND COMB: HANDOFF

Pen name Elif Kessler. Repo `aliwaziri10/Voxel`. Folder `novels/larkmere-book-3/`. Last updated 2026-11-12 (Claude chat).
Read order, every session: `novels/FROZEN_DO_NOT_EDIT.md`, `novels/EDITORIAL_CHARTER.md`, `novels/HUMAN_WRITING.md`, `canon/CANON_LOCK.md`, `canon/STAKES_LADDER.md`, `VOICE_GUIDE.md`, `canon/CRAFT_SUPPLEMENT.md`, `canon/IMAGE_LEDGER.md`, `canon/HEAT_LADDER.md`, then the chapter's brief and the previous chapter. RE-VERIFY against live GitHub, do not trust this file at face value.
Precedence: `CANON_LOCK.md` wins on names, places, objects and honey rules. `STAKES_LADDER.md` wins over any brief's STAKES line.

## DECISION (Zia, 2026-11-12): CLAUDE WRITES THE CHAPTERS IN CHAT
The OpenRouter writer was too slow (free pool 429, short drafts). Chapters are written by Claude in chat, strict order, one push per chapter. `scripts/write_keel_and_comb.py` and `.github/workflows/write-keel-and-comb.yml` stay in the repo but must NOT run: a Gemma draft of chapter 1 would collide with a chat chapter 1. HYPOTHESIS that Zia disabled the schedule (not verified). Before every push, list `chapters/` live; the push is create-only, so it fails if the file exists.

## CHAT WRITING WORKFLOW (every chapter)
1. Clone the repo, list `chapters/`, find the first missing chapter. Never skip ahead.
2. Read the files in the read order above, plus the previous chapter in full.
3. Plan 2 to 4 sub-beats (CRAFT_SUPPLEMENT section 1) and the chapter's line in STAKES_LADDER.
4. Draft to `novels/larkmere-book-3/chapters/chapter_NN.md`. First line: `<!-- keel-and-comb chapter N | POV | season -->`, then a blank line, then prose. 2,300 to 2,700 words, ceiling 3,000, never padded, never cut for length.
5. Run `python scripts/write_keel_and_comb.py --check novels/larkmere-book-3/chapters/chapter_NN.md --chapter N` in the clone. Fix every HARD. Read every SOFT.
6. Manual read: lexicon, tells, POV comparison domain, canon, brief, stakes line, ending.
7. Push the chapter, re-fetch it from the GitHub API, confirm the word count.
8. Stamp it in `canon/STATUS.md` and log it in `canon/IMAGE_LEDGER.md`. Update this file every 2 to 3 chapters.

## PRIOR WORK CHECK (verified live 2026-11-12)
Written by one earlier Claude session (commits 52156f8 to a1ec9c2, 05:20 to 05:25 UTC) and nothing by any other profile since:
- `canon/CANON_LOCK.md`: DONE (closed world, cast, places, objects, magic, locked lines, hidden-fact schedule).
- `canon/HEAT_LADDER.md`: DONE.
- `briefs/ch01.md` to `briefs/ch40.md`: DONE, 40 files, about 14 lines each. These ARE the beat map. There is no separate `BEAT_MAP` file for this book (the other books have one).
- Against `novels/BEAT_MAP_PROTOCOL.md`: canon lock before plan, 15 to 20 line entries, tags inline, locked lines flagged, hidden-fact schedule, handoff from the start: all met. Calendar dates: none by design (time is season and light, no digits). Small-batch verification: applies to the auto writer, replaced by the chat workflow.
- Name audit: Bryony, Ewan, Tobiah, Ottoline, Abel, Trent, Fairlie, Marrick, Keel: zero hits in every other repo file (grep, 2026-11-12).
- Weakness found: the briefs' STAKES lines were mostly feeling-level and thin from chapter 10 to 30. Fixed by `canon/STAKES_LADDER.md` (seven devices, a per-chapter line for all 40).

## TITLE LOCKED: Keel and Comb
Chosen 2026-11-12 (Zia delegated). Zia once said it does not sound romantic, then said it sounded unique; the romance is carried by cover, subtitle and blurb. No subtitle "A Novel". STILL TO DO BY ZIA: type "Keel and Comb" and "Elif Kessler" into Amazon search before publishing.

## DECIDED
- Series bible grid line 3: second chance, someone who left comes home in the thaw, beekeeper, honey that remembers, spring to early summer. Standalone.
- Elif Kessler profile (`FACTORY_DECISIONS.md`): cozy slow burn, closed door, sensual not explicit. 40 chapters, 2,300 to 2,700 words, ceiling 3,000, no padding, alternating POV, close third past. Obstacles only feeling, weather, magic or a person who loves them.
- Story (Claude's proposal, Zia delegated, may overrule): Bryony Fairlie (33, boatwright) returns after seven springs to rebuild the Heron's failing hull; Ewan Marrick (34, beekeeper) stayed. Honey remembers. The Leaving Jar is opened in chapter 33. First kiss chapter 28. Release chapter 40, closed door. Role flip from Book 2.
- Stakes upgrade (Zia, 2026-11-12): see `canon/STAKES_LADDER.md`.
- Lexicon rule (Zia, 2026-11-12): the exact word, not the fancier word. `VOICE_GUIDE.md` and `canon/CRAFT_SUPPLEMENT.md`.

## CONFIRMED THIS SESSION (verified live)
- `chapters/` does not exist: zero chapters written.
- Free-model test (chapter 1 prompt): Gemma 4 31B free got HTTP 429 on all six keys (upstream pool busy). `thinkingmachines/inkling:free` returns 404, no longer free. `nvidia/nemotron-3.5-lightning:free` wrote 645 words against a 2,300 minimum. Draft in `model_tests/`, not part of the book.
- The auto writer reads only `VOICE_GUIDE.md`, not the craft supplement, ledger or stakes ladder.

## NOT DONE / UNKNOWN
- Chapters 1 to 40: none written.
- Whether the scheduled auto writer is disabled: unverified.
- Amazon title search: Zia.
- Cover, blurb, subtitle, listing, paperback interior: not started. Cover rule: author name as large as the title. Paperback rule: running header, author name on even pages, book title on odd pages.
- Release timing: 20 days between releases, pen names alternate (`RELEASE_DATES.md`). Warm Enough was reported released 2026-11-12, so an Ivy Cassel release is due next.

## NEXT ACTION
Write chapter 1 (Bryony, thaw) per `briefs/ch01.md` and its STAKES_LADDER line.
