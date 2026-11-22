# Larkmere Book 3: KEEL AND COMB: HANDOFF

Pen name Elif Kessler. Repo `aliwaziri10/Voxel`. Folder `novels/larkmere-book-3/`. Last updated 2026-11-22 (Claude chat), after chapter 14.
Read order, every session: `novels/FROZEN_DO_NOT_EDIT.md`, `novels/EDITORIAL_CHARTER.md`, `novels/HUMAN_WRITING.md`, `canon/CANON_LOCK.md`, `canon/STAKES_LADDER.md`, `VOICE_GUIDE.md`, `canon/CRAFT_SUPPLEMENT.md`, `canon/IMAGE_LEDGER.md`, `canon/HEAT_LADDER.md`, then the chapter's brief and the previous chapter. RE-VERIFY against live GitHub (list `chapters/` and the last commits first), do not trust this file at face value. Books 1 (Proof of Home) and 2 (Warm Enough) are published and frozen; never touch them, Kindling Line or Amity Falls.
Precedence: `CANON_LOCK.md` wins on names, places, objects and honey rules. `STAKES_LADDER.md` wins over any brief's STAKES line.

LOCK: none. (ch.14 is stamped.) Before writing ch.15, put a line here: `LOCK: ch.15 claimed by <session>, <date and time IST>`. Remove it when ch.15 is stamped in `canon/STATUS.md`. If ch.15 is not on `main` and the line is more than a few hours old, treat the claim as stale and take it over.

## STATE, VERIFIED LIVE 2026-11-22 by Claude chat
- `chapters/` holds chapter_01.md to chapter_14.md. Every chapter is stamped in `canon/STATUS.md`; `canon/IMAGE_LEDGER.md` has rows for ch.1 to 14.
- Word counts: ch1 2177, ch2 1591, ch3 2147, ch4 1825, ch5 1932, ch6 2322, ch7 2149, ch8 1865, ch9 2028, ch10 about 2300 (supplied from another session), ch11 2257, ch12 1461, ch13 2145, ch14 2419. Chapters under the 2,300 floor were left short on purpose, not padded (flagged for Zia in STATUS).
- Lexicon passes done: ch.1, ch.2, ch.6, ch.8, ch.12 (filler verbs, banned 'kind', 'between them', repeated rose/stopped). Manual reads done (this session, against canon, brief and neighbours): ch.3, ch.10, ch.11, no blocking findings.
- Ch.14 (Ewan, touch level 3): hive-yard quarrel with Tobiah ("You lie about everything", the lantern said aloud, the boot-box in Ewan's thought only); Ewan fetches the wax past the Leaving Jar with his back to it; the wax scene at the Sheds (thumbnails meet, four hands round the cake too long, she draws back first); Tobiah is already in the Fairlie yard asking "Show me how"; ends on the plane's first clean shaving.
- Continuity facts fixed on the page (ch.10 to 14): the punt's patched seam held in the squall (ch.10); the last wedge dropped the keel and the keel note "Mind the heel. Marrick wax in every seam." was found in the scarf joint (ch.11); the Leaving Jar was told plainly by Ottoline as the comb cut the morning Bryony left, never tasted (ch.11); Ewan said "Aunt"; Bryony held him in the loft and he left with the stove glowing (ch.12); Ottoline admitted she wrote the letter, burned three drafts with the word home, Bryony said "I'll finish her" (ch.13); Ewan left a board on a folded sack at the jamb (ch.13), now on her trestles (ch.14).
- The chapter check is `novels/larkmere-book-3/tools/check_chapter.py`. Copy it to a work folder and run `python3 -I check_chapter.py chapter_NN.md`. The checker's "etched" hit is a false alarm ("fetched").
- The GitHub CLI token in the sandbox is invalid. A local `git clone` of the repo works (read only). Push with the GitHub tools (`create_or_update_file` for one new chapter, `push_files` for several files in one commit); after a push the returned blob sha must equal `git hash-object` of the local file.
- Repo owner trap: the book lives in `aliwaziri10/Voxel`. `Wazzaboyzz/Voxel` is a different repo and is never used. GitHub search hides forks unless `fork:true` is added.

## NEXT ACTION
Write chapter 15 (Bryony) per `briefs/ch15.md` and STAKES_LADDER line 15 (if she cannot say thank you now to the man she left, she never will). Reveal for ch.15 per CANON_LOCK section 10: why Tobiah is cold, and who raised him. Follows ch.14 directly (Tobiah at the Fairlie yard door with her father's plane). Put the LOCK line above first. End on a dialogue turn or a question (ch.14 ended on an action beat; the last held-image ending was ch.11). Do not open the boot-box, do not state what is in the Leaving Jar, no Abel on the page before the schedule (letter 17, arrives 23). Read `canon/IMAGE_LEDGER.md` first: no image repeats within six chapters, no honey taste note repeats ever; in Bryony's chapter use boats, wood, tools, water and weather only.

## DECIDED (still in force)
- Writer: Claude in chat, strict order, one push per chapter. The auto writer (`write-keel-and-comb.yml`) must NOT run; `scripts/write_keel_and_comb.py` is not in the repo.
- Working rule (Zia, 2026-11-22): no parallel work. One profile works on one chapter at a time. If Zia pastes text from another session, check it against live `main` first and never overwrite a chapter that already exists.
- Standing rules from Zia: check the live repo and latest commits FIRST and say what was found; tell him before changing any file; put anything to be copied and pasted in a code block; after every two chapters update this file and `canon/STATUS.md`.
- Length: 2,300 to 2,700 words, ceiling 3,000. Plan 3 to 4 real sub-beats from the brief's own people, objects and stakes line BEFORE drafting; never pad. A short true chapter is allowed and is flagged for Zia.
- Chapter first line: `<!-- keel-and-comb chapter N | POV | season -->`, then a blank line. Zero em dashes, zero digits, American spelling except grey, banned words (some, something, someone, somewhere, somehow, somebody, particular, kind, specific), filler verbs (came, went, got, felt, looked, moved, just, very, good, big, small, thing).
- Title locked: Keel and Comb. STILL TO DO BY ZIA: type "Keel and Comb" and "Elif Kessler" into Amazon search before publishing.
- Story: Bryony Fairlie (33, boatwright) returns after seven springs to rebuild the Heron's failing hull; Ewan Marrick (34, beekeeper) stayed. Honey remembers. The Leaving Jar is opened in chapter 33. First kiss chapter 28. Release chapter 40, closed door.

## OPEN ITEMS
- Chapters 1 and 2: Zia has not yet chosen between leaving them short and approving a real added scene. Ch.1 opening-line hook review awaits Zia.
- Manual read still pending for ch.6 (lexicon fixed, canon read not done), and a full voice-guide lexicon read for ch.9 and ch.13.
- Whether the scheduled auto writer is disabled: unverified.
- Cover, blurb, subtitle, listing, paperback interior: not started. Cover rule: author name as large as the title. Paperback rule: running header, author name on even pages, book title on odd pages.
- Release timing: 20 days between releases, pen names alternate (`RELEASE_DATES.md`). Book 2 is published, so the next Larkmere or Ivy Cassel release timing is Zia's call.
- Optional (offered to Zia, not yet done): a "Larkmere series timeline" section here. Series history found 2026-11-21: Proof of Home Oct 15 to 24, Warm Enough Oct 21 to Nov 12, Keel and Comb from Nov 12.
