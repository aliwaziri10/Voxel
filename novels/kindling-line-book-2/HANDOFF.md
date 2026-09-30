# HANDOFF - Kindling Line Book 2

**Rules (Zia):**
1. Do not trust this file. Check the live repo (the chapter, the latest commits) before acting.
2. No profile works without Zia's permission in the current conversation.
3. Only job: run the 7 checks on a chapter, fix only what they find, and record the chapter as ticked in the same commit.
4. Skip a chapter only if it is ticked below and no later commit touched the file.
5. STOP EXPANDING. Never add words for a count. Word count is not enforced.
6. Every profile that edits this file must trim it. Keep only what the next profile needs.

**The 7 checks** (a real read, not only a grep):
1. Banned terms and names
2. Hedge words, case-insensitive: particular, something, someone, somewhere, somebody, some, kind of, the specific
3. Em-dashes: zero
4. Date and count math
5. Invented mechanisms
6. Restaged firsts
7. AI tells: rule-of-three cadence, throat-clearing openers, a closing line that explains the takeaway, stacked hedging in dialogue

**Reference:**
- Banned terms: Contract of Perpetual Surety, Deep Vault, Keeper of the Burning Ledger as an office, Accord Hall, Great Hall, Grand Auditor, Nine Houses, inquiry board, Tripartite Seal, Founding Council, invented article or section numbers, Consultant. Site is Anchor Seven only.
- Banned names: Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor, Varrick, Helseth, Dallin Vorys, a living or clerk Valerius (Valerius Ashworth is Kael's dead father in Book 2, fine). Grep with word boundaries: "Hest" matches "chest".
- Dates: Sunspire is 30 days. Ch.N is day (N+8) of Sunspire through ch.22. From ch.23, ch.N is day (N-22) of Cinderveil.
- Firsts: "I love you" and the first kiss happen in ch.28, never earlier, never restaged.
- Canon (checked against Book 1 manuscript): the old system is "the ward trade" (Book 1 has no "Compact"; Book 2 ch.01, 05, 06 use "former Compact" in passing). Book 1 uses lowercase "ward contract" only, so no capitalised bare "the Contract". The Vault tap ledger starts in Year One (three years of draw). Sol is "Lady Vane" (20 times in Book 1). Petition needs eight signatures. Varel has 31 years on the roll (ch.09), so he is about fifty. Hearing is 24 Sunspire; the box is opened ninth bell on the 28th.

**Ticked (all 7 checks, live-read):**
01 `17c9ba1e`, `22eb16b3` | 02 `24367622` | 03 `9dfb1db1` | 04 `7fc007ab` | 05 clean | 06 `28d0468f` | 07 `7ca17064` | 08 `fe3ce400`, `35f3b754` | 09 `ab532554` | 10 `e1cce6d3` | 11 `2f3dc3be` + commit titled `ch.11-13 fix-only` | 12 commits titled `ch.11-13 fix-only`, `ch.12 fix-only`, `ch.12 ward-trade wording` | 13 commit titled `ch.11-13 fix-only` | 14, 15, 16 commit titled `ch.14-16 fix-only`

**Next: ch.17.** Ch.17 to 45 are unticked. To tick one, add it to the Ticked line with its commit.
