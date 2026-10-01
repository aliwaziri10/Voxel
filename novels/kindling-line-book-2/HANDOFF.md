# HANDOFF - Kindling Line Book 2

**Rules (Zia):**
1. Do not trust this file. Check the live repo (the chapter, the latest commits) before acting.
2. No profile works without Zia's permission in the current conversation.
3. Only job: run the 7 checks on a chapter, fix only what they find, and tick it below in the same commit, with the commit SHA.
4. Skip a chapter only if it is ticked below and no later commit touched the file.
5. STOP EXPANDING. Never add words for a count. Word count is not enforced.
6. Keep this file short. Trim before you add. Do not write notes, history or canon essays here.
7. Workflow (Zia): do three chapters, then update this file, then keep going without waiting. After that, one chapter at a time, updating this file each time.

**The 7 checks** (a real read, not only a grep):
1. Banned terms and names
2. Hedge words, case-insensitive: particular, something, someone, somewhere, somebody, some (so "somehow" also hits), kind of, the specific
3. Em-dashes: zero
4. Date and count math
5. Invented mechanisms
6. Restaged firsts
7. AI tells: rule-of-three cadence, throat-clearing openers, a closing line that explains the takeaway, stacked hedging in dialogue, a simile that explains a feeling

**Reference:**
- Banned terms: Contract of Perpetual Surety, Deep Vault, Keeper of the Burning Ledger as an office, Accord Hall, Great Hall, Grand Auditor, Nine Houses, inquiry board, Tripartite Seal, Founding Council, invented article or section numbers, Consultant. Site is Anchor Seven only. Never "the Compact" or "the annex" (use "the ward trade", "the second head"). Spell grey, not gray.
- Banned names: Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor, Varrick, Helseth, Dallin Vorys, a living or clerk Valerius (Valerius Ashworth is Kael's dead father, fine). Grep with word boundaries: "Hest" matches "chest".
- Dates: Sunspire is 30 days. Ch.N is day (N+8) of Sunspire through ch.22. From ch.23, ch.N is day (N-22) of Cinderveil. Ch.29 and 30 open on the 6th and 7th but carry the chapter_date of the day they end on.
- Firsts: "I love you" and the first kiss are staged in ch.28. Any earlier use or later restaging is a bug. "Later" was said twice (ch.29, 31); do not pay it off before the book decides. Avoid the stock phrase "a moment longer than X needed".
- Canon, only what later chapters need:
  - Sol is "Lady Vane". Holders, not "men". Eight signatures bring the petition to a vote; nine of twelve houses set the Deed aside; its thirty days run to 28 Cinderveil.
  - Counts: 252 signed the standard (251 until Tam signed on 10 Cinderveil). The slate's "hold" column counts held holders and FALLS as holders sign the withdrawal paper: 288 on the 15th, 286 on the 16th and 25th, 282 on the 26th.
  - Tam is Ansa's nephew (her sister's son). His mother is alive (a bearer six years under the old trade, now at home) and he has a sister at home. The slate boy is "Ansa's boy", her son, so he is Tam's COUSIN. Never "uncle", never say Tam's mother is dead.
  - Renn missing since the night of 4 Cinderveil; Sol holds his brass peg. The second peg was placed, not found; Dessa chairs the surveyors' commission. Cellar water rose, then fell a hand's width by the 14th. Joren's rule is said aloud to Corren and Joren by name every time. Mara hurt 4 Cinderveil, cold at the wrists, not waking. Kael's left leg is numb.
  - Co-lead: Sol says yes, timed by her, after the reading on 28 Cinderveil. Kael drafts nothing until she says. Corwin cast the Thorne die eight years ago (ch.39, 40).
  - The public sitting is on 28 Cinderveil (ch.40, 41). Say "the last week", never "the third week".
  - Houses: eight signed the petition (Thorne, Estler, Farrow, Lenmoor, Pryce, Corvane, Dellyn, Tavarel); four never did (Ashworth, Vane, and two unnamed seats). In ch.42 four voices are lodged to set the Deed aside (Ashworth, a non-signer, Vane, Lenmoor); nine are needed.
- OPEN: ch.20 and ch.26 still say the public sitting is in "the third week" of Cinderveil. Change to "the last week" when you reach them (ch.25 is fixed).
- OPEN, check ch.43-45: any mention of "291" or another hold count after the 26th must read 282; houses and the vote count must match ch.42.
- OPEN, ch.40: the fisherman's sighting of Renn on a skiff heading south is a lead no later chapter picks up (ch.45 does not). Decide at ch.45 whether to leave it.

**Ticked (all 7 checks, live-read):**
01 `17c9ba1e`, `22eb16b3` | 02 `24367622` | 03 `9dfb1db1` | 04 `7fc007ab` | 05 clean, no SHA recorded | 06 `28d0468f` | 07 `7ca17064` | 08 `fe3ce400`, `35f3b754` | 09 `ab532554` | 10 `e1cce6d3` | 11 `2f3dc3be` + commit titled `ch.11-13 fix-only` | 12 commits titled `ch.11-13 fix-only`, `ch.12 fix-only`, `ch.12 ward-trade wording` | 13 commit titled `ch.11-13 fix-only` | 14, 15, 16 commit titled `ch.14-16 fix-only` | 17 `a3b4bc34` | 18 `2ec82805` | 19 `6fbb4752` | 20 `161372d5` | 21 `eddcfb2c` | 22 commit titled `ch.22 fix-only` | 23, 24 commit titled `ch.23-25 fix-only` | 25 commit titled `ch.23-25 fix-only`, plus "third week" to "last week" in `9c887cb2` | 26, 27, 28 commit titled `ch.26-28 fix-only` | 29, 30, 31 commit titled `ch.29-31 fix-only` | 32 `940214c6` | 33 fix-only, no SHA recorded | 34 clean, no SHA recorded | 35 `a57d3bc6` (clean) | 36 `6b3c73d1` | 37 `28b54bab`, then Tam "uncle" to "cousin" in `b06117e1` | 38 `5cd4c8dc` | 39 `c68ae885` | 40 `b06117e1` | 41 `9c887cb2` | 42 commit titled `ch.42 fix-only`

**Next: ch.43.** Ch.43 to 45 are unticked. To tick one, add it to the Ticked line with its commit.
