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
truncated sentence). Six structural questions were flagged for Zia; he
delegated the call. Five were decided and are in the log; **one (Josiah
vs. Ambrose Whitlock — who tried to end the bargain and hid the terms) was
decided wrong once already** on a re-read of chapters 3, 9, 17, 21, and was
corrected mid-session (see log, "CORRECTION"). **As of this handoff it is
being corrected a SECOND time**: chapter 3, the anchor chapter, is
unambiguous that **Ambrose Whitlock** (not Josiah) tried and failed in 1889
and hid the complete terms — this was verified by directly reading chapter
3's text, not by trusting the existing fix cascade. Chapters 2, 6, 7, 9, 12,
13, 15 currently say "Josiah" for this and are now believed to be WRONG,
not chapter 3. **No chapter text has been touched for this reversal yet** —
only the log has been updated. This is the single most important thing for
whoever picks this up next: do not add more "Josiah" fixes, and do not trust
earlier sessions' confidence on this question. Reverting the 7 chapters
back to Ambrose is the next concrete task; it has not been started.

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
