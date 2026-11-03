# Warm Enough: AUDIT HANDOFF (2026-10-31, Claude chat, Zia in charge, Claude acting alone)

Read AFTER `novels/EDITORIAL_CHARTER.md`, `novels/warm-enough/HANDOFF.md` and `HANDOFF_2026-10-31_TOOLS.md`. Repo: `aliwaziri10/Voxel` (the connector is logged in as `aliwaziri10`; do NOT use Wazzaboyzz/Voxel).

## STANDING RULES FROM ZIA (read first, every session)
- THE ACCOUNT NAME: the GitHub account is "Ali Waziri 10" (login `aliwaziri10`). It is NOT "Ali Waziri". Earlier Claude sessions wrote "Ali Waziri" in their memory notes, which is wrong; always say "Ali Waziri 10". (Zia asked for this correction on 2026-11-03. Claude's memory could not be edited in that chat because memory writes are blocked once a chat has used the GitHub connector, so a later chat that has NOT used a connector should fix the memory lines that say "Ali Waziri" or "Ali 10.0".)
- Anything Zia must copy and paste goes INSIDE a code block with a copy button. One step at a time. Browser only, never a terminal. Free tools only.
- Say what you will change BEFORE changing it. Never touch a published novel (Kindling Line, Amity Falls, Proof of Home).
- Zia has told Claude to act alone, not wait for input, keep going until the session runs out, and write a handoff before the session ends. Claude must do everything it can itself. The only things it cannot do from chat are start a workflow run and edit files under `.github/workflows`; only those go to Zia. (Claude's own memory could not save this: once a chat uses the GitHub connector, memory writes are blocked for that chat. This file is the record.)

## CONFIRMED (checked live this session)
1. Connector can READ and WRITE files and notes in the repo, but is REFUSED on anything under `.github/workflows` (GitHub error 403, "without `workflows` permission"). Workflow fixes must be pasted by Zia in the browser.
2. Last commits on main before this session's work (2026-10-31): `warm-enough-mechanical-fixes.yml`, `ext-tools-readonly.yml`, `humanizer-pass.yml` created in the browser by Zia; two notes-only tools handoff commits.
3. Full-book scan of all 40 chapters of Warm Enough, fetched from the raw files: total about 99,700 words. Zero em or en dashes, zero digits, zero banned words, zero banned names (Wren, Pell, Bram, Hale, Oakes, weekdays, months). Only flags: ch13 (2,745 before the fix), ch18 (2,820), ch19 (3,331) over length, left uncut on purpose per STATUS.md; ch31 has one "somebody" (read in context: "somebody had been out at dusk with a taper", a plain use, left).
4. Workflow audit of the three new files:
   - `humanizer-pass.yml`: looks correct. `scripts/humanizer_pass.py` and root `humanizer.py` both exist.
   - `warm-enough-mechanical-fixes.yml`: looks safe. Report mode changes nothing; apply mode pushes a review branch, never main. Caution: it rewrites every "gray" to "grey", so a character surnamed Gray would be changed. No such name was seen in the chapters.
   - `ext-tools-readonly.yml`: had ONE bug in the Harper step. FIXED by Zia in the browser (commit `4e9f5272e807812e583d0f2f30a2b9afdc77f10d`, 2026-11-03): the download line now names the exact file `harper-cli-x86_64-unknown-linux-gnu.tar.gz`. The next line (`tar -xzf ./*.tar.gz`) is fine because only one file is now downloaded. File checked valid YAML. Not yet seen running in Actions. Vale v3.25.1 exists and its file `vale_3.25.1_Linux_64-bit.tar.gz` matches the pattern. The slop-score list URL returns 200.

## DONE THIS SESSION (all verified after the push)
Voice-rule breaks (VOICE_GUIDE: Ansel odd chapters = NO wool or knitting comparisons; Hester even chapters = NO schoolroom or river comparisons). Most wool words in odd chapters are literal wool on the page, which is allowed. Even-chapter words like chalk, children, river appear literally in Hester chapters (setting); only COMPARISONS are banned. Five phrases in three chapters were real breaks and are now fixed in the files:
- ch13 (Ansel), commit `4f0299e581d5fcdcc57cefcecff07e1f066c10ad`: "as though it had been cast on in one frame of mind and bound off in another" -> "as though it had been started in one frame of mind and finished in another". Now 2,743 words.
- ch22 (Hester), commit `64881dd041025fad7527def5652b24656ad5c5c8`: "cold as slate" -> "cold as a skein left out in the frost". Now 2,569 words.
- ch31 (Ansel), commit `0aadbef5532212de7ecda35b65162703f9211436`, three phrases: "as plain as a selvedge" -> "as plain as a rule drawn across a slate"; "as if a stitch had gone through the eye of a needle the wrong way and she had felt it" -> "as chalk catches on a slate and the hand feels it before the ear does"; "like wool round a spindle" -> "like river ice round a stone". Still 2,817 words.
Verification: each pushed file was fetched back by commit SHA and compared byte for byte with the original plus only those phrase swaps (exact match for ch13, ch22 and ch31). A re-scan found no dashes, no digits and no remaining comparison breaks. Humanizer scores before and after the edits: ch13 51.6 to 51.6, ch22 56.5 to 56.5, ch31 50.6 to 50.7. NOT stamped in `stamps/`: these were targeted voice fixes, not a chapter review.

Stale files corrected:
- `book_config.json` (commit `5c7729cfc513d8849ba00a67f53c00210a441d99`): stage changed from `planning_done_no_chapters` to `all_40_chapters_drafted_review_pending`, one history line added. JSON checked valid. All manual gates left exactly as they were (only the name audit is true). No script checked reads the stage field.
- `STATUS.md` (commit `80d85462195b55c8035ac1420ab42e5e3ee4f8a6`): the 2026-10-28 claim on ch35 to ch40 was released; the ch38 line was finished; ch39 and ch40 lines added; a line recording the voice fixes added. Checked: every other line is byte-identical to before.
- `HANDOFF.md` (commit `5e08f7dc09108adad451275b88aabc4ed889306c`, 2026-11-03): nine stale lines corrected after a second Claude chat reviewed the humanizer session's work (config and STATUS already fixed; `humanizer-pass.yml` pasted; pointers added). Nothing else in that file changed.

Reviewed 2026-11-03 (other session's work, verified): `scripts/slop_flags.py` (commit 41e621a) is the file reported (git blob hash matches), compiles, and runs. `humanizer-pass.yml` (commit c941bd3) runs the humanizer score and then slop_flags. `humanizer-revise.yml` and `scripts/humanizer_revise.py` (created 2026-10-31) are a paragraph REWRITE tool: dry-run is safe, apply mode pushes a review branch only. Do NOT run apply mode until Zia decides between option A (keep the humanizer spec frozen, recommended in HANDOFF.md) and option B.

## Sequential human read: STARTED
Chapter 1 was read against `briefs/ch01.md` on 2026-11-03 (read only so far, no stamp, no edits yet). Notes: the chapter matches the brief's plot and ending image (Hester's mouth thinning like a stroke of chalk, first lantern lit behind her), has no tin, no Grey, no school or cottage, and Hester says almost nothing. Open question to settle before stamping: the brief says quay folk have "one short line each at most". Lines found: the deckhand speaks one longer speech (STATUS.md already notes two lines for him); the woman with the red blanket one line; the porter "Here now"; the stout woman one line; the old woman at the post "Well,"; the smallest child "You're an onion" (plus Ansel's reply). The deckhand's speech is the main overrun. Gran speaks to the quay, not to him, as the brief says. Not yet checked against canon: whether the letter's description matches `canon/CANON_LOCK.md`.

## NOT DONE / UNKNOWN (do not trust this file as a final review)
- No workflow run result has been seen. The connector cannot read Actions runs. Zia or a browser session must open `https://github.com/aliwaziri10/Voxel/actions` and report which runs are green, red or yellow.
- `scripts/write_warm_enough.py --check` and `scripts/novel_guard.py` were NOT run on any chapter this session (no way to run Actions from here). Run them on ch13, ch22, ch31 and ch38 to ch40.
- The strict sequential human read of chapters 1 to 40 is only begun (chapter 1 read, nothing stamped). `book_config.json` manual gates are open. `AUDIT_REPORT.md` and `PROOFREAD_TRACKER.md` were not read or updated.
- Only the comparison breaks above were searched for, using a pattern (comparison words followed by wool or schoolroom words within 40 characters), so a comparison phrased differently could still be missed.

## PROBLEMS NOTICED, NOT CHANGED (need Zia or a browser edit)
- `.github/workflows/write-warm-enough.yml` is still on a schedule (four runs a day) and carries the note "Do not commit to the repo while this is running". All 40 chapters exist, so it should only rewrite the audit report. Zia should consider disabling it: Actions tab > Write Warm Enough > the three dots menu > Disable workflow.
- `.github/workflows/proofread-languagetool.yml` defaults to `novels/proof-of-home/chapters`, a PUBLISHED book. Default should be changed to `novels/warm-enough/chapters`.

## NEXT STEPS (in order)
1. Zia runs `External tools report (read-only)` and tells the next session which parts are green (Harper fix is in), then runs `Humanizer score (read only)` to see the slop step.
2. Run `Warm Enough mechanical fixes` in report mode first, read the table, and only then consider apply mode (it makes a review branch, never touches main).
3. Continue the strict sequential human read from chapter 1 (finish chapter 1 against `canon/CANON_LOCK.md`, then chapter 2 onward), against `briefs/` and `canon/`, fixing flags in the file, stamping each chapter in `stamps/`.
4. Proofread and the KDP gates in `book_config.json`.
