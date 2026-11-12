# Larkmere Book 3: KEEL AND COMB: HANDOFF

Pen name Elif Kessler. Repo `aliwaziri10/Voxel`. Folder `novels/larkmere-book-3/`. Last updated 2026-11-12 (Claude chat).
Read order, every session: `novels/FROZEN_DO_NOT_EDIT.md`, `novels/EDITORIAL_CHARTER.md`, `novels/HUMAN_WRITING.md`, `canon/CANON_LOCK.md`, `VOICE_GUIDE.md`, `canon/CRAFT_SUPPLEMENT.md`, `canon/IMAGE_LEDGER.md`, `canon/HEAT_LADDER.md`, then the chapter's brief and the previous chapter. RE-VERIFY against live GitHub, do not trust this file at face value.

## DECISION (Zia, 2026-11-12): CLAUDE WRITES THE CHAPTERS IN CHAT
The OpenRouter writer was too slow (free pool 429, short drafts). Chapters are written by Claude in chat, strict order, one push per chapter. `scripts/write_keel_and_comb.py` and `write-keel-and-comb.yml` stay in the repo but must NOT run: a Gemma draft of chapter 1 would collide with a chat chapter 1. STATUS OF THE SCHEDULE: HYPOTHESIS that Zia disabled it (not verified). Before every push, list `chapters/` live; the push is create-only, so it fails if the file exists.

## CHAT WRITING WORKFLOW (every chapter)
1. Clone the repo, list `chapters/`, find the first missing chapter. Never skip ahead.
2. Read the files in the read order above, plus the previous chapter in full.
3. Plan 2 to 4 sub-beats (CRAFT_SUPPLEMENT section 1).
4. Draft to `novels/larkmere-book-3/chapters/chapter_NN.md`. First line: `<!-- keel-and-comb chapter N | POV | season -->`. Then a blank line, then prose. 2,300 to 2,700 words, ceiling 3,000, never padded, never cut for length.
5. Run `python scripts/write_keel_and_comb.py --check novels/larkmere-book-3/chapters/chapter_NN.md --chapter N` in the clone. Fix every HARD. Read every SOFT.
6. Manual read: lexicon, tells, POV comparison domain, canon, brief, ending.
7. Push the chapter, re-fetch it from the GitHub API, confirm the word count.
8. Stamp it in `canon/STATUS.md` and log it in `canon/IMAGE_LEDGER.md`. Update this file every 2 to 3 chapters.

## TITLE LOCKED: Keel and Comb
Chosen 2026-11-12 (Zia delegated). Zia once said it does not sound romantic, then said it sounded unique; the romance is carried by cover, subtitle and blurb. No subtitle "A Novel" (removed from Book 2 config the same day; do not add to this book). STILL TO DO BY ZIA: type "Keel and Comb" and "Elif Kessler" into Amazon search before publishing.

## DECIDED
- Series bible grid line 3: second chance, someone who left comes home in the thaw, beekeeper, honey that remembers, spring to early summer. Standalone.
- Elif Kessler profile (`FACTORY_DECISIONS.md`): cozy slow burn, closed door, sensual not explicit. 40 chapters, 2,300 to 2,700 words, ceiling 3,000, no padding, alternating POV, close third past. Obstacles only feeling, weather, magic or a person who loves them.
- Story (Claude's proposal, Zia delegated, may overrule): Bryony Fairlie (33, boatwright) returns after seven springs to rebuild the Heron's failing hull; Ewan Marrick (34, beekeeper) stayed. Honey remembers. The Leaving Jar is opened in chapter 33. First kiss chapter 28. Release chapter 40, closed door. Role flip from Book 2. Full detail: `canon/CANON_LOCK.md` (wins over this file).

## CONFIRMED THIS SESSION (verified live)
- Repo has: `canon/CANON_LOCK.md`, `canon/HEAT_LADDER.md`, `canon/STATUS.md`, `VOICE_GUIDE.md` (lexicon added, commit `01fd1d9`), `WRITER_COMMAND.md`, `book_config.json`, `briefs/ch01.md` to `ch40.md`, `scripts/write_keel_and_comb.py`, `scripts/compare_keel_models.py`.
- `chapters/` does not exist: zero chapters written.
- Free-model test (workflow run, chapter 1 prompt): Gemma 4 31B free got HTTP 429 on all six keys (upstream pool busy, not the daily limit). `thinkingmachines/inkling:free` returns 404, no longer free. `nvidia/nemotron-3.5-lightning:free` wrote 645 words against a 2,300 minimum. Draft saved in `model_tests/`, not part of the book. Nemotron 3 Ultra was dropped earlier for ignoring rules and writing short.
- The auto writer reads only `VOICE_GUIDE.md`, not `CRAFT_SUPPLEMENT.md` or `IMAGE_LEDGER.md`.

## LEXICON (Zia, 2026-11-12: "improve lexicon, use better words")
Standing rule: the exact word, not the fancier word. Details in `VOICE_GUIDE.md` (Lexicon) and `canon/CRAFT_SUPPLEMENT.md`. Research basis: slop is vague stand-ins for specific words, and density, not one use, is the tell.

## NOT DONE / UNKNOWN
- Chapters 1 to 40: none written.
- Whether the scheduled auto writer is disabled: unverified.
- Amazon title search: Zia.
- Cover, blurb, subtitle, listing, paperback interior: not started. Cover rule: author name as large as the title. Paperback rule: running header, author name on even pages, book title on odd pages.
- Release timing: 20 days between releases, pen names alternate (`RELEASE_DATES.md`). Warm Enough was reported released 2026-11-12, so an Ivy Cassel release is due next.
- Warm Enough bookshelf date and Amazon IDs not entered in `RELEASE_DATES.md`.

## NEXT ACTION
Write chapter 1 (Bryony, thaw) per `briefs/ch01.md`.
