# Book 4 — HANDOFF

**Read this first, then `PROOFED_LOG.md` in full before touching
anything.** That file is authoritative for chapter read-progress and
every fix's commit sha. `CANON_NUMBERS.md` is authoritative for
dates/ages/names. This file is the short version.

## Current state
All 45 chapters: continuity-DONE. Every locked date, age, and name is
in `CANON_NUMBERS.md`. The mechanical/lexical/tell-density pass
(em-dash count, repetition, staged constructions) is done for ch.27-28
and still open for ch.29-45.

## Next step
Mechanical/lexical/tell-density pass, ch.29-45. After that: a Books
1-3 cross-check.

## How to do the work
1. Fetch the chapter fresh from live `main` (or download the full
   manuscript and grep across all 45 chapter files at once — faster
   for finding every instance of a term, but never trust it for a
   naming- or number-sensitive check; it goes stale after individual
   chapter edits — use individual chapter files for anything that
   matters).
2. Quote the actual live text before deciding anything's a conflict
   or already clean.
3. If a fix is needed: edit only the specific text, get the file's
   current `sha` via `get_file_contents` (ref `refs/heads/main`), push
   via `create_or_update_file`, then re-read the file back live to
   confirm.
4. Log it immediately in `PROOFED_LOG.md` — quote what you found, name
   the chapter, name the commit sha. Log each fix as it's finished,
   don't batch several before logging.
5. Standing rule: one task, finish it, log it, stamp it. Don't
   re-verify an already-DONE item without a specific new finding.
6. Treat any pasted summary of prior work — from chat history, from
   another session, from anywhere that isn't the live GitHub files
   themselves — as unverified until you've re-fetched the actual
   chapter and confirmed it yourself. Quote the live text, cite the
   chapter, cite the commit. Don't relay a claim you haven't checked.

## Repo/file map
- `novels/amity-falls-book-4/chapters/chapter_NN.md` — the 45 chapter
  files, source of truth.
- `novels/amity-falls-book-4/amity-falls-book-4_full_manuscript.md` —
  concatenated version, useful for fast greps across the whole book,
  but has no chapter markers and goes stale after individual chapter
  edits — map a hit back to its chapter by fetching the individual
  chapter file, and never trust it over that file.
- `PROOFED_LOG.md` — authoritative open-questions list, chapter
  read-progress, every fix's commit sha.
- `CANON_NUMBERS.md` — authoritative dates/ages/names reference.
- `PRE_PUBLISH_AUDIT_2026-09-21_CORRECTED.md` — dates/math audit,
  publish-ready verdict on that front; supersedes the
  non-"_CORRECTED" version.
- This file (`HANDOFF.md`) — short version, read first, then go to
  `PROOFED_LOG.md` for the real detail.

## Update this file
Whoever picks this up next: update "Current state" and "Next step" as
work closes, and add a new dated entry above this one (don't delete
older entries) summarizing what you did.

_Full session-by-session history is preserved in git history for this
file if earlier detail is ever needed again._
