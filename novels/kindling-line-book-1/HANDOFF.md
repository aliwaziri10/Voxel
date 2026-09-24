# Book 1 — HANDOFF (Kindling Line, "What the Gift Demands")

**Read this first**, then `architecture.md` in full, then `VOICE_GUIDE.md`.
Read `../EDITORIAL_CHARTER.md` before either. Standing rule: re-verify everything below against live GitHub before trusting it.

## FIRST ACTION NEXT SESSION: cross-check the beat-map cleanup
The first beat map (generated 2026-09-25, workflow run committed as `8e9e0d3`) FAILED review and was being cleared. Verify live whether the clear landed:
- Fetch `story_bibles/kindling-line.json` from `aliwaziri10/Voxel` main via the GitHub API (not raw.githubusercontent.com, which serves stale copies).
- CLEARED = `"book_beat_maps": {}` (no `"Kindling Line Book 1"` key).
- NOT CLEARED = the key `"Kindling Line Book 1"` still holds 45 entries. In that case DO NOT run the workflow (`cmd_novel` reuses an existing beat map with a matching chapter count and would skip planning). Clear it first: rewrite the file with `book_beat_maps` set to `{}`, keeping `series_slug`, `characters`, `visual_style`, `plot_facts`, `books` as they are.
- The old beat map stays recoverable from git history (commit `8e9e0d3`) if anyone wants to compare.
Report the result to Zia before anything else.

## Why the first beat map failed (all confirmed by reading the live JSON)
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
- Assistant writes to `.github/workflows/` return 403: Zia must paste workflow edits himself.

## Next steps, in order
1. Cross-check the cleanup (top of this file).
2. Zia runs the workflow "Voxel Novel (one command)" from `https://github.com/aliwaziri10/Voxel/actions` with: series `kindling-line`, book `Kindling Line Book 1` (slugs to `novels/kindling-line-book-1/`; do NOT use the title "What the Gift Demands"), chapters `45`, brief box EMPTY, brief_file `novels/kindling-line-book-1/brief.txt`, beat_map_only TICKED.
3. Re-read the new beat map from the API and check it against the 10 rules in `brief.txt` and the six set pieces in `architecture.md`. Specifically: ch.20 hides the proof plus an Ashworth offer; a ward is hurt by Kael's delay in ch.26-28; a real rupture in ch.33-35 not resolved by ch.35; no voluntary ward for Kael; one Reckoning in ch.40-43; consistent countdown; dates with real gaps; 45 entries, every `chapter_date` non-empty.
4. If it fails again, fix the entries by hand in the JSON rather than re-rolling repeatedly, and tell Zia.
5. Only after Zia approves the beat map: run the same workflow with beat_map_only UNticked. It reuses the saved beat map and `--checkpoint` resumes after any crash.
6. `proofreader.py` is NOT wired into `cmd_novel`. Possible later task.

## Verified state (2026-09-25)
- `voxel_cli.py` and `content_provider.py` compile. `--beat-map-only` and `chapter_date` wiring confirmed in `voxel_cli.py`.
- No chapters exist. `book_config.json` stage is `outline`.
- `CONSENSUS_LOG.md`, referenced by `architecture.md`, is NOT in this folder.
- The run log showed `NVIDIA_API_KEY` empty, so the run used OpenRouter.

## Open decisions still deferred to Zia
- Cover design direction.
- `ai_disclosure_included` / `kdp_metadata_approved` gates (heat level open-door affects these).

## Scope note carried over from architecture.md
This book's outline has real machinery (six set pieces, three ledgers, a two-stage hidden-proof subplot) beyond what Amity Falls used. The ledgers are not built in `story_bible.py`. Worth a deliberate go/no-go read after the first 10 chapters draft.
