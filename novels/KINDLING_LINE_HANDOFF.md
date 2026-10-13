# KINDLING LINE HANDOFF (current, 2026-10-13)

The log is the source of truth: `novels/KINDLING_LINE_PROOFED_LOG.md`. Read it, then `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md`, then this file. Do not trust any summary, including this one. Re-fetch the log and the commit list before every write; several sessions edit the repo.

## Status
- Book 1, Book 2 and Book 3: 45 of 45 stamped each. Proofread pass complete for all three (Book 3 ch42 to 45 stamped 2026-10-13). Stamps: Books 1 and 2 in `novels/KINDLING_LINE_STAMPS_B1_B2.md`, Book 3 in the log.
- Before any further work, list `novels/kindling-line-book-3/chapters` with `fields: name, sha, size` and compare blobs to the log's stamps. A stamp is void if the blob changed. On 2026-10-13 14:50 IST the void ones were ch01, ch02, ch03, ch05, ch06, ch34, ch35 (marked VOID in the log; not yet re-read).
- First check `get_me`: the chat's GitHub connector was once logged in as adrian001234 (403 on every write). It must say aliwaziri10.

## ZIA ORDER 2026-10-13: BRING SMALL B3 CHAPTERS TO THE FLOOR
- Floor = 2,300 words per chapter (`CANON_LOCK.md` line 20; beat maps say 2,300 to 2,700). This order overrides the charter line that Book 3 chapters are not to be padded up to a floor. Real sub-beats from each chapter's beat map and romance entry only, no padding, no new named characters, no invented plot.
- Chapters and words before: ch02 2,263; ch03 1,000; ch04 1,741; ch07 1,732; ch09 1,809; ch10 1,638; ch41 2,137.
- Progress: ch02 done (ea9e6a1); ch03 done (c857899a, blob 77ffdae5, STAMP PENDING: ch03 needs a read and a stamp, the old stamp is void); ch04 done and stamped; ch07 done (40b8c60d, stamped); ch09 done (c2434943, stamped); ch10 done (5f776867, stamped); ch41 done (e01c033d, stamped). All the floor-order chapters are now at or above 2,300 words. ch02 stamp is void too (needs a read and a stamp).
- After each chapter: re-fetch, check word count (`wc -w` on the raw file by commit SHA), banned-word scan, size not below before, new stamp in the log.

## What Zia wants
1. Check what other sessions did (log, handoff, commits) before acting. Never work from memory.
2. Fix facts and clear AI tells only. No cosmetic tweaks, no style passes. It should read as written by a human.
3. No chapter is left FLAGGED. Fix everything, then stamp.
4. Never reduce a file's size, and never pad. Replace leaked or pasted text with correct scene content that belongs in the chapter.
5. One chapter at a time (she has allowed three or four at a time when she says so). No em dashes or AI tells in anything you write.
6. Keep the log and this file short. Trim on every write. Stamp in batches (the tool cannot append, so each log write resends the whole file).
7. Work only inside the three Kindling Line books. Claim only checks done in the same turn. Continue without asking permission.

## Still open for Zia (do not start without her word)
- Flags 16 and 17: Sol's mother (bound ward-taker in Book 2, paper-only in Book 1) and the Mara name clash.
- Final humanizer and proofreading pass over Book 2, then KDP. Build KDP from `chapters/`, not the old full_manuscript file.
- CANON_LOCK lists the smith as Corwin; Books 2 and 3 use Edmar. Update it.
