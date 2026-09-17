## PROCEDURE (READ FIRST)

Defers to `novels/EDITORIAL_CHARTER.md` for methodology. This file = this book's own facts: locked word floor, canon, review log.

Mechanical proofreading (word count/em-dash/"particular"/meta-leak) is DONE — see `PROOFREAD_REPORT.md`. This file tracks the deeper pass: continuity, voice, canon, timeline math — the stuff a script can't catch.

**STATUS 2026-09-17: ch.1-28 fully reviewed and fixed. Ch.29-45 still need the full pass.** Not publish-ready until that's done. Don't assume any unreviewed chapter is fine just because it's mechanically clean.

**Rule going forward: keep log entries SHORT.** One line per chapter: status + the one thing that mattered, if anything. The git commit message on each fix already holds the full detail — don't duplicate it here. This file bloated past 7,000 words once already; don't let it happen again.

## Locked facts

- **Word floor: 1,900-2,700w/chapter, FINAL, no more padding, ever.** (Book 4+ uses the charter's 2,300w standard instead — don't conflate them.)
- No em dashes. Zero "particular" anywhere. Confirmed book-wide.
- Voice: Mara dry/engineering-metaphor, Caleb steady/plainspoken, Wren blunt/fast-talking, Priya procedural, Dev hardening through the climax then softening post-eclipse. **Caleb and Mara are married** (est. ch.21).
- "Kind of" pattern: **"own kind of ___" and bare "a kind of + generic emotion noun" = filler, fix on sight.** "Kind of" attached to something concrete/specific = legitimate, leave alone.
- **"Some/something ___" hedge is present in every chapter, unresolved.** Confirmed the book's single biggest remaining defect. Needs a dedicated pass — Zia hasn't greenlit that yet, don't start it unprompted.
- Eclipse countdown math is the recurring bug class in this book (found in ch.8,9,13,15,18×2,20,24,25). Can drift either direction. Always check the actual arithmetic against the most recent confirmed chapter, never assume a repeated number is safe.
- Never call Book 2 "the last book" etc. in-prose (found/fixed once, ch.25).

## Story summary

Sequel to Book 2. Dev (Priya's brother) inherits a hereditary Whitlock-line hunger, triggered by direct contact with Book 2's well ritual. A hidden "quiet family" faction wants it to complete rather than be stopped; splinter leader Corwin Drake leads violent opposition in Act Three. Six-week countdown to the autumn eclipse. Resolves fully: a ten-person ring redistributes what Dev carries at the eclipse-night ritual despite Drake's armed interference; Dev survives whole. Ends on an open Book 4 hook (Drake at large, other Whitlock-line families exist elsewhere). Full chapter-by-chapter beat breakdown lives in `beat_map.md` — read that for outline, this file for what's actually been verified against the live text.

Read before writing: `EDITORIAL_CHARTER.md`, Book 2's `chapter_41.md` (Adelaide's letter) and `HANDOFF.md`, Book 1's `architecture.md`, this book's `beat_map.md`.

## Confirmed-good canon from the review so far

- Dev's blackout count and escalation is consistent (5 confirmed by ch.12, fixed 2 dropped-recap bugs in ch.8/9).
- Trigger mechanism: Dev physically touched the well during Book 2's ritual — direct contact, not proximity (fixed a contradiction in ch.10).
- Two Act One recruiter contacts (ch.12, ch.14) → Act Two escalates to the coat-button read (ch.17, doctrine reveal) → Elias Thorne mole arc (ch.20→23→24→28, resolved with proportionate consequence, not punishment) → ring proposal (ch.25) → first volunteer Odette (ch.28) → public disclosure via town gathering (ch.27) → ring finalized at 10 (ch.32, per beat_map, not yet independently re-verified).
- Eclipse countdown, verified chapter-by-chapter through ch.28: 32→31→27→(ch.24/25 bug, fixed)→21→21→19→18 days, all internally consistent as of ch.28.
- Ch.26 raised a possible second/new leak (precisely-timed blackout approach) — **still needs to be checked against ch.29's "sightline gap" resolution to confirm it's the same thread, not dangling.**

## Review log (short form — full detail in each chapter's commit message on GitHub)

✅ ch.1-28 reviewed, several fixed (dropped-blackout recaps ch.8/9, well-contact contradiction ch.10, countdown math ch.13/15/18/24/25, filler "kind of" ch.15/27/28, meta-leak ch.25). All fixes are live and pushed.

**Next: start at ch.29.** Confirm ch.26's leak thread resolves here.

| Ch | Status |
|---|---|
| 1-5 | OK, no fixes needed |
| 6-7 | Fixed: "months since the well" → "weeks" (anchor consistency) |
| 8-9 | Fixed: dropped 4th-blackout recap |
| 10 | Fixed: well-contact mechanism contradicted Book 2 canon |
| 11-12 | OK |
| 13 | Fixed: countdown undercounted |
| 14 | OK |
| 15 | Fixed: countdown wrong-direction + filler "kind of" |
| 16 | OK |
| 17 | OK (countdown pre-confirmed correct) |
| 18 | Fixed: countdown, twice |
| 19 | OK |
| 20 | OK (countdown pre-confirmed correct) |
| 21 | OK — established Caleb/Mara marriage |
| 22 | OK |
| 23 | OK (countdown pre-confirmed correct) |
| 24-25 | Fixed: this book's biggest countdown bug (7 instances) + meta-leak (ch.25) |
| 26 | OK — flags possible 2nd leak thread for ch.29 |
| 27-28 | Fixed: filler "kind of" ×4 total |
| 29-45 | NOT YET REVIEWED |

## Pending decisions for Zia

1. Continue the sequential review ch.29-45? (Confirmed yes, in progress.)
2. Commission a dedicated "some/something" hedge-word sweep across all 45 chapters? Not yet greenlit.

## Proofreading — Last Verified
- Run: 2026-09-16, 45 chapters scanned, 99,892w, 0 hard violations.
- Full report: `novels/amity-falls-book-3/PROOFREAD_REPORT.md`
