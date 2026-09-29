# HANDOFF - Kindling Line Book 2 Polish Pass

Read `../EDITORIAL_CHARTER.md`, this file, `brief.txt`. Update this file in the SAME commit as any chapter edit. Stamp every chapter in Status + Progress log. No em-dash strip on a broken chapter; fix structure first. Full commit history (older canon detail, per-commit reasoning) lives in git log, not here - this file holds only what's needed to keep going.

**For the NEXT book:** `../BEAT_MAP_PROTOCOL.md`. Not relevant to finishing this one.

**Two books, one repo.** `kindling-line-book-1/` has its own HANDOFF, different profile. Check `get_commit` files before assuming overlap. Re-list `main` and re-fetch this file at the start of every turn - stale copies have cost wasted passes twice already.

## Canon lock

- Site: **Anchor Seven** only (ch.13-15). Never Embervein/Graywater/Greyledge/Veilward/any waystation.
- Thorne seal: three strands, knotted, drop/flame/feather at each end, violet+copper, near-black wax. No crown/vine/hawk/fox/motto. Malrik's clasp: plain silver.
- Scripted line ("I'm not asking you to tell me everything...") appears ONCE, ch.16 only.
- Deed's meaning known from ch.21 on - don't re-explain as news.
- Thorne's line ("a house that has already paid the cost...") - Malrik ch.1, steward ch.15 only. No other lord repeats it.
- Formal co-lead/cession is ch.39 ONLY. Ch.17 = private promise only. No "Equals, starting now" before ch.39.
- Cost-transfer (Sol/Kael): involuntary, non-redirectable, never a chosen tool. Not used ch.24-33.
- Dates: Sunspire=30 days. Ch.N=(N+8) Sunspire through ch.22. From ch.23: ch.N=(N-22) Cinderveil. Story spans ~40 days total - never "two months."
- Style: no em-dashes, no "particular/something/someone/kind of/the specific", no chapter numbers in prose, 1,800-word floor (count with header).
- Names: Kael Ashworth (Auditor, father Valerius DEAD, never alive on-page, no uncle exists), Isolde "Sol" Vane ("Lady Vane", never "Consultant"), Lord Malrik Thorne, Aldous (grandson), unnamed steward, Keeper Cormac Vrell, Renn (surveyor), Joren + Mara (wardens), Corren (a second, younger warden, ch.33+), Ansa (splicer), Tam, Bram (clerk), Varel (was missing, now safe). Council = TWELVE houses. Banned names: Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor. No "Accord Hall", no article numbers, no invented Ashworth relatives.

## Status

| Ch | State |
|----|-------|
| 1-9 | UNVERIFIED - wrong seal wording, and session 10 found Valerius alive, Nine Houses (should be Twelve), inconsistent Ashworth seal. Needs full read + rewrite, not yet started. |
| 10-32 | Clean, rewritten/proofread across many sessions. Commit shas in git log if needed. |
| 33 | Rewritten this session. 11 Cinderveil, Sol POV. Not yet separately proofread on a fresh read. |
| 34-45 | UNCHECKED - treat as broken until read. Session 10 skim (not full read) flagged old-canon drift in every one; see git log commit for specifics if a chapter's issue isn't obvious on read. |

## Live canon (only what's needed going forward)

- **Boiling-house cellar:** past the iron door and table (from ch.32), a SECOND, narrower stair cuts down further into rock, previously unknown, discovered ch.33. Water rising roughly an inch an hour by sound. Not yet explored past where Kael reached it.
- **Ch.33 rupture (opened, NOT resolved):** Kael went down alone at dawn, breaking the joint-consent rule he and Sol set in ch.32 (both must say so aloud together) by saying it "for the both of them" to Joren/Corren instead. Sol followed, confronted him below. He admitted the exact failure without excuse: not concealment this time, but still deciding the danger was his to meet first. Sol connected it explicitly to her own admitted urge to have held Tam back (ch.31-32) - named the shared shape of the problem, not just his. She left him at the stair, unresolved, saying only "I'm not finishing it tonight... Come up when you're done being brave alone." Ch.34-35 must continue this, not resolve it early.
- **Ch.31 standard-reading:** Tam chose to sign the new standard himself; Kael didn't decide for him. Sol's blind spot (silently wanting Tam held back) first named here, now explicitly linked to Kael's pattern in ch.33.
- **Ch.32:** Ansa knew of Tam's choice at dawn, kept it from Sol at Tam's request. Sol felt "kept-from" from the receiving end.
- **Petition math:** 8/12 houses signed, need 9 to set Deed aside. Deed's 30 days lapse 28 Cinderveil. Chain clock (ch.19) cycling toward failure by end of Cinderveil if unresolved - honor at climax.
- **Kael's injury:** stick in right hand, left leg dead below hip.

## Plan for ch.34 (author may override)

Read old ch.34 in full first. Rupture continues (ch.33-35 locked, NOT resolved yet). Ch.33 ended with Sol leaving Kael at the stair mid-rupture - ch.34 can pick up same day (aftermath, both still raw) or a short beat later, but must not let either of them resolve the shared "deciding for the other" pattern neatly. Do not resolve the second stair/rising water thread here either; it's a separate plot line that can stay open or advance slightly, not conclude.

## Open threads (don't resolve cheaply)

1. Second stair below the iron door, found ch.33 - unexplored, water rising.
2. Iron door / second tally peg (ch.32) - who left it, why - separate from the new stair.
3. Renn missing since ~the 4th; commission sits the 12th; a man with lantern+flat case on Tar Lane that night, unconfirmed as him.
4. Mara's recovery - unchanged, no update yet.
5. Aldous's "I did not" (ch.16) - still open.
6. Sol's unspoken word FIRST (someone must prove the new standard survivable) - complicated by Tam choosing it himself.
7. The "leaving paper" (ch.31) - never read, nobody's signed it.
8. The silent grey man at ch.31's reading - never resolve into a named Keeper.
9. Who drew the standard originally.

## Findings still open (fix when circling back to 1-9 and 34-45)

- Ch.1-9: Valerius alive (should be dead), Nine Houses (should be Twelve), inconsistent Ashworth seal, retired site names, wrong Thorne seal wording. Full rewrite needed, not started.
- Ch.34-45: skim-only so far, old-canon drift confirmed in the pattern (wrong seal/name/count errors, invented relatives, consistent with 1-9 and the original 31/32/33 drafts). Treat every one as needing full read + likely full rewrite. Ch.33's old draft (now replaced) also had an invented "Kael's uncle" - watch for this character reappearing in 34+ if generated in the same run.
- Grep targets for 34-45: Embervein, Veilward, Veyra, Veldt, Mirelle, Hest, "seventeen Sunspire", Voss, Marius, Hale, Cressida, Elsbeth, Merrow, Hestor, "31 Sunspire", "Accord Hall", "Lady Varel", "Disciplinary Board", "Consultant", "two months", "uncle", "thirty-seven".
- Word-floor sweep still owed for ch.1-27 (only 26-33 confirmed counted so far).

## Process notes

- Re-list `main` + re-fetch this file at start of every turn.
- `raw.githubusercontent.com` works via curl for quick word-count/grep checks.
- Before each chapter: read charter + this file + brief.txt + the chapter before + the OLD chapter in full. Assume broken, replace don't patch.
- Check every rewrite for: wrong magic system, wrong seal, front-loaded plot, under word floor, chapter-number references, duplicated locked beats, wrong date math, wrong counts, invented family members.
- `kindling-line-book-2_full_manuscript.md` is stale - regenerate at the very end, not per-chapter.
- Em-dash pass and full banned-word scan happen after structure is fixed everywhere, not before.

## Progress log (keep to last few entries; older detail is in git log)

- Ch.10-30 rewritten/proofread across many sessions (see git log for per-commit detail).
- Session 12-13: rewrote and proofread ch.31, ch.32 (both badly broken - wrong characters, wrong plot, under word floor).
- 2026-09-29: wrote `../BEAT_MAP_PROTOCOL.md` for the next book; trimmed this file from ~17KB to ~7KB, load-bearing content only.
- 2026-09-29: rewrote ch.33 (old draft: invented uncle, wrong house count, wrong site name "Veilward", scripted line repeated in violation of once-only rule). New ch.33 opens the rupture grounded in ch.32's iron-door/joint-consent thread, draws on both Kael's and Sol's parallel patterns. NOT resolved - by design. Next: read old ch.34 in full, continue the rupture.
