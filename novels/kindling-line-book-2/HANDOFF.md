# HANDOFF - Kindling Line Book 2

**Rules (Zia):**
1. Do not trust this file. Check the live repo (the chapter, the latest commits) before acting.
2. No profile works without Zia's permission in the current conversation.
3. Only job: run the 7 checks on a chapter, fix only what they find, and record the chapter as ticked in the same commit.
4. Skip a chapter only if it is ticked below and no later commit touched the file.
5. STOP EXPANDING. Never add words for a count. Word count is not enforced.
6. Every profile that edits this file must trim it. Keep only what the next profile needs.
7. Workflow (Zia): do three chapters, then update this file, then keep going without waiting. After that, one chapter at a time.

**The 7 checks** (a real read, not only a grep):
1. Banned terms and names
2. Hedge words, case-insensitive: particular, something, someone, somewhere, somebody, some, kind of, the specific
3. Em-dashes: zero
4. Date and count math
5. Invented mechanisms
6. Restaged firsts
7. AI tells: rule-of-three cadence, throat-clearing openers, a closing line that explains the takeaway, stacked hedging in dialogue

**Reference:**
- Banned terms: Contract of Perpetual Surety, Deep Vault, Keeper of the Burning Ledger as an office, Accord Hall, Great Hall, Grand Auditor, Nine Houses, inquiry board, Tripartite Seal, Founding Council, invented article or section numbers, Consultant. Site is Anchor Seven only. A case-insensitive grep also hits "nine houses" used as a vote count; reword it.
- Banned names: Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor, Varrick, Helseth, Dallin Vorys, a living or clerk Valerius (Valerius Ashworth is Kael's dead father in Book 2, fine). Grep with word boundaries: "Hest" matches "chest".
- Dates: Sunspire is 30 days. Ch.N is day (N+8) of Sunspire through ch.22. From ch.23, ch.N is day (N-22) of Cinderveil.
- Firsts: "I love you" and the first kiss happen in ch.28, never earlier, never restaged.
- Canon (checked against Book 1 manuscript): the old system is "the ward trade" (Book 1 has no "Compact"; Book 2 ch.01, 05, 06 use "former Compact" in passing). Book 1 uses lowercase "ward contract" only, so no capitalised bare "the Contract". The Vault tap ledger starts in Year One (three years of draw). Sol is "Lady Vane" (20 times in Book 1). Petition needs eight signatures, and eight signatures bring it to a vote (ch.16). Varel has 31 years on the roll (ch.09), so he is about fifty. Hearing is 24 Sunspire; the box is opened ninth bell on the 28th.
- Canon from ch.10 to ch.20: Thorne's first card (18 Sunspire) went to Kael alone and he refused it; the second (25) names both. Cormac Vrell keeps the Precedent Archive (first seen ch.16). Sol's mother's schedule line reads "Isolde, daughter, age 8" (ch.17); Sol is eleven in the records-room memory (ch.13), no conflict. The steward is the small upright woman with the copper clasp. Sol's hands: second knuckle curl (ch.18), pinches a peg (ch.19), turns a page in two tries (ch.20). Chain: twelve pounds, cycle ten, falls to nine mid-Cinderveil and eight at the end (ch.19); one copper link with the knot found on the plate, so the survey has a missing way in. Ward Deed of Succession has eleven leaves and a six-leaf Schedule; clauses 7, 12, 19 are read in ch.20; thirty days run from 28 Sunspire to 28 Cinderveil.
- OPEN, check at ch.41: ch.20, 25 and 26 put the public sitting in "the third week" of Cinderveil, but ch.41 is a public sitting on 28 Cinderveil. Work out the real sitting date when you reach it.

**Ticked (all 7 checks, live-read):**
01 `17c9ba1e`, `22eb16b3` | 02 `24367622` | 03 `9dfb1db1` | 04 `7fc007ab` | 05 clean | 06 `28d0468f` | 07 `7ca17064` | 08 `fe3ce400`, `35f3b754` | 09 `ab532554` | 10 `e1cce6d3` | 11 `2f3dc3be` + commit titled `ch.11-13 fix-only` | 12 commits titled `ch.11-13 fix-only`, `ch.12 fix-only`, `ch.12 ward-trade wording` | 13 commit titled `ch.11-13 fix-only` | 14, 15, 16 commit titled `ch.14-16 fix-only` | 17 `a3b4bc34` | 18 `2ec82805` | 19 `6fbb4752` | 20 `161372d5`

**Next: ch.21.** Ch.21 to 45 are unticked. To tick one, add it to the Ticked line with its commit.
