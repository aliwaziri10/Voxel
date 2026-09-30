# HANDOFF - Kindling Line Book 2

**Rules (Zia):**
1. Do not trust this file. Check the live repo (the chapter, the latest commits) before acting.
2. No profile works without Zia's permission in the current conversation.
3. Only job: run the 7 checks on a chapter, fix only what they find, and record the chapter as ticked in the same commit.
4. Skip a chapter only if it is ticked below and no later commit touched the file.
5. STOP EXPANDING. Never add words for a count. Word count is not enforced.
6. Every profile that edits this file must trim it. Keep only what the next profile needs.
7. Workflow (Zia): do three chapters, then update this file, then keep going without waiting. After that, one chapter at a time, updating this file each time. Do not stop until the session is exhausted.

**The 7 checks** (a real read, not only a grep):
1. Banned terms and names
2. Hedge words, case-insensitive: particular, something, someone, somewhere, somebody, some, kind of, the specific
3. Em-dashes: zero
4. Date and count math
5. Invented mechanisms
6. Restaged firsts
7. AI tells: rule-of-three cadence, throat-clearing openers, a closing line that explains the takeaway, stacked hedging in dialogue

**Reference:**
- Banned terms: Contract of Perpetual Surety, Deep Vault, Keeper of the Burning Ledger as an office, Accord Hall, Great Hall, Grand Auditor, Nine Houses, inquiry board, Tripartite Seal, Founding Council, invented article or section numbers, Consultant. Site is Anchor Seven only. A case-insensitive grep also hits "nine houses" as a vote count; reword it.
- Banned names: Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor, Varrick, Helseth, Dallin Vorys, a living or clerk Valerius (Valerius Ashworth is Kael's dead father, fine). Grep with word boundaries: "Hest" matches "chest".
- Dates: Sunspire is 30 days. Ch.N is day (N+8) of Sunspire through ch.22. From ch.23, ch.N is day (N-22) of Cinderveil.
- Firsts: "I love you" and the first kiss happen in ch.28, never earlier, never restaged.
- Canon: the old system is "the ward trade", never "the Compact" or a capitalised bare "the Contract". Sol is "Lady Vane". Eight signatures bring the petition to a vote; nine of twelve houses set the Deed aside (ch.20). Hearing 24 Sunspire; box opened ninth bell 28 Sunspire; the Deed's thirty days run to 28 Cinderveil. The petition has four heads; the second (contract standard) was withdrawn at noon on 28 Sunspire. Call it "the second head", never "the annex". The steward is the small upright woman with the copper clasp. Cormac Vrell keeps the Precedent Archive. Bram is the junior clerk. One copper link with the knot was found on the Council's chain (ch.19): the survey has a missing way in. Chain cycle is ten, falls to nine mid-Cinderveil and eight at the end. Sol's hands: pinch (ch.19), page turn (ch.20), closed fists and first pen-writing (whole-fist grip, *I.V.*) in ch.22 on 30 Sunspire, a day early; linen off ch.23 (1 Cinderveil); rope due about the fifth. Violet awning at the foot of the Lower Spine stair opened 29 Sunspire; Tam (Ansa's nephew) signed first afternoon, 31 names by dusk (ch.22). Name counts by lamps: 31 (29 Sun), 69 (30 Sun), 143 (1 Cin), 214 (2 Cin) of about 400. Hold notices on 3 Cinderveil (ch.25) hit the three who asked to read the standard at dawn on the 1st.
- OPEN, check at ch.41: ch.20, 25 and 26 put the public sitting in "the third week" of Cinderveil, but ch.41 is a public sitting on 28 Cinderveil. Work out the real sitting date when you reach it.

**Ticked (all 7 checks, live-read):**
01 `17c9ba1e`, `22eb16b3` | 02 `24367622` | 03 `9dfb1db1` | 04 `7fc007ab` | 05 clean | 06 `28d0468f` | 07 `7ca17064` | 08 `fe3ce400`, `35f3b754` | 09 `ab532554` | 10 `e1cce6d3` | 11 `2f3dc3be` + commit titled `ch.11-13 fix-only` | 12 commits titled `ch.11-13 fix-only`, `ch.12 fix-only`, `ch.12 ward-trade wording` | 13 commit titled `ch.11-13 fix-only` | 14, 15, 16 commit titled `ch.14-16 fix-only` | 17 `a3b4bc34` | 18 `2ec82805` | 19 `6fbb4752` | 20 `161372d5` | 21 `eddcfb2c` | 22 commit titled `ch.22 fix-only` | 23, 24, 25 commit titled `ch.23-25 fix-only`

**Next: ch.26.** Ch.26 to 45 are unticked. To tick one, add it to the Ticked line with its commit.
