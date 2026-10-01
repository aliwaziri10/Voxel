# HANDOFF - Kindling Line Book 2

**CLAIM: full re-verification pass ch.01-45 in progress (claude.ai session, 2026-10-01, Zia's permission given). Do not start a second pass.**

**Rules (Zia):**
1. Do not trust this file. Check the live repo (the chapter, the latest commits) before acting.
2. No profile works without Zia's permission in the current conversation.
3. Only job: run the 7 checks on a chapter, fix only what they find, and tick it below in the same commit, with the commit SHA.
4. Skip a chapter only if it is ticked below and no later commit touched the file.
5. STOP EXPANDING. Never add words for a count. Word count is not enforced.
6. Keep this file short. Trim before you add. Do not write notes, history or canon essays here.
7. Workflow (Zia): do five chapters, then update this file, then keep going without waiting.
8. **NO UNNECESSARY CHANGES (Zia, firm).** The writer has a style. Leave it alone. Change a line ONLY for: (a) an obvious AI tell from check 7 (clear, or repeated; not one ordinary rhetorical question, simile or chapter ending), (b) a lexical error (banned term or name, hedge word, em-dash, spelling), or (c) a continuity, date or count problem that contradicts another chapter or the canon below. Rhythm, endings, wording taste and "could be better" are NOT findings. Test: would an ordinary reader notice it or be misled? If not, leave it. If in doubt, leave it. If a chapter has none of (a) to (c), do not touch the file; tick it clean. No poking.

**The 7 checks** (a real read, not only a grep):
1. Banned terms and names
2. Hedge words, case-insensitive: particular, something, someone, somewhere, somebody, some (so "somehow" also hits), kind of, the specific
3. Em-dashes: zero
4. Date and count math
5. Invented mechanisms
6. Restaged firsts
7. AI tells: rule-of-three cadence, throat-clearing openers, a closing line that explains the takeaway, stacked hedging in dialogue, a simile that explains a feeling

**Reference:**
- Banned terms: Contract of Perpetual Surety, Deep Vault, Keeper of the Burning Ledger as an office, Accord Hall, Great Hall, Grand Auditor, Nine Houses, inquiry board, Tripartite Seal, Founding Council, invented article or section numbers, Consultant. Site is Anchor Seven only. Never "the Compact" or "the annex" (use "the ward trade", "the second head"). Spell grey, not gray. A vote count must not read "nine houses" (write "nine of the twelve houses").
- Banned names: Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor, Varrick, Helseth, Dallin Vorys, a living or clerk Valerius (Valerius Ashworth is Kael's dead father, fine). Grep with word boundaries: "Hest" matches "chest".
- Dates: Sunspire is 30 days. Ch.N is day (N+8) of Sunspire through ch.22. From ch.23, ch.N is day (N-22) of Cinderveil. Ch.29 and 30 open on the 6th and 7th but carry the chapter_date of the day they end on. Ch.41-44 are the 28th and 29th; ch.45 is the 30th.
- Seal and clasp figures, in order of the three strands: drop, feather, flame. The third strand is the flame.
- Firsts: "I love you" and the first kiss are staged in ch.28. Any earlier use or later restaging is a bug. "Later" was said twice (ch.29, 31); do not pay it off before the book decides. Avoid the stock phrase "a moment longer than X needed".
- Canon, only what later chapters need:
  - Sol is "Lady Vane". Holders, not "men". Eight signatures bring the petition to a vote; nine of twelve houses set the Deed aside; its thirty days run to 28 Cinderveil.
  - Counts: 252 signed the standard (251 until Tam signed on 10 Cinderveil). The slate's "hold" column FALLS as holders withdraw: 288 on the 15th, 286 on the 16th and 25th, 282 on the 26th.
  - Tam is Ansa's nephew (her sister's son); his mother is alive. The slate boy is "Ansa's boy", her son, so he is Tam's COUSIN. Never "uncle".
  - Renn missing since the night of 4 Cinderveil. Joren's rule is said aloud to Corren and Joren by name every time. Mara hurt 4 Cinderveil, not waking. Kael's left leg is numb.
  - Co-lead: Sol says yes after the reading on 28 Cinderveil; the petition is heard on the 30th (ch.45).
  - The public sitting is on 28 Cinderveil. Say "the last week", never "the third week".
  - Vote on 28 Cinderveil, voices to set the Deed aside in order: Ashworth, the sixth-chair lord, Vane, Lenmoor, Pryce, Corvane, Farrow, Dellyn, Tavarel = nine. Estler absent, Thorne last. Which of Dellyn and Tavarel signed is not stated; do not state it. Farrow's letter postscript: "Ask the boy who taught him his letters."
- OPEN: ch.20 and ch.26 still say "the third week" of Cinderveil. Change to "the last week".
- OPEN, Zia to decide: ch.40 chapter_date says 18 Cinderveil but the text runs to the 28th. Ch.43 says the family account is due the 29th, ch.44-45 say the 30th. Ch.44's closing sill scene pays off an intimate night against the "later" rule.
- OPEN, ch.45 unverified: "the second line below the boiling house" and the Chancellor's "forty years ago" are not set up in a chapter I read.

**Ticked (all 7 checks, live-read):**
01 `17c9ba1e`, `22eb16b3` | 02 `24367622` | 03 `9dfb1db1` | 04 `7fc007ab` | 05 clean, no SHA recorded | 06 `28d0468f` | 07 `7ca17064` | 08 `fe3ce400`, `35f3b754` | 09 `ab532554` | 10 `e1cce6d3` | 11 `2f3dc3be` + commit titled `ch.11-13 fix-only` | 12 commits titled `ch.11-13 fix-only`, `ch.12 fix-only`, `ch.12 ward-trade wording` | 13 commit titled `ch.11-13 fix-only` | 14, 15, 16 commit titled `ch.14-16 fix-only` | 17 `a3b4bc34` | 18 `2ec82805` | 19 `6fbb4752` | 20 `161372d5` | 21 `eddcfb2c` | 22 commit titled `ch.22 fix-only` | 23, 24 commit titled `ch.23-25 fix-only` | 25 commit titled `ch.23-25 fix-only`, plus "third week" to "last week" in `9c887cb2` | 26, 27, 28 commit titled `ch.26-28 fix-only` | 29, 30, 31 commit titled `ch.29-31 fix-only` | 32 `940214c6` | 33 fix-only, no SHA recorded | 34 clean, no SHA recorded | 35 `a57d3bc6` (clean) | 36 `6b3c73d1` | 37 `28b54bab`, then Tam "uncle" to "cousin" in `b06117e1` | 38 `5cd4c8dc` | 39 `c68ae885` | 40 `b06117e1` | 41 `9c887cb2` | 42 `57c086c9` | 43 `4c99c0bd` | 44 `ea6a9d70`, `b7c67e1d` | 45 `b7c67e1d`

**Round 3 (Zia, light touch), ch.01-15 done:** 07 `1aa01158`; 10 `e38cec34`; 11, 13, 14 commit titled `ch.11-14 round-3 fix-only`; 08, 09, 12, 15 read clean, no edit.

**Next:** round 3 continues at ch.16. Remaining: the OPEN items above.
