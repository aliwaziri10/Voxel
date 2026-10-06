# KINDLING LINE PROOFREAD HANDOFF

Written 2026-10-07 by Claude at Zia's request, before continuing the job. Update this file (do not replace it) whenever work closes. The stamp log is the source of truth for which chapters are done; this file says how to work and where it stands.

## Read order for any new session
1. `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md` (ten checks, scope, stamp rules).
2. `novels/KINDLING_LINE_PROOFED_LOG.md` (coverage, flags, locked facts, stamps).
3. This file.
Do not trust any summary, including this one, for the current state of the chapters. List the live folder and compare blob SHAs to the stamps.

## Zia's standing rules for this job
- Do not stop partway to ask questions. Do the work, and write a handoff entry before the session ends.
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
2. Read in full only the chapters the scan flags, plus the chapters needed to stamp in order.
3. Get blob SHAs for a whole book in one call by listing the chapters folder with the sha field, instead of opening each file.
4. Push only changed chapters, with the file's current blob SHA. The GitHub tool needs the full chapter content, so build the fixed file in the sandbox and print it once.
5. Stamp each chapter in the log right after finishing it.

## State at 2026-10-07 (Book 1)
- All 45 chapters of Book 1 were fetched live and scanned. Findings are in the log under SCAN NOTES.
- Fixed and stamped: ch.26 (whole chapter had been pasted twice; commit `09e03c582e82b59aab68eacd8ca19c9aeb88752b`), ch.11 (stray repeated last line; commit `5c7953aa8cd81ff6a0a0beacfa52297367425c10`).
- Not yet read in full: the other 43 chapters. The scan found nothing else structural in Book 1.
- Next in order: read the hedge-heavy and banned-word chapters (29, 30, 36, 39; "particular" in 16, 22, 28, 32, 41), fix only what reads as an AI tell, then read the rest in order and stamp.
- When Book 1 is fully stamped: write a BOOK 1 COMPLETE entry in the log and update `novels/kindling-line-book-1/00_READ_FIRST.md`, then start Book 2 chapter 1.

## Open flags for Zia (see the log for quoted lines)
Six flags: the ward's death told several ways, Sol's mother and Kael's father details, Auda Ashworth in Book 2, the father's fate between Books 1 and 2, the Reckoning day counts in Book 1 ch.09 vs ch.11, and the repeated chapter-ending formula.

## Book 3 reminder
Book 3 chapter 3 on GitHub still has the scene pasted twice, plan text spoken in dialogue, and an early reveal. Fix it when the pass reaches Book 3, after Books 1 and 2 are stamped.

## Known tooling limits
- Claude cannot edit files under `.github/workflows/` (access denied). Workflow changes are pasted in by Zia.
- The raw GitHub copy can lag a minute after a push. Confirm a push by reading the file through the GitHub tool.
- The scan script is a map only. It cannot judge voice, continuity, or whether a hedge word is a tell.
