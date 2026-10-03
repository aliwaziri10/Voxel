# HANDOFF - Kindling Line (series level, Book 3 not yet started)

Updated 2026-10-03 after a verified read of the live repo and a critical review. This replaces the earlier pasted handoff, which had errors (see "Corrections").

## READ FIRST - ZIA'S STANDING RULES
1. Anything Zia must copy, paste or run (links, paths, commands, text) goes full length, full link or path, in its own code block with a copy button. Never shortened.
2. NEVER ASSUME. Research and verify against the live repo first, then answer. The repo can be cloned in the sandbox (git clone https://github.com/aliwaziri10/Voxel.git) and searched with grep; do not rely on the GitHub search tool, which returns incomplete results. Run git fetch and git pull before every edit: another session also writes to this repo.
3. Titles: this is NOT a ban on What/Where/When/Why/How. Zia's point is variety: of the seven novels (four published, three new Kindling books) the new ones should have a different flavor instead of always opening that way.
4. The Kindling Line is a ROMANCE (Romantasy). Romance is the A-plot. Politics may be pressure, never the plot.
5. Zia dictates by voice, so proper nouns may arrive garbled. Verify before trusting.
6. Zia is a man, 51. An earlier handoff wrongly said "she".
7. Be critical. Do not accept another session's corrections or your own earlier decisions without testing them against the text. Zia wants challenged ideas and real changes, not agreement.

REPO: aliwaziri10/Voxel (NOT Wazzaboyzz/Voxel). Branch main. Read novels/EDITORIAL_CHARTER.md first, then the book's HANDOFF.md.

## STATE OF BOOKS 1 AND 2 (verified)
- Both 45 chapters, proofread, not published. Plan: write all three books first, then publish 1, 2, 3 in order.
- Book 1 ch.45 ending REWRITTEN (commit c56f3f4): the chain-fist letter, Contract of Perpetual Surety, Deep Vault, Magister Vane, Keeper of the Burning Ledger and the diving hawk are gone. New ending: a Records clerk sends a loose ledger leaf found in Corrin's seized books. Every row's total is a year or two above its lines, the difference in a second, darker hand under the word "carried". Sol's mother's row has one. The newest row (29 Frostveil, Vane and Ashworth) has one too, after Corrin was frozen at noon. Kael starts to take it up alone, Sol says no, he agrees. Verified by grep: no other Book 1 chapter mentions the old terms.
- Commit 42bba69: in that leaf the carried hand now "leans to the right" (was "the other way"), a clue for the Book 3 handwriting thread below.
- Book 2 ch.1 (commit 2561565) and ch.3 (commit 1fa8e02, by another session): "three years" became "a year" where it meant Sol and Kael's time together. Book 1 covers about ten weeks and Book 2 opens 9 Sunspire Year 4.
- Finalize Kindling must be RE-RUN after commits 1fa8e02 and 42bba69. Run page: https://github.com/aliwaziri10/Voxel/actions/workflows/finalize-kindling.yml
- Do not commit while Finalize is running. Assistant writes to .github/workflows return 403; Zia pastes workflow edits. The GitHub tool replaces whole files only.

## VERIFIED FACTS THAT SHAPE BOOK 3
- Book 2 NEVER mentions the Kindling or Sol's burn (searched every chapter). Book 3 must reintroduce the clock on the page, early.
- Sol's clock, Book 1 ch.44 (5 Sunspire Year 3), is the final word: nine years at the old rate, twenty-two before the Reckoning, nineteen now, eighteen if the winter is hard; ch.3 says the count is years of life, stopping does not raise it. Earlier Book 1 numbers disagree with each other and with ch.44: ch.3 twenty-two, ch.17 8.3, ch.21 23 down to 18 or 17 plus a ledger line 42 falling to 38.7. Not fixed; flagged for a later pass. Kael says about thirty to thirty-five years. Her mother died at 42.
- Book 2 world: "the Vault" is the old pre-Accord charge trunk line under the Reach (ch.8, 13, 14, 41). Sol quotes her mother (ch.14): "a ward-line is a debt that hasn't decided who owes it yet". The Instrument of Dissolution (ch.1) puts "the reserves of stored charge" under Council custody. Thorne tapped the trunk line for three years and held the clerk Varel. Charge cycle is eleven breaths (ch.14, ch.45).
- Book 2 ch.13: old tap entries in "another hand, older and blunter" were never balanced against the register.
- Book 2 ends 30 Cinderveil Year 4 (ch.45): tap at Anchor Seven closed on eleven; a pulse from under the boiling house on the eleventh breath; the second line "adds a breath to every cycle" (the text does NOT say it stores years); petition signed with two names; Chancellor asks who held the ledger pen forty years ago.
- Open Book 2 threads: Renn (Council surveyor) missing since 4 Cinderveil, last seen on a skiff going south; Mara hurt, cold at the wrists, not waking; forged Council witness line; the twin brass pegs; the smith Corwin (only named lead, cast a die for Thorne eight years ago, questioned gently, no proof); the second ward-line under the boiling house (a surveyor recalls talk of it forty years ago); Farrow's postscript "Ask the boy who taught him his letters"; Aldous Thorne spoke against his house in ch.42; Kael's left leg numb, recovering; techs Odo Marl and Tessa Rook; the Lower Spine anchor (Sol's mother's plate, 211 steps, ch.2-4).
- Calendar: attested consecutive months Emberfall, Frostveil, Sunspire (30 days), Cinderveil. Year length is UNKNOWN. "Eight months in the ground" for Valerius (Book 2 ch.1, 2) rules out a four-month year but fits twelve. Do not use "Year 5" anywhere until Zia gives the real month list.
- Loose end: Book 1 ch.3, Kael gives Sol his father's ward-chain (twenty years of stored capacity). Never appears again. Default: stays dropped.
- Locked canon: transfer is always involuntary; no ward-binding or chosen buffer between Sol and Kael; wards belong to the paid trade only; Sol burned 3 years at the Reckoning and Kael absorbed 3; "every time" rule (say it aloud to Joren and Corren by name); no em dashes; avoid particular and some/something hedges; spell grey; 2,300-2,700 words per chapter.

## BOOK 3 PLAN (revised after critical review; items marked [PROPOSED] need Zia's approval)
Kept from before: payoff list of every Book 2 thread; romance beat first in every chapter; politics is pressure only (max three short political scenes, none is the midpoint or climax); hooks vary; viewpoint alternates; dark moment earned (Sol sees the cost land on Kael and leaves with a reasoned plan); the public step at the midpoint is theirs alone and not a ward-binding; a happy ending that costs something.

[PROPOSED] THE ONE NEW RULE (the HEA cannot work without it; the old "no new magic rules" collided with Book 1 ch.44's "time to grow old together"):
- The years the hidden hand "carried" are stored on the second line under the boiling house. Book 3 must plant this by about chapter 8; it is NOT in Book 2.
- When that line is closed, the stored years discharge involuntarily to every living body within five feet, split equally by headcount. This mirrors the cost transfer. No chosen recipient, no redirecting. The only choice anyone has is where to STAND.
- Size [NEW, number to confirm]: 24 years in total. Sol alone would gain all 24; with Kael within five feet each gains 12. Pool is the SUM of decades of carried years, not any single row.
- Price: cutting the line takes a Kindling flight that burns Sol's years first, and the cost bleeds to whoever stands near her. It pays out once.
- Climax: Kael stands near knowing it halves her return and that he absorbs the cost; Sol says yes aloud. The dark moment mirrors it: Sol leaves so Kael is never within five feet. The scene geometry must make sure no stranger can be within five feet, or the rule becomes a lottery.
- Outcome: Sol ends with roughly thirty more years, past her mother's age with real margin; epilogue years later. Retiring from large flights is part of the price.

[PROPOSED] THE HAND: the Thorne steward is the carrying hand AND Aldous's tutor. Evidence, all verified in the text: Aldous (B2 ch.42) says "a hand I have trusted since I was small stopped it", and the steward's hand is the one on his sleeve (ch.41, 42); Farrow's postscript (ch.43) says to ask the boy who taught him his letters; Aldous's letters lean right while the forged witness line stands upright with closed tails, "a practised hand, careful to look younger than it is" (ch.42); the Book 1 ch.45 carried hand now leans right. So her natural hand leans right, like the hand Aldous learned, and she disguised it upright for the forgery. No new villain: do NOT add a tutor named Xanthe. Constraints: Renn's hand in Book 2 ch.2 is "small and level, every descender closed", similar to the forgery's closed tails, so Renn's disappearance must be resolved as a red herring or as complicity; the Spine-stair steward in ch.4 is a narrow man, so treat him as a different person or fix the slip; who held the pen forty years ago is UNSET (the steward is past sixty).

Chapter 1 opens with Sol and Kael together after Book 2's ending; the Kindling clock returns in the first three chapters. Zia has not yet approved this shape or the rule.

## OPEN ITEMS NEEDING ZIA
1. Approve the one new rule and the size 24.
2. The real month list and year length.
3. Count entering Book 3: eighteen (about a year after ch.44's nineteen) or nineteen.
4. Titles (below).

## NEXT STEPS (per novels/BEAT_MAP_PROTOCOL.md)
1. Finish reading Book 2 ch.5-13 and ch.15-35 (read so far: 1-4, 14, 36-45); build the payoff list.
2. Name audit against EVERY Voxel novel. Book 1 has Auditor Mara Vex (ch.40) and Book 2 has an Ashworth warden named Mara. A parallel session has a draft canon lock (v2, not pushed); merge, do not duplicate.
3. Canon lock with a closed cast list (add Corwin, Odo Marl, Tessa Rook, the Lower Spine anchor), calendar, locked one-time lines.
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
- Book 2 ch.5-13 and 15-35, and most Book 1 chapters, were searched but not read in full.
