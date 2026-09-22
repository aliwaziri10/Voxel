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
files has been wrong before, including this one, more than once.

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
  `PROOFREAD_REPORT.md`, `amity-falls-book-4_full_manuscript.md`
- `scripts/book4_fixes.json`, `scripts/proofread_novel.py` (mechanical fixer;
  see the log for how exact-text fixes are applied — old/new pairs, applies
  once, skips silently if already applied)
- `story_bibles/amity-falls.json`

Other: `novels/kindling-line-book-1/` (separate romantasy series, don't mix
with Amity Falls).

## Current state (see PROOFED_LOG.md for full detail — this is a summary)

Sequential real read: chapters 1–26 done. 27–45 not yet read. Several
mechanical fixes applied and verified live (ages, names, an em dash, a
truncated sentence, custody-status wording).

Josiah vs. Ambrose Whitlock is **resolved**: two distinct people, father
and son, both real, both intentional — see `CANON_NUMBERS.md`. Do not
reopen without a fresh read of ch.3 and ch.9 together plus that file's
entry.

Open items needing Zia, in priority order: the three-way kiss mismatch
(ch.17/21/26), Drake's ch.21 motel arrest (contradicts the ch.41 arrest
that's actually canon), Martha Whitlock's relation to Ambrose (ch.22), the
calendar/season inconsistency across the back half of the book. Full list
in `PROOFED_LOG.md`.

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
  not this file — with new findings. Keep this file short: it describes
  where to look, it doesn't carry the facts themselves.
