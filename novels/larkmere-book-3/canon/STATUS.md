# Keel and Comb: canon build status

Updated 2026-11-12.

- `canon/CANON_LOCK.md`: DONE.
- `canon/HEAT_LADDER.md`: DONE. The writer injects each chapter's line as its body target.
- `briefs/ch01.md` to `briefs/ch40.md`: see the commit log (written in two batches).
- `WRITER_COMMAND.md`, `VOICE_GUIDE.md`, `book_config.json`: DONE.
- Writer: `scripts/write_keel_and_comb.py` (wraps `scripts/write_warm_enough.py`, reuses its checks, swaps in this book's cast, places, locked lines and briefs). Pinned to the same free writer model.
- Workflow: `novels/larkmere-book-3/WORKFLOW_TO_PASTE.yml` must be pasted by Zia into `.github/workflows/write-keel-and-comb.yml` (the connector gets a 403 on workflow files).
- Chapters: none written. Check `chapters/` before trusting this line.
