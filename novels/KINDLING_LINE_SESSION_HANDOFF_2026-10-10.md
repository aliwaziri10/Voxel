# KINDLING LINE SESSION HANDOFF (2026-10-10)

Short version. The log is the source of truth: `novels/KINDLING_LINE_PROOFED_LOG.md`. Read it, then `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md`, then this file. Re-fetch the log before every write; several sessions edit it.

## Status
- Book 1: 45 of 45 stamped. Book 2: 45 of 45 stamped. Book 3: 0 of 45, not started.
- Last log commit: `3efce072`. Last Book 2 fix commit: `6d9426e6`.
- Before any work: list `novels/kindling-line-book-N/chapters` with `fields: name, sha, size` and compare each blob to the STAMPS lines.

## What I did
- Book 1: proofread and stamped ch23 to ch25 and ch35 to ch39 (commits `941e9920`, `61a592a0`, `e9a712a9`, `90345efc`). Added decision D20 (Kael keeps the auditor's bench until the Reckoning ends).
- Book 2 leftovers (`6d9426e6`): ch37 Tam no longer the 10 Cinderveil signer; ch40 four-house arithmetic fixed; twelfth house named House Ostrand (ch40, ch42, ch43); ch43 plants Kael's grandmother before ch44.
- Restamped Book 2 ch36, 37, 40, 41, 42, 43. Closed flags 15, 18, 20, 21.
- Wrote `KINDLING_LINE_SESSION_HANDOFF_2026-10-08.md` earlier (now partly out of date; this file replaces it).

## What I found and did not fix
- Flags 16 and 17: Book 2 says Sol's mother was a bound ward-taker; Book 1 (D4) says paper-only ward, in about ten chapters (ch03, 04, 05, 07, 13, 15, 16, 19, 31, 33). The name Mara also clashes (mother, dead ward, wardens). Needs Zia's direction first.
- Flag 19: Book 2 ch16 calls Sol "accredited ward-taker" (tied to flag 16); "tar-shop"/"tar shop" and "stylus" left as cosmetic.
- Book 2 ch36 and ch41 were restamped from their new blobs without rereading the `f51ca904` edits.
- My checks were by byte-size arithmetic and live reads, not byte diffs. No sandbox, network off.

## What the next profile must do
1. Read the log and protocol. Compare blobs. Do not trust any summary, including this one.
2. Ask Zia which way flags 16 and 17 go (Book 2 canon or Book 1 canon). Do not start that rewrite without the answer.
3. Do not start the final humanizer and proofreading pass on Book 2 ch1 to 45 until Zia says go. Then build the KDP interior from `chapters/`, not from the stale full_manuscript file.
4. Book 3 starts at ch01 only after Zia agrees. Expect damage in ch02 to ch04 and ch06 (copied text, leaked "Ch.N", many dashes) and ch03 (scene pasted twice, plan text in dialogue, early reveal). Book 3 bans the month name Frostveil.
5. If asked, reread Book 2 ch36 and ch41 against the live text and restamp.

## How Zia wants it done
- One chapter at a time. Five at a time eats the session.
- Scope rule: fix facts and clear AI tells only. No cosmetic tweaks, no style passes, no rewrites. Do not shrink chapters.
- No em dashes or AI tells in anything you write. Brief updates only. Full file or full link when Zia must paste.
- Work only inside the three Kindling Line books.
- Push with `push_files`. Claim only checks done in the same turn.
