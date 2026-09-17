## PROCEDURE (READ FIRST)

Defers to `novels/EDITORIAL_CHARTER.md` for methodology. This file = this book's own facts: locked word floor, canon, review log.

Mechanical proofreading (word count/em-dash/"particular"/meta-leak) is DONE — see `PROOFREAD_REPORT.md`. This file tracks the deeper pass: continuity, voice, canon, timeline math — the stuff a script can't catch.

**STATUS 2026-09-17: ch.1-45 FULLY REVIEWED AND FIXED.** The full sequential continuity/voice/canon pass is complete across the whole book. This is a major milestone — every chapter has now had the deep pass, not just the mechanical scan. Still not "never needs another look" ready: the book-wide "some/something" hedge sweep is a separate, real, not-yet-greenlit task (see Pending decisions below).

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
- **Eleanor/Ambrose genealogy — RESOLVED, ch.42-45:** Eleanor was Ambrose's wife (ring engraved E.W. & A.W.), widowed 1945, remarried Samuel 1947. Ch.42 calls Dev/Priya "her grandchildren"; ch.45 calls Dev's arrival the culmination of "three generations"; Ambrose's own letter (ch.45) says he is "not the first of my blood," his grandfather having begun the doctrine, and that he "carried [it] into our marriage" with Eleanor. Together these confirm Eleanor and Ambrose had a child together before his 1945 death — that child is Dev/Priya's parent's parent, carrying the Whitlock blood forward. Never stated in one explicit sentence, but consistent across three chapters with no contradiction — not a bug, just an implicit (intentional) mystery-novel detail. Don't "fix" this by adding an explicit line unless Zia asks for it.

## Story summary

Sequel to Book 2. Dev (Priya's brother) inherits a hereditary Whitlock-line hunger, triggered by direct contact with Book 2's well ritual. A hidden "quiet family" faction wants it to complete rather than be stopped; splinter leader Corwin Drake leads violent opposition in Act Three. Six-week countdown to the autumn eclipse. Resolves fully: a ten-person ring redistributes what Dev carries at the eclipse-night ritual despite Drake's armed interference; Dev survives whole. Ends on an open Book 4 hook (Drake at large, other Whitlock-line families exist elsewhere). Full chapter-by-chapter beat breakdown lives in `beat_map.md` — read that for outline, this file for what's actually been verified against the live text.

Read before writing: `EDITORIAL_CHARTER.md`, Book 2's `chapter_41.md` (Adelaide's letter) and `HANDOFF.md`, Book 1's `architecture.md`, this book's `beat_map.md`.

## Confirmed-good canon from the full review

- Dev's blackout count/escalation, well-contact trigger mechanism, both confirmed consistent (fixed early bugs in ch.8/9/10).
- Full arc through eclipse night (ch.35) confirmed clean: recruiter contacts → doctrine reveal → Elias mole arc → ring proposal → three genuinely distinct security leaks (Elias/mole, ch.29 sightline, ch.34 scheduling gap) → ring finalized at 10 → Halloran's murder by Drake's splinter faction → Drake's eclipse-night standoff.
- **Ch.36:** ritual begins, all ten channels connect, distribution working. Drake's people open fire; Hollis wounded. Fixed a contradiction where the chapter's closing line attributed the gunfire to "Drake's own carefully planned disruption," directly contradicting his ch.35 promise to only watch — reattributed to followers he can't fully control, paralleling Halloran's own splinter-faction fate.
- **Ch.37:** Drake's people had planted a sabotage stake (iron, hidden in the dirt) at Delacroix's position before the ring ever arrived — pre-existing sabotage, not live disruption. Mara finds and pulls it under pressure, restoring even distribution. Drake admits to planting it afterward, consistent with his cold, patient characterization. Minor unfixed soft-timing note: "eleven minutes into totality" + "two minutes left" doesn't sum precisely to ch.35's stated 15-minute totality window, but within normal narrative slack for a fast action scene, not treated as a hard bug.
- **Ch.38:** Dev's internal fight against the bargain itself (personified pressure, not a physical attacker) — refuses it, draws strength from the ring's collective support rather than facing it alone the way Eleanor did. Distribution completes, eclipse ends, Dev survives whole.
- **Ch.39:** dawn aftermath — distribution held clean across all ten, Hollis stable (shoulder wound, will recover), Drake's outbuilding found abandoned and deliberately cleared, Odette admits she was wrong about the doctrine's inevitability, Dev commits to watching for other affected families going forward. Matches beat_map exactly.
- **Ch.40:** closed council session, Millbrook case (19 years ago) confirms Drake operated long before Dev, Denise becomes valley advisor, documentation project begins. Matches beat_map.
- **Ch.41:** Dev's clean bloodwork, Odette's and Castellan's visits, Delacroix's dinner teased. Matches beat_map.
- **Ch.42:** Eleanor/Ambrose wife reveal (ring, photograph). Fixed one filler "kind of" ("only a tired kind of gravity"). See genealogy note above.
- **Ch.43:** town meeting, Yusuf thanks the ring by name, Walt Pruitt's vindication, Farrow's daughter thanks Dev, Yusuf/Denise reflect on his growth. Matches beat_map exactly. No fixes needed.
- **Ch.44:** Denise's kitchen scene (her fifty years now "obsolete," well "ordinary again"), Odette's real cost (lost her husband's exact proposal words, not the memory itself), private dinner honoring both women. Matches beat_map exactly. No fixes needed.
- **Ch.45 (FINALE):** Ambrose's hidden letter found behind a false panel confirms his own doubt and that the doctrine predates him ("my grandfather began" it); final porch scene between Dev and Priya; ends on the open Book 4 hook (Drake at large, other families exist). Matches beat_map exactly. No fixes needed.

## Review log (short form — full detail in each chapter's commit message on GitHub)

✅ **ch.1-45 — FULL SEQUENTIAL REVIEW COMPLETE.** All fixes live and pushed.

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
| 38 | OK — Dev's internal turning point; Eleanor/Ambrose flag raised, resolved by ch.45 |
| 39 | OK — dawn aftermath, matches beat_map exactly |
| 40-41 | OK — council session, Millbrook case, Dev's clean bloodwork |
| 42 | Fixed: filler "kind of gravity"; Eleanor/Ambrose wife reveal confirmed |
| 43-45 | OK — town meeting, Denise/Odette honored, Ambrose's letter, finale. Genealogy flag closed (see Locked facts). |

## Pending decisions for Zia

1. ~~Continue the sequential review ch.40-45?~~ **Done — full book reviewed, 2026-09-17.**
2. Commission a dedicated "some/something" hedge-word sweep across all 45 chapters? Still the single biggest remaining defect, book-wide. Not yet greenlit — needs an explicit go-ahead before any session starts it, since it's real, substantial work across all 45 chapters.

## Proofreading — Last Verified
- Run: 2026-09-16, 45 chapters scanned, 99,892w, 0 hard violations.
- Full report: `novels/amity-falls-book-3/PROOFREAD_REPORT.md`
