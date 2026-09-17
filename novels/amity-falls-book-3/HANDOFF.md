## PROCEDURE (READ FIRST)

Defers to `novels/EDITORIAL_CHARTER.md` for methodology. This file = this book's own facts: locked word floor, canon, review log.

Mechanical proofreading, sequential continuity/voice/canon review, and repeated-words pass are all DONE (ch.1-45). **The hedge sweep below is the only open item.**

## STOP — READ THIS BEFORE TOUCHING THE HEDGE SWEEP

**The book-wide "17-32 instances per chapter" figures logged earlier today were WRONG.** They came from a naive grep that also matched "someone," "somewhere," "somehow," "sometime" — none of which are the defect. When filtered to the actual pattern (a bare "some ___" / "something ___" standing in for an unnamed feeling, e.g. "some part of him," "some old instinct," "something steadier") the REAL count is roughly **0-2 genuine instances per chapter**, not 17-32. "Something closer to X than Y" and similar concrete comparisons are NOT the defect and should never be touched.

**Verified 2026-09-17 (fresh re-check against live files, filtered for the real pattern only):** ch.1-2 clean (already fixed by an earlier session today). Ch.3 mostly clean, one instance may remain — verify before assuming done. Genuinely unfixed instances confirmed still present as of this check:

| Ch | Unfixed instance(s) |
|---|---|
| 4 | "some old instinct for not making a frightened man..."; "costing the old woman something too, some quiet grief of her own" |
| 7 | "some part of him" |
| 12 | "some deeper instinct" |
| 15 | "some part of him" |
| 18 | "some part of him" |
| 21 | "some protective instinct" |
| 24 | "some old grief" |
| 26 | "some part of him heard it and some part of him agreed" (2 in one sentence); "some fresh weight" |
| 42 | "some echo of him" |

Also present, lower-confidence/borderline (bare "something old"/"something quiet"/"something steadier" with no defining clause — judge each on read, may be fine as-is): ch.3, 5, 16, 17, 23(x2), 27, 30, 31, 32, 38, 40, 43, 44(x2).

**That's it. ~9 confirmed real fixes plus a dozen borderline judgment calls across the whole 45-chapter book — NOT a large job.** Whoever picks this up: fix the confirmed list first (each is a 5-minute in-context edit, same style as the ch.1/ch.3 fixes already done), then use judgment on the borderline list per the standard below. Do NOT re-derive counts from PROOFREAD_REPORT.md's raw grep — it overcounts by roughly 10x.

**Standard:** only fix a bare "some/something ___" that stands in for an unnamed feeling/instinct/thread with no concrete referent. Leave "something closer to X than Y," "something [concrete noun]," and anything already qualified by a specific adjective or defining clause. When in doubt, leave it — this is cosmetic polish, not a structural defect, and does not block publishing.

**Coordination note:** multiple sessions touched this file and these chapters within the same hour on 2026-09-17. Always re-read a chapter fresh immediately before editing it — don't trust this table's "unfixed" status without a quick grep first, in case another session got there first.

## Locked facts

- **Word floor: 1,900-2,700w/chapter, FINAL, no more padding, ever.** (Book 4+ uses the charter's 2,300w standard instead — don't conflate them.)
- No em dashes. Zero "particular" anywhere. Confirmed book-wide.
- Voice: Mara dry/engineering-metaphor, Caleb steady/plainspoken, Wren blunt/fast-talking, Priya procedural, Dev hardening through the climax then softening post-eclipse. **Caleb and Mara are married** (est. ch.21).
- "Kind of" pattern: **"own kind of ___" and bare "a kind of + generic emotion noun" = filler, fix on sight.** "Kind of" attached to something concrete/specific = legitimate, leave alone.
- Eclipse countdown resolved to zero at ch.35 (eclipse night). No more day-counts past that point.
- Never call Book 2 "the last book" etc. in-prose (found/fixed once, ch.25).
- **Eleanor/Ambrose genealogy — RESOLVED, ch.42-45:** Eleanor was Ambrose's wife (ring engraved E.W. & A.W.), widowed 1945, remarried Samuel 1947. Ch.42 calls Dev/Priya "her grandchildren"; ch.45 calls Dev's arrival the culmination of "three generations"; Ambrose's own letter (ch.45) says he is "not the first of my blood," his grandfather having begun the doctrine, and that he "carried [it] into our marriage" with Eleanor. Together these confirm Eleanor and Ambrose had a child together before his 1945 death. Not stated in one explicit sentence, but consistent across three chapters — intentional mystery-novel detail, don't "fix" by adding an explicit line unless Zia asks.

## Story summary

Sequel to Book 2. Dev (Priya's brother) inherits a hereditary Whitlock-line hunger, triggered by direct contact with Book 2's well ritual. A hidden "quiet family" faction wants it to complete rather than be stopped; splinter leader Corwin Drake leads violent opposition in Act Three. Six-week countdown to the autumn eclipse. Resolves fully: a ten-person ring redistributes what Dev carries at the eclipse-night ritual despite Drake's armed interference; Dev survives whole. Ends on an open Book 4 hook (Drake at large, other Whitlock-line families exist elsewhere). Full chapter-by-chapter beat breakdown lives in `beat_map.md`.

Read before writing: `EDITORIAL_CHARTER.md`, Book 2's `chapter_41.md` (Adelaide's letter) and `HANDOFF.md`, Book 1's `architecture.md`, this book's `beat_map.md`.

## Confirmed-good canon from the full review

Full arc through eclipse night (ch.35) confirmed clean: recruiter contacts → doctrine reveal → Elias mole arc → ring proposal → three genuinely distinct security leaks (Elias/mole, ch.29 sightline, ch.34 scheduling gap) → ring finalized at 10 → Halloran's murder by Drake's splinter faction → Drake's eclipse-night standoff → ritual succeeds despite sabotage and gunfire → dawn aftermath → council session → Eleanor/Ambrose genealogy reveal → town meeting → Denise/Odette honored → Ambrose's letter → finale, open Book 4 hook (Drake at large, other families exist).

## Continuity/voice/canon review log

✅ ch.1-45 fully reviewed, all real defects fixed (countdown bugs, one meta-leak, filler "kind of" instances, one ch.36 contradiction). Full detail in each chapter's git commit message.

## Repeated-words pass log

✅ ch.1-45 fully checked. Only 3 real fixes needed (ch.4, ch.8, ch.11) — everything else flagged by the mechanical report was earned repetition (chapter's actual subject) or ordinary prose frequency. Full detail in each chapter's git commit message.

## Pending / open items

1. **Hedge sweep — DONE (2026-09-18).** Re-checked the confirmed-instances table above against the live files: 8 of the 9 flagged lines had already been fixed by an earlier session (ch.4, 7, 12, 15, 18, 21, 26, 42 — clean). Only ch.24 still had the defect ("some old grief... some gap..." stacked in one sentence); fixed that one line only, and pushed the fix directly to GitHub. Borderline/judgment-call list (ch.3, 5, 16, 17, 23, 27, 30, 31, 32, 38, 40, 43, 44) deliberately left untouched per Zia's instruction not to over-polish — those are cosmetic and non-blocking per the standard above.

## KDP manuscript — DONE (2026-09-18)

Built a KDP-ready .docx: `What the Blood Remembers - Manuscript.docx`. Title confirmed as **"What the Blood Remembers"** (was sitting in `beat_map.md`'s own header the whole time — check that file for a title before asking Zia, it's usually already there). Author name: **Elif Kessler** (carried forward from Books 1 & 2, per Book 2's `PRE_PUBLISH_CHECKLIST.md`).

**Repo → manuscript workflow (repeat this for Book 4+):**
1. Zia downloads the whole repo as a zip from `github.com/aliwaziri10/Voxel` (green "Code" button → Download ZIP) and uploads it to Claude directly. This step is still needed because chat sessions don't auto-load repo state — but once uploaded, Claude DOES have live GitHub push/write access in this project via a connected GitHub tool (`get_file_contents` / `create_or_update_file` / `push_files`), confirmed working 2026-09-18 (this very commit). Don't assume no access — check by actually calling `get_file_contents` on the repo before telling Zia otherwise.
2. Claude unzips to a writable directory (`/mnt/user-data/uploads` is read-only, extract to `/home/claude/` instead), reads `novels/<book>/chapters/chapter_NN.md` for all chapters, strips the leading "CHAPTER X" line (regenerated, not reused, so numbering/formatting is controlled by the build script).
3. Build script: Node + the `docx` npm package. 6"×9" trim (8640×12960 DXA), Garamond 12pt body, justified, first-line indent (skip indent on each chapter's opening paragraph), chapter headings as "CHAPTER <SPELLED-OUT-NUMBER>" centered, page numbers centered in the footer starting at 1 on the first chapter page (front matter section has no page numbers — uses a separate docx `section` for this reason). Front matter built: title page, copyright page, "Also in the series" page listing Book 1 ("Where the Frost Doesn't Reach"), Book 2 ("What the Valley Still Owes"), Book 3.
4. Render to PDF (`soffice.py --convert-to pdf`) and `pdftoppm` to JPEGs to visually verify title page, a chapter-opening page, and the final page before handing off — catches page-numbering/margin/font issues before Zia sees them.
5. Committing back to GitHub: use the connected GitHub tool directly — `get_file_contents` (with `ref: refs/heads/main`) to get the current SHA, then `create_or_update_file` with that SHA to push the change. No manual copy-paste-in-browser step needed; this works from within the same session that did the editing.

Not yet done for Book 3: name-collision audit, real-person name check, back-cover blurb, cover image. Same open items Book 2 never finished either — worth doing before actual KDP upload, not required to generate the manuscript file itself.

## Proofreading — Last Verified
- Run: 2026-09-16, 45 chapters scanned, 99,892w, 0 hard violations.
- Full report: `novels/amity-falls-book-3/PROOFREAD_REPORT.md`
