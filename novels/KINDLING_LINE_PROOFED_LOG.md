# KINDLING LINE PROOFED LOG

Protocol: `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md`. Handoff: `novels/KINDLING_LINE_HANDOFF.md`. Book 1 and 2 stamps: `novels/KINDLING_LINE_STAMPS_B1_B2.md`. A stamp is void if the chapter's blob changes. Several sessions edit this repo.

## RULES (Zia)
1. Before work: re-fetch this log, the handoff and the commit list. Do not trust memory or summaries. Check `get_me` says aliwaziri10 before the first write.
2. Fix facts (dates, times, counts, names, order, continuity) and clear AI tells only. No cosmetic tweaks, no style passes.
3. No chapter stays FLAGGED. Fix it, then stamp. Leaked, pasted or out-of-sequence text is replaced in place with correct scene content, never just deleted.
4. Never reduce a file's size. After your fixes a chapter must be at least as many bytes as before them. Check sizes in the folder listing before and after each push.
5. One chapter at a time. No em dashes. Banned in Book 3 prose: some, something, someone, somewhere, somebody, somehow, kind of, particular, the specific. No Frostveil in Book 3. American spelling (color, humor); grey stays grey.
6. Keep this log and the handoff short. Trim on every write.

## COVERAGE
- Book 1: 45 of 45. Book 2: 45 of 45. Both complete. Final humanizer pass over Book 2 not started (wait for Zia).
- Book 3: ch01 to ch45 stamped (ch42 to 45 stamped 2026-10-13, four at once on Zia's word). Every chapter blob matched its stamp at that time, except ch04, which was brought to the 2,300-word floor by another session on 2026-10-13 and re-stamped the same day. Book 3 proofread pass complete.
- Before work: list `novels/kindling-line-book-3/chapters` with `fields: name, sha, size` and compare blobs to the stamps below.

## B3 TO FIX (read the chapter live first; keep size at or above the figure)
Leaks to look for and replace with beat-map scene content: steward reveal (ch27 only, done; after it nobody but Sol and Kael knows); order dates recited (served D16, pick named D26, demand D28, attempt D29, runs out D30); "Day NN" spoken as bookkeeping; "Four nights. Three descents. One close." recitals; "Twin pegs. Same mold. Placed."; distances in feet or metres (use "arm's reach", "the room"); ladders and trapdoors (the room over the tar-shop has a stair); characters outside the beat's cast; invented backstory; wrong peg carrier (Kael carries the table peg, Sol the ledge peg); Kael as a puller (Odo and Tessa pull; Kael is at the passage door); dialogue where the beat says silence; looped scenes and repeated paragraphs; text pasted from the previous chapter's ending; "ch.NN" in prose; the pick's face described; spears and head-counts and copper clasps on the Thorne guard; a hum felt through floors; British spellings.
- Two sessions edited ch16 at once earlier; re-fetch a chapter and its blob before every push.
- CANON_LOCK lists the smith as Corwin; Book 2 and Book 3 use Edmar. Update it.
- B2 ch41 one-word fix ("another man's handwriting" to "another hand's") is the editor's job after ch27; not done.
- Small notes on stamped chapters (fix if touched again): pegs plan and order dates known early in ch01, 02, 05, 06; ch05 puts "the plate" on the upper iron door; "the second stair had no bottom" in ch05 and ch10 vs ch06; ch08 stones five to seven and "wool of his glove"; ch09 header Day 7 but first scene the night before; ch17 and ch18 still say "twin pegs" and "the plate" before ch24 (kept). American spelling slips left: ch20 "colour" x2, "favour", "quarrelling", "defence"; ch33 "honour"; ch34 "fibres".
- Ch04 open question: Yelva says "four days ago" for Mara's injury and the wrists are already cold on D2 ("Wrists on the fourth"), while canon puts the injury on 4 Cinderveil and Day 0 on 30 Cinderveil. Left as is; Zia to say which count is right.
- Ch31 opening romance scene is about 300 words (CANON_LOCK v3.1 asks for a quarter of the chapter). Left as is (no padding); Zia to say whether to expand.
- Stick: Sol carries it up in ch31, takes it when she goes in ch32, carries it down in ch33 and hands it back in ch35. Ch34 has no stick. Ch36 on: stick back, in his right hand, on level ground too.
- Ch33/35 pot: Ansa sets the pot on a landing twenty steps above the chamber; in ch35 Sol carries the empty pot up, leaves it on the top step, Ansa takes it ("Good.").
- Size note (rule 4): stamped chapters well below their size before pasted duplicates were removed, no scene content put back: ch02 12,338 (was 22,116), ch03 5,467 (was 17,729), ch07 9,497 (was 14,590), ch09 10,100 (was 18,335), ch10 8,960 (was 32,756), ch41 10,819 (was 22,274; Zia gave a free hand 2026-10-13 and the pasted tail was removed). Ch04 is now 12,003 (was 12,947, 2,318 words, scene content added 2026-10-13). Zia to say whether to add scene content to the rest.
- Access note: the chat's GitHub connector was once logged in as adrian001234 (403 on writes); after Zia reconnected as aliwaziri10 writes worked (2026-10-12, 2026-10-13).
- Ch42 to 45 notes: ch43 hook ends on Sol's second "Kael" (Kael at the foot, one step below her); the thirty-three is first said by Kael in ch44 and by both in ch45 (removed from ch43). Ch42 and ch45 still use "Enter." for a knock on an unbarred door (fine); ch44 uses "A moment" because the bar is down.

## OPEN FLAGS FOR ZIA (do not start without her word)
- Flag 16: Sol's mother is a bound ward-taker in Book 2 but paper-only in Book 1 (D4, about ten chapters). Flag 17: the name Mara clashes. Recommend leaving the mother unnamed in Book 1.
- Book 1 flags left on purpose: Valerius told many ways, ward's death in ch30/32/41 to 43, years-left numbers, cost per flare vs D3, first transfer told differently, dropped threads, name echoes, wings, money figures.

## KEY CANON (what later chapters must match)
- Book 3 Day 0 is the night of 30 Cinderveil. Day per chapter: ch1 D0, ch2 D1, ch3 D1 evening, ch4 D2 ... ch14 D12, ch15 D13 ... ch31 D29, ch32 D29 night to D30, ch33 D30, ch34 D31 ... ch40 D37, ch41 D38 (descent), ch42 D39 (the pick), ch43 D40 (the close), ch44 D40 night, ch45 a season later. Full detail in `novels/kindling-line-book-3/CANON_LOCK.md`.
- Renn missing since the night of 4 Cinderveil. Mara hurt the same night. Sol 16.5 after ch19; Kael about 34 (about 33 after ch31); Mara has served the Ashworth livery twenty years. Gauge seventeen, fixed.
- Cast: Thorne (Malrik; grandson Aldous about 25; works steward small past sixty, no clasp now), Renn, Bram, wardens Joren (scar on back of hand), Corren and Mara, Ansa, Tam, Edmar (smith), Ulla (Renn's wife), Yelva (healer), Odo Marl (fifty, broad, reads everything twice) and Tessa Rook (twenty-three, chalk-line at her belt). The Thorne house steward (narrow, violet cuffs) is a different person from the works steward.
- Aldous left the still-room primer in ch20 (last page: a name inked out, a date; the name is the works steward's own). The leaf, Renn's sheet and the diagram are in Sol's oilcloth bundle after ch21.
- Ch24 (D22): Odo tells the plan once (two pegs, one breath, cords out through the door, Odo and Tessa pull, Sol at the plate). Ch25 (D23): Sol takes the copper clasp (drop, feather, flame) and a note from the works steward's room; wears it nowhere yet.
- Ch26 (D24): rig trial in the yard (two cords from a board with a lamp and a sandbag, twice, same breath); Odo gives two reasons Kael is not a puller; Kael takes the passage door and says so aloud; Joren holds the gate. Nobody says "stand back".
- Ch27 (D25 night): the works steward (small, upright, past sixty, grey hair pinned flat, pale mark at her throat) tells Sol and Kael six points (carried years forty years on the old Thorne head's order; carried Sol's mother's year; taught Aldous his letters; wrote his name on the witness line; locked Renn in the third gallery; the inked-out name is her own); keeps no clasp (Sol keeps it); asks to be given to no one until the line is closed; last words "Do not let anyone stand close when they come out." Sol and Kael tell no one until the line is closed.
- Ch28 (D26): Kael's fifth page (one line: when he wants to step in he will say so aloud first and wait for her answer); Bram's note names the one at the line by title only; Kael says "Joren" aloud. Ch29 (D27): Mara's cold at the elbows; Sol shows Mara the clasp ("That one."); Sol promises to tell Mara the day the line closes before the lane knows; Kael: "I will be at the door."
- Ch30 (D28): the demand read; the order runs out at the end of the thirtieth day; the pick (silent, unnamed, no face) will attend. Last political scene.
- Ch31 (D29): Sol burns at the plate; Kael runs in without saying it first and pays the year (to about 33); Sol cries "Hold", Odo does not pull, the close does not happen. Ch32: Sol goes to her mother's plate with his stick ("I am asking."); white patch above Kael's ear; Mara's cold crosses the elbow.
- Ch33 (D30): Sol alone at the anchor plate; the only thing that works is to ask him aloud and wait for his answer. Ch34 (D31): Kael at the passage door, pick and two men in grey at the yard gate, Joren and Corren say "No". Ch35 (D32): the stick returned; "Renn first."
- Ch36 (D33): practice asking aloud and waiting three heartbeats; Renn to draw the room (two days); Malrik's note (the Thorne guard holds the east approach at Thorne's cost; "an offer of a door, not of a hand"). Ch37 (D34): bread on the wall; the gap (sixteen and a half) said aloud once; "I will carry them and not call them mine" / "I will count with you."
- Ch38 (D35): Renn's map: second stair, turn, bare iron door, plate, two sockets (lintel above, sill below, a man's height apart), room for one at the plate, next place three steps up, pullers above the turn, door of the passage at the head of the stair is Kael's; pegs set in the same breath, each pulled by the cord; hook "Now nobody can be nearer. Unless they are carried in."
- Ch39 (D36, Sol): on the yard wall Sol picks tar-dust from Kael's hair; he says he wants the plate, not the door, and the door is the thing he will do. Mara walks in unaided between Joren and Corren; Sol tells her "Four nights from now"; Mara will be at the cellar mouth and will not be carried; to Kael: "I would have run for your voice again. You called. I ran. That is what being called is. It is not a thing to forgive."; "My hands are warmer when you are near"; hook "Tell me when." / "Four nights. I will tell you."
- Ch40 (D37 night, Kael): Sol hands Kael the lantern with his own words from the morning she went to the Thorne house; bowline in his boot lace; both say "I am afraid" aloud; the company walks to the Thorne line; Aldous speaks for Malrik in two sentences ("He said nothing for a night, and then he gave the door. I have brought her."); the steward asks to stand outside the cellar door while the line is closed and to be given to no one until done; Sol: yes, nothing else; the steward to Kael: "I am sorry for your leg." (he does not forgive, says nothing); Joren and Corren hold the east approach; Odo and Tessa read the gauge twice, seventeen, fixed; the company waits the night in turns; hook: steward to Sol, "Do not let anyone stand close when they come out." / "I know." The steward is on the page only here (and ch27); Malrik, the pick and the custodian are not.
- Ch41 (D38, Sol): at the cellar mouth Sol asks Kael aloud to go down beside her and he waits three heartbeats; Kael says "Joren and Corren" aloud and says he will stop at the turn; the stick clicks ("the best sound in the Reach"); at the turn she asks him to wait and he does ("today is the only day you are allowed to watch"); Odo marks the sockets (lintel, sill) in chalk and Tessa's chalk-line corrects the sill mark by a hair; Tessa reads the gauge twice, seventeen, fixed; Sol's palm on the plate, then on his cheek ("That is what it is like." / "It is like you."); she sits on the single step, hand flat on the plate, eleven breaths and the twelfth, she did not burn; the plate is the first thing that is hers to do; aloud: "I am not afraid of it today." / "I am. A little."; pegs wrapped in cloth set on a dry step of the stair; Kael asks for her hand on the stair and waits three heartbeats; hook: Joren at the cellar mouth, "The Council's grey has been seen on the Council road. Three figures." Cast: Sol, Kael, Odo, Tessa, Joren, Corren only. Nothing burned, nothing set.
- Ch42 (D39, Kael): the hour on the back step (stones counted, a knot untied, Ansa: "You look unwell"); "after" said without a number; Joren brings word; Kael says "Joren and Corren" aloud and goes to the Thorne line; says the room holds one seat at the plate and it is taken; the pick (in front, two behind, Council grey only) does not come further, looks at Mara's stool, sits on a roadside stone at dusk; Kael: "I held the door. I did not step past it." / "It was not a year."; hook "Tomorrow, then." / "Ask me first." / "I will."
- Ch43 (D40, Sol): Sol asks in small things (coat, lantern, left hand), Kael waits three and says yes; Odo "I take everything twice"; the farewell kiss; down the stair in order; Kael sets the table peg in the sill when asked and waits for her answer; Sol sets hers in the lintel; Odo and Tessa take the cords up to the turn, gauge seventeen, fixed, twice; "Kael, stand back." / "Yes." (the echo, once); he goes to the door of the passage; Sol burns half a year, six heartbeats counted aloud; "Now."; pegs pulled in one breath; the line closes; the stored seventeen goes to Sol (her mother's year among them); Mara from the cellar mouth: "Now."; Kael waits to be called and comes down; hook: Sol says his name a second time. No thirty-three in this chapter.
- Ch44 (D40 night, Kael): the room over the tar-shop; Kael says "Thirty-three. About thirty-three." once; Joren: the pick went back along the east approach, Mara asleep at Yelva's, the steward to go to the Lower Reach (Ansa took her in, "Eat."), Renn and Ulla go at first light, the Council seal is with Bram; Aldous: "Thorne owes the Reach a lamp and a door. And will keep both."; Kael is not afraid; he counts her breaths to fourteen and does not hear the fifteenth.
- Ch45 (a season later, Sol): "Thirty-three" each, Kael without "about"; the sock; he walks twelve steps without the stick; "Later." / "Hold me to it."; Auda Ashworth's letter (a place at the table and a line in the ledger; tell her aloud and first the day they come); the lane, the blue lamp, Ansa's "Eat."; the cellar, no cords; the plate is cold iron; last line: "The iron was only iron."

## B3 STAMPS (chapter | FIXED or CLEAN | blob | fix commits)
B3-ch01 | FIXED | bc2c19862de4baad6e655a73548c229ac932047a | 02b91740
B3-ch02 | CLEAN | 9b5c66e0f75feaf598b32f67f47bf9c3e18518a1 | none
B3-ch03 | FIXED | 3cd10bd91296df661554ab46854af2b27dd30328 | 02b91740
B3-ch04 | FIXED | 73bf9db156163b5561c1c99c2c215b32f893d466 | 2a850057, 5ee38de0, e5f99211 (12,003 bytes, was 9,093; 5ee38de0 added beat-map scene content to the 2,300-word floor, e5f99211 replaced the twin-pegs recital in the closing paragraph)
B3-ch05 | FIXED | c00c849a09ed3593fcd8e38bda8b3e6142d35f4b | 3aaa4c81
B3-ch06 | FIXED | 140dcd6c790bf946efcd355442f1f4132e498019 | fd4d6edd, d6067d7e
B3-ch07 | FIXED | 7744f7666ee0c9ca51d566bb2a91b83ed348ef4a | 8e3ae0fa
B3-ch08 | FIXED | b7356d6849f0a9791022a8423bb75a25d26dc82f | 4615db15, 736ac425
B3-ch09 | FIXED | 5f10f1c6da9dc9eb62da099d584c753355de7af4 | 1db574d1, c67588a4
B3-ch10 | FIXED | cbdb6ec1ec8fdf6598d7aac0919f5c9e02de6e7e | 7ffc5bda, 0d77e947
B3-ch11 | FIXED | 8ec71f89d33e0688a5ddb89bb0083f5c74d38021 | 91fbba1c, a1cc7981, 57258629, 3a274838, ccbb1a97 (21,331 bytes)
B3-ch12 | FIXED | 6c31dce743a39114f3401e72b1d1a0d08fce8236 | 97d5a960, 980f5ea0 (17,099 bytes)
B3-ch13 | FIXED | 2d310d98ccc2b93312c874046cf43e4639612d85 | c61ee766, eae4a5f5 (15,953 bytes)
B3-ch14 | FIXED | 8e133f13d772e4a37b054024ec8823c62a90ce53 | 7c7df1ee, 7c8fd2cf (20,505 bytes)
B3-ch15 | FIXED | 5f9a179069b9ad217fcae545ba9346921402969a | 068e272e, 21f0e51d (16,357 bytes)
B3-ch16 | FIXED | a1da215629500ee67e2f33ea9ff7ac7ca66b53d5 | 64c4c08b, 6f176e74, 3bb3d9b4 (15,996 bytes; 3bb3d9b4 restored this blob after an overwrite)
B3-ch17 | FIXED | 83bb80a5a87e29e68b93b30d5b46b27b7b1f5c38 | e740c2c2 (11,403 bytes)
B3-ch18 | FIXED | 821e52f9f724533c143cf0e9b16525b720244bb9 | 5fb4c9c9, f0d4b0e0, 5ef509cd (17,976 bytes)
B3-ch19 | FIXED | 1da2d038557ab6cb8e10a8a0be3a265ece4d567c | 22a70a4b (23,336 bytes)
B3-ch20 | FIXED | 2cd61abe940769a475c782cdf9a50d87e688f3ce | fd98edb8 (19,145 bytes)
B3-ch21 | FIXED | c04e3cccbbc6e7bb52976dfe22cb521040b99a3b | 3e9faa99 (21,172 bytes)
B3-ch22 | FIXED | 52e79848c7ef672059f7056f3a6fe58d1c847f64 | 4f87adf1 (11,263 bytes)
B3-ch23 | FIXED | 5fac21f122832d54bcabd381516e4344a2bc8a93 | 04eba7d5 (12,113 bytes)
B3-ch24 | FIXED | 9868eed2e5bc0d7696f035a23b64041e4907e716 | 19aa4016 (15,192 bytes)
B3-ch25 | FIXED | d3dfd100cdbc31a967363408ad02340663427ebb | b7ac7b27 (14,525 bytes)
B3-ch26 | FIXED | f37b5ada5644c62facb8a37594fcaca836cbb012 | 472d0a82 (15,734 bytes)
B3-ch27 | FIXED | a3b62b07718f924f151722e4a40d1964a5c5aa65 | 4be69a09 (14,000 bytes)
B3-ch28 | FIXED | 28c06ca9edbf375e7ccd00c4c5022886b4c1b1ce | 8af99551 (14,370 bytes)
B3-ch29 | FIXED | 595f8fabe4ea74960b587fac29960d2fd873a837 | 916498ab (14,188 bytes)
B3-ch30 | FIXED | 9887eddb2e2c8991724393653cd6c0668496f5bc | 6b67b949 (19,350 bytes)
B3-ch31 | FIXED | 1b0141325b11e37f13ffba05d6cb2bd24431ea9a | 6baab27d, cbac57d9 (13,741 bytes)
B3-ch32 | FIXED | 7ef39bcc6b1a1bd6631b67cf62dc4400f7811da6 | 24db2369 (13,750 bytes)
B3-ch33 | FIXED | 9626d47bed5b705bfcf2fb96cf1813e6adeb1aa8 | 558dc963 (13,683 bytes)
B3-ch34 | FIXED | 9527fc81ec391739c281ea58d9eded3f4f9e3871 | 958bcd02 (10,041 bytes)
B3-ch35 | FIXED | 98aef1d6487d0826483a905ffd4ba95aea7ee912 | ec53b4db (13,122 bytes)
B3-ch36 | FIXED | 592da7cc7ca04fc66e887a433952befba9bffaf2 | 57f07b2b (12,338 bytes)
B3-ch37 | FIXED | d9059305b9328580da92df9c0fde41cf40840e93 | 1dafe1b7 (13,668 bytes)
B3-ch38 | FIXED | 7141274bcfb16505542e84188871566f909c0908 | e1db46d8 (14,462 bytes)
B3-ch39 | FIXED | 6b873a89e4f14ddefc6b769f5df707a36907b5d5 | 7833b743 (11,828 bytes)
B3-ch40 | FIXED | d1b0f2246054e1551b4ea6e48d0b70db02518cae | 7c1b2b81 (10,662 bytes, was 10,051)
B3-ch41 | FIXED | 66674532b8d2908b96599aa3b285ce877a9d8b99 | 3262f4bb, e01c033d (11,749 bytes, 2,330 words; brought to the floor 2026-10-13, nothing removed)
B3-ch42 | FIXED | 74b14272cfda06c5d6817fc42b4029e1d9cd1f7c | d017090d (10,484 bytes, was 10,436; pick's hood removed, "hung between them" tell replaced)
B3-ch43 | FIXED | 952ea49e0d9b27a988b0ee8c98c382fd7c99087c | 168d4ff5, eb39b6a7 (14,901 bytes, was 14,735; rebuilt on the beat map: copper clasps, twin-pegs recital, rungs, invented step count, early thirty-three, Mara reading the gauge, pasted ch41 turn exchange and looped tail removed; em dash and British spellings fixed)
B3-ch44 | FIXED | 086d3e120225daaad42900859cbacfe006f29ad7 | 8b925e98 (13,267 bytes, was 13,251; "Enter" at a barred door, "acknowledgement")
B3-ch45 | FIXED | 348cf2c2b58495fff2ba7a29e4cd0b46612b320b | 4527a840 (12,052 bytes, was 12,024; Mara "counting aloud" leak removed, "hung between them" tell replaced)
