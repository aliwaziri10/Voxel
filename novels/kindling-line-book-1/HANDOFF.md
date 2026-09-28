# Book 1 — HANDOFF (Kindling Line, "What the Gift Demands")

**Read this first**, then `architecture.md` in full, then `VOICE_GUIDE.md`.
Read `../EDITORIAL_CHARTER.md` before either. Standing rule: re-verify everything below against live GitHub before trusting it.

## 2026-09-28: Reckoning-date / countdown pass — ch.3, 11, 12, 16, 20 fixed and pushed
Canon (verified live): ch.1 fixes the Reckoning at **29 Frostveil, Year 3**; ch.40 header is 29 Frostveil. Calendar used by chapter_date headers: Emberfall (ch.1 = 1 Emberfall), Frostveil, Sunspire. There is NO month "Frostfall" — it appeared only as an error. Assumed 30-day months (matches every verified header gap).
Fixed (each pushed to `main`, re-fetched sizes match):
- ch.3: "15 Frostfall" → 29 Frostveil; all "forty-two days" → 55 (true count from 4 Emberfall). Commit `14f9d912`.
- ch.11: "Frostfall twenty-eight, 42 days" → Frostveil 29, 43 days (true from 16 Emberfall). Commit `69fe4851`.
- ch.12: Reckoning 12 Frostveil → 29 Frostveil; offer expiry 28 Frostveil → 13 Sunspire; "two weeks before" → six weeks. Commit `4d041d5a`.
- ch.16: "23rd of Frostfall" → 29 Frostveil; countdown 13/30 → 36 days (true from 23 Emberfall); removed "dead for two years". Commit `b3233559`.
- ch.20: "14th of Frostfall" → 29 Frostveil; offer expiry 3rd Frostfall → 13 Frostveil (14 days, matches "Fourteen days" line). Commit `344d634c`.

**STILL WRONG, NOT YET FIXED (true days-to-Reckoning from each chapter's header; text currently says otherwise):**
ch.2 says 38 (true 57); ch.6 says 87 (true 51); ch.13 says 43 (true 40); ch.17 says 43 (true 34); ch.23 says 47 (true 25); ch.24 "six weeks" (true 24 days); ch.25 "six weeks/42 days" (true 22); ch.27 says 30 (true 19); ch.28 says 27 (true 18); ch.29 "six weeks/42 days" (true 16); ch.30 "three weeks" (true 15); ch.34 says 9 (true 9, OK). ch.18 says "six weeks" (true 33 days). Also ch.22 says "eighteen weeks"/"Reckoning in eighteen weeks" (true 27 days) and ch.3/11 "twelve years"/"three years" references not audited.

## OPEN DECISION FOR ZIA — is Valerius Ashworth alive or dead in Book 1?
On-page ALIVE and speaking: ch.2, 6, 12, 18, 20, 30, 32, 36 (councils), 40 (confronts Kael at the Reckoning), 44 (stripped of his seat). DEAD: ch.3 (Kael says he died 3 months after retiring, sealed autopsy, and gives Sol his chain), ch.3 line "my father died for a lie", ch.22 (uncle Lord Corven Ashworth "head of house since Kael's father died" makes the offer), ch.24 ("son of the late High Auditor Valerius"), ch.34 ("offer from my uncle"). Book 2's other-session note also says Valerius is "supposed to be dead". Not changed here: ch.3's death is woven into a major reveal and ch.22 is a large scene. Zia must choose canon before those chapters are touched; alive is the majority of on-page scenes.

## OTHER UNFIXED FINDINGS (verified by grep, not yet edited)
- ch.22 is heavily off-canon: Sol's mother is alive and speaking ("Lady Vane", "her mother"), though she died after her Reckoning in ch.3/13/16; uncle Corven replaces Valerius; it contains literal "chapter twenty / chapter five / chapter thirteen / chapter eleven" references in narration. Needs a rewrite of the affected scenes, not a patch.
- Literal "chapter N" meta-references in narration also in ch.14 (line 59), ch.23 (117), ch.27 (39, 41 "date fixed in chapter one of the founding charter"), ch.44 (83). Remove or rephrase.
- ch.34 line 27: "hearing in the Hall of Ledgers, Twenty Frostveil last year" — no such hearing exists on the page.
- Book 2 (`novels/kindling-line-book-2`) is being worked by another session; its own handoff lists its own issues (Valerius alive in its ch.1, "Nine Houses" vs twelve, seal changes, ch.36 "co-equals" early). Do not merge the two.

## STATUS 2026-09-27: all 45 chapters CONFIRMED DRAFTED — this supersedes the 2026-09-25 "no chapters exist yet" note below, which was stale
Verified live via GitHub: `chapters/chapter_01.md` through `chapter_45.md` all exist and contain full prose (world: Ashworth/Corrin/Vane, Kindling cost-transfer mechanic, leads Kael Ashworth and Sol/Isolde Vane, Reckoning Accord). Future sessions: don't trust "no chapters yet" language in old handoff sections without a live listing check first.

## 2026-09-27: continuity pass — 4 chapters fixed, pushed, verified live
- **Missing `chapter_date` headers** in ch.10, 12, 20, 21: fixed from in-text dates (ch.10 → 14 Emberfall, ch.12 → 17 Emberfall, ch.20 → 29 Emberfall, ch.21 → 1 Frostveil).
- **ch.21 timeline**: "three weeks since the hearing" → "two days since he returned from the Ashworth archive" (unestablished hearing dropped).
- **ch.21**: "his uncle's steward" → "his father's steward" (twice). NOTE: given the open Valerius decision above, this may need to revert.
- Commits: `0a462a7f`→`86a35d46` (ch.10), `5bfe9da3` (ch.12), `72ea2b2b` (ch.20), `09070933` (ch.21).
- The earlier "Thorne house seal / Ward Deed / Anchor Seven / co-lead" audit does not match any file in this repo (zero search hits for "Thorne" as a seal or house; "Thorne" is only a Corrin envoy name in ch.16). It was not run against this book.

## STATUS 2026-09-25: beat map re-run PASSED review — ready for Zia to run drafting
The second beat map (generated per the fixed `brief.txt`, workflow run committed as `be1dd31`, key `book_beat_maps.kindling-line` in `story_bibles/kindling-line.json`) was cross-checked live against all 8 items below and passed every one:
1. Ch.20-21: Kael pockets the proof and says nothing to Sol — hides it, does not send it (was: sent a coded message). ✓
2. Ch.19: dated House Ashworth offer exists and arrives before ch.20's discovery. ✓
3. Ch.26: a Corrin ward dies from Kael's unreported delay, directly preceding the ch.27 kiss — no more consequence-free kiss. ✓
4. Ch.33-35: real rupture (Sol confronts him with the disclosure; they part unresolved through ch.35). ✓
5. No voluntary ward anywhere for Kael — involuntary transfer mechanic stays intact all 45 chapters. ✓
6. One Reckoning event only, spread across ch.40-43 as four consecutive days (not two separate climaxes). ✓
7. Countdown consistent: the ch.1 date lands exactly on ch.40 "Reckoning Day One". ✓ (the drafted prose does NOT keep this consistent — see 2026-09-28 section.)
8. Dates have real gaps; all 45 entries present with non-empty `chapter_date`. ✗ corrected 2026-09-27, see above.

## Next step
Finish the continuity pass: (1) Zia rules on Valerius alive/dead; (2) fix the remaining countdown numbers listed above; (3) rewrite ch.22's off-canon scenes; (4) strip "chapter N" meta-references; (5) re-run `python voxel_cli.py proofread --book "Kindling Line Book 1"` after fixes.

## 2026-09-25 (later same day): proofreader.py wired into voxel_cli.py
`date_consistency_check` (mechanical, no LLM call) runs inside `novel` per chapter; writes `chapters_date_report.md`. `grammar_scan` is a separate command: `python voxel_cli.py proofread --book "Kindling Line Book 1"`. Pushed to `voxel_cli.py`, commit `5085035`.

## Why the first beat map failed — kept for reference, superseded
1. Ch.20-21 coded message; no Ashworth offer. 2. Engineered failure revealed before ch.20. 3. Consequence-free kiss. 4. No rupture ch.33-35. 5. Kael volunteers as ward (broke involuntary mechanic). 6. Two Reckoning events and a broken countdown. 7. One chapter per day. 8. Ending hint mismatch.

## What was done to fix it (2026-09-25)
- `brief.txt` rewritten with 10 LOCKED RULES. `voxel-novel.yml` reads it via `brief_file`.
- Assistant writes to `.github/workflows/` return 403: Zia must paste workflow edits himself. Other repo files can be pushed directly.

## Open decisions still deferred to Zia
- Valerius alive/dead (above).
- Cover design direction.
- `ai_disclosure_included` / `kdp_metadata_approved` gates (heat level open-door affects these).

## Scope note carried over from architecture.md
The outline has real machinery (six set pieces, three ledgers, a two-stage hidden-proof subplot) beyond what Amity Falls used. The ledgers are not built in `story_bible.py`.
