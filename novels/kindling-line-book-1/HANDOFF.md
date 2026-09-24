# Book 1 — HANDOFF (Kindling Line, "What the Gift Demands")

**Read this first**, then `architecture.md` in full, then `VOICE_GUIDE.md`.
Read `../EDITORIAL_CHARTER.md` before either. Standing rule: re-verify everything below against live GitHub before trusting it.

## STATUS 2026-09-25: beat map re-run PASSED review — ready for Zia to run drafting
The second beat map (generated per the fixed `brief.txt`, workflow run committed as `be1dd31`, key `book_beat_maps.kindling-line` in `story_bibles/kindling-line.json`) was cross-checked live against all 8 items below and passed every one:
1. Ch.20-21: Kael pockets the proof and says nothing to Sol — hides it, does not send it (was: sent a coded message). ✓
2. Ch.19: dated House Ashworth offer exists and arrives before ch.20's discovery. ✓
3. Ch.26: a Corrin ward dies from Kael's unreported delay, directly preceding the ch.27 kiss — no more consequence-free kiss. ✓
4. Ch.33-35: real rupture (Sol confronts him with the disclosure; they part unresolved through ch.35). ✓
5. No voluntary ward anywhere for Kael — involuntary transfer mechanic stays intact all 45 chapters. ✓
6. One Reckoning event only, spread across ch.40-43 as four consecutive days (not two separate climaxes). ✓
7. Countdown consistent: the ch.1 date (28 Ashenwind) lands exactly on ch.40 "Reckoning Day One". ✓
8. Dates have real gaps (1-3 days between chapters, not rigid one-per-day); all 45 entries present with non-empty `chapter_date`. ✓

Not re-checked this session: full sentence-level prose quality (there is no prose yet — this is still just the beat map). This confirms the OUTLINE is sound, not the eventual drafted chapters.

## Next step (Zia's call to make, not automated)
Run the workflow **"Voxel Novel (one command)"** from `https://github.com/aliwaziri10/Voxel/actions` with:
```
series: kindling-line
book: Kindling Line Book 1
chapters: 45
brief: (leave empty)
brief_file: novels/kindling-line-book-1/brief.txt
beat_map_only: UNTICKED
```
This reuses the passed beat map and drafts all 45 chapters. `--checkpoint` resumes after any crash.

## 2026-09-25 (later same day): proofreader.py wired into voxel_cli.py
`proofreader.py` existed but nothing called it — Zia asked why. Fixed by splitting the two checks it offers:
- `date_consistency_check` (mechanical, no LLM call) now runs automatically inside `novel`, once per chapter right after it's written. Writes `chapters_date_report.md` next to the chapters folder. Zero added API cost, so no reason to hold it back from the drafting run.
- `grammar_scan` (one LLM call per chapter) was deliberately NOT added to `novel` — it would roughly double the API calls a 45-chapter run makes, real risk of quota exhaustion given the free-tier-only constraint. Instead it's a new separate command: `python voxel_cli.py proofread --book "Kindling Line Book 1"`. Run it any time after drafting finishes, against a fresh day's quota. Read-only, flags only, mirrors `audit`'s report style.
Pushed directly to `voxel_cli.py` (not a workflow file, so no 403) — commit `5085035`, verified live.

## Why the first beat map failed (all confirmed by reading the live JSON) — kept for reference, this attempt is superseded
1. Ch.20-21: Kael sends Sol a coded message about the proof and she trusts him. Architecture says he HIDES it until the rupture. No House Ashworth incentive offer exists anywhere.
2. Ch.14 (father's signature) and ch.16 (Corrin link) reveal the engineered failure before the ch.20 discovery.
3. Ch.26-28: kiss happens, but no ward is hurt because of Kael's delay.
4. Ch.33-35: no rupture at all. Corrin attack, then reconciliation.
5. Central mechanic broken: Kael volunteers as a ward (ch.17-18), ward-binding ceremony (ch.38-39), so the climax is chosen, not involuntary.
6. Two Reckoning-type events (trial ch.25, flight ch.40-42) and self-contradicting countdown (ch.13 "days away", ch.16 "two weeks").
7. One chapter per day for 45 days, no realistic gaps.
8. Ending hint (a "blight") does not match the planned final line about who controls ward contracts.

## What was done to fix it (2026-09-25)
- `brief.txt` (this folder) rewritten: original brief plus 10 LOCKED RULES covering every point above. The workflow reads it via the `brief_file` input, so no brief is pasted by hand.
- The `voxel-novel.yml` workflow (fixed and verified live earlier): `beat_map_only` input, `brief_file` input, words 2300/2700.
- Assistant writes to `.github/workflows/` return 403: Zia must paste workflow edits himself. (Other repo files, like `voxel_cli.py` above, do NOT 403 — assistant can push those directly.)

## Verified state (2026-09-25)
- `voxel_cli.py` and `content_provider.py` compile. `--beat-map-only` and `chapter_date` wiring confirmed in `voxel_cli.py`. `proofreader` import and both its checks now wired in (see above).
- No chapters exist yet. `book_config.json` stage is `outline`.
- `CONSENSUS_LOG.md`, referenced by `architecture.md`, is NOT in this folder.
- The beat-map run's log showed `NVIDIA_API_KEY` empty, so the run used OpenRouter.

## Open decisions still deferred to Zia
- Cover design direction.
- `ai_disclosure_included` / `kdp_metadata_approved` gates (heat level open-door affects these).

## Scope note carried over from architecture.md
This book's outline has real machinery (six set pieces, three ledgers, a two-stage hidden-proof subplot) beyond what Amity Falls used. The ledgers are not built in `story_bible.py`. Worth a deliberate go/no-go read after the first 10 chapters draft.
