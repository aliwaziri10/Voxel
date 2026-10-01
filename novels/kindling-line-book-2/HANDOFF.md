# HANDOFF - Kindling Line Book 2

**CLAIM: full re-verification pass ch.01-45 in progress (claude.ai session, 2026-10-01, Zia's permission given). Do not start a second pass.**

**Rules (Zia):**
1. Do not trust this file. Check the live repo (the chapter, the latest commits) before acting.
2. No profile works without Zia's permission in the current conversation.
3. Only job: run the 7 checks on a chapter, fix only what they find, and tick it below in the same commit, with the commit SHA.
4. Skip a chapter only if it is ticked below and no later commit touched the file.
5. STOP EXPANDING. Never add words for a count. Word count is not enforced.
6. Keep this file short. Trim before you add. Do not write notes, history or canon essays here.
7. Workflow (Zia): do five chapters, then update this file, then keep going without waiting. A chapter with no finding gets no commit of its own; tick it clean in that update.
8. **FACTS ARE ALWAYS FIXED, STYLE IS LEFT ALONE (Zia, firm).**
   - (a) FACTS, always fix, even if an ordinary reader would not notice: any date, time of day, count, age, years of service, name, order or seal detail that contradicts another chapter, the same chapter, or the canon below. Check the other chapters (grep them) and fix the wrong one. Never log a contradiction as "noted, left alone". Also always fix: banned terms and names, hedge words, em-dashes, spelling.
   - (b) AI TELLS from check 7: fix every clear or repeated one. One ordinary rhetorical question, simile or chapter ending is not a tell.
   - (c) STYLE (rhythm, endings, wording taste, "could be better"): leave alone. The "would an ordinary reader notice" test applies to style only, never to facts.
   - Change the fewest words that fix the problem. If a chapter has no (a) or (b) finding, do not touch it; tick it clean. No poking.

**The 7 checks** (a real read, not only a grep):
1. Banned terms and names
2. Hedge words, case-insensitive: particular, something, someone, somewhere, somebody, some (so "somehow" also hits), kind of, the specific
3. Em-dashes: zero
4. Date, time and count math, including ages and years, checked against the other chapters
5. Invented mechanisms
6. Restaged firsts
7. AI tells: rule-of-three cadence, throat-clearing openers, a closing line that explains the takeaway, stacked hedging in dialogue, a simile that explains a feeling

**Reference:**
- Banned terms: Contract of Perpetual Surety, Deep Vault, Keeper of the Burning Ledger as an office, Accord Hall, Great Hall, Grand Auditor, Nine Houses, inquiry board, Tripartite Seal, Founding Council, invented article or section numbers, Consultant. Site is Anchor Seven only. Never "the Compact" or "the annex" (use "the ward trade", "the second head"). Spell grey, not gray. A vote count must not read "nine houses" (write "nine of the twelve houses").
- Banned names: Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor, Varrick, Helseth, Dallin Vorys, a living or clerk Valerius (Valerius Ashworth is Kael's dead father, fine). Grep with word boundaries: "Hest" matches "chest".
- Dates: Sunspire is 30 days. Ch.N is day (N+8) of Sunspire through ch.22. From ch.23, ch.N is day (N-22) of Cinderveil. A chapter that spans days carries the chapter_date of the day it ends on (ch.29, 30, 40). Ch.41-44 are the 28th and 29th; ch.45 is the 30th.
- Seal and clasp figures, in order of the three strands: drop, feather, flame. The third strand is the flame.
- Firsts: "I love you" and the first kiss are staged in ch.28. Any earlier use or later restaging is a bug. "Later" was said twice (ch.29, 31); do not pay it off before the book decides. Avoid the stock phrase "a moment longer than X needed".
- Canon, only what later chapters need:
  - Sol is "Lady Vane". Holders, not "men". Eight signatures bring the petition to a vote; nine of twelve houses set the Deed aside; its thirty days run to 28 Cinderveil.
  - Counts: 252 signed the standard (251 until Tam signed on 10 Cinderveil). The slate's "hold" column FALLS as holders withdraw: 288 on the 15th, 286 on the 16th and 25th, 282 on the 26th.
  - Ansa spliced for forty years (ch.12). Tam is Ansa's nephew (her sister's son); his mother is alive. The slate boy is "Ansa's boy", her son, so he is Tam's COUSIN. Never "uncle".
  - Renn missing since the night of 4 Cinderveil. Joren's rule is said aloud to Corren and Joren by name every time. Mara hurt 4 Cinderveil, not waking. Kael's left leg is numb.
  - On 6 Cinderveil Kael and Sol go below the forge in the morning and come up at first grey on the 7th.
  - The family account Ferra asks for on the 28th is due and taken at first bell on the 30th.
  - Co-lead: Sol says yes after the reading on 28 Cinderveil; the petition is heard on the 30th (ch.45).
  - The public sitting is on 28 Cinderveil. Say "the last week", never "the third week".
  - Vote on 28 Cinderveil, voices to set the Deed aside in order: Ashworth, the sixth-chair lord, Vane, Lenmoor, Pryce, Corvane, Farrow, Dellyn, Tavarel = nine. Estler absent, Thorne last. Which of Dellyn and Tavarel signed is not stated; do not state it. Farrow's letter postscript: "Ask the boy who taught him his letters."
- OPEN, Zia to decide (a book decision, not a fact error): ch.44's closing sill scene pays off an intimate night against the "later" rule.

**Ticked (all 7 checks, live-read):**
01 `17c9ba1e`, `22eb16b3` | 02 `24367622` | 03 `9dfb1db1` | 04 `7fc007ab` | 05 clean, no SHA recorded | 06 `28d0468f` | 07 `7ca17064` | 08 `fe3ce400`, `35f3b754` | 09 `ab532554` | 10 `e1cce6d3` | 11 `2f3dc3be` + commit titled `ch.11-13 fix-only` | 12 commits titled `ch.11-13 fix-only`, `ch.12 fix-only`, `ch.12 ward-trade wording` | 13 commit titled `ch.11-13 fix-only` | 14, 15, 16 commit titled `ch.14-16 fix-only` | 17 `a3b4bc34` | 18 `2ec82805` | 19 `6fbb4752` | 20 `161372d5` | 21 `eddcfb2c` | 22 commit titled `ch.22 fix-only` | 23, 24 commit titled `ch.23-25 fix-only` | 25 commit titled `ch.23-25 fix-only`, plus "third week" to "last week" in `9c887cb2` | 26, 27, 28 commit titled `ch.26-28 fix-only` | 29, 30, 31 commit titled `ch.29-31 fix-only` | 32 `940214c6` | 33 fix-only, no SHA recorded | 34 clean, no SHA recorded | 35 `a57d3bc6` (clean) | 36 `6b3c73d1` | 37 `28b54bab`, then Tam "uncle" to "cousin" in `b06117e1` | 38 `5cd4c8dc` | 39 `c68ae885` | 40 `b06117e1` | 41 `9c887cb2` | 42 `57c086c9` | 43 `4c99c0bd` | 44 `ea6a9d70`, `b7c67e1d` | 45 `b7c67e1d`

**Round 3 (Zia), ch.01-30 done:** 07 `1aa01158`; 10 `e38cec34`; 11, 13, 14 commit titled `ch.11-14 round-3 fix-only`; 16, 20 commit titled `ch.16-20 round-3 fix-only` (seal order in both; ch.20 also "third week" to "last week"); 22 `23988aa0` (Ansa "fifty years" to "forty"); 26 `41f76b2f` ("third week" to "last week" twice, seal order); 28 `9cdd660a` (stock phrase); 30 `aba8f167` (time below the forge: "from the morning of the sixth", "a day and a night"); 08, 09, 12, 15, 17, 18, 19, 21, 23, 24, 25, 27, 29 read clean, no edit.
Fixed under the new rule 8 outside the 01-30 range: 40 `02e9d234` (chapter_date 18 to 28 Cinderveil); 43 `e2d2eb10` (account due "by the first bell of the thirtieth").

**Next:** round 3 continues at ch.31, under the new rule 8.
