# HANDOFF - Kindling Line (series level, Book 3 not yet started)

Updated 2026-10-03 after a verified read of the live repo. This replaces the earlier pasted handoff, which had errors (see "Corrections").

## READ FIRST - ZIA'S STANDING RULES
1. Anything Zia must copy, paste or run (links, paths, commands, text) goes full length, full link or path, in its own code block with a copy button. Never shortened.
2. NEVER ASSUME. Research and verify against the live repo first, then answer. The repo can be cloned in the sandbox (git clone https://github.com/aliwaziri10/Voxel.git) and searched with grep; do not rely on the GitHub search tool, which returns incomplete results.
3. Titles: this is NOT a ban on What/Where/When/Why/How. Zia's point is variety: of the seven novels (four published, three new Kindling books) the new ones should have a different flavor instead of always opening that way.
4. The Kindling Line is a ROMANCE (Romantasy). Romance is the A-plot. Politics may be pressure, never the plot.
5. Zia dictates by voice, so proper nouns may arrive garbled. Verify before trusting.
6. Zia is a man, 51. An earlier handoff wrongly said "she".
7. Use critical reasoning and push back. Do not just agree. Do not assert what you have not read; if a check is possible, do it.

REPO: aliwaziri10/Voxel (NOT Wazzaboyzz/Voxel). Branch main. Read novels/EDITORIAL_CHARTER.md first, then the book's HANDOFF.md.

## STATE OF BOOKS 1 AND 2 (verified)
- Both 45 chapters, proofread, not published. Plan: write all three books first, then publish 1, 2, 3 in order.
- Book 1 ch.45 ending REWRITTEN (commit c56f3f4): the chain-fist letter, Contract of Perpetual Surety, Deep Vault, Magister Vane, Keeper of the Burning Ledger and the diving hawk are gone. New ending: a Records clerk sends a loose ledger leaf found in Corrin's seized books. Every row's total is a year or two above its lines, the difference in a second, darker hand under the word "carried". Sol's mother's row has one. The newest row (29 Frostveil, Vane and Ashworth) has one too, after Corrin was frozen at noon. Kael starts to take it up alone, Sol says no, he agrees. Verified by grep: no other Book 1 chapter mentions the old terms.
- Book 2 ch.1 fixed (commit 2561565): "three years" became "a year" in three places. Book 1 covers about ten weeks, Book 2 opens 9 Sunspire Year 4.
- Finalize Kindling workflow ran green after the ch.45 change (commit 3f30f60, Book 1 now 3940 paragraphs, Book 2 2602). It must be RE-RUN after the Book 2 ch.1 fix. Run page: https://github.com/aliwaziri10/Voxel/actions/workflows/finalize-kindling.yml
- Do not commit while Finalize is running. Assistant writes to .github/workflows return 403; Zia pastes workflow edits. The GitHub tool replaces whole files only.

## VERIFIED FACTS THAT SHAPE BOOK 3
- Sol's clock (Book 1 ch.44, 5 Sunspire Year 3): nine years at the old burn rate, twenty-two at the new one before the Reckoning, nineteen now, eighteen if the winter is hard. Kael says about thirty to thirty-five. Ch.44 ends "Time to grow old. Together. If the Kindling allows it." Her mother died at 42. UNVERIFIED: Sol's age and the count a year later in Book 2.
- Book 2 world: "the Vault" is the old pre-Accord charge trunk line under the Reach (ch.8, 13, 14, 41). Ward-lines carry charge; Sol quotes her mother (ch.14): "a ward-line is a debt that hasn't decided who owes it yet". The Instrument of Dissolution (ch.1) puts "the reserves of stored charge" under Council custody. Thorne tapped the trunk line for three years and held the clerk Varel. Charge cycle is eleven breaths (ch.14, ch.45); Thorne's family tally says ten.
- Book 2 ch.13: old tap entries in "another hand, older and blunter" were never balanced against the register. This echoes the new Book 1 ending.
- Book 2 ends 30 Cinderveil Year 4 (ch.45): tap at Anchor Seven closed on a count of eleven; a pulse from the east, from under the boiling house, on the eleventh breath; petition signed with two names ("two names or none"); Chancellor asks who held the ledger pen forty years ago and what Kael will do if the hand belongs to a trusted house.
- Open Book 2 threads at the end: Renn missing since 4 Cinderveil (a coast lead, a lamp on the stair emptied by hand); Mara hurt 4 Cinderveil, cold at the wrists, not waking; forged Council witness line (Farrow's postscript: "Ask the boy who taught him his letters", Aldous's tutor); twin brass peg placed in the cellar (a smith who cast a ceremonial die for Thorne eight years ago); Council surveyor missing since first week of Cinderveil; second ward-line under the boiling house (an older surveyor recalls talk of it forty years ago); Ansa's lamp dark; Kael's left leg numb, recovering; Kael's private fourth page for Sol; Ferra's family account; Aldous Thorne asked leave to speak (ch.41, unresolved there).
- Loose end: Book 1 ch.3, Kael gives Sol his father's ward-chain (twenty years of stored capacity, registered to Valerius). It never appears again in Book 1 or Book 2 (grep). Decide whether Book 3 uses it or it stays dropped.
- Locked canon: transfer is always involuntary; no ward-binding or chosen buffer between Sol and Kael; wards belong to the paid trade only; Sol burned 3 years at Book 1's Reckoning and Kael absorbed 3; "every time" rule (say it aloud to Joren and Corren by name); no em dashes; avoid particular and some/something hedges; spell grey; 2,300-2,700 words per chapter.

## BOOK 3 PLAN (Claude's decision, revised after reading Book 2)
Zia asked Claude to decide the shape and wants it deeply reasoned. Revisions after review:
- Do NOT drop Book 2's threads. Build a payoff list from all 45 Book 2 chapters; every thread gets a slot, paid through the romance, not through votes and hearings.
- Spine: "the count is wrong". A hidden hand has been adding cost for decades. One small mystery with people already on the page. No new factions, no new magic rules.
- The clock is the romance engine: Sol's remaining years against the promise to grow old together. The way the hidden hand's extra cost connects to the years Sol burns is NOT yet established in the text. It must be set up on the page early (around chapter 8) and written in the canon lock, or the clock needs another resolution. This is the main open design decision.
- Chapter 1 opens with Sol and Kael together after Book 2's ending; first problem comes from the pulse or the consequences of the petition.
- Midpoint: a public step that is theirs alone, not a ward-binding and not a repeat of the petition.
- Dark moment earned: Sol sees the cost land on Kael and leaves to protect him, with a reasoned plan. Climax: a rescue only Sol can fly, decided together out loud. The happy ending costs them something real but small.
- Every chapter names a romance beat first; chapters end on hooks; viewpoint alternates.
- Zia has not explicitly approved this shape.

## NEXT STEPS (per novels/BEAT_MAP_PROTOCOL.md)
1. Read Book 2 ch.2-12 and ch.37-42 and Book 1 key chapters; settle the cost mechanism link and write the payoff list.
2. Name audit against EVERY Voxel novel. Note Book 1 has Auditor Mara Vex (ch.40) and Book 2 has an Ashworth warden named Mara.
3. Canon lock with a closed cast list, a calendar computed once (month list not yet verified), locked one-time lines.
4. Beat map, 15-20 lines per chapter, five chapters per batch, real text of the previous chapter fed forward, verify between batches.
5. Create novels/kindling-line-book-3/ (brief.txt, book_config.json, VOICE_GUIDE.md, architecture.md).
6. Genre guard in the canon lock. UNVERIFIED whether scripts/proofreader.py can enforce a cast whitelist.

## TITLES
- Book 1: Zia chose BORROWED YEARS (not yet applied; book_config.json title is still "What the Gift Demands").
- Book 2: rejected "What the Ledger Keeps", "Hold Me to It", "Eleven Breaths". Options (not Amazon-checked): Count With Me; Two Names or None; Say It Aloud; Ink and Ash.
- Book 3: rejected "What the Years Hold", "All the Years Between". Options: Years Enough; Silver at His Temples; Stand Near Me; Slow to Burn.
- Series name stays "The Kindling Line". Not yet picked: Book 2 and Book 3 titles.

## STILL OPEN (not verified)
- Whether the Finalize docx look right in Word.
- Front matter or blurb drafts that may carry old titles.
- Whether Book 1's book_config.json author is Ivy Cassel.
- Book 2 ch.2-12 and 37-42, and most Book 1 chapters, were searched but not read in full.
