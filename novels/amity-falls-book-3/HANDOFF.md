## STATUS: Book 3 complete, manuscript built (2026-09-18)

All editorial work is finished — proofreading, continuity/voice/canon review, repeated-words pass, and the hedge sweep are all DONE across ch.1-45 (only real fix left was ch.24, already pushed to GitHub). A KDP-ready manuscript file (`What the Blood Remembers - Manuscript.docx`) has been generated from these chapters. Nothing below is a blocker — it's reference only.

## Repo → manuscript workflow (repeat this for Book 4+)

1. Zia downloads the whole repo as a zip from `github.com/aliwaziri10/Voxel` (green "Code" button → Download ZIP) and uploads it to Claude directly.
2. Claude has live GitHub read/write access in this project via a connected tool (`get_file_contents` / `create_or_update_file` / `push_files`) — confirmed working. Use it directly for any repo edits; don't assume it's unavailable.
3. Claude unzips the upload to a writable directory (`/mnt/user-data/uploads` is read-only — extract to `/home/claude/` instead), reads `novels/<book>/chapters/chapter_NN.md` for all chapters.
4. Manuscript build: Node + the `docx` npm package. 6"×9" trim, Garamond 12pt body, justified, first-line indent, "CHAPTER <NUMBER>" headings, page numbers starting at 1 on the first chapter page, front matter (title page, copyright page, series list).
5. Render to PDF and check a few pages visually before handing off.
6. To push any file changes back: `get_file_contents` (ref: `refs/heads/main`) for the current SHA, then `create_or_update_file` with that SHA.

## Locked facts (for Book 4+ consistency)

- Word floor: 1,900-2,700w/chapter for Book 3 (Book 4+ uses the charter's 2,300w standard instead).
- No em dashes. Zero "particular" anywhere.
- Voice: Mara dry/engineering-metaphor, Caleb steady/plainspoken, Wren blunt/fast-talking, Priya procedural, Dev hardening through the climax then softening post-eclipse. Caleb and Mara are married.
- Eleanor/Ambrose genealogy resolved ch.42-45: Eleanor was Ambrose's wife, widowed 1945, remarried Samuel 1947, had a child with Ambrose before his death — Dev and Priya are their grandchildren. Left as an intentional unstated-but-consistent detail, not spelled out in one line.

## Story summary

Sequel to Book 2. Dev (Priya's brother) inherits a hereditary Whitlock-line hunger, triggered by direct contact with Book 2's well ritual. A hidden "quiet family" faction wants it to complete rather than be stopped; splinter leader Corwin Drake leads violent opposition in Act Three. Six-week countdown to the autumn eclipse. Resolves fully: a ten-person ring redistributes what Dev carries at the eclipse-night ritual despite Drake's armed interference; Dev survives whole. Ends on an open Book 4 hook (Drake at large, other Whitlock-line families exist elsewhere). Full chapter-by-chapter beat breakdown lives in `beat_map.md`.

## Not yet done (before actual KDP upload)

Name-collision audit, real-person name check, back-cover blurb, cover image. Same open items Book 2 never finished either.

## Proofreading — Last Verified
- Run: 2026-09-16, 45 chapters scanned, 99,892w, 0 hard violations.
- Full report: `novels/amity-falls-book-3/PROOFREAD_REPORT.md`
