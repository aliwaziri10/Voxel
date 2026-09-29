# HANDOFF - Kindling Line Book 2 Polish Pass

Read `../EDITORIAL_CHARTER.md`, this file, `brief.txt`. Update this file in the SAME commit as any chapter edit. Stamp every chapter in Status + Progress log. No em-dash strip on a broken chapter; fix structure first. Full commit history (older canon detail, per-commit reasoning) lives in git log, not here - this file holds only what's needed to keep going.

**For the NEXT book:** `../BEAT_MAP_PROTOCOL.md`. Not relevant to finishing this one.

**Two books, one repo.** `kindling-line-book-1/` has its own HANDOFF, different profile. Check `get_commit` files before assuming overlap. Re-list `main` and re-fetch this file at the start of every turn - stale copies have cost wasted passes twice already.

## Canon lock

- Site: **Anchor Seven** only (ch.13-15). Never Embervein/Graywater/Greyledge/Veilward/any waystation.
- Thorne seal: three strands, knotted, drop/flame/feather at each end, violet+copper, near-black wax. No crown/vine/hawk/fox/motto. Malrik's clasp: plain silver.
- Scripted line ("I'm not asking you to tell me everything...") appears ONCE, ch.16 only. A short callback (paraphrase, not verbatim) is fine, used ch.33.
- Deed's meaning known from ch.21 on - don't re-explain as news.
- Thorne's line ("a house that has already paid the cost...") - Malrik ch.1, steward ch.15 only. No other lord repeats it.
- Formal co-lead/cession is ch.39 ONLY. Ch.17 = private promise only. No self-nomination/co-lead mechanism invented before ch.39.
- "I love you" first spoken ch.28 (Kael, Tar Lane forge, Renn's chalk). Never restaged as a first-time event in a later chapter.
- Cost-transfer (Sol/Kael): involuntary, non-redirectable, never a chosen tool. Not used ch.24-34.
- Injury canon: Mara was injured (ch.24-26), unconscious since, no change through ch.34. NOT Joren. Kael visits her and talks to her while she's unconscious - an established, repeatable beat, not a one-off.
- Dates: Sunspire=30 days. Ch.N=(N+8) Sunspire through ch.22. From ch.23: ch.N=(N-22) Cinderveil. Story spans ~40 days total - never "two months."
- Style: no em-dashes, no "particular/something/someone/kind of/the specific", no chapter numbers in prose, 1,800-word floor (count with header).
- Names: Kael Ashworth (Auditor, father Valerius DEAD, never alive on-page, no uncle exists), Isolde "Sol" Vane ("Lady Vane", never "Consultant"), Lord Malrik Thorne, Aldous (grandson), unnamed steward, Keeper Cormac Vrell, Renn (surveyor), Joren + Mara (wardens - Mara unconscious, not a clerk, no "Mara Ven"), Corren (second, younger warden, ch.33+), Ansa (splicer), Tam, Bram (clerk), Varel (was missing, now safe). Council = TWELVE houses. Banned names: Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor. No "Accord Hall", no article/section numbers, no invented Ashworth relatives, no "inquiry board".

## Status

| Ch | State |
|----|-------|
| 1-9 | UNVERIFIED - wrong seal wording, and session 10 found Valerius alive, Nine Houses (should be Twelve), inconsistent Ashworth seal. Needs full read + rewrite, not yet started. |
| 10-32 | Clean, rewritten/proofread across many sessions. Commit shas in git log if needed. |
| 33-34 | Rewritten this session. Ch.33: 11 Cinderveil, Sol POV. Ch.34: 12 Cinderveil, Kael POV. Not yet separately proofread on a fresh read. |
| 35-45 | UNCHECKED - treat as broken until read. Session 10 skim (not full read) flagged old-canon drift in every one checked so far; ch.33 and ch.34's old drafts were both fully broken on full read. |

## Live canon (only what's needed going forward)

- **Boiling-house cellar / second stair:** past the iron door and table (ch.32), a second narrower stair cuts down further (found ch.33), water rising, Joren has it closed until water settles. Not explored past where Kael reached it. Both pegs promised to Renn's commission, sitting in two days (the 14th).
- **Ch.33-34 rupture (opened, NOT resolved):** Kael broke the ch.32 joint-consent rule by going down alone and saying it "for the both of them" instead of together. Sol confronted him, connected it explicitly to her own admitted urge to hold Tam back - named the shared shape, not just his. She left him mid-conversation. Ch.34: Kael visited unconscious Mara, admitted the relapse and his fear of repeating "I love you" only as an apology; found Sol at the Tar Lane overlook (where he first said it), told her plainly he can't yet promise the pattern is done, she said she can't either about her own urge with Tam. Ended in an unresolved but slightly less raw middle ground - not repair, not further rupture. Ch.35 should decide which way this actually breaks.
- **Petition math:** 8/12 houses signed, need 9 to set Deed aside. Deed's 30 days lapse 28 Cinderveil. Chain clock (ch.19) cycling toward failure by end of Cinderveil if unresolved - honor at climax.
- **Kael's injury:** stick in right hand, left leg dead below hip.

## Plan for ch.35 (author may override)

Read old ch.35 in full first. This is the LAST locked rupture chapter (ch.33-35) - ch.36 begins repair per the brief. Ch.35 needs to either (a) bring the rupture to its lowest point before repair can begin, or (b) be the turning point itself, author's call based on what old ch.35 offers once read. Keep both Kael's and Sol's parallel patterns in play; don't let ch.36's repair get preempted here.

## Open threads (don't resolve cheaply)

1. Second stair below the iron door - unexplored, water rising, closed until commission on the 14th.
2. Iron door / second tally peg (ch.32) - who left it, why.
3. Renn missing since ~the 4th; commission sits the 14th (per ch.34); a man with lantern+flat case on Tar Lane that night, unconfirmed as him.
4. Mara's recovery - unchanged through ch.34.
5. Aldous's "I did not" (ch.16) - still open.
6. Sol's unspoken word FIRST (someone must prove the new standard survivable) - complicated by Tam choosing it himself.
7. The "leaving paper" (ch.31) - never read, nobody's signed it.
8. The silent grey man at ch.31's reading - never resolve into a named Keeper.
9. Who drew the standard originally.

## Findings still open (fix when circling back to 1-9 and 35-45)

- Ch.1-9: Valerius alive (should be dead), Nine Houses (should be Twelve), inconsistent Ashworth seal, retired site names, wrong Thorne seal wording. Full rewrite needed, not started.
- Ch.35-45: skim-only so far (session 10), old-canon drift confirmed in the pattern for every chapter fully read so far (33, 34 were both fully broken - invented characters like "Mara Ven", wrong injury victim, invented legal mechanisms, misplaced "I love you"). Treat every remaining chapter as needing full read + likely full rewrite.
- Grep targets for 35-45: Embervein, Veilward, Veyra, Veldt, Mirelle, Hest, "seventeen Sunspire", Voss, Marius, Hale, Cressida, Elsbeth, Merrow, Hestor, "31 Sunspire", "Accord Hall", "Lady Varel", "Disciplinary Board", "Consultant", "two months", "uncle", "thirty-seven", "Mara Ven", "inquiry board", "self-nomination", "co-lead" (before ch.39), "first time" near "I love you".
- Word-floor sweep still owed for ch.1-27 (only 26-34 confirmed counted so far).

## Process notes

- Re-list `main` + re-fetch this file at start of every turn.
- `raw.githubusercontent.com` works via curl for quick word-count/grep checks.
- Before each chapter: read charter + this file + brief.txt + the chapter before + the OLD chapter in full. Assume broken, replace don't patch.
- Check every rewrite for: wrong magic system, wrong seal, front-loaded plot, under word floor, chapter-number references, duplicated locked beats, wrong date math, wrong counts, invented family members, invented legal/procedural mechanisms not in the brief.
- `kindling-line-book-2_full_manuscript.md` is stale - regenerate at the very end, not per-chapter.
- Em-dash pass and full banned-word scan happen after structure is fixed everywhere, not before.

## Progress log (keep to last few entries; older detail is in git log)

- Ch.10-32 rewritten/proofread across many sessions (see git log for per-commit detail).
- 2026-09-29: wrote `../BEAT_MAP_PROTOCOL.md` for the next book; trimmed this file from ~17KB to ~7KB.
- 2026-09-29: rewrote ch.33 (invented uncle, wrong house count, wrong site name, scripted line repeated) and ch.34 (invented "Mara Ven" alive, wrong injury victim, invented co-lead nomination mechanism, "I love you" wrongly restaged as first-time). Both replaced with a continuous, unresolved rupture grounded in ch.32-33's actual threads. Next: read old ch.35 in full, decide whether it's the rupture's low point or its turning point.
