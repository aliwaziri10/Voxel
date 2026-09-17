## PROCEDURE (READ FIRST)

Defers to `novels/EDITORIAL_CHARTER.md` for methodology. This file = this book's own facts: locked word floor, canon, review log.

Mechanical proofreading (word count/em-dash/"particular"/meta-leak) is DONE — see `PROOFREAD_REPORT.md`. This file tracks the deeper pass: continuity, voice, canon, timeline math — the stuff a script can't catch.

**STATUS 2026-09-17: ch.1-35 fully reviewed and fixed. Ch.36-45 still need the full pass.** Not publish-ready until that's done. Don't assume any unreviewed chapter is fine just because it's mechanically clean.

**Rule going forward: keep log entries SHORT.** One line per chapter: status + the one thing that mattered, if anything. The git commit message on each fix already holds the full detail — don't duplicate it here. This file bloated past 7,000 words once already; don't let it happen again.

**Rule going forward (2): review in batches of 5-6 chapters before writing to this file, not one at a time.** Reduces overhead. Still fix genuine defects in the chapter file itself the moment they're found — only the HANDOFF write waits for the batch.

## Locked facts

- **Word floor: 1,900-2,700w/chapter, FINAL, no more padding, ever.** (Book 4+ uses the charter's 2,300w standard instead — don't conflate them.)
- No em dashes. Zero "particular" anywhere. Confirmed book-wide.
- Voice: Mara dry/engineering-metaphor, Caleb steady/plainspoken, Wren blunt/fast-talking, Priya procedural, Dev hardening through the climax then softening post-eclipse. **Caleb and Mara are married** (est. ch.21).
- "Kind of" pattern: **"own kind of ___" and bare "a kind of + generic emotion noun" = filler, fix on sight.** "Kind of" attached to something concrete/specific = legitimate, leave alone.
- **"Some/something ___" hedge is present in every chapter, unresolved.** Confirmed the book's single biggest remaining defect. Needs a dedicated pass — Zia hasn't greenlit that yet, don't start it unprompted.
- Eclipse countdown math is the recurring bug class in this book (found in ch.8,9,13,15,18×2,20,24,25,31). Can drift either direction. Always check the actual arithmetic against the most recent confirmed chapter, never assume a repeated number is safe. Not every chapter states a number — that's fine, only check when one is given.
- Never call Book 2 "the last book" etc. in-prose (found/fixed once, ch.25).
- **Ring operations relocated to an isolated grain silo as of ch.29** (kitchen/household windows compromised a passive sightline leak). Confirmed still the silo through ch.35 (eclipse-night staging happens at the orchard/well field, not the silo itself — that's correct, the silo was rehearsal space, the orchard was always the intended ritual site per beat_map).
- **Eclipse night is ch.35.** Countdown fully resolves to zero here — no more day-counts to track past this point, only "totality in N minutes" style in-scene timing.

## Story summary

Sequel to Book 2. Dev (Priya's brother) inherits a hereditary Whitlock-line hunger, triggered by direct contact with Book 2's well ritual. A hidden "quiet family" faction wants it to complete rather than be stopped; splinter leader Corwin Drake leads violent opposition in Act Three. Six-week countdown to the autumn eclipse. Resolves fully: a ten-person ring redistributes what Dev carries at the eclipse-night ritual despite Drake's armed interference; Dev survives whole. Ends on an open Book 4 hook (Drake at large, other Whitlock-line families exist elsewhere). Full chapter-by-chapter beat breakdown lives in `beat_map.md` — read that for outline, this file for what's actually been verified against the live text.

Read before writing: `EDITORIAL_CHARTER.md`, Book 2's `chapter_41.md` (Adelaide's letter) and `HANDOFF.md`, Book 1's `architecture.md`, this book's `beat_map.md`.

## Confirmed-good canon from the review so far

- Dev's blackout count and escalation is consistent (5 confirmed by ch.12, fixed 2 dropped-recap bugs in ch.8/9).
- Trigger mechanism: Dev physically touched the well during Book 2's ritual — direct contact, not proximity (fixed a contradiction in ch.10).
- Two Act One recruiter contacts (ch.12, ch.14) → Act Two escalates to the coat-button read (ch.17, doctrine reveal) → Elias Thorne mole arc (ch.20→23→24→28, resolved with proportionate consequence, not punishment) → ring proposal (ch.25) → first volunteer Odette (ch.28) → public disclosure via town gathering (ch.27) → ring finalized at 10 (ch.32, confirmed).
- Eclipse countdown, verified chapter-by-chapter through ch.35 (eclipse night): 32→31→27→(bug,fixed)→21→21→19→18→16→(ch.30, none stated)→(ch.31 bug, fixed to 2wk)→11(ch.32, Halloran's murder)→7(ch.33, "fourth day after Halloran's death")→6(ch.34, "fifth night")→0/eclipse-night (ch.35). Fully consistent end to end, zero unresolved contradictions across the whole countdown arc.
- Second leak thread (ch.26 flagged, RESOLVED ch.29): passive sightline gap, not a mole. Ring relocates to grain silo for rehearsal/planning.
- Third leak (ch.34): a scheduling overlap during a shift change, not a mole either — three leaks, three genuinely different root causes, correctly non-repetitive per the charter.
- Ch.30: Halloran outbuilding confrontation, sincere-doctrinal-leader framing, Dev refuses him directly. Ch.31: Dev's private 2am doubt with Priya, reaffirms his choice, announces it to the group the next morning. Ch.32: ring finalized at 10, Halloran murdered by Drake's splinter faction same chapter, closing at 11 days. Ch.33: Corwin Drake identified via fingerprint match to decades-old eclipse-timed disappearances. Ch.34: Drake's people box in Farrow on a dark road as a warning, not a real abduction attempt — confirmed reconnaissance, not capture, per Mara's read. Ch.35 CHECKPOINT: full ring staging at the orchard/well field on eclipse night, Drake arrives with 7-8 followers, admits to killing Halloran, declines to use force ("I intend to watch... so there will be no question of what happened when it fails"), Yusuf draws a hard perimeter line, Dev gives the go-ahead. All confirmed matching beat_map exactly, no contradictions found across this whole stretch.

## Review log (short form — full detail in each chapter's commit message on GitHub)

✅ ch.1-35 reviewed, several fixed (dropped-blackout recaps ch.8/9, well-contact contradiction ch.10, countdown math ch.13/15/18/24/25/31, filler "kind of" ch.15/27/28/31, meta-leak ch.25). All fixes are live and pushed.

**Next: start at ch.36** — the ritual itself begins here (contact across all ten stakes, Drake's people open fire, Deputy Hollis wounded, circle holds per beat_map). Verify this lands consistently with ch.35's staging and Drake's stated intent to only watch (does his faction's decision to open fire contradict his own words in ch.35, or is that shift itself the point — check the actual prose for how it's justified).

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
| 26 | OK — flagged possible 2nd leak thread, resolved ch.29 |
| 27-28 | Fixed: filler "kind of" ×4 total |
| 29 | OK — 2nd leak resolved as sightline gap, ring relocates to silo, countdown 16 days confirmed |
| 30 | OK — Halloran confrontation, matches canon exactly, no countdown stated |
| 31 | Fixed: countdown ("nine more weeks" → "two more weeks") + filler "kind of tiredness" |
| 32 | OK — ring finalized at 10, Halloran murdered, 11 days confirmed |
| 33 | OK — Drake identified, countdown 7 days confirmed (11-4=7) |
| 34 | OK — Farrow ambush/warning, 3rd leak (scheduling gap) resolved, countdown 6 days confirmed (11-5=6) |
| 35 | OK — eclipse-night checkpoint, Drake's standoff, matches beat_map exactly, countdown resolves to zero |
| 36-45 | NOT YET REVIEWED |

## Pending decisions for Zia

1. Continue the sequential review ch.36-45? (Confirmed yes, in progress.)
2. Commission a dedicated "some/something" hedge-word sweep across all 45 chapters? Not yet greenlit.

## Proofreading — Last Verified
- Run: 2026-09-16, 45 chapters scanned, 99,892w, 0 hard violations.
- Full report: `novels/amity-falls-book-3/PROOFREAD_REPORT.md`
