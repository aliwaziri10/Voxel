# Voxel — Handoff

Read this first, then read `novels/amity-falls-book-4/PROOFED_LOG.md` —
that file, not this one, is the live source of truth for Book 4's
proofreading/canon state. This file is orientation only; it does not
duplicate canon facts, because those go stale and this one already had.

Read `novels/EDITORIAL_CHARTER.md` before touching any chapter.

Rule zero: verify against live `main` before claiming anything is missing,
done, or true. Read by commit SHA right after a push
(`raw.githubusercontent.com/aliwaziri10/Voxel/<sha>/<path>`) since a plain
`main` fetch can be briefly stale. Never trust a HANDOFF or log claim over
what the live chapter file actually says — this file has been wrong before.

## Where everything lives

Repo: `aliwaziri10/Voxel`. Upstream `Wazzaboyzz/Voxel` is stale, don't use it.

Published (frozen, never edited/scanned): `novels/where-the-frost-doesnt-reach/`,
`novels/amity-falls-book-2/`, `novels/amity-falls-book-3/` — all on `main`.

Book 4, "The Secret She Kept Forever," on `main`:
- `novels/amity-falls-book-4/chapters/chapter_01.md` .. `chapter_45.md` (complete)
- `novels/amity-falls-book-4/PROOFED_LOG.md` — **read this for current state,
  open questions, and what's decided vs. still needs Zia.**
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
truncated sentence).

**Josiah vs. Ambrose Whitlock is RESOLVED as of `e14a5fc` — do not reopen
this without a new chapter-text reading.** Chapter 3, the anchor chapter,
is unambiguous that Ambrose Whitlock (not Josiah) tried and failed in 1889
and hid the complete terms. Chapters 2, 6, 7, 12, 13, 15 have been reverted
to Ambrose and verified live. Chapter 14 already read Ambrose correctly
(separate earlier fix, `bfeee2c`). This question was decided wrong at least
twice before landing here — see PROOFED_LOG.md's top STAMP for the full
trail. **Chapter 9 is the one exception, deliberately left alone**: it
frames "Josiah Whitlock" as a distinct ancestor generations before Ambrose,
which may be correct as written or may be the same error in a different
shape — this needs a full read of ch.9 before anyone touches it (see
PROOFED_LOG.md, Q21). Do not treat ch.9 as evidence for reopening the
Ambrose question elsewhere; treat it as its own separate open item.

Five other structural questions were flagged for Zia; he delegated the
call, and those decisions are in the log along with two new open items
(Q21 above, Q22: Martha Whitlock's relation to Ambrose in ch.22, still
unfixed, still needs Zia).

## Rules for anyone working here

- Zia is a non-coder, browser-only, often by voice. Small steps, code
  blocks for anything copyable, decide technical calls yourself rather than
  asking him to check things.
- Before asserting any canon fact ("X tried the bargain," "Y is Z's
  grandmother"), read the actual chapter text yourself. This project's
  biggest recurring failure mode is confidently repeating an earlier
  session's conclusion without re-verifying it against the primary chapter
  text — this has happened at least twice now (Elena Castellano, and
  Josiah/Ambrose above). A prior fix landing in 7 chapters is not evidence
  it was right; it's evidence a prior session was confident.
- Published books are never edited, scanned, or padded.
- Never push a placeholder as content. After any push, re-fetch and compare.
- Never claim a fix is applied without reading it back from the repo.
- Update `PROOFED_LOG.md`, not this file, with new findings. Keep this file
  short — it should describe where to look, not carry the facts themselves.
