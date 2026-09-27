# Book 1 — HANDOFF (Kindling Line, "What the Gift Demands")

**Read this first**, then `architecture.md` in full, then `VOICE_GUIDE.md`.
Read `../EDITORIAL_CHARTER.md` before either. Standing rule: re-verify everything below against live GitHub before trusting it.

## STATUS 2026-09-27: all 45 chapters CONFIRMED DRAFTED — this supersedes the 2026-09-25 "no chapters exist yet" note below, which was stale
Verified live via GitHub: `chapters/chapter_01.md` through `chapter_45.md` all exist and contain full prose (world: Ashworth/Corrin/Vane, Kindling cost-transfer mechanic, leads Kael Ashworth and Sol/Isolde Vane, Reckoning Accord). The drafting run referenced in the "Next step" section below has already happened at some point between 2026-09-25 and now — no record in this file of when or by whom. Future sessions: don't trust "no chapters yet" language in old handoff sections without a live listing check first.

## 2026-09-27: continuity pass — 4 chapters fixed, pushed, verified live
Ran a real (not assumed) continuity check on ch.1–21 by downloading all 45 chapters and grepping chapter_date headers plus in-text date/name references. Found and fixed:
- **Missing `chapter_date` headers**: ch.10, ch.12, ch.20, ch.21 had no header at all (every other chapter does). This breaks `date_consistency_check` for those 4 chapters. Fixed by pulling the date from each chapter's own in-text evidence, not invented:
  - ch.10 → 14 Emberfall (chapter's own addendum is explicitly dated "14 Emberfall")
  - ch.12 → 17 Emberfall (chapter states "Today: 17 Emberfall" directly)
  - ch.20 → 29 Emberfall (chapter states "The date on the offer: today. 29 Emberfall" directly)
  - ch.21 → 1 Frostveil (chapter's own ledger entries are headed "1 Frostveil, Year 3" twice)
- **Timeline contradiction, ch.21**: opened with "Three weeks since the hearing... three weeks since he returned from the archive" — but ch.21 is 1 Frostveil and the archive discovery is ch.20, dated 29 Emberfall (2 days prior, confirmed above), not three weeks. Also referenced an unestablished "hearing in the High Auditor's chamber" that doesn't appear in ch.1–20. Fixed to "Two days since he had returned from the Ashworth archive," dropping the unestablished hearing clause rather than inventing a scene to justify it.
- **Character/relationship error, ch.21**: twice called the source of the House Ashworth incentive offer "his uncle's steward." Ch.12 and ch.20 both establish, explicitly and repeatedly, that this offer comes directly from Kael's **father**, Valerius Ashworth (High Seat, House Ashworth). Fixed both instances to "his father's steward."
- Commits: `0a462a7f`→`86a35d46` (ch.10, first push was header-only by my own error, corrected same session), `5bfe9da3` (ch.12), `72ea2b2b` (ch.20), `09070933` (ch.21). All four re-fetched and confirmed live after push.

**Not yet checked**: ch.1–9, ch.13–19, ch.22–45 against the same date/character-consistency standard. ch.9 and ch.13 were read in full this session (content noted above, both clean, no seal/date issues found in either). Also noticed but NOT investigated: two similarly-named months appear in dialogue — "Frostveil" (used in chapter_date headers) and "Frostfall" (used as a deadline name in ch.16, ch.20, ch.27 dialogue/narration) — worth checking whether these are meant to be the same month or are a real duplicate-name bug. Flagging, not fixing — would need to read the full calendar system in `architecture.md`/`story_bible.py` before touching it.

**Also flagging, unresolved**: earlier the same day, a prior session/thread ran a "continuity audit" describing a completely different apparatus for this book — a "Thorne house seal," a "Ward Deed," "Anchor Seven," a co-lead-authority beat for a character called "Kael" — none of which exists anywhere in this repo (confirmed via `search_code` for "Thorne": zero results repo-wide, plus direct reads of ch.9/ch.13). That audit was not run against this book's live files. If it was run against a different Voxel book, that book hasn't been identified yet.

## STATUS 2026-09-25: beat map re-run PASSED review — ready for Zia to run drafting
The second beat map (generated per the fixed `brief.txt`, workflow run committed as `be1dd31`, key `book_beat_maps.kindling-line` in `story_bibles/kindling-line.json`) was cross-checked live against all 8 items below and passed every one:
1. Ch.20-21: Kael pockets the proof and says nothing to Sol — hides it, does not send it (was: sent a coded message). ✓
2. Ch.19: dated House Ashworth offer exists and arrives before ch.20's discovery. ✓
3. Ch.26: a Corrin ward dies from Kael's unreported delay, directly preceding the ch.27 kiss — no more consequence-free kiss. ✓
4. Ch.33-35: real rupture (Sol confronts him with the disclosure; they part unresolved through ch.35). ✓
5. No voluntary ward anywhere for Kael — involuntary transfer mechanic stays intact all 45 chapters. ✓
6. One Reckoning event only, spread across ch.40-43 as four consecutive days (not two separate climaxes). ✓
7. Countdown consistent: the ch.1 date (28 Ashenwind) lands exactly on ch.40 "Reckoning Day One". ✓
8. Dates have real gaps (1-3 days between chapters, not rigid one-per-day); all 45 entries present with non-empty `chapter_date`. ✗ **CORRECTED 2026-09-27: this was false. ch.10, ch.12, ch.20, ch.21 had no chapter_date at all — see above. Now fixed.**

Not re-checked this session: full sentence-level prose quality (there is no prose yet — this is still just the beat map). This confirms the OUTLINE is sound, not the eventual drafted chapters. **[2026-09-27: superseded — prose exists now, see top of file.]**

## Next step (Zia's call to make, not automated)
~~Run the workflow **"Voxel Novel (one command)"**~~ **Already done — all 45 chapters exist, see top of file.** Next real step is finishing the continuity pass on the remaining un-checked chapters (ch.1–9, ch.13–19, ch.22–45) and resolving the Frostveil/Frostfall question above.

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

## Verified state (2026-09-25) — see 2026-09-27 section at top for what's changed since
- `voxel_cli.py` and `content_provider.py` compile. `--beat-map-only` and `chapter_date` wiring confirmed in `voxel_cli.py`. `proofreader` import and both its checks now wired in (see above).
- ~~No chapters exist yet. `book_config.json` stage is `outline`.~~ **False as of 2026-09-27 — see top.**
- `CONSENSUS_LOG.md`, referenced by `architecture.md`, is NOT in this folder.
- The beat-map run's log showed `NVIDIA_API_KEY` empty, so the run used OpenRouter.

## Open decisions still deferred to Zia
- Cover design direction.
- `ai_disclosure_included` / `kdp_metadata_approved` gates (heat level open-door affects these).
- Which book (if any) the "Thorne house seal / Ward Deed / Anchor Seven" continuity audit was actually about — not this one.

## Scope note carried over from architecture.md
This book's outline has real machinery (six set pieces, three ledgers, a two-stage hidden-proof subplot) beyond what Amity Falls used. The ledgers are not built in `story_bible.py`. Worth a deliberate go/no-go read after the first 10 chapters draft.
