# HANDOFF - Kindling Line Book 2 Polish Pass

Read `../EDITORIAL_CHARTER.md`, this file, `brief.txt`. Update this file in the SAME commit as any chapter edit. Stamp every chapter in Status + Progress log. No em-dash strip on a broken chapter; fix structure first. Full commit history (older canon detail, per-commit reasoning) lives in git log, not here - this file holds only what's needed to keep going.

**For the NEXT book:** `../BEAT_MAP_PROTOCOL.md`. Not relevant to finishing this one.

**Two books, one repo.** `kindling-line-book-1/` has its own HANDOFF, different profile. Check `get_commit` files before assuming overlap. Re-list `main` and re-fetch this file at the start of every turn.

## Canon lock

- Site: **Anchor Seven** only (ch.13-15). Never Embervein/Graywater/Greyledge/Veilward/Blackwater/any waystation.
- Thorne seal: three strands, knotted, drop/flame/feather at each end, violet+copper, near-black wax. No crown/vine/hawk/fox/motto. Malrik's clasp: plain silver.
- Scripted line ("I'm not asking you to tell me everything...") appears ONCE, ch.16 only. Paraphrased callbacks (not verbatim) are fine, used ch.33.
- Deed's meaning known from ch.21 on - don't re-explain as news.
- Thorne's line ("a house that has already paid the cost...") - Malrik ch.1, steward ch.15 only. No other lord repeats it verbatim.
- Formal co-lead/cession is ch.39 ONLY. No self-nomination/co-lead mechanism invented before then.
- "I love you" first spoken ch.28 (Kael, Tar Lane forge, Renn's chalk). Never restaged as a first-time event later.
- Cost-transfer (Sol/Kael): involuntary, non-redirectable, never a chosen tool. Not used ch.24-35.
- Injury canon: Mara injured ch.24-26, unconscious since, no change through ch.35. NOT Joren. Kael visits and talks to her unconscious - a repeatable beat.
- Dates: Sunspire=30 days. Ch.N=(N+8) Sunspire through ch.22. From ch.23: ch.N=(N-22) Cinderveil. Story spans ~40 days total - never "two months."
- Style: no em-dashes, no "particular/something/someone/kind of/the specific", no chapter numbers in prose, 1,800-word floor (count with header), no invented Accord article/section numbers.
- Names: Kael Ashworth (Auditor, father Valerius DEAD, no uncle exists), Isolde "Sol" Vane ("Lady Vane", never "Consultant"), Lord Malrik Thorne, Aldous (grandson), unnamed steward, Keeper Cormac Vrell, Renn (surveyor), Joren + Mara (wardens, Mara unconscious), Corren (second warden, ch.33+), Ansa (splicer), Tam, Bram (clerk), Varel (was missing, now safe). Council = TWELVE houses. Never name a clerk "Valerius" (collision with Kael's dead father) or any variant of Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor. No "Accord Hall", no "inquiry board".

## Status

| Ch | State |
|----|-------|
| 1-9 | UNVERIFIED - wrong seal, Valerius alive, Nine Houses (should be Twelve). Full rewrite needed, not started. |
| 10-32 | Clean, rewritten/proofread across many sessions. |
| 33-35 | Rewritten this session - the full rupture arc (opens ch.33, holds ch.34, turns ch.35 into a concrete new rule rather than a full repair). Not yet separately proofread on a fresh read. |
| 36-45 | UNCHECKED - treat as broken until read. Every chapter fully read so far (33/34/35) was fully broken on the old draft; assume the same going in. |

## Live canon (only what's needed going forward)

- **Boiling-house / second stair:** unexplored past where Kael reached it (ch.33), water rising, closed by Joren. Both tally pegs going to Renn's commission, sitting the 14th.
- **Rupture arc closed (ch.33-35), NOT a full repair:** Kael broke the ch.32 joint-consent rule (went down alone, told the wardens instead of Sol). Sol confronted him, named her own parallel blind spot (wanting to hold Tam back). Ch.34: raw middle ground at the Tar Lane overlook, neither promising the pattern is fixed. Ch.35: Sol, prompted by Ansa's advice, proposes a NEW rule - not a private promise but something that must be said aloud to a third person (a warden) every time, specifically because a rule only two people hold can be quietly excused by either of them alone. Kael agrees. This is the concrete seed ch.36+ repair should build from - test it, don't resolve it instantly.
- **Petition math:** 8/12 houses signed, need 9 to set Deed aside. Deed's 30 days lapse 28 Cinderveil. Chain clock (ch.19) failing by end of Cinderveil if unresolved - honor at climax.
- **Kael's injury:** stick in right hand, left leg dead below hip.

## Plan for ch.36 (author may override)

Read old ch.36 in full first. Per the brief this is where REPAIR begins (ch.36-39), building toward Kael formally ceding unilateral authority and Sol becoming co-equal lead at ch.39 specifically, not before. Ch.36 should show the new "say it aloud to a third person" rule actually being tested in practice - ideally under real pressure, not just narrated as working. Do not let ch.36 jump straight to the ch.39 cession.

## Open threads (don't resolve cheaply)

1. Second stair below the iron door - unexplored, water rising, closed until the 14th.
2. Iron door / second tally peg (ch.32) - who left it, why.
3. Renn missing since ~the 4th; commission sits the 14th.
4. Mara's recovery - unchanged through ch.35.
5. Aldous's "I did not" (ch.16) - still open.
6. Sol's unspoken word FIRST - complicated by Tam choosing it himself.
7. The "leaving paper" (ch.31) - never read, nobody's signed it.
8. The silent grey man at ch.31's reading - never resolve into a named Keeper.
9. Who drew the standard originally.

## Findings still open (fix when circling back to 1-9 and 36-45)

- Ch.1-9: Valerius alive, Nine Houses, wrong seal. Full rewrite needed, not started.
- Ch.36-45: skim-only so far, old-canon drift confirmed in the pattern for every chapter fully read to date. Assume full rewrite needed for each.
- Grep targets: Embervein, Veilward, Blackwater, Greyledge, Veyra, Veldt, Mirelle, Hest, Voss, Marius, Hale, Cressida, Elsbeth, Merrow, Hestor, "31 Sunspire", "Accord Hall", "Disciplinary Board", "Consultant", "two months", "uncle", "thirty-seven", "Mara Ven", "inquiry board", "co-lead" (before ch.39), "Clerk Valerius" or any clerk named Valerius, article/section numbers.
- Word-floor sweep still owed for ch.1-27 (only 26-35 confirmed counted so far).

## Process notes

- Re-list `main` + re-fetch this file at start of every turn.
- `raw.githubusercontent.com` works via curl for quick word-count/grep checks.
- Before each chapter: read charter + this file + brief.txt + the chapter before + the OLD chapter in full. Assume broken, replace don't patch.
- Check every rewrite for: wrong magic system, wrong seal, front-loaded plot, under word floor, chapter-number references, duplicated locked beats, wrong date math, wrong counts, invented family/legal mechanisms, banned names.
- `kindling-line-book-2_full_manuscript.md` is stale - regenerate at the very end.
- Em-dash pass and full banned-word scan happen after structure is fixed everywhere, not before.

## Progress log (keep to last few entries; older detail is in git log)

- Ch.10-32 rewritten/proofread across many sessions.
- 2026-09-29: wrote `../BEAT_MAP_PROTOCOL.md` for the next book (added Step 0: cross-series name-collision check, since names like Mara/Renn/Aldous are a generic-fantasy-name artifact, not intentional reuse); trimmed this file to ~7-8KB.
- 2026-09-29: rewrote ch.33-35, the full rupture arc. Old drafts all fully broken (invented uncle, invented "Mara Ven", invented "Clerk Valerius", wrong sites/seals, invented legal mechanisms, scripted lines repeated). New arc: opens (ch.33), holds (ch.34), turns into a concrete new rule - said aloud to a third party, not just privately promised (ch.35) - without fully resolving. Next: read old ch.36 in full, begin repair per the brief.
