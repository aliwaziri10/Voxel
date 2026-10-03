# HANDOFF - Kindling Line (series level, Book 3 not yet started)

Updated 2026-10-03, end of session, after a verified read of the live repo and a critical review. FREEZE: do not add new rules, sections or checks until Zia approves the simple version below.

## READ FIRST - ZIA'S STANDING RULES
1. Anything Zia must copy, paste or run (links, paths, commands, text) goes full length, full link or path, in its own code block with a copy button. Never shortened.
2. NEVER ASSUME. Research and verify against the live repo first. Clone it in the sandbox (git clone https://github.com/aliwaziri10/Voxel.git) and use grep; the GitHub search tool returns incomplete results. Run git fetch and git pull before every edit: another session also writes to this repo.
3. Titles: not a ban on What/Where/When/Why/How. Zia wants variety: of the seven novels (four published, three new Kindling books) the new ones should not all open that way.
4. The Kindling Line is a ROMANCE (Romantasy). Romance is the A-plot. Politics is pressure, never the plot.
5. Zia dictates by voice, so proper nouns may arrive garbled. Verify before trusting.
6. Zia is a man, 51.
7. Be critical. Test other sessions' claims and your own earlier decisions against the text. Zia wants challenged ideas and real changes. Zia also says: do not overdo it. Keep it simple.
8. When Zia asks for a reply to the other session, write the reply itself in a code block, not an explanation to Zia.

REPO: aliwaziri10/Voxel (NOT Wazzaboyzz/Voxel). Branch main. Read novels/EDITORIAL_CHARTER.md first, then the book's HANDOFF.md.

## STATE OF BOOKS 1 AND 2 (verified)
- Both 45 chapters, proofread, not published. Plan: write all three books, then publish 1, 2, 3 in order.
- Book 1 ch.45 ending REWRITTEN (commit c56f3f4). The chain-fist letter, Contract of Perpetual Surety, Deep Vault, Magister Vane, Keeper of the Burning Ledger and the diving hawk are gone. New ending: a Records clerk sends a loose ledger leaf from Corrin's seized books. Every row's total is a year or two above its lines, the difference in a second, darker hand under the word "carried". Sol's mother's row has one. The newest row (29 Frostveil, Vane and Ashworth) has one too, after Corrin was frozen. No other Book 1 chapter mentions the old terms (grep).
- Commit 42bba69: the carried hand now "leans to the right" (was "the other way").
- Book 2 ch.1 (commit 2561565) and ch.3 (commit 1fa8e02, another session): "three years" became "a year" where it meant Sol and Kael's time together.
- Finalize Kindling must be RE-RUN after commits 1fa8e02 and 42bba69. Run page: https://github.com/aliwaziri10/Voxel/actions/workflows/finalize-kindling.yml
- Do not commit while Finalize is running. Assistant writes to .github/workflows return 403; Zia pastes workflow edits. The GitHub tool replaces whole files only.

## VERIFIED FACTS THAT SHAPE BOOK 3
- Book 2 never mentions the Kindling or Sol's burn (every chapter searched). Book 3 must bring the clock back on the page early.
- Sol's clock, Book 1 ch.44, is final: nineteen now, eighteen if the winter is hard (nine at the old rate, twenty-two before the Reckoning). Ch.3 says the count is years of life, stopping does not raise it. Earlier Book 1 numbers disagree (ch.3 twenty-two, ch.17 8.3, ch.21 23 down to 18 plus a ledger line 42 to 38.7). Not fixed. Kael says about thirty to thirty-five years. Her mother died at 42.
- Cost rule in Book 1: ch.3 "The nearest living body pays"; ch.10 three percent bleeds to the nearest living body within five feet; ch.14 "the cost splits, most goes to the nearest body". Ch.3 also says "the nearest living body is not always the one standing closest", so "nearest" needs one plain definition in the canon lock.
- Book 2: "the Vault" is the old pre-Accord charge trunk line under the Reach. Ward-lines are "a debt that hasn't decided who owes it yet" (ch.14). The Instrument of Dissolution puts "the reserves of stored charge" under Council custody (ch.1). Charge cycle is eleven breaths.
- Book 2 ch.13: old tap entries in "another hand, older and blunter" never balanced against the register.
- Book 2 ends 30 Cinderveil Year 4 (ch.45): tap closed on eleven; a pulse from under the boiling house; the second line "adds a breath to every cycle" (the text does NOT say it stores years); petition signed with two names; the Chancellor asks who held the ledger pen forty years ago.
- Open Book 2 threads: Renn (Council surveyor) missing since 4 Cinderveil; Mara hurt and not waking; forged Council witness line; twin brass pegs; the smith Corwin (only named lead); the second ward-line under the boiling house; Farrow's postscript "Ask the boy who taught him his letters"; Aldous Thorne spoke against his house (ch.42); Kael's left leg numb, recovering; techs Odo Marl and Tessa Rook; the Lower Spine anchor (Sol's mother's plate, 211 steps, ch.2-4).
- Calendar: consecutive months Emberfall, Frostveil, Sunspire (30 days), Cinderveil. Year length UNKNOWN. "Eight months in the ground" rules out a four-month year but fits twelve. No "Year 5" until Zia gives the month list.
- Ward-chain (Book 1 ch.3) never reappears. Default: stays dropped.
- Locked canon: transfer is always involuntary; no ward-binding or chosen buffer between Sol and Kael; wards belong to the paid trade only; Sol burned 3 and Kael absorbed 3 at the Reckoning; "every time" rule; no em dashes; avoid particular and some/something hedges; spell grey; 2,300-2,700 words per chapter.

## BOOK 3 PLAN - SIMPLE VERSION (needs Zia's approval; nothing below is final)
Kept: payoff list of every Book 2 thread; romance beat first in every chapter; politics is pressure only (max three short political scenes, none is the midpoint or climax); varied hooks; alternating viewpoint; an earned dark moment (Sol sees the cost land on Kael and leaves); the midpoint public step is theirs alone, not a ward-binding; a happy ending that costs something.

ENDING RULE (reuse Book 1's existing rule, no new one): the "carried" years are stored on the second line under the boiling house (Book 3 must plant this by about chapter 8; Book 2 does not say it). When that line closes, the stored years go to the NEAREST LIVING BODY, exactly as cost already does. No headcount split, no fixed figure. Rejected: an equal split, because both gain the same and Sol (about 18) stays far behind Kael (about 32), so standing near does not help her.
- The choice is who stands nearest. Each tries to stand back so the other gets the years, and they solve it together, aloud.
- Notes to check, not decided: the cost of the flight and the stored years both go to the nearest body, so the same person pays and gains. For the ending to work, the pool must be at least as large as the gap between their years (about fourteen), stated once on the page. Scene geometry must keep any stranger from being nearer.

THE HAND (proposal only): the Thorne steward as the carrying hand and Aldous's tutor is an unconfirmed idea. Evidence for: Aldous says "a hand I have trusted since I was small stopped it" and the steward's hand is on his sleeve (Book 2 ch.41-42); Farrow's postscript (ch.43). Cautions, verified: ch.41 says Aldous found his name "in another man's handwriting"; the steward's everyday hand is "even" (ch.6) and "flat and firm" (ch.17); the narrow man at the Spine stair (ch.4) and the small woman are likely two roles (house steward, works steward). No new villain unless Zia approves. Renn's hand in ch.2 is "small and level, every descender closed", close to the forged line's closed tails, so Renn's disappearance must be resolved as a red herring or as complicity. Who held the pen forty years ago is UNSET.

Chapter 1 opens with Sol and Kael together after Book 2's ending; the Kindling clock returns in the first three chapters.

## OPEN ITEMS NEEDING ZIA
1. Approve the simple ending rule above.
2. Real month list and year length.
3. Count entering Book 3: eighteen or nineteen.
4. Titles.

## NEXT STEPS (per novels/BEAT_MAP_PROTOCOL.md), only after approval
1. Read Book 2 ch.5-13 and ch.15-35 (read so far: 1-4, 14, 36-45); build the payoff list.
2. Name audit across all Voxel novels. Book 1 has Auditor Mara Vex (ch.40); Book 2 has an Ashworth warden Mara. A parallel session has an unpushed canon lock draft (v2); merge, do not duplicate.
3. Canon lock with a closed cast list (add Corwin, Odo Marl, Tessa Rook, the Lower Spine anchor), calendar, locked one-time lines.
4. Beat map, five chapters per batch, real text fed forward, verify between batches.
5. Create novels/kindling-line-book-3/ files (brief.txt, book_config.json, VOICE_GUIDE.md, architecture.md).

## TITLES
- Book 1: Zia chose BORROWED YEARS (not yet applied; book_config.json title is still "What the Gift Demands").
- Book 2: rejected "What the Ledger Keeps", "Hold Me to It", "Eleven Breaths". Options (not Amazon-checked): Count With Me; Two Names or None; Say It Aloud; Ink and Ash.
- Book 3: rejected "What the Years Hold", "All the Years Between". Options: Years Enough; Silver at His Temples; Stand Near Me; Slow to Burn.
- Series name stays "The Kindling Line". Book 2 and Book 3 titles not yet picked.

## STILL OPEN (not verified)
- Whether the Finalize docx look right in Word; front matter or blurbs carrying old titles; whether Book 1's book_config.json author is Ivy Cassel.
- Book 2 ch.5-13 and 15-35, and most of Book 1, were searched but not read in full.
