# Book 4 — HANDOFF (2026-09-22, end of session)

**Read this first, then read `PROOFED_LOG.md` in full before touching
anything.** That file is authoritative for open questions, chapter
read-progress, and every fix's commit sha. `CANON_NUMBERS.md` is
authoritative for dates/ages/names. This file is just the short version:
what happened this session, what's still open, what to do next.

## Critical warning — do not repeat this session's mistake
A pasted, unsourced transcript fragment claimed Q4, Q7, Q8, Q11 were all
already closed, with specific-sounding detail ("Q7 is answered — Elena
is a retired baker," "Q4 confirmed: this closes"). **That transcript did
not describe this book.** There is no character named "Elena" anywhere
in Book 4's live text. Q4 and Q7 were still open. Treat any pasted
summary of prior work — from chat history, from another session, from
anywhere that isn't the live GitHub files themselves — as unverified
until you've re-fetched the actual chapter and confirmed it yourself.
This session's rule, and the next session's rule: **quote the live text,
cite the chapter, cite the commit. Don't relay a claim you haven't
checked.**

## What THIS session actually did (verified, not relayed)
- **Q8 (Harriet's home terminology) — FIXED.** Ch.9 (2 instances) and
  ch.22 (1 instance) said "nursing home"; ch.4, ch.30, ch.34, ch.41
  already said "assisted living facility" (ch.41 names it "Willow Creek
  Assisted Living"). Standardized ch.9 and ch.22 to match. Commits
  `e48fdeb` (ch.9), `990a104` (ch.22). Both pushed to `main`, read back
  live to confirm the exact wording landed. Closed.
- **Q11 (two "Silas" characters) — verified genuinely clean, no fix
  needed.** Downloaded the full manuscript, grepped for "Silas," found
  exactly two: Silas Kettering (coerced Millbrook Finder, Dev's dialogue,
  ch.5 area) and Silas Harker (the Weather who held the 2003 wind debt,
  ch.37/38 area — text itself says "Not Old Man Harker, who was alive
  and difficult"). Already distinguished on the page. Closed.
- Both fixes logged in `PROOFED_LOG.md` with quotes and commit shas —
  read that file's "Q8" and "Q11" entries for the full evidence trail,
  not just this summary.

## Still genuinely open — pick up here next
In priority order (matches `PROOFED_LOG.md`'s own "NEXT STEPS" line):
1. **Q4 — ch.5 unreliable/anachronistic (Ambrose alive 2005-2009).**
   Not touched this session. Fetch ch.5 fresh from live `main`, quote
   the actual anachronistic line(s), decide fix vs. no-fix, log it the
   way Q8/Q11 were just logged (quote + commit sha), don't guess.
2. **Q7 — Wren's mother's job.** Not touched this session. Grep all 45
   live chapters for mentions of Wren's mother's occupation, quote what
   you find, log the result.
3. **Q2** (Drake's 2005 Millbrook target), **Q3** (Adelaide/Ambrose
   relationship — do NOT guess, needs Zia's input, a prior pass tried
   and had to revert it), **Q5** (lineage roster), **Q6 remainder**
   (season/calendar progression across all 45 chapters — needs Zia's
   specific date decisions), **Q10** (Archive building has 3+ competing
   physical descriptions), **Q12** (spaced hyphens as em-dash
   substitutes, general sweep), **Q14** ("the house on the ridge"),
   **Q15/Q16** (self-contained threads, lower priority), **Q18** (Theo's
   age: 26 stated vs. 27 by birth-year math, low priority).
4. Genuine fresh sequential read of ch.1-45: **IN PROGRESS**, only
   ch.1-3 done so far (see `PROOFED_LOG.md`'s top section). Continue at
   ch.4.
5. After the open-question list and the fresh read: Books 1-3
   cross-check, and the ch.27-45 mechanical/lexical/tell-density pass
   (em dashes, repetition, staged constructions) — never done for that
   stretch, only the continuity read was.

## How to do the work (the method that's been working)
1. Fetch the chapter fresh from live `main` (or download the full
   manuscript with `curl` from `raw.githubusercontent.com` and `grep`
   across all 45 chapter files at once — faster for finding every
   instance of a term). Don't trust GitHub's code-search index; it lags
   or returns zero hits on this repo for reasons that were never fully
   diagnosed this session.
2. Quote the actual live text in your reasoning before deciding
   anything's a conflict or already clean.
3. If a fix is needed: edit only the specific text, get the file's
   current `sha` via `get_file_contents` (ref `refs/heads/main`), push
   via `create_or_update_file`, then re-read the file back live to
   confirm.
4. Log it immediately in `PROOFED_LOG.md` — quote what you found, name
   the chapter, name the commit sha, move the item from "Open questions"
   to "Decisions locked" or a dated entry. Don't batch several fixes
   before logging; log each one as it's finished, the way Zia has asked
   for directly this session.
5. Zia's explicit standing instruction this session: "one task, finish
   it, log it, stamp it" — don't re-verify the same closed item
   repeatedly, don't let unlogged work pile up.

## Repo/file map
- `novels/amity-falls-book-4/chapters/chapter_NN.md` — the 45 chapter
  files, source of truth.
- `novels/amity-falls-book-4/amity-falls-book-4_full_manuscript.md` —
  concatenated version, useful for fast greps across the whole book, but
  has no chapter markers — map a hit back to its chapter by fetching
  individual chapter files, not by line-counting the concatenation.
- `PROOFED_LOG.md` — authoritative open-questions list, chapter
  read-progress, every fix's commit sha. Read in full before starting.
- `CANON_NUMBERS.md` — authoritative dates/ages/names reference.
- `PRE_PUBLISH_AUDIT_2026-09-21_CORRECTED.md` — dates/math audit,
  publish-ready verdict on that front specifically; supersedes the
  non-"_CORRECTED" version, which contained unverified claims.
- This file (`HANDOFF.md`) — short version, read first, then go to
  `PROOFED_LOG.md` for the real detail.

## Update this file
Whoever picks this up next: update the "Still genuinely open" section
as items close, and add a new dated entry above this one (don't delete
this session's entry) summarizing what you did, the same honest,
quote-and-cite way this session did it.
