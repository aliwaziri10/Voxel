## PROCEDURE (READ FIRST)

Defers to `novels/EDITORIAL_CHARTER.md` for methodology. This file = this book's own facts: locked word floor, canon, review log.

Mechanical proofreading (word count/em-dash/"particular"/meta-leak) is DONE — see `PROOFREAD_REPORT.md`. The deeper continuity/voice/canon pass is ALSO DONE (ch.1-45). The **repeated-words pass is ALSO NOW DONE (ch.1-45, see below)**. All three mechanical/craft passes are complete.

**Repeated-words pass standard (Zia's explicit instruction, 2026-09-17): only fix a distinctive word (noun/verb/adjective with real weight) that clusters within a paragraph or two, perceptible to an actual reader. Never touch common function/connector words (though, back, like, still, time, something, right, he'd, himself, etc.) even if the mechanical report's raw count flags them 10-20+ times in a chapter — that's noise, not a defect, at normal chapter length. A word repeating because it's the chapter's actual subject (e.g. "name"/"stone" in the chapter where a name is found in a stone; "years"/"fifty" in Denise's chapter about her fifty years) is earned, not a tic — leave it. When in doubt, leave it alone. Do not "clean" a chapter that has no real clustering issue — over-fixing spoils the book.**

**Rule going forward: keep log entries SHORT.** One line per chapter: status + the one thing that mattered, if anything. The git commit message on each fix already holds the full detail — don't duplicate it here. This file bloated past 7,000 words once already; don't let it happen again.

**Rule going forward (2): stamp this file after every chapter (or every small cluster of chapters) actually checked in a session — not batched at the very end. If the session is interrupted, the log must reflect exactly what's been checked so far, not lag behind the live work.** Still fix genuine defects in the chapter file itself the moment they're found.

**ALL THREE MECHANICAL/CRAFT PASSES ARE NOW COMPLETE AS OF 2026-09-17: mechanical proofread, sequential continuity/voice/canon review, repeated-words pass. The only remaining open item is the "some/something" hedge sweep (not yet greenlit by Zia — see Pending decisions). Once that's resolved one way or the other, this book is publish-ready.**

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

## Continuity/voice/canon review log (COMPLETE — full detail in each chapter's commit message on GitHub)

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

## Repeated-words pass log (COMPLETE — full detail 2026-09-17)

Standard applied: see PROCEDURE above. Most of PROOFREAD_REPORT.md's flagged words are ordinary function-word frequency, not real defects — only genuine clustering of a distinctive word gets fixed. "Checked, OK" means the chapter was read and its overused_words list evaluated against the standard, not that any change was made — most chapters need none.

**Final rate across all 45 chapters: only 3 real fixes (ch.4, ch.8, ch.11) — confirmed rare, because this book already had multiple dedicated "kind of"/filler sweeps done during the earlier continuity pass. Everything else flagged by the mechanical report was genuinely earned (chapter's actual subject) or ordinary prose frequency.**

| Ch | Status |
|---|---|
| 1 | OK — no real clustering. "Stone" (9x) is the chapter's earned central object. |
| 2 | OK — "porch"/"steps" repeat because the whole chapter happens on a porch. |
| 3 | OK — "stone"/"name" are the literal plot mechanism this chapter. Earned. |
| 4 | **Fixed:** "cold" describing the same cup of tea 3x in one scene — trimmed one instance. |
| 5 | OK — "name"/"ledger"/"record"/"marriage" earned; chapter is about genealogical records. |
| 6 | OK — "years"/"decades"/"fifty" earned (Denise's fifty-years chapter); "take small" is a deliberate thematic phrase. |
| 7 | OK — "porch"/"cold"/"eight years" all earned (setting + Caleb's own backstory). |
| 8 | **Fixed:** bare filler "a kind of understanding" → "an understanding." |
| 9 | OK — flagged "kind of" ("the kind of thing you'd miss...") is attached to something concrete — legitimate per the book's own rule. |
| 10 | OK — same as ch.9, flagged "kind of" is concrete/legitimate. "Well"/"ritual" earned. |
| 11 | **Fixed:** bare filler "a tired kind of honesty" → "a tired, plain honesty." |
| 12 | OK — no real clustering. |
| 13 | OK — "number"/"days" earned (chapter about an untraceable ID number). |
| 14 | OK — "version"/"ending" earned (chapter is literally a debate between two endings). |
| 15 | OK — "read" earned (Wren's full read is the chapter's subject). |
| 16 | OK — "shape"/"pattern" earned (Mara literally mapping a pattern). |
| 17 | OK — "button" earned (the chapter's central object). |
| 18 | OK — "square"/"body"/"clinic" earned (collapse-and-aftermath chapter). |
| 19 | OK — "wall" earned (Mara's diagram wall is the chapter's subject). |
| 20 | OK — high "room" count (25x) is a legitimate narrative device for a group scene in one room, not a tic. |
| 21 | OK — "smaller"/"version" earned (chapter's central contrast: smaller vs. total payment). |
| 22 | OK — "woman"/"headcount" earned (the visitor and the plot-critical detail she reveals). |
| 23 | OK — "timeline"/"afraid" earned (Priya's investigation, Elias's fear — both the chapter's actual subject). |
| 24 | OK — "fear"/"version" earned (chapter's theme: fear as its own generational debt). Flagged "the specific" is attached to a concrete detail, not vague filler. |
| 25 | OK — "nine"/"twelve"/"people"/"ring" all earned — this is the chapter where the ring plan is literally designed. |
| 26 | OK — "door" (metaphor for Dev's unguarded blackout-self) and setting words all earned. |
| 27 | OK — "silence"/"story"/"room" earned (town-meeting chapter about breaking silence). |
| 28 | OK — "trust"x10 earned (Yusuf's whole speech is about narrowing the circle of trust); "kind of" instances concrete/legitimate. |
| 29 | OK — "window"/"board"/"schedule" all earned — literal plot mechanism (the sightline-gap discovery chapter). |
| 30 | OK — "kind of" concrete/legitimate ("the kind of property..."). |
| 31 | OK — "kind of" concrete/legitimate ("the kind of clear autumn sky..."); "cold"x12 earned (porch/frost scene). |
| 32 | OK — "circle"/"center" earned, literal ring-staging chapter. |
| 33 | OK — "used"x7 varied/idiomatic ("used to mark," "used to be," "used to when..."), not repetitive filler. |
| 34 | OK — both "kind of" instances concrete/legitimate; "door" repetition is the literal focal point of the confrontation scene. |
| 35 | OK — "circle"/"perimeter"/"tree"/"line"/"drake" all earned, eclipse-night staging chapter. |
| 36 | OK — "stake"/"circle"/"line"/"hold" all earned, ritual-in-progress chapter. |
| 37 | OK — "iron"/"stake" are the literal sabotage object being fought over; no filler clustering. |
| 38 | OK — "relief" (x6) varied across distinct characters/moments (Delacroix's, Wren's, Priya's, Dev's), not a repeated tic. |
| 39 | OK — "field"/"weeks" earned, dawn-aftermath setting/timeline chapter. |
| 40 | OK — "drake"/"days"/"room" earned (council-session chapter); "kind of" concrete/legitimate. |
| 41 | OK — "ordinary"x8 is a deliberate, earned thematic motif (post-crisis contrast), not a tic. |
| 42 | OK — "name"/"past" earned (genealogy-reveal chapter); no new "kind of" filler beyond the one already fixed. |
| 43 | OK — "hall"x8 is setting-appropriate for the grange-hall town-meeting chapter. |
| 44 | OK — "kind of carrying"/"kind of gratitude" both qualified by a defining clause, not bare filler; left as-is. |
| 45 | OK — "found"/"letter"/"ambrose's" earned (the letter-discovery finale chapter); "kind of" instances concrete/legitimate. |

**FULL 45-CHAPTER REPEATED-WORDS PASS COMPLETE, 2026-09-17.**

## Pending decisions for Zia

1. ~~Continue the sequential review ch.40-45?~~ **Done — full book reviewed, 2026-09-17.**
2. **Commission a dedicated "some/something" hedge-word sweep across all 45 chapters?** Still the single biggest remaining defect, book-wide, and now the ONLY remaining open item before the book is fully publish-ready. Not yet greenlit — needs an explicit go-ahead before any session starts it, since it's real, substantial work across all 45 chapters.

## Proofreading — Last Verified
- Run: 2026-09-16, 45 chapters scanned, 99,892w, 0 hard violations.
- Full report: `novels/amity-falls-book-3/PROOFREAD_REPORT.md`
