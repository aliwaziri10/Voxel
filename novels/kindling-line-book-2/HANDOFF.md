# HANDOFF - Kindling Line Book 2 Polish Pass

Read `../EDITORIAL_CHARTER.md`, this file, `brief.txt`. Update this file in the SAME commit as any chapter edit. Stamp every chapter in Status + Progress log. No em-dash strip on a broken chapter; fix structure first. Full commit history (older canon detail, per-commit reasoning) lives in git log, not here - this file holds only what's needed to keep going.

**For the NEXT book:** `../BEAT_MAP_PROTOCOL.md`. Not relevant to finishing this one.

**Two books, one repo.** `kindling-line-book-1/` has its own HANDOFF, different profile. Check `get_commit` files before assuming overlap. Re-list `main` and re-fetch this file at the start of every turn - stale copies have cost wasted passes twice already.

## Canon lock

- Site: **Anchor Seven** only (ch.13-15). Never Embervein/Graywater/Greyledge/any waystation.
- Thorne seal: three strands, knotted, drop/flame/feather at each end, violet+copper, near-black wax. No crown/vine/hawk/fox/motto. Malrik's clasp: plain silver.
- Scripted line ("I'm not asking you to tell me everything...") appears ONCE, ch.16 only.
- Deed's meaning known from ch.21 on - don't re-explain as news.
- Thorne's line ("a house that has already paid the cost...") - Malrik ch.1, steward ch.15 only. No other lord repeats it.
- Formal co-lead/cession is ch.39 ONLY. Ch.17 = private promise only. No "Equals, starting now" before ch.39.
- Cost-transfer (Sol/Kael): involuntary, non-redirectable, never a chosen tool.
- Dates: Sunspire=30 days. Ch.N=(N+8) Sunspire through ch.22. From ch.23: ch.N=(N-22) Cinderveil. Story spans ~40 days total - never "two months."
- Style: no em-dashes, no "particular/something/someone/kind of/the specific", no chapter numbers in prose, 1,800-word floor (count with header).
- Names: Kael Ashworth (Auditor, father Valerius DEAD, never alive on-page), Isolde "Sol" Vane ("Lady Vane", never "Consultant"), Lord Malrik Thorne, Aldous (grandson), unnamed steward, Keeper Cormac Vrell, Renn (surveyor), Joren + Mara (wardens), Ansa (splicer), Tam, Bram (clerk), Varel (was missing, now safe). Council = TWELVE houses. Banned names: Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor. No "Accord Hall", no article numbers.

## Status

| Ch | State |
|----|-------|
| 1-9 | UNVERIFIED - wrong seal wording, and session 10 found Valerius alive, Nine Houses (should be Twelve), inconsistent Ashworth seal. Needs full read + rewrite, not yet started. |
| 10-30 | Clean, rewritten/proofread across many sessions. Commit shas in git log if needed. |
| 31 | Rewritten + proofread, session 13. 1,821w, clean. |
| 32 | Rewritten + proofread, session 13. 1,868w, clean. |
| 33-45 | UNCHECKED - treat as broken until read. Session 10 skim (not full read) flagged old-canon drift in every one; see git log commit for specifics if a chapter's issue isn't obvious on read. |

## Live canon (only what's needed going forward)

- **Boiling-house cellar:** iron door now open (was shut), second tally peg left inside on the table, deliberately placed. Sol keeps peg 1 (glove), Kael has peg 2 (coat pocket). Not explored past the table - Joren posted two wardens, nobody proceeds unless Kael AND Sol both say so aloud together. Open thread: who left it and why.
- **Ch.31 standard-reading:** Kael certified nothing, only that he read it; entered the distinction between tonight's standard and the one 250 men signed. Hold lifted on all five incl. Tam. Tam chose to sign the new standard himself, unprompted - Kael didn't decide for him either way. Sol named her own overcorrection-shaped blind spot (silently wanting Tam held back) for the first time. Unresolved - this is rupture material for ch.33-35, not yet used.
- **Ch.32:** Ansa knew of Tam's choice at dawn, kept it from Sol at Tam's request. Sol felt the "kept-from" pattern from the receiving end. Also unresolved.
- **Kael/Sol growth:** ch.26 relapse, ch.27-32 steady repair. Sol's own blind spot (ch.31-32) is a live parallel thread - do not let either resolve neatly before the ch.33-35 rupture; it needs both patterns still raw.
- **Petition math:** 8/12 houses signed, need 9 to set Deed aside. Deed's 30 days lapse 28 Cinderveil. Chain clock (ch.19) cycling toward failure by end of Cinderveil if unresolved - honor at climax.
- **Kael's injury:** stick in right hand, left leg dead below hip.

## Plan for ch.33 (author may override)

Read old ch.33 in full first - don't assume broken without checking. This is the LOCKED rupture (ch.33-35). Draw on: Kael's overcorrection history, Sol's own blind spot from ch.31-32 (make it a real parallel failure, not just his), the still-open iron-door/peg thread (do NOT resolve it here, it's a separate plot line), Tam's choice, Renn and Mara both still unresolved.

## Open threads (don't resolve cheaply)

1. Iron door / second peg - who, why.
2. Renn missing since ~the 4th; commission sits the 12th; a man with lantern+flat case on Tar Lane that night, unconfirmed as him.
3. Mara's recovery - unchanged, no update yet.
4. Aldous's "I did not" (ch.16) - still open.
5. Sol's unspoken word FIRST (someone must prove the new standard survivable) - now complicated by Tam choosing it himself, not her plan.
6. The "leaving paper" (ch.31) - a courtesy beside the standard, never read, nobody's signed it.
7. The silent grey man at ch.31's reading - never resolve into a named Keeper.
8. Who drew the standard originally.

## Findings still open (fix when circling back to 1-9 and 33-45)

- Ch.1-9: Valerius alive (should be dead), Nine Houses (should be Twelve), inconsistent Ashworth seal, retired site names, wrong Thorne seal wording. Full rewrite needed, not started.
- Ch.33-45: skim-only so far, old-canon drift confirmed in the pattern (wrong seal/name/count errors consistent with 1-9 and the original 31/32 drafts). Treat every one as needing full read + likely full rewrite.
- Grep targets for 33-45: Embervein, Veyra, Veldt, Mirelle, Hest, "seventeen Sunspire", Voss, Marius, Hale, Cressida, Elsbeth, Merrow, Hestor, "31 Sunspire", "Accord Hall", "Lady Varel", "Disciplinary Board", "Consultant", "two months".
- Word-floor sweep still owed for ch.1-27 (only 26-32 confirmed counted so far).

## Process notes

- Re-list `main` + re-fetch this file at start of every turn.
- `raw.githubusercontent.com` works via curl for quick word-count/grep checks.
- Before each chapter: read charter + this file + brief.txt + the chapter before + the OLD chapter in full. Assume broken, replace don't patch.
- Check every rewrite for: wrong magic system, wrong seal, front-loaded plot, under word floor, chapter-number references, duplicated locked beats, wrong date math, wrong counts.
- `kindling-line-book-2_full_manuscript.md` is stale - regenerate at the very end, not per-chapter.
- Em-dash pass and full banned-word scan happen after structure is fixed everywhere, not before.

## Progress log (keep to last few entries; older detail is in git log)

- Ch.10-30 rewritten/proofread across many sessions (see git log for per-commit detail).
- Session 12-13: rewrote and proofread ch.31, ch.32 (both were badly broken - wrong characters, wrong plot, under word floor).
- 2026-09-29: wrote `../BEAT_MAP_PROTOCOL.md` for the next book. Trimmed this file from ~17KB to keep only what's load-bearing. Next: read old ch.33 in full, write the rupture opening.
