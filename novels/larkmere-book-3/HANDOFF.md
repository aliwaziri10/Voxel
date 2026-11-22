# Larkmere Book 3: KEEL AND COMB: HANDOFF

Pen name Elif Kessler. Repo `aliwaziri10/Voxel`. Folder `novels/larkmere-book-3/`. Last updated 2026-11-22, 13:55 IST (Claude chat).
Read order, every session: `novels/FROZEN_DO_NOT_EDIT.md`, `novels/EDITORIAL_CHARTER.md`, `novels/HUMAN_WRITING.md`, `canon/CANON_LOCK.md`, `canon/STAKES_LADDER.md`, `VOICE_GUIDE.md`, `canon/CRAFT_SUPPLEMENT.md`, `canon/IMAGE_LEDGER.md`, `canon/HEAT_LADDER.md`, then the chapter's brief and the previous chapter. RE-VERIFY against live GitHub, do not trust this file at face value.
Precedence: `CANON_LOCK.md` wins on names, places, objects and honey rules. `STAKES_LADDER.md` wins over any brief's STAKES line.

LOCK: ch.7 claimed by Claude chat, 2026-11-22 13:55 IST. Remove this line when ch.7 is stamped in `canon/STATUS.md`. If ch.7 is not on `main` and this line is more than a few hours old, treat the claim as stale and take it over.

## DECISION (Zia, 2026-11-12): CLAUDE WRITES THE CHAPTERS IN CHAT
The OpenRouter writer was too slow (free pool 429, short drafts). Chapters are written by Claude in chat, strict order, one push per chapter. `scripts/write_keel_and_comb.py` and `.github/workflows/write-keel-and-comb.yml` stay in the repo but must NOT run: a Gemma draft of chapter 1 would collide with a chat chapter 1. HYPOTHESIS that Zia disabled the schedule (not verified). Before every push, list `chapters/` live; the push is create-only, so it fails if the file exists.

## PARALLEL SESSIONS WARNING (learned 2026-11-21)
Zia runs several profiles at once and pastes text between them. Chapter 6 was drafted in two sessions at the same time and pushed by one of them while the other was still editing. Before writing any chapter: (1) list `chapters/` live, (2) list the last five commits, (3) put a LOCK line at the top of this file, (4) re-list `chapters/` immediately before the push. Never overwrite a chapter that appeared while you worked; read it and stamp it instead.

## CHAT WRITING WORKFLOW (every chapter)
1. List `chapters/` and the last five commits live (GitHub tools). Find the first missing chapter. Never skip ahead.
2. Read the files in the read order above, plus the previous chapter in full.
3. Plan 2 to 4 sub-beats (CRAFT_SUPPLEMENT section 1) and the chapter's line in STAKES_LADDER.
4. Draft to `chapters/chapter_NN.md`. First line: `<!-- keel-and-comb chapter N | POV | season -->`, then a blank line, then prose. 2,300 to 2,700 words, ceiling 3,000, never padded, never cut for length.
5. Run `python3 -I novels/larkmere-book-3/tools/check_chapter.py chapter_NN.md` (the checker is in the repo since 2026-11-22; copy it to a work folder first). Fix every banned word, filler verb, em dash, digit, banned-name substring, planning word and any ordinary word used 8 or more times. Read the rest.
6. Manual read: lexicon, tells, POV comparison domain, canon, brief, stakes line, ending. Check physical logic (what a character could really see or reach).
7. Push with `create_or_update_file` on `main`. Verify: the blob sha the push returns must equal `git hash-object chapter_NN.md` of the local file. The GitHub CLI token (`GH_TOKEN`) in the sandbox is invalid, so `gh` and `git push` do not work; use the GitHub tools.
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
- Zia's rule (2026-11-21): padding must come out naturally from the scene, never efforted. A short true chapter is allowed; an added scene needs Zia's approval or must be a real sub-beat.

## CONFIRMED 2026-11-12 (older; superseded by the sections below)
- `chapters/` did not exist then: zero chapters written.
- Free-model test (chapter 1 prompt): Gemma 4 31B free got HTTP 429 on all six keys (upstream pool busy). `thinkingmachines/inkling:free` returns 404, no longer free. `nvidia/nemotron-3.5-lightning:free` wrote 645 words against a 2,300 minimum. Draft in `model_tests/`, not part of the book.
- The auto writer reads only `VOICE_GUIDE.md`, not the craft supplement, ledger or stakes ladder.

## STATE, VERIFIED LIVE 2026-11-22 (IST), by Claude chat
- Account `aliwaziri10` confirmed with the get-authenticated-user tool; writes succeed (commits 4a427aa, af539de).
- `chapters/` holds chapter_01.md to chapter_06.md. Latest commit before this one: 730b85b.
- Word counts: ch1 2177, ch2 1600, ch3 2147, ch4 1825, ch5 1932, ch6 2327 (ch6 was expanded from 1377 by a parallel session with real sub-beats: dead-out hive, split bars, thaw road, veil, cut-clock interior). Chapters 1 to 5 are under the 2,300 floor and were left short on purpose.
- Provenance: ch1 and ch2 written in chat; ch3 and ch6 first drafts were supplied by Zia from other sessions and pushed here; ch4 and ch5 written in chat. A different profile's local ch5 draft (about 1700 words) was never pushed and is lost; ch5 on `main` was written fresh from the brief.
- Every chapter is stamped in `canon/STATUS.md` and logged in `canon/IMAGE_LEDGER.md`. Last chapters ended: ch3 held image, ch4 dialogue turn, ch5 held image, ch6 action beat.
- Continuity facts now fixed on the page: Ottoline's key (ch3) opens the Net Sheds only; Bryony forced the yard door in ch5 using Ewan's hive tool and gave it back; the garboard was torn out in ch4 and the heel sits on props; Tobiah and Ewan mended the Fairlie yard roof (revealed ch5); a bee stung Bryony's left wrist in ch6, old honey from a cracked frame was put on the sting and she tasted it and did not say what it held; Tobiah is to carry the yard oak to the Net Sheds (set up in ch6, delivered in ch7); one hive in the third row died in the winter (ch6).

## PENDING FIXES (do these only in strict order, charter rule)
- ch1: opening-line hook review (awaiting Zia).
- ch2: lexicon pass pending ("knocked the whole board off", pink ears used 3 times, big/small/just/got).
- ch3: full manual read against canon still pending (mechanical check only).
- ch4: no known open items.
- ch5: no known open items.
- ch6: manual read and lexicon pass pending per its stamp ("stopped" 6, "out" 8).

## NOT DONE / UNKNOWN
- Chapters 7 to 40: none written.
- Whether the scheduled auto writer is disabled: unverified.
- Amazon title search: Zia.
- Cover, blurb, subtitle, listing, paperback interior: not started. Cover rule: author name as large as the title. Paperback rule: running header, author name on even pages, book title on odd pages.
- Release timing: 20 days between releases, pen names alternate (`RELEASE_DATES.md`). Warm Enough was reported released 2026-11-12, so an Ivy Cassel release is due next.

## SESSION 2026-11-21 early (Claude chat), verified live
- Repo owner trap: the book lives in the fork `aliwaziri10/Voxel`. GitHub search hides forks unless `fork:true` is added. `Wazzaboyzz/Voxel` is a different repo and is never used.
- `scripts/write_keel_and_comb.py` and `scripts/novel_guard.py` are NOT in the repo. The chapter check is now `novels/larkmere-book-3/tools/check_chapter.py`.
- Chapter 1 (pushed 2026-11-18, 2754 words) failed the rules: stock phrases, British spellings, "seven years", Ewan naming Ottoline early, heat above level 0. Rewritten and re-pushed (2180 words).

## NEXT ACTION
Write chapter 7 (Bryony, thaw, touch level 1) per `briefs/ch07.md` and its STAKES_LADDER line (her letters went unanswered; every jar on the shelf is a truth she cannot stop being fed; one jar is "not for eating"). No locked line in this chapter. Read `canon/IMAGE_LEDGER.md` first: no image repeats within six chapters, no honey taste note repeats ever, and do not end on a held image (ch.5 did; ch.6 ended on an action beat). The Leaving Jar is seen only across the yard, with the exact canon description; no explanation of the jar and no reason for Tobiah's coldness beyond "you left". Four jars: a day of plain content, a day of grief, a day of a saved swarm, and the brief's fourth; each taste described in Bryony's domain (wood, tools, water, weather), never bees. Then chapter 8 (Ewan): the town's silence, Ewan's lantern lie.
