# Voxel — Handoff

## READ-BEFORE-WRITE RULE (do not remove or soften)
**Before touching ANY chapter, read ALL FOUR of these files in full, in
this order:**
1. This file (`HANDOFF.md`) — orientation only.
2. `novels/EDITORIAL_CHARTER.md` — methodology, applies to every Voxel book.
3. `novels/amity-falls-book-4/PROOFED_LOG.md` — live source of truth for
   open editorial questions and read-progress.
4. `novels/amity-falls-book-4/CANON_NUMBERS.md` — the single reference for
   every date, age, and name in this book.

**Do this even if you are resuming mid-task and think you already know the
state.** This rule exists because on 2026-09-22, this project had TWO
separate canon-numbers files (`CANON_NUMBERS.md` and a now-deleted
`DATES_BIBLE.md`) that silently disagreed with each other on a plot-level
fact (whether "Josiah Whitlock" was a real character or a naming error).
Three different sessions read only a subset of the available sources —
one chapter, or one of the two files — and each produced a different
confident, wrong-in-a-different-way answer. The fix wasn't "read more
carefully," it was "read every source every time," because the conflict
lived in the disagreement between sources, not inside any single one.
The two files have since been merged into one (`CANON_NUMBERS.md`) and the
question is resolved — see that file's Josiah/Ambrose entry — but the
same failure mode can recur on a different question if this rule is
skipped. If you ever find two files, or a file and the live chapter text,
disagreeing again: do not pick a winner. Stamp `PROOFED_LOG.md` with the
exact conflicting lines and leave everything else untouched until Zia
decides.

Rule zero (unchanged): verify against live `main` before claiming anything
is missing, done, or true. Read by commit SHA right after a push
(`raw.githubusercontent.com/aliwaziri10/Voxel/<sha>/<path>`) since a plain
`main` fetch can be briefly stale. Never trust a HANDOFF, log, or canon
claim over what the live chapter file actually says — every one of these
files has been wrong before, including this one, more than once. This
file itself went stale again on 2026-09-22 (its "Current state" section
listed the kiss mismatch, ch.21 arrest, and Martha Whitlock's relation as
still open, after `PROOFED_LOG.md` had already closed all three) — synced
below, but treat that as a live risk, not a one-time fix.

## Where everything lives

Repo: `aliwaziri10/Voxel`. Upstream `Wazzaboyzz/Voxel` is stale, don't use it.

Published (frozen, never edited/scanned): `novels/where-the-frost-doesnt-reach/`,
`novels/amity-falls-book-2/`, `novels/amity-falls-book-3/` — all on `main`.

Book 4, "The Secret She Kept Forever," on `main`:
- `novels/amity-falls-book-4/chapters/chapter_01.md` .. `chapter_45.md` (complete)
- `novels/amity-falls-book-4/PROOFED_LOG.md` — open editorial questions,
  read-progress, what's decided vs. still needs Zia.
- `novels/amity-falls-book-4/CANON_NUMBERS.md` — **the single reference**
  for every date, age, and name. (Previously split across two files that
  disagreed with each other; merged 2026-09-22. Do not create a second
  canon-numbers file — add to this one.)
- `novels/amity-falls-book-4/architecture.md`, `PRE_PUBLISH_AUDIT_2026-09-21*.md`,
  `PROOFREAD_REPORT.md` (last auto-regenerated 2026-09-22 11:03 UTC, report
  content only, no chapter touched), `amity-falls-book-4_full_manuscript.md`
- `scripts/book4_fixes.json`, `scripts/proofread_novel.py` (mechanical fixer;
  see the log for how exact-text fixes are applied — old/new pairs, applies
  once, skips silently if already applied)
- `story_bibles/amity-falls.json`

Other: `novels/kindling-line-book-1/` (separate romantasy series, don't mix
with Amity Falls).

## Current state (see PROOFED_LOG.md for full detail — this is a summary)

**Synced 2026-09-22 against live PROOFED_LOG.md — do not let this section
drift again; update it every time the log's top-level status changes.**

Four major conflicts are now CLOSED and fixed live (see log for exact
commits): Drake's arrest (ch.41 is canon, ch.21/25/26/34/39/40 all match
it now), the ch.20 timeline reset, the ch.31 rupture-vs-ch.19 duplicate,
and the three-way kiss chronology (ch.17 first, ch.21 second/interrupted,
ch.26 deepest-commitment). Also closed: Q1 (grandmother's death age,
standardized to fourteen), Q13 (Denise's granddaughter's-husband line was
already correct), Q17 (Martha Whitlock is Ambrose's daughter, confirmed
book-wide, no conflicting reference exists anywhere).

Josiah vs. Ambrose Whitlock is **resolved**: two distinct people, both
real, both intentional, independently reconfirmed four separate times
(ch.2, 3, 9, 15, 18, 21 all agree) — see `CANON_NUMBERS.md`. Do not reopen
without a fresh read of ch.2, 3, 9, and 15 together plus that file's entry.

A genuinely fresh, start-to-finish sequential read (fetched live, not from
memory or a prior session's summary) is IN PROGRESS: ch.1-3 done this
pass, all clean. Ch.1-10 currently claimed — check `PROOFED_LOG.md`'s
claim line before starting ch.4+ to avoid duplicate work. An EARLIER
session's claim of "full sequential read ch.1-45 complete" was itself
downgraded mid-session to "not independently verified, treat as
hypothesis" — most of ch.4-45 has real fixes and targeted re-reads behind
it (see the log's "Fixed and locked" section, chapter by chapter), but has
not had this fresh line-by-line pass yet.

Open items needing Zia, in priority order: Q2 (Drake's 2005 Millbrook
target — three accounts, may be compatible), Q3 (Adelaide's exact
relationship to Ambrose — a prior pass tried guessing and reverted it, do
not guess again), Q6 (season/calendar progression across the full 45
chapters), Q10 (Archive building has 3+ competing descriptions). Full list,
including the lower-priority Q4/Q5/Q7/Q8/Q11/Q12/Q14-Q16/Q18-Q20, is in
`PROOFED_LOG.md`.

## Rules for anyone working here

- **Read all four files listed at the top before touching a chapter.**
- Zia is a non-coder, browser-only, often by voice. Small steps, code
  blocks for anything copyable, decide technical calls yourself rather than
  asking him to check things — except genuine two-source canon conflicts,
  which are his call, not a technical decision.
- Before asserting any canon fact, read the actual chapter text yourself
  AND check `CANON_NUMBERS.md`. Repeating an earlier session's conclusion,
  or one file's claim, without cross-checking is this project's biggest
  recurring failure mode — it has now happened at least three times on one
  question alone.
- Published books are never edited, scanned, or padded.
- Never push a placeholder as content. After any push, re-fetch and compare.
- Never claim a fix is applied without reading it back from the repo.
- Update `PROOFED_LOG.md` and, for dates/ages/names, `CANON_NUMBERS.md` —
  not this file — with new findings. This file's "Current state" section
  is a summary that must be re-synced whenever the log's top-level status
  changes (see above) — it is not itself a source of new facts.
