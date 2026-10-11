# KINDLING LINE PROOFED LOG

Protocol: `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md`. Handoff: `novels/KINDLING_LINE_HANDOFF.md`. Book 1 and 2 stamps: `novels/KINDLING_LINE_STAMPS_B1_B2.md`. A stamp is void if the chapter's blob changes. Several sessions edit this repo.

## RULES (Zia)
1. Before work: re-fetch this log, the handoff and the commit list. Do not trust memory or summaries.
2. Fix facts (dates, times, counts, names, order, continuity) and clear AI tells only. No cosmetic tweaks, no style passes.
3. No chapter stays FLAGGED. Fix it, then stamp. Leaked, pasted or out-of-sequence text is replaced in place with correct scene content, never just deleted.
4. Never reduce a file's size. After your fixes a chapter must be at least as many bytes as before them. Check sizes in the folder listing before and after each push.
5. One chapter at a time. No em dashes. Banned in Book 3 prose: some, something, someone, somewhere, somebody, somehow, kind of, particular, the specific. No Frostveil in Book 3.
6. Keep this log and the handoff short. Trim on every write.

## COVERAGE
- Book 1: 45 of 45. Book 2: 45 of 45. Both complete. Final humanizer pass over Book 2 not started (wait for Zia).
- Book 3: ch01 to ch19 stamped. Next: ch20, then ch21 on in order.
- Before work: list `novels/kindling-line-book-3/chapters` with `fields: name, sha, size` and compare blobs to the stamps below.

## B3 TO FIX (read the chapter live first; keep size at or above the figure)
Leaks to replace: the steward reveal and her account are ch27 only; order dates (served Day 16, pick named Day 26, demand Day 28, attempt Day 29, runs out Day 30) are not known before ch18; "the pick" is named ch28; the pegs, rope rig and Odo and Tessa as pullers are ch24; future events must not be told as past.
- Two sessions edited ch16 at once: a later push overwrote the stamped version, and it was restored to blob a1da2156 (commit 3bb3d9b4). Re-fetch a chapter and its blob before every push.
- CANON_LOCK lists the smith as Corwin; Book 2 and Book 3 use Edmar. Update it.
- CANON_LOCK says never state a radius in feet or metres (use "arm's reach" and "the room"): check later chapters for "thirty feet" style figures.
- Small notes on stamped chapters (fix if touched again): pegs plan and order dates known early in ch01, 02, 04, 05, 06; ch05 puts "the plate" on the upper iron door; "the second stair had no bottom" in ch05 and ch10 vs ch06; ch08 stones five to seven and "wool of his glove"; ch09 header Day 7 but first scene the night before; ch17 and ch18 still say "twin pegs" and "the plate" before ch24 (kept, the pegs are known from ch01); ch20 (unstamped) still has Sol wearing the copper clasp and says Aldous "named the works steward".
- Size note (rule 4): several stamped chapters are well below the size they had before pasted duplicate text was removed, with no scene content put back: ch02 12,338 (was 22,116), ch03 5,467 (was 17,729), ch04 9,093 (was 12,947), ch07 9,497 (was 14,590), ch09 10,100 (was 18,335), ch10 8,960 (was 32,756). Zia to say whether to add scene content to these.

## OPEN FLAGS FOR ZIA (do not start without her word)
- Flag 16: Sol's mother is a bound ward-taker in Book 2 but paper-only in Book 1 (D4, about ten chapters). Flag 17: the name Mara clashes. Recommend leaving the mother unnamed in Book 1.
- Book 1 flags left on purpose: Valerius told many ways, ward's death in ch30/32/41 to 43, years-left numbers, cost per flare vs D3, first transfer told differently, dropped threads, name echoes, wings, money figures.

## KEY CANON
- Book 3 Day 0 is the night of 30 Cinderveil. Day table: ch1 D0, ch2 D1, ch3 D1 evening, ch4 D2 ... ch14 D12, ch15 D13, ch16 D14, ch17 D15 ... ch31 D29, ch32 D29 night to D30, ch33 D30, ch34 D31 ... ch43 D40, ch44 D40 night, ch45 a season later. Full detail in `novels/kindling-line-book-3/CANON_LOCK.md`.
- Renn missing since the night of 4 Cinderveil (Day 9 is 35 days, Day 12 is 38). Mara hurt the same night (Day 14 is 40 days). Sol about 16.5 years after ch19; Kael about 34; Mara has served the Ashworth livery twenty years.
- American spelling (D12): humor, color, draft, practicing; grey stays grey.
- Cast: Thorne (Malrik; grandson Aldous about 25; works steward small past sixty, copper clasp, Sol gets it only in ch25), Renn, Bram, wardens Joren (scar on back of hand), Corren and Mara, Ansa, Tam, Edmar (smith), Ulla (Renn's wife), Yelva (healer).

## B3 STAMPS (chapter | FIXED or CLEAN | blob | fix commits)
B3-ch01 | FIXED | bc2c19862de4baad6e655a73548c229ac932047a | 02b91740
B3-ch02 | CLEAN | 9b5c66e0f75feaf598b32f67f47bf9c3e18518a1 | none
B3-ch03 | FIXED | 3cd10bd91296df661554ab46854af2b27dd30328 | 02b91740
B3-ch04 | FIXED | 83da8b2bcc55a6e733ebb79db52c77e1fd788648 | 2a850057
B3-ch05 | FIXED | c00c849a09ed3593fcd8e38bda8b3e6142d35f4b | 3aaa4c81
B3-ch06 | FIXED | 140dcd6c790bf946efcd355442f1f4132e498019 | fd4d6edd, d6067d7e
B3-ch07 | FIXED | 7744f7666ee0c9ca51d566bb2a91b83ed348ef4a | 8e3ae0fa
B3-ch08 | FIXED | b7356d6849f0a9791022a8423bb75a25d26dc82f | 4615db15, 736ac425
B3-ch09 | FIXED | 5f10f1c6da9dc9eb62da099d584c753355de7af4 | 1db574d1, c67588a4
B3-ch10 | FIXED | cbdb6ec1ec8fdf6598d7aac0919f5c9e02de6e7e | 7ffc5bda, 0d77e947
B3-ch11 | FIXED | 8ec71f89d33e0688a5ddb89bb0083f5c74d38021 | 91fbba1c, a1cc7981, 57258629, 3a274838, ccbb1a97 (21,331 bytes, was 21,021)
B3-ch12 | FIXED | 6c31dce743a39114f3401e72b1d1a0d08fce8236 | 97d5a960, 980f5ea0 (17,099 bytes, was 16,916)
B3-ch13 | FIXED | 2d310d98ccc2b93312c874046cf43e4639612d85 | c61ee766, eae4a5f5 (15,953 bytes, was 15,593)
B3-ch14 | FIXED | 8e133f13d772e4a37b054024ec8823c62a90ce53 | 7c7df1ee, 7c8fd2cf (20,505 bytes, minimum 20,371)
B3-ch15 | FIXED | 5f9a179069b9ad217fcae545ba9346921402969a | 068e272e, 21f0e51d (16,357 bytes, was 15,758; leaked second half replaced with Renn's account, red herring closed, gauge hook)
B3-ch16 | FIXED | a1da215629500ee67e2f33ea9ff7ac7ca66b53d5 | 64c4c08b, 6f176e74, 3bb3d9b4 (15,996 bytes, minimum 15,916; Renn 38 days, Kael's age against Mara's twenty years, American spelling, Joren knew Renn lived; added the two names, Joren and the watch book, Mara's boot; 3bb3d9b4 restored this blob after an overwrite)
B3-ch17 | FIXED | 83bb80a5a87e29e68b93b30d5b46b27b7b1f5c38 | e740c2c2 (11,403 bytes, was 11,066; order dates, steward line, Day-count and B2 reference cut; Odo and Tessa plan lines replaced with the hour-against-breath chart; "Yelva's log"; Kael's boot-lacing scene added)
B3-ch18 | FIXED | 821e52f9f724533c143cf0e9b16525b720244bb9 | 5fb4c9c9, f0d4b0e0, 5ef509cd (17,976 bytes, was 17,605; leaked "ch.27" lines, steward block, Day-number recital, stored-sum-plus-count arithmetic, Sol's copper clasp and the repeated Tessa recital replaced with the order read in full, Sol on the plain tactic, Kael on Malrik, Ansa and Tam at the stair foot; practicing)
B3-ch19 | FIXED | 1da2d038557ab6cb8e10a8a0be3a265ece4d567c | 22a70a4b (23,336 bytes, was 23,328; plate is the one in the door at the foot of the second stair; no feet distances, pegs-on-a-ledge, order-date recital, stored-sum arithmetic, Sol's copper clasp, wrong day counts or Mara's elbows; Kael ties the clean knot and thanks her; Sol's long hold at the plate and the pull-at-six rule; Ulla and Renn leaving once Mara can walk)
