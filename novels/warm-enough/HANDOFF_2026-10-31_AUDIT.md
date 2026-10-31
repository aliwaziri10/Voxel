# Warm Enough: AUDIT HANDOFF (2026-10-31, Claude chat, Zia in charge, Claude acting alone)

Read AFTER `novels/EDITORIAL_CHARTER.md`, `novels/warm-enough/HANDOFF.md` and `HANDOFF_2026-10-31_TOOLS.md`. Repo: `aliwaziri10/Voxel` (the connector is logged in as `aliwaziri10`; do NOT use Wazzaboyzz/Voxel).

## STANDING RULES FROM ZIA (read first, every session)
- Anything Zia must copy and paste goes INSIDE a code block with a copy button. One step at a time. Browser only, never a terminal. Free tools only.
- Say what you will change BEFORE changing it. Never touch a published novel (Kindling Line, Amity Falls, Proof of Home).
- Zia has told Claude to act alone, not wait for input, and to write a handoff before the session ends.

## CONFIRMED (checked live this session)
1. Connector can READ and WRITE files and notes in the repo, but is REFUSED on anything under `.github/workflows` (GitHub error 403, "without `workflows` permission"). Workflow fixes must be pasted by Zia in the browser.
2. Last commits on main (2026-10-31): `warm-enough-mechanical-fixes.yml`, `ext-tools-readonly.yml`, `humanizer-pass.yml` created in the browser by Zia; two notes-only tools handoff commits.
3. Full-book scan of all 40 chapters of Warm Enough, fetched from the raw files: total about 99,700 words. Zero em or en dashes, zero digits, zero banned words, zero banned names (Wren, Pell, Bram, Hale, Oakes, weekdays, months). Only flags: ch13 (2,745), ch18 (2,820), ch19 (3,331) over length, left uncut on purpose per STATUS.md; ch31 has one "somebody" (read in context: "somebody had been out at dusk with a taper", a plain use, left).
4. Workflow audit of the three new files:
   - `humanizer-pass.yml`: looks correct. `scripts/humanizer_pass.py` and root `humanizer.py` both exist.
   - `warm-enough-mechanical-fixes.yml`: looks safe. Report mode changes nothing; apply mode pushes a review branch, never main. Caution: it rewrites every "gray" to "grey", so a character surnamed Gray would be changed. No such name was seen in the chapters.
   - `ext-tools-readonly.yml`: ONE REAL BUG in the Harper step (see next section). Vale v3.25.1 exists and its file `vale_3.25.1_Linux_64-bit.tar.gz` matches the pattern. The slop-score list URL returns 200. Harper v3.0.0 exists; its Linux file is `harper-cli-x86_64-unknown-linux-gnu.tar.gz` and unpacks to a file named `harper-cli`.

## BUG TO FIX BY ZIA (Claude cannot edit workflows)
In `.github/workflows/ext-tools-readonly.yml`, the Harper install line uses the wildcard `'*harper-cli*linux*'`, which matches FOUR Linux files (two chip types, two builds). The next line then tries to unpack all four at once and fails, so the Harper job fails (the other jobs still report because of continue-on-error).
Replace these two lines:
```
          if gh release download v3.0.0 --repo Automattic/harper --pattern '*harper-cli*linux*' && ls ./*.tar.gz >/dev/null 2>&1; then
            tar -xzf ./*.tar.gz
```
with these two lines:
```
          if gh release download v3.0.0 --repo Automattic/harper --pattern 'harper-cli-x86_64-unknown-linux-gnu.tar.gz' && ls ./harper-cli-x86_64-unknown-linux-gnu.tar.gz >/dev/null 2>&1; then
            tar -xzf ./harper-cli-x86_64-unknown-linux-gnu.tar.gz
```
Edit page: `https://github.com/aliwaziri10/Voxel/edit/main/.github/workflows/ext-tools-readonly.yml`
(Even unfixed, the job falls back to `cargo install` only when the download fails, and here the download succeeds, so the fix is needed.)

## VOICE-RULE BREAKS FOUND (VOICE_GUIDE: Ansel odd chapters = NO wool or knitting comparisons; Hester even chapters = NO schoolroom or river comparisons)
Most wool words in odd chapters are literal wool on the page, which is allowed. These are the real comparison breaks:
- ch13 (Ansel): "as though it had been cast on in one frame of mind and bound off in another" -> planned fix: "started" and "finished" in place of "cast on" and "bound off".
- ch22 (Hester): "cold as slate" -> planned fix: "cold as a skein left out in the frost".
- ch31 (Ansel), three: "as plain as a selvedge" -> "as plain as a line ruled across a slate"; "as if a stitch had gone through the eye of a needle the wrong way and she had felt it" -> "as chalk catches on a slate and the hand feels it before the ear does"; "like wool round a spindle" -> "like river ice round a stone".
STATUS of these fixes: see the bottom section "WHAT WAS DONE AFTER THIS NOTE". If that section is empty, none has been applied yet.
Even-chapter words like chalk, children, river appear literally in Hester chapters (Ansel's world, the setting); only COMPARISONS are banned, so those were left.

## NOT DONE / UNKNOWN (do not trust this file as a final review)
- No workflow run result has been seen. The connector cannot read Actions runs. Zia or a browser session must open `https://github.com/aliwaziri10/Voxel/actions` and report which runs are green, red or yellow.
- `scripts/write_warm_enough.py --check` and `scripts/novel_guard.py` were NOT run on any chapter this session (no way to run Actions from here).
- The strict sequential human read of chapters 1 to 40 is still NOT done. `book_config.json` manual gates are open. `AUDIT_REPORT.md` and `PROOFREAD_TRACKER.md` were not read or updated.
- Chapter edits this session were targeted voice fixes only, not a read.

## PROBLEMS NOTICED, NOT CHANGED (need Zia or a browser edit)
- `.github/workflows/write-warm-enough.yml` is still on a schedule (four runs a day) and carries the note "Do not commit to the repo while this is running". All 40 chapters exist, so it should only rewrite the audit report. Zia should consider disabling it: Actions tab > Write Warm Enough > the three dots menu > Disable workflow.
- `.github/workflows/proofread-languagetool.yml` defaults to `novels/proof-of-home/chapters`, a PUBLISHED book. Default should be changed to `novels/warm-enough/chapters`.
- `book_config.json` stage says planning_done_no_chapters although chapters 1 to 40 exist.
- STATUS.md still has the claim line for ch35 to ch40 (2026-10-28) and says ch38 "checks pending". Chapters 38 to 40 were written, verified and handed off on 2026-10-28 (see HANDOFF_2026-10-28_SIXTH.md), so the claim is stale; confirm with Zia, then remove it.

## NEXT STEPS (in order)
1. Zia pastes the two-line Harper fix above, then runs `External tools report (read-only)`, then `Humanizer score (read only)` and tells the next session which are green.
2. Run `Warm Enough mechanical fixes` in report mode first, read the table, and only then consider apply mode (it makes a review branch, never touches main).
3. Strict sequential human read, chapter 1 to 40, fixing flags in the file, stamping each chapter in `stamps/`.
4. Proofread and the KDP gates in `book_config.json`.

## WHAT WAS DONE AFTER THIS NOTE
(empty so far)
