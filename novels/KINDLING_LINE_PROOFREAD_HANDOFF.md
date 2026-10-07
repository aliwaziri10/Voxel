# KINDLING LINE PROOFREAD HANDOFF

Written 2026-10-07 by Claude at Zia's request; state section updated the same day. Update this file (do not replace it) whenever work closes. The stamp log is the source of truth for which chapters are done; this file says how to work and where it stands.

## Read order for any new session
1. `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md` (ten checks, scope, stamp rules).
2. `novels/KINDLING_LINE_PROOFED_LOG.md` (coverage, decisions D1 to D7, flags, locked facts, stamps for Book 1 ch01 to ch26).
3. `novels/KINDLING_LINE_STAMPS_B1_CH27_ON.md` (stamps and decisions D8 onward for Book 1 ch27 and later).
4. This file.
Do not trust any summary, including this one, for the current state of the chapters. List the live folder and compare blob SHAs to the stamps.

## Zia's standing rules for this job
- Do not stop partway to ask questions. Do the work, and write a handoff entry before the session ends.
- Zia gave the proofreading session full liberty on Book 1 (2026-10-07): decide, apply, log. Do not stop for approval.
- Do not overcorrect. Fix only what a reader would feel. Chapter length is not a defect.
- No AI tells, no AI takes; it must read human-written. Details must match across all three books.
- Work in order: Book 1, then Book 2, then Book 3, chapter by chapter.
- Work only inside the three Kindling Line books. Do not read, mention or edit any other series.
- Anything Zia must copy goes in its own code block with the full link or path. No find-and-replace snippets: when Zia must paste, give the full file.
- Only claim a check that was done in the same turn.

## Token-saving method (use this, it works)
1. Run the scan script to download the whole book to the sandbox and map every chapter in one pass:
```
python3 scripts/kindling_scan.py 1
```
(In a fresh sandbox, fetch the script first from `https://raw.githubusercontent.com/aliwaziri10/Voxel/main/scripts/kindling_scan.py`. The book number is 1, 2 or 3. The chapters land in `/tmp/kl_book<N>/`.)
2. Read in full only the chapters you are about to stamp, in order. Apply edits to a local copy with a one-match check, push with push_files, then fetch the immutable commit URL `raw.githubusercontent.com/aliwaziri10/Voxel/<commit sha>/...`, diff it against the local copy and compute the blob SHA with sha1("blob <len>\0" + bytes).
3. Get blob SHAs for a whole book in one call by listing the chapters folder with the sha field, instead of opening each file.
4. Stamp each chapter right after finishing it. The main log is about 67 KB and costs a full re-push for every edit, so new stamps go in the small stamps file above until a session merges them.

## State at 2026-10-07 (Book 1)
- Stamped and matching live: ch01 to ch26 (log) and ch27 (stamps file). Next in order: ch28.
- The scan found Book 2 structurally clean (no duplicates, no dashes, no leaked text). Book 3 has the known damage (ch02 to ch04 and ch06 copied text, leaked "Ch.N" text, many dashes); fix when the pass reaches it.
- Ch28 onward is expected to carry the same ward-death inconsistency that ch27 had (see D8): ch28 opens with the "Gathering Square disaster". Check ch28, 29, 30, 32, 38 and 43 against D8.
- When Book 1 is fully stamped: write a BOOK 1 COMPLETE entry in the log, update `novels/kindling-line-book-1/00_READ_FIRST.md`, then start Book 2 chapter 1.

## Open flags for Zia
See the log's FLAGS section (29 flags at last count). None blocks the pass; decisions under the liberty grant are logged as D-numbers.

## Book 3 reminder
Book 3 chapter 3 on GitHub still has the scene pasted twice, plan text spoken in dialogue, and an early reveal. Fix it when the pass reaches Book 3, after Books 1 and 2 are stamped.

## Known tooling limits
- Claude cannot edit files under `.github/workflows/` (access denied). Workflow changes are pasted in by Zia.
- The raw GitHub copy can lag a minute after a push. Confirm a push by reading the file through the GitHub tool or the immutable commit URL.
- The scan script is a map only. It cannot judge voice, continuity, or whether a hedge word is a tell.
