# HANDOFF - Kindling Line (series level, Book 3 planning)

Updated 2026-10-03. FREEZE: do not add new rules, sections or checks.

## MEMORY RULE (Zia, 2026-10-03)
Claude has no memory between sessions. The repo is the memory. Do NOT re-read Book 1 or Book 2 chapters to answer a fact question. Read the digests first:
- novels/kindling-line-book-2/digest/INDEX.md (progress, snags, method) and the DIGEST_*.md files beside it.
- novels/kindling-line-book-1/digest/INDEX.md if it exists (Book 1 digest not started as of this update).
Then read the chapter only to confirm one fact. Before ending any session: push what was done, update the digest INDEX.md and this file. Zia wants every profile and the OpenRouter writer to work from the repo.

## BOOK 3 FILES (all on main, read in this order)
1. novels/EDITORIAL_CHARTER.md
2. novels/BEAT_MAP_PROTOCOL.md
3. novels/kindling-line-book-3/CANON_LOCK.md (draft v1: mechanics, closed cast, calendar, count, locked beats)
4. novels/kindling-line-book-3/BEAT_MAP.md (draft v1: batches 1-3 full entries, batches 4-9 spine only)
5. the Book 2 digest (above)

DECIDED 2026-10-03 (Claude, under Zia's full delegation): Sol starts at 18 years left; stored sum 17; the one-word fix to B2 ch.41 is allowed only if the steward is the hand (ch.27). Book 3 is 45 chapters [proposed], odd chapters Sol, even Kael. Three political scenes only: ch.2, 12, 30.

STATUS: nothing drafted. Batches 1-3 (ch.1-15) are ready for generation once the checks below pass. Batches 4-9 are spine only: expand each ONLY after the previous batch is generated and verified. A parallel session may hold an unpushed canon lock v2: merge it into CANON_LOCK.md, do not keep two.
Digest progress: Book 2 ch.5-14 done. Remaining: ch.15-35, then ch.1-4 and ch.36-45, then Book 1. After each batch of the digest, check CANON_LOCK.md and BEAT_MAP.md against it and correct conflicts.

## READ FIRST - ZIA'S STANDING RULES
1. Anything Zia must copy, paste or run (links, paths, commands, text) goes full length, full link or path, in its own code block with a copy button. Never shortened.
2. NEVER ASSUME. Research and verify against the live repo first. Clone it in the sandbox (git clone https://github.com/aliwaziri10/Voxel.git) and use grep; the GitHub search tool returns incomplete results. Run git fetch and git pull before every edit: another session also writes to this repo.
3. Titles: not a ban on What/Where/When/Why/How. Zia wants variety: of the seven novels (four published, three new Kindling books) the new ones should not all open that way.
4. The Kindling Line is a ROMANCE (Romantasy). Romance is the A-plot. Politics is pressure, never the plot.
5. Zia dictates by voice, so proper nouns may arrive garbled. Verify before trusting.
6. Zia is a man, 51.
7. Be critical. Test other sessions' claims and your own earlier decisions against the text. Zia wants challenged ideas and real changes. Zia also says: do not overdo it. Keep it simple.
8. When Zia asks for a reply to the other session, write the reply itself in a code block, not an explanation to Zia.

REPO: aliwaziri10/Voxel (NOT Wazzaboyzz/Voxel). Branch main.

## STATE OF BOOKS 1 AND 2 (verified)
- Both 45 chapters, proofread, not published. Plan: write all three books, then publish 1, 2, 3 in order.
- Book 1 ch.45 ending REWRITTEN (commit c56f3f4). New ending: a Records clerk sends a loose ledger leaf from Corrin's seized books. Every row's total is a year or two above its lines, the difference in a second, darker hand under the word "carried". Sol's mother's row has one. The newest row (29 Frostveil, Vane and Ashworth) has one too, after Corrin was frozen.
- Commit 42bba69: the carried hand now "leans to the right".
- Book 2 ch.1 (commit 2561565) and ch.3 (commit 1fa8e02): "three years" became "a year" where it meant Sol and Kael's time together.
- Finalize Kindling must be RE-RUN after commits 1fa8e02 and 42bba69. Run page: https://github.com/aliwaziri10/Voxel/actions/workflows/finalize-kindling.yml
- Do not commit while Finalize is running. Assistant writes to .github/workflows return 403; Zia pastes workflow edits. The GitHub tool replaces whole files only.

## VERIFIED FACTS THAT SHAPE BOOK 3
- Book 2 never mentions the Kindling or Sol's burn. Book 3 brings the clock back on the page in ch.1.
- Sol's clock, Book 1 ch.44: nineteen now, eighteen if the winter is hard. Book 3 uses 18 (decided). Earlier Book 1 numbers disagree; not fixed. Kael says about thirty to thirty-five years. Her mother died at 42.
- Cost rule in Book 1: ch.3 "The nearest living body pays"; ch.10 three percent bleeds to the nearest living body within five feet; ch.14 "the cost splits, most goes to the nearest body". Book 3 defines nearest once in CANON_LOCK.md and states no radius number.
- Book 2: "the Vault" is the old pre-Accord charge trunk line under the Reach. Ward-lines are "a debt that hasn't decided who owes it yet" (ch.14). Charge cycle is eleven breaths (first on the page in ch.14).
- Book 2 ends 30 Cinderveil Year 4 (ch.45): tap closed on eleven; a pulse from under the boiling house; the second line "adds a breath to every cycle" (the text does NOT say it stores years); petition signed with two names; the Chancellor asks who held the ledger pen forty years ago.
- Open Book 2 threads: Renn missing since 4 Cinderveil; Mara hurt and not waking; forged Council witness line; twin brass pegs; the smith Corwin; the second ward-line under the boiling house; Farrow's postscript "Ask the boy who taught him his letters"; Aldous Thorne spoke against his house (ch.42); Kael's left leg numb; techs Odo Marl and Tessa Rook; the Lower Spine anchor (Sol's mother's plate, 211 steps).
- Calendar: Emberfall, Frostveil, Sunspire (30 days), Cinderveil. Year length UNKNOWN. No "Year 5" until Zia gives the month list.
- Ward-chain (Book 1 ch.3) stays dropped.
- Locked canon: transfer is always involuntary; no ward-binding or chosen buffer; wards belong to the paid trade only; Sol burned 3 and Kael absorbed 3 at the Reckoning; "every time" rule; no em dashes; avoid particular and some/something hedges; spell grey; 2,300-2,700 words per chapter.

## ENDING (reuses Book 1's rule, nothing new)
The second line stores years carried off other people. When it closes, the whole stored sum goes to the nearest living body. Sol is at the plate, so she is nearest. Kael stands back because she asks aloud and he says yes. Sol 15 plus 17 is 32; Kael about 32. Planted in ch.1 and ch.8. Full detail in CANON_LOCK.md.

## OPEN ITEMS NEEDING ZIA
1. Real month list and year length.
2. Titles (below).
3. Sol's full first name; Corwin's tag; the Chancellor's name; whether the Reach has a handfast custom (ch.23); the steward's motive for the forged witness line.

## NEXT STEPS
1. Finish the Book 2 digest (ch.15-35, then 1-4 and 36-45), then Book 1. Correct the beat map where it conflicts.
2. Name audit across all Voxel novels (Book 1 has Auditor Mara Vex, ch.40; Book 2 has an Ashworth warden Mara).
3. Verify batch 1 against the real text, generate it, then verify before batch 2. Five chapters per batch, real text of the previous chapter fed forward.
4. Create brief.txt, book_config.json, VOICE_GUIDE.md, architecture.md for Book 3.

## TITLES
- Book 1: Zia chose BORROWED YEARS (not yet applied; book_config.json title is still "What the Gift Demands").
- Book 2: rejected "What the Ledger Keeps", "Hold Me to It", "Eleven Breaths". Options (not Amazon-checked): Count With Me; Two Names or None; Say It Aloud; Ink and Ash.
- Book 3: rejected "What the Years Hold", "All the Years Between". Options: Years Enough; Silver at His Temples; Stand Near Me; Slow to Burn.
- Series name stays "The Kindling Line".
