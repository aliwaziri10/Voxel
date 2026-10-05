# HANDOFF - Kindling Line Book 3

## LATEST STATUS 2026-10-06 (IST): Book 3 chapter writing has STARTED. This section is newer than everything below it; where they disagree, trust this one (the old "wait for Zia's reaction" line below is out of date).
- HOW CHAPTERS ARE WRITTEN: `scripts/write_kindling.py`, run by the workflow "Write Kindling Book 3" (`.github/workflows/write-kindling.yml`, manual, Zia clicks Run workflow). One run writes 5 chapters from the start number you give (cap 45), strictly in order, each chapter committed as soon as it is written. Each chapter is written in two model calls (first half, then second half). Existing chapters are kept unless "force" is ticked. NEVER tick force without a reason: it overwrites chapter 1.
- CHAPTER 1 IS SAVED: commit `542bbb4`, 2,569 words. Not yet read by an editor and not checked against its beat. The checker left these notes for the editor: 8 em or en dashes, and "someone" x4, "something" x3, "somewhere" x2.
- CHAPTER 2 IS NOT SAVED. The last run took about 41 minutes and stopped on chapter 2 because the name check rejected it. The pasted log was cut off, so the exact flagged words were not seen. The cause is known: the check treated ordinary English words as invented names.
- WHAT WAS CHANGED TO ADDRESS THAT (commit `908cebc`, `scripts/write_kindling.py`, live file checked byte for byte against the tested copy): an everyday word no longer counts as a name (any word that appears in lower case anywhere in Books 1 and 2, its plural, -ed, -ing and -ly forms, and compounds like Everybody, Elsewhere, Ourselves). A word that appears only at the start of a sentence, once, no longer fails. A name still fails if it appears mid-sentence or twice. The log line now prints each flagged word with the text around it. Earlier same-day changes: `faaa915` (two halves per chapter), `53f07e1` (only "the series", "this series", "Book N", "protagonist" and "Scene N" label lines are rejected).
- TESTED ON: sample text and all 45 Book 2 chapters. The name check flags 19 of 45 Book 2 chapters instead of 29, and what remains is only real Book 2 names and titles (Pryce, Vrell, Corvane, Herald and similar). Chapter 1 passes with no hard findings. NOT yet run against the live model, so chapter 2 may still need one more look.
- THE MODEL SIDE IS UNSTABLE: the first line of the last log shows OpenRouter returning 200 with no `choices` ("Upstream error from Nvidia: Service te..."), which retries and stretches a run. If a run stalls or is slow, read the log for that line before blaming the checker.
- NEXT, ONE STEP: Zia opens https://github.com/aliwaziri/Voxel/actions/workflows/write-kindling.yml and clicks Run workflow with start 1, both boxes unticked. Chapter 1 is kept and chapters 2 to 5 are written. He pastes the end of the log (from the line REPORT upward). If chapter 2 fails again, the HARD line now shows the flagged words with context: change the checker from that text, not from a guess.
- NOT YET DONE: an editor read of chapter 1 (dashes, the someone/something words, fit with the beat); Book 3 `brief.txt`, `book_config.json`, `VOICE_GUIDE.md`, `architecture.md` (the writer does not need them).
- HOW THIS SESSION WORKED (method that held up): put the change in a script in the repo and have Zia run it from the Actions tab, instead of retyping chapters by hand through the chat (about 45k tokens per pair of chapters); test on a fresh clone of the live repo first; after Zia runs it, check the live repo, not his word and not the green tick; one step at a time; every link and path in its own code block. Zia's rule from 2026-10-02: no profile changes anything without his permission in the current conversation; he may delegate a decision explicitly, as he did for Valerius and the mother, and for the checker fix on 2026-10-06.
- BOOKS 1 AND 2 CONTEXT (so nobody redoes it): the Book 1 continuity passes and the Book 2 Year 4 header change were applied by the workflow "Fix Book 1" (commits `b2c3ff2`, `1ea8800`; later passes by other sessions are recorded in the Book 1 HANDOFF). The canon from those passes is in the Book 1 and Book 2 HANDOFF files. Do not reopen it here.

Updated 2026-10-04 (IST, after the BEAT_MAP_BATCH9, ROMANCE_BATCH9 and STORY_SUMMARY pushes). FREEZE: no new rules, sections or checks.

## STATUS UPDATE (latest session, same day)
- DONE: the whole book now has a beat map and a full-scene romance beat for every chapter. Plot beats: BEAT_MAP.md (ch.1-15), BEAT_MAP_BATCH4.md (16-20), BEAT_MAP_BATCH5.md (21-25), BEAT_MAP_BATCH6.md (26-30), BEAT_MAP_BATCH7.md (31-35), BEAT_MAP_BATCH8.md (36-40), BEAT_MAP_BATCH9.md (41-45). Romance scenes: ROMANCE_BATCH1.md to ROMANCE_BATCH9.md (ch.1-45). Also THREAD_LEDGER.md and STORY_SUMMARY.md (the one-page plain story for Zia).
- BEAT_MAP_BATCH8.md and BEAT_MAP_BATCH9.md were written from the old one-line spine and CANON_LOCK v3.1. Everything in them beyond the old spine is the author's proposal and can be changed: Malrik's note and the Thorne guard holding the door (ch.36); Renn's map with the sockets in the lintel and sill (ch.38); Mara's "You called. I ran." (ch.39); Aldous bringing the steward (ch.40); the pick held at the line with words and then sitting down on a stone (ch.42); the close and the one echo (ch.43); the steward sent to the Lower Reach (ch.44); Auda's letter and the cold iron (ch.45).
- Zia decided to stop over-checking. Ordinary readers do not calculate ages, counts or days. Read READER_FIX_LIST.md in this folder. The snag lists in the digest INDEX files are NOT a to-do list. Do not hunt for new snags and do not read chapters to look for them.
- Zia is tired of "fixing" talk. Do the work; report what was built and what is next in plain words. Do not announce that things are "fixed".
- NEXT: Zia has NOT yet reacted to any batch or to STORY_SUMMARY.md. Wait for his reaction and make his changes first. Then, in order: (1) Name audit for Ulla, Yelva and any new name. (2) Create brief.txt, book_config.json, VOICE_GUIDE.md, architecture.md for Book 3. (3) Generate chapters batch by batch: verify batch 1 first, generate it, verify against the real text, then batch 2, and so on. Feed the REAL text of the previous chapter into each generation.
- The collar beat belongs to ch.12 and ch.23 only. "Later" and "Hold me to it" are the couple's private words from ch.5 (used again in ch.25 and as the last exchange of ch.45).
- Small tidy-ups for the editor (not for the writer): ROMANCE_BATCH7.md ch.34 has a line saying a rooster or bell "is not needed" (the writer must not add either). ROMANCE_BATCH9.md ch.45 says the closing "Later / Hold me to it" is "the fifth time"; the count of earlier uses is not verified, so drop "fifth" when writing the chapter.

## ROMANCE SPINE (Zia said "yes" to this in outline; it is the author's draft, not verified against the Book 1 and 2 digests)
- Sol wants years with Kael and wants to be his equal, never the one he pays for. Kael wants her safe; his habit is to stand near her and pay. He must learn to let her ask.
- Between them: Sol about 18 years left, Kael about 34; his protecting her is what could burn him out.
- Arc: ch.1-11 the clock is back on the page and they say the numbers aloud again; ch.12-23 they grow closer and make the public step; ch.24-33 the strain peaks, his habit breaks the plan, they are apart; ch.34-45 trust is rebuilt and in the end she asks and he steps back. That one act is the love scene at the heart of the book.
- POLITICS: Book 2 is mostly political, so politics must ease off slowly, not end in one chapter. Tension changes owner: from political stakes to stakes on the couple (the years, Mara's cold, the order's deadline, the pick). A thread may live while it presses on the couple; when it presses only on the Council, close it quickly and off the page. Three short political scenes only: ch.2, 12, 30.

## CRITICAL REVIEW OF EARLIER DECISIONS (for the next session to weigh, not obey)
1. ENDING ARITHMETIC. The "thirty-three each" ending is neat but engineered (Kael 34, he pays a year in ch.31, Sol 16 plus 17). It reads like a puzzle if numbers are stated often. Batch 9 states thirty-three only in ch.44 and ch.45. A reader should feel the ending, not add it up.
2. BATCH 7. Ch.32-34 keep them apart (about 7,500 words). The romance there is carried by the sock, the stick and the counts said aloud; ch.31 and ch.35 carry real scenes together. The day table is the author's own choice and can change (for example, bringing Sol back a day sooner).
3. INVENTED PLOT. Much of ch.6-45 is [PROPOSED] by the author. Zia has approved the shape only loosely. STORY_SUMMARY.md is the one-page version for him to approve or change BEFORE any generation.
4. OVER-ENGINEERING. Zia has said many times "do not overdo it". Fourteen writer rules per batch and a long canon lock risk stiff prose. Keep them as safety rails, do not add more.
5. DELEGATED CALLS (reversible, all decided as Zia): Chancellor is Ingrith Tenn (off the page); no month names but Cinderveil; Sol is Isolde Vane; the Reach has no handfast custom; the steward's motive (CANON_LOCK section 8).
6. UNVERIFIED BY THE AUTHOR: everything from Book 2 ch.20-45 and all of Book 1 comes from the digests, not from the chapters. Batch 1 (ch.1-5) was written by another session and checked only lightly.

## HOW SESSIONS WORK
- Claude has no memory between sessions. The repo is the memory. Zia says sessions run one at a time. The GitHub tool replaces whole files only and needs the current SHA, so fetch the file before every edit; workflow commits (Finalize Kindling) also change SHAs.
- Do NOT re-read Book 1 or Book 2 chapters to answer a fact. Use the digests: novels/kindling-line-book-1/digest/ (ch.1-10 digested so far, DIGEST_ch01-10.md; a Book 1 INDEX.md is not written yet) and novels/kindling-line-book-2/digest/INDEX.md (complete, ch.1-45).
- Write files straight to GitHub with the tool; a sandbox file has to be sent twice.
- Before ending a session: push the work and update this file.

## READ IN THIS ORDER
1. novels/EDITORIAL_CHARTER.md
2. novels/BEAT_MAP_PROTOCOL.md
3. novels/kindling-line-book-3/CANON_LOCK.md (v3.1: days, counts, plates, cast, calendar)
4. STORY_SUMMARY.md (the plot on one page), then the batch files in novels/kindling-line-book-3/: BEAT_MAP.md (ch.1-15), BEAT_MAP_BATCH4.md (16-20) to BEAT_MAP_BATCH9.md (41-45).
5. READER_FIX_LIST.md, THREAD_LEDGER.md, and ROMANCE_BATCH1.md to ROMANCE_BATCH9.md (the full-scene romance beats; each chapter's romance scene comes first in the chapter).

## DECIDED (Claude under Zia's full delegation; Zia may reverse any)
- Sol (Isolde Vane) starts at 18 years left; Kael about 34. Stored sum 17. Ending: Kael stands back because Sol asks aloud; she is at the plate, so the whole stored sum goes to her. Burn ledger in CANON_LOCK section 4.
- 45 chapters, odd Sol, even Kael. No month names except Cinderveil; headers say "Day N".
- The steward is the carrying hand; reveal in ch.27 only. One-word fix to B2 ch.41 ("another man's handwriting" to "another hand's") only after ch.27 is generated and verified, by the editor, never the writer.

## ZIA'S STANDING RULES
1. Zia is a man, 51, not technical. ONE step at a time, plain language, click by click. Anything he must copy goes in its own code block, full length, full link or path.
2. NEVER ASSUME. Verify against the live repo; label unverified items. Be proactive.
3. Be critical; flag problems, do not bury them. Also: keep it simple, do not overdo it.
4. Romance (Romantasy) is the A-plot. Politics is pressure only.
5. Zia dictates by voice; verify proper nouns.
6. When Zia asks for a reply for another profile, write the reply itself in a code block.
7. Titles: variety; the new Kindling books should not all open What/Where/When/Why/How.

REPO: aliwaziri10/Voxel (NOT Wazzaboyzz/Voxel), branch main.

## BOOKS 1 AND 2
- Both 45 chapters, proofread, not published. Plan: write all three, then publish 1, 2, 3 in order.
- Finalize Kindling must be re-run after commits 1fa8e02 (B2 ch.3) and 42bba69 (B1 carried hand "leans to the right"). Zia runs it here: https://github.com/aliwaziri10/Voxel/actions/workflows/finalize-kindling.yml
- Do not commit while Finalize is running. Assistant writes to .github/workflows return 403; Zia pastes workflow edits.
- Book 1 ch.45 was rewritten (commit c56f3f4): a Records clerk sends a loose ledger leaf from Corrin's seized books; every row's total is a year or two above its lines, the difference in a second, darker hand under "carried".

## TITLES (Zia's call; not needed to write the book)
- Book 1: Zia chose BORROWED YEARS (not yet applied; book_config.json still says "What the Gift Demands").
- Book 2: rejected "What the Ledger Keeps", "Hold Me to It", "Eleven Breaths". Options: Count With Me; Two Names or None; Say It Aloud; Ink and Ash.
- Book 3: rejected "What the Years Hold", "All the Years Between". Options: Years Enough; Silver at His Temples; Stand Near Me; Slow to Burn.
- Series name stays "The Kindling Line".
