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
state.**

## ⚠️ TRUST WARNING — read this before believing ANY "DONE"/"FIXED"/"CLOSED"
## marker anywhere in this project, including in this file

On 2026-09-22, across a single day, this project accumulated MULTIPLE
confirmed cases of status markers that did not match live chapter text:

1. `PROOFED_LOG.md` marked ch.31 "FIXED — rupture-scene insert (commit
   0963500)". That commit does not exist in the repo (404 on direct
   lookup). The chapter had never been touched.
2. The same log marked ch.32 "clean" and ch.33 "clean." Both, read live,
   contained a plot mechanism (who took Harriet Marsh's memory) that
   directly contradicted the "Kettering" mechanism used in five other
   chapters, including the ch.38 courtroom scene. Neither had been fixed.
3. ch.45's "Wren had already paid one large debt" fix, made and verified
   earlier the same day, was found REVERTED back to "Wren had never paid
   a large debt" later that same day — with no record of who reverted it
   or why.
4. This very file's previous revision claimed "the ch.31 rupture-vs-ch.19
   duplicate" was closed. It was never ch.19 — it was ch.31 vs. ch.32 —
   and it was not closed at the time that claim was written.

None of these were caught by re-reading the log. All four were caught
only by fetching the live chapter file and reading it directly, then
checking cited commit hashes against the actual repo. **A status word in
any file — including this one — is a claim, not a fact.** Multiple
sessions have worked this project in parallel across long gaps (10+
hours between some sessions), and edits have been silently lost or
overwritten at least once. Before telling Zia something is ready to
publish, independently re-verify by reading live text — do not chain
trust through a log entry, however confident or detailed it reads.

## Current state, as of the session ending 2026-09-22 (this handoff)

**Five real contradictions were found and fixed this session, each
independently verified by TWO separate reasoning threads that cross-
checked each other's work by reading live chapter text directly (not
by trusting either thread's summary):**

| Ch | What was wrong | Fix | Commit | Independently re-verified |
|---|---|---|---|---|
| 33 | Elena confessed to personally redirecting the toll onto Harriet — contradicted the Kettering mechanism used in 5 other chapters | Rewritten: Elena knew about Kettering/Drake and concealed it, rather than having acted herself | `c657d22` | Yes — live text fetched and diffed after push |
| 34 | Theo told Harriet Drake personally extracted her memory, no Finder involved | Rewritten: Drake coerced Kettering into doing it | `f40a696` | Yes |
| 45 | "Wren had never paid a large debt" — contradicted ch.24's grandmother's-face debt | Rewritten to acknowledge it | `064f17e` | Yes, then found reverted, then re-verified fixed again — see warning above |
| 32 | Ended in Theo leaving for Millbrook permanently + a two-volume publication split — directly contradicted ch.31's full reconciliation, which ch.34 depends on | Ending reworked: the fight is interrupted, unresolved but together, setting up ch.31 as the next morning's resolution. Dev's evidence-log content (load-bearing for ch.38) untouched | `9d88668` | Yes |
| 31 | (No change — confirmed as the version to KEEP, since ch.34 depends on its reconciliation having happened) | — | — | — |

Kettering (a coerced Millbrook Finder) is now the single, consistent
account of what happened to Harriet Marsh, appearing in ch.4, 11, 21, 33,
34, 35, 38. No chapter should ever again say Drake acted alone, or that
Wren's mother personally redirected the toll.

**Everything else in this project's various logs and canon files —
including claims that all 45 chapters are "DONE," that Josiah/Ambrose is
fully resolved, that specific Q-numbered items are "CLOSED" — should be
treated as unverified by this session.** We verified exactly five
chapters (31, 32, 33, 34, 45) by direct read this session. We did not
re-check the other 40 chapters, or re-verify any older "closed" item,
against live text. Given the trust warning above, do not assume those are
safe just because a file says so.

## Before publishing

Given the pattern above, recommend one dedicated pass before Zia
publishes anything: pick every chapter marked DONE/FIXED/CLOSED anywhere
in this project's files, and for each one, fetch the live chapter text
and confirm the specific claim against it — not against another log
entry. This doesn't need to re-litigate plot judgment calls, just confirm
that claimed edits are actually present in the file Zia will publish.
Given how many false-positive "DONE" markers have already surfaced, treat
an unverified DONE as equivalent to NOT DONE until checked.

## Where everything lives

Repo: `aliwaziri10/Voxel`. Upstream `Wazzaboyzz/Voxel` is stale, don't use it.

Published (frozen, never edited/scanned): `novels/where-the-frost-doesnt-reach/`,
`novels/amity-falls-book-2/`, `novels/amity-falls-book-3/` — all on `main`.

Book 4, "The Secret She Kept Forever," on `main`:
- `novels/amity-falls-book-4/chapters/chapter_01.md` .. `chapter_45.md` (complete)
- `novels/amity-falls-book-4/PROOFED_LOG.md` — open editorial questions,
  read-progress, what's decided vs. still needs Zia. **Treat any DONE/
  CLOSED marker as unverified per the warning above unless you personally
  re-check it.**
- `novels/amity-falls-book-4/CANON_NUMBERS.md` — reference for dates,
  ages, and names. Same caveat applies.
- `novels/amity-falls-book-4/architecture.md`, audit files,
  `PROOFREAD_REPORT.md`, `amity-falls-book-4_full_manuscript.md`
  (concatenation file — has been observed stale relative to individual
  chapter files before; never trust it over the individual chapter file)
- `scripts/book4_fixes.json`, `scripts/proofread_novel.py`
- `story_bibles/amity-falls.json`

Other: `novels/kindling-line-book-1/` (separate series, don't mix in).

## Rules for anyone working here

- **Read all four files listed at the top before touching a chapter.**
- **Independently re-verify any "DONE" claim by fetching live chapter
  text before relying on it or repeating it to Zia** — see the trust
  warning above. This is now the single most important rule in this
  file, ahead of any specific canon fact.
- Zia is a non-coder, browser-only, often by voice. Small steps, code
  blocks for anything copyable, decide technical calls yourself — except
  genuine plot/structure decisions (cutting or rewriting a chapter's
  ending, choosing between two canon versions), which are his call.
- Before asserting any canon fact, read the actual chapter text yourself
  AND check `CANON_NUMBERS.md`. Do not chain trust through a prior
  session's summary.
- Published books are never edited, scanned, or padded.
- Never push a placeholder as content. After any push, re-fetch and compare.
- Never claim a fix is applied without reading it back from the repo,
  and re-check it again later in the same session if you're about to
  tell Zia it's safe to publish — fixes have been observed reverting
  silently within the same day.
- Update `PROOFED_LOG.md` and `CANON_NUMBERS.md`, not this file, with new
  findings. This file is a summary, re-synced when the log's top-level
  status changes — it is not itself a source of new facts.
