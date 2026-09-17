## PROCEDURE (READ FIRST)

Defers to `novels/EDITORIAL_CHARTER.md` for methodology. This file = this book's own facts: locked word floor, canon, review log.

Mechanical proofreading (word count/em-dash/"particular"/meta-leak) is DONE — see `PROOFREAD_REPORT.md`. This file tracks the deeper pass: continuity, voice, canon, timeline math — the stuff a script can't catch.

**STATUS 2026-09-17: ch.1-39 fully reviewed and fixed. Ch.40-45 still need the full pass.** Not publish-ready until that's done. Don't assume any unreviewed chapter is fine just because it's mechanically clean.

**Rule going forward: keep log entries SHORT.** One line per chapter: status + the one thing that mattered, if anything. The git commit message on each fix already holds the full detail — don't duplicate it here. This file bloated past 7,000 words once already; don't let it happen again.

**Rule going forward (2): review in batches of 5-6 chapters before writing to this file, not one at a time.** Reduces overhead. Still fix genuine defects in the chapter file itself the moment they're found — only the HANDOFF write waits for the batch.

## Locked facts

- **Word floor: 1,900-2,700w/chapter, FINAL, no more padding, ever.** (Book 4+ uses the charter's 2,300w standard instead — don't conflate them.)
- No em dashes. Zero "particular" anywhere. Confirmed book-wide.
- Voice: Mara dry/engineering-metaphor, Caleb steady/plainspoken, Wren blunt/fast-talking, Priya procedural, Dev hardening through the climax then softening post-eclipse. **Caleb and Mara are married** (est. ch.21).
- "Kind of" pattern: **"own kind of ___" and bare "a kind of + generic emotion noun" = filler, fix on sight.** "Kind of" attached to something concrete/specific = legitimate, leave alone.
- **"Some/something ___" hedge is present in every chapter, unresolved.** Confirmed the book's single biggest remaining defect. Needs a dedicated pass — Zia hasn't greenlit that yet, don't start it unprompted.
- Eclipse countdown resolved to zero at ch.35 (eclipse night). No more day-counts past that point.
- Never call Book 2 "the last book" etc. in-prose (found/fixed once, ch.25).
- **PENDING VERIFICATION AT CH.42:** Eleanor's relationship to the Whitlock bloodline. Ch.38/39 both frame her as a young woman who personally faced this same hereditary hunger and "ran," burying it in 1947. But her surname "Whitlock" may be a married name (from Ambrose), not blood — ch.42's reveal (Eleanor was Ambrose's WIFE, widowed 1945, remarried Samuel 1947) needs to be checked against ch.38/39's framing for whether Dev's blood-descent actually runs through an Eleanor/Ambrose child, or some other path. Don't assume either chapter is right until ch.42 is read carefully.

## Story summary

Sequel to Book 2. Dev (Priya's brother) inherits a hereditary Whitlock-line hunger, triggered by direct contact with Book 2's well ritual. A hidden "quiet family" faction wants it to complete rather than be stopped; splinter leader Corwin Drake leads violent opposition in Act Three. Six-week countdown to the autumn eclipse. Resolves fully: a ten-person ring redistributes what Dev carries at the eclipse-night ritual despite Drake's armed interference; Dev survives whole. Ends on an open Book 4 hook (Drake at large, other Whitlock-line families exist elsewhere). Full chapter-by-chapter beat breakdown lives in `beat_map.md` — read that for outline, this file for what's actually been verified against the live text.

Read before writing: `EDITORIAL_CHARTER.md`, Book 2's `chapter_41.md` (Adelaide's letter) and `HANDOFF.md`, Book 1's `architecture.md`, this book's `beat_map.md`.

## Confirmed-good canon from the review so far

- Dev's blackout count/escalation, well-contact trigger mechanism, both confirmed consistent (fixed early bugs in ch.8/9/10).
- Full arc through eclipse night (ch.35) confirmed clean: recruiter contacts → doctrine reveal → Elias mole arc → ring proposal → three genuinely distinct security leaks (Elias/mole, ch.29 sightline, ch.34 scheduling gap) → ring finalized at 10 → Halloran's murder by Drake's splinter faction → Drake's eclipse-night standoff.
- **Ch.36:** ritual begins, all ten channels connect, distribution working. Drake's people open fire; Hollis wounded. Fixed a contradiction where the chapter's closing line attributed the gunfire to "Drake's own carefully planned disruption," directly contradicting his ch.35 promise to only watch — reattributed to followers he can't fully control, paralleling Halloran's own splinter-faction fate.
- **Ch.37:** Drake's people had planted a sabotage stake (iron, hidden in the dirt) at Delacroix's position before the ring ever arrived — pre-existing sabotage, not live disruption. Mara finds and pulls it under pressure, restoring even distribution. Drake admits to planting it afterward, consistent with his cold, patient characterization. Minor unfixed soft-timing note: "eleven minutes into totality" + "two minutes left" doesn't sum precisely to ch.35's stated 15-minute totality window, but within normal narrative slack for a fast action scene, not treated as a hard bug.
- **Ch.38:** Dev's internal fight against the bargain itself (personified pressure, not a physical attacker) — refuses it, draws strength from the ring's collective support rather than facing it alone the way Eleanor did. Distribution completes, eclipse ends, Dev survives whole. See the Eleanor flag above for the one open question from this chapter.
- **Ch.39:** dawn aftermath — distribution held clean across all ten, Hollis stable (shoulder wound, will recover), Drake's outbuilding found abandoned and deliberately cleared, Odette admits she was wrong about the doctrine's inevitability, Dev commits to watching for other affected families going forward. All matches beat_map exactly.

## Review log (short form — full detail in each chapter's commit message on GitHub)

✅ ch.1-39 reviewed, several fixed. All fixes live and pushed.

**Next: start at ch.40** (closed council session, Drake's Millbrook case, Denise becomes valley advisor, per beat_map).

| Ch | Status |
|---|---|
| 1-5 | OK |
| 6-7 | Fixed: "months since the well" → "weeks" |
| 8-9 | Fixed: dropped 4th-blackout recap |
| 10 | Fixed: well-contact mechanism contradicted Book 2 canon |
| 11-12 | OK |
| 13 | Fixed: countdown undercounted |
| 14 | OK |
| 15 | Fixed: countdown + filler "kind of" |
| 16-17 | OK |
| 18 | Fixed: countdown, twice |
| 19-20 | OK |
| 21 | OK — established Caleb/Mara marriage |
| 22-23 | OK |
| 24-25 | Fixed: biggest countdown bug (7 instances) + meta-leak |
| 26 | OK — flagged 2nd leak thread, resolved ch.29 |
| 27-28 | Fixed: filler "kind of" ×4 |
| 29 | OK — 2nd leak = sightline gap, ring relocates to silo |
| 30 | OK — Halloran confrontation, matches canon |
| 31 | Fixed: countdown + filler "kind of" |
| 32-33 | OK — ring finalized, Halloran murdered, Drake identified |
| 34 | OK — Farrow warning, 3rd leak = scheduling gap |
| 35 | OK — eclipse-night checkpoint, matches beat_map exactly |
| 36 | Fixed: closing line contradicted Drake's ch.35 promise of restraint |
| 37 | OK — planted sabotage stake, Mara's fix, minor unfixed soft-timing note |
| 38 | OK — Dev's internal turning point; flagged Eleanor/Ambrose relationship for ch.42 check |
| 39 | OK — dawn aftermath, matches beat_map exactly |
| 40-45 | NOT YET REVIEWED |

## Pending decisions for Zia

1. Continue the sequential review ch.40-45? (Confirmed yes, in progress.)
2. Commission a dedicated "some/something" hedge-word sweep across all 45 chapters? Not yet greenlit.

## Proofreading — Last Verified
- Run: 2026-09-16, 45 chapters scanned, 99,892w, 0 hard violations.
- Full report: `novels/amity-falls-book-3/PROOFREAD_REPORT.md`
