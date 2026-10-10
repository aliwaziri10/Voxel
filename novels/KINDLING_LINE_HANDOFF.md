# KINDLING LINE HANDOFF (current, 2026-10-10)

The log is the source of truth: `novels/KINDLING_LINE_PROOFED_LOG.md`. Read it, then `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md`, then this file. Do not trust any summary, including this one. Re-fetch the log and the commit list before every write; several sessions edit the repo.

## Status
- Book 1 and Book 2: 45 of 45 stamped each (stamps in `novels/KINDLING_LINE_STAMPS_B1_B2.md`). Complete.
- Book 3: ch01 to ch15 stamped. Next: ch16 (fixes listed in the log under B3 TO FIX), then ch17 on in order.
- Before work, list `novels/kindling-line-book-3/chapters` with `fields: name, sha, size` and compare blobs to the log's stamps.

## What Zia wants
1. Check what other sessions did (log, handoff, commits) before acting. Never work from memory.
2. Fix facts and clear AI tells only. No cosmetic tweaks, no style passes. It should read as written by a human.
3. No chapter is left FLAGGED. Fix everything, then stamp.
4. Never reduce a file's size, and never pad. Replace leaked or pasted text with correct scene content that belongs in the chapter.
5. One chapter at a time. No em dashes or AI tells in anything you write.
6. Keep the log and this file short. Trim on every write. Stamp in batches (the tool cannot append, so each log write resends the whole file).
7. Work only inside the three Kindling Line books. Claim only checks done in the same turn.

## Still open for Zia (do not start without her word)
- Flags 16 and 17: Sol's mother (bound ward-taker in Book 2, paper-only in Book 1) and the Mara name clash.
- Final humanizer and proofreading pass over Book 2, then KDP. Build KDP from `chapters/`, not the old full_manuscript file.
- CANON_LOCK lists the smith as Corwin; Books 2 and 3 use Edmar. Update it.
