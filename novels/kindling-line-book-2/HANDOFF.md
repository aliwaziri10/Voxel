# HANDOFF — Kindling Line Book 2 Polish Pass

STATUS AS OF 2026-09-27 (updated): All 45 chapters exist and are pushed.
This file tracks a cross-session polish pass authorized by Zia with no
budget constraint - quality is the only priority, and Zia has explicitly
said do NOT strip em-dashes on a chapter that is structurally broken.
Fix the chapter completely first. ANY session picking up this work must
read this file FIRST, before touching a chapter, and must UPDATE this
file's table in the SAME commit as any chapter edit, before ending its
turn. Do not batch updates for later.

## CRITICAL, READ THIS BEFORE ANYTHING ELSE

Four defect categories found so far, all serious enough that every
remaining unconfirmed chapter must be checked for them before any
em-dash work is done on it:

1. **Wrong magic system.** Some generated chapters describe a "burner's
   brand," "ward-crew," "flare-back" system where workers physically
   bear ward-loads and carry visible burn scars. This is NOT the
   established mechanic. Book 1 and the locked architecture establish
   the Kindling: an involuntary flame that steals YEARS OF LIFE,
   transferred to whoever stands nearest, leaving a silver tracer mark
   on skin (chapter_04.md's Lower Spine anchor description is a clean
   reference example of the correct mechanic). If a chapter uses
   burns/brands/physical load-bearing instead of years-of-life
   cost-transfer, it is not a style problem, it is using a different
   magic system and must be rewritten.
2. **Character name drift.** Chapter 1 (correct) establishes Lord
   Malrik Thorne as House Thorne's head, with grandfather/father/himself
   as the three generations of ward service. The original chapter 3 had
   invented a different person, "Lord Corvin Thorne," with a different
   family lineage. ANY chapter featuring Thorne must be checked against
   chapter_01.md's actual text for name and lineage consistency, not
   against the beat map summary alone. Kael's father is Valerius
   Ashworth, confirmed consistent through ch.6.
3. **Plot front-loading (three variants seen so far).**
   - Original ch.2/3: full confrontation + full "together" resolution,
     days into the story.
   - Original ch.4 AND original ch.5 AND original ch.6 (three separate
     chapters, independently): each used the EXACT scripted
     confrontation line locked for ch.16-18 ("I'm not asking you to
     tell me everything. I'm asking you to stop deciding what I don't
     need to know") verbatim. This line is now confirmed to be a
     recurring generation artifact, not a one-off - CHECK EVERY
     REMAINING CHAPTER FOR THIS EXACT SENTENCE, especially ch.9, 13-15,
     and anything before ch.16.
   - Original ch.6 additionally invented a Sol "vision/gift" mechanic
     (unprompted precognitive flashes) that does not exist anywhere in
     brief.txt or the established magic system, and used it to reveal
     the "Ward Deed of Succession" by name six chapters before it is
     even supposed to be discovered (ch.13-15) and fourteen chapters
     before it is supposed to be understood (ch.20). Any chapter that
     names "Ward Deed of Succession" before ch.13 is broken on this
     ground alone, regardless of anything else in it.
   The locked beat map spaces the Kael-pattern arc out deliberately:
   ch.3 = Sol notices and privately files away one instance. ch.4-6 (as
   rewritten) = further small instances, noticed, named quietly between
   Sol and Kael once or twice, never with the scripted line, never
   resolved. ch.5-8 = Kael's first small unilateral acts as auditor,
   not yet formally "named as a problem" at the Council/plot level
   (Sol naming it privately to Kael in ch.6 is fine and was kept; a
   full public/structural naming is still ch.9's job). ch.9 = pattern
   formally named. ch.13-15 = infiltration set piece, Ward Deed
   discovered but not understood. ch.16-18 = entry-pass discovery +
   THIS is where the scripted confrontation line belongs. ch.20 = Ward
   Deed fully understood. ch.26-28 = solo handling backfires, injury,
   first "I love you." ch.33-35 = the real rupture, UNRESOLVED. ch.36-39
   = repair, Kael formally cedes unilateral authority. Check every
   early chapter (roughly 2-20) against brief.txt's locked beat for its
   SPECIFIC chapter number, not just its general subject.

Given this, the workstream priority is: **structural/continuity
correctness comes before em-dash stripping, on every chapter, not
after.** A full rewrite already includes a clean em-dash-free draft, so
those two tasks collapse into one for a broken chapter, and stay
separate only for a chapter that turns out to be genuinely fine.

## Chapter table

Columns: chapter / structural check done? / structural verdict / em-dash
done? / genre call / notes.

| Ch | Structural check | Verdict | Em-dash done | Genre call | Notes |
|----|-------------------|---------|---------------|------------|-------|
| 01 | yes | fine, no rewrite needed | yes | keep, confirmed well-balanced | em-dashes stripped 2026-09-27 |
| 02 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to locked Council-vote/appointment beat | wrong magic system (burner's brand) removed, invented Vane council-seat/signet-ring lore removed, front-loaded rupture content removed. Commit 26e8ec17b19c620edba38cb550073701727c8cab |
| 03 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to locked "notices and files away" beat | Thorne name fixed Corvin to Malrik, front-loaded confrontation/resolution removed. Commit f9c72347023dc8f0f6125eee1b9dbc581e57c6e1 |
| 04 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to a second small "noticed, not confronted" beat | original used the ch.16-18 scripted line verbatim + fully resolved the arc 3 days in. Rewrite: Kael solo-surveys Lower Spine anchor, finds unexplained cut seam, doesn't report same-day; Sol independently finds a diversion-route diagram with a missing appendix; both notice, name once, don't resolve. Commit 9e10b3250e00cea2973a7d3a31ef9ed0874e1d8f |
| 05 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to locked ch.5-8 Thorne-public-proposal beat | original used the scripted line verbatim again + fully resolved into "together" agreement + had a stray corrupted non-Latin character from a bad generation pass. Rewrite: keeps Thorne's public reform proposal speech (with the required locked line "a house that has already paid the cost...") intact, keeps Sol memorizing the Thorne seal (satisfies brief rule 3's "establish Sol has seen the seal" requirement), removes the scripted confrontation + resolution, ends with Kael quietly scheduling an unannounced solo site visit to Kestrel's Hollow that he doesn't show Sol. Commit 3ae56edfffd60c119a1786b7b14d202e92aae8c0 |
| 06 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to a quiet escalation of Sol's private noticing | original used the scripted line a THIRD time, AND invented an unestablished Sol "vision/precognitive gift" mechanic to reveal "Ward Deed of Succession" by name 14 chapters early (locked ch.20 reveal). Rewrite: keeps the three-minor-Thorne-wards solo audit day, keeps Sol memorizing/hand-copying the Thorne knot seal (no gift, just diligence), Sol tells Kael plainly she's "keeping a private count" of small unilateral decisions without a confrontation scene, no Ward Deed mention anywhere. Commit 87c3c65c9bbf149cbcc49334f2276a30ce9f96f9 |
| 07 | no | UNCHECKED | no | unknown | also verify against 2300w floor note; CHECK FOR THE SCRIPTED LINE, it has now appeared in 3 of the last 3 chapters checked |
| 08 | no | UNCHECKED | no | unknown | CHECK FOR THE SCRIPTED LINE |
| 09 | partial (read for genre only, not for the two defect categories) | needs re-check | no | rebalance suspected, unconfirmed for structural issues | re-open and check against defect categories 1-4 above; this IS the correct chapter for the pattern to be formally named (not the confrontation line itself, that's still ch.16-18) |
| 10 | no | UNCHECKED | no | unknown | |
| 11 | no | UNCHECKED | no | unknown | |
| 12 | no | UNCHECKED | no | unknown | |
| 13 | no | UNCHECKED | no | unknown | ALSO needs date header fix regardless of structural check outcome; this is where "Ward Deed of Succession" may FIRST be named (discovered, not understood) - if it was already named in an earlier chapter, that earlier chapter has the defect, not this one |
| 14 | no | UNCHECKED | no | unknown | |
| 15 | no | UNCHECKED | no | unknown | regenerated once during original run (meta-leak) |
| 16 | no | UNCHECKED | no | unknown | this is the locked entry-pass discovery chapter AND the correct home for the scripted confrontation line - if that line already appears in an earlier chapter (it has, 3 times, all now fixed), confirm THIS chapter still has its own full, undamaged version of the scene |
| 17 | no | UNCHECKED | no | unknown | |
| 18 | no | UNCHECKED | no | unknown | |
| 19 | no | UNCHECKED | no | unknown | |
| 20 | no | UNCHECKED | no | unknown | longest chapter, check for trim as well as structure; this is where Ward Deed of Succession should be FULLY UNDERSTOOD for the first time |
| 21 | no | UNCHECKED | no | unknown | |
| 22 | no | UNCHECKED | no | unknown | regenerated once during original run (unfinished sentence) |
| 23 | no | UNCHECKED | no | unknown | generated on the retry run, has not been read at all yet |
| 24 | no | UNCHECKED | no | unknown | |
| 25 | no | UNCHECKED | no | unknown | |
| 26 | no | UNCHECKED | no | unknown | |
| 27 | no | UNCHECKED | no | unknown | |
| 28 | no | UNCHECKED | no | unknown | this is the locked "I love you" chapter, check it hasn't already happened earlier in a broken chapter |
| 29 | no | UNCHECKED | no | unknown | |
| 30 | no | UNCHECKED | no | unknown | |
| 31 | no | UNCHECKED | no | unknown | |
| 32 | partial (read for genre only) | genre confirmed good, structural defect categories NOT yet checked | no | keep, confirmed well-executed, do not pad | re-open and check against defect categories 1-4 above |
| 33 | no | UNCHECKED | no | unknown | this is the locked rupture chapter, check it hasn't already happened earlier, and that it stays UNRESOLVED per brief.txt rule 8 |
| 34 | no | UNCHECKED | no | unknown | highest em-dash count in original generation, but do not strip until structurally checked |
| 35 | no | UNCHECKED | no | unknown | |
| 36 | no | UNCHECKED | no | unknown | |
| 37 | no | UNCHECKED | no | unknown | |
| 38 | no | UNCHECKED | no | unknown | this is the locked first-intimate-scene chapter |
| 39 | no | UNCHECKED | no | unknown | |
| 40 | no | UNCHECKED | no | unknown | regenerated once during original run (meta-leak) |
| 41 | no | UNCHECKED | no | unknown | check the explicit non-alteration-of-mechanic line is still present and uses the correct (years-of-life) mechanic |
| 42 | no | UNCHECKED | no | unknown | |
| 43 | no | UNCHECKED | no | unknown | longest along with ch.20, check for trim as well as structure |
| 44 | no | UNCHECKED | no | unknown | |
| 45 | no | UNCHECKED | no | unknown | check the final Keeper line is still institutional-not-personal |

## Additional known issues to fix as encountered

- `chapters_date_report.md` in this folder has a fuller date-consistency
  report from the original generation run - check it, but treat it as
  possibly stale now that chapters 2-6 have been substantially rewritten
  with corrected dates carried over unchanged (10, 11, 12, 13, and 14
  Sunspire respectively, all still correct and sequential).
- Every chapter, before rewrite, carried a generation-log warning that
  the automated humanizer pass failed and fell back to pre-humanizer
  text. This means NOTHING in this book has been through a successful
  automated smoothing pass. Manual review carries more weight than usual
  on every remaining chapter.
- The original generation log's em-dash counts do not reliably match a
  direct manual count of the same chapter. Do not trust the log number;
  always verify by reading the actual current chapter text.
- brief.txt holds the full locked beat map (all 15 numbered rules) and
  should be re-fetched at the start of any session before checking
  chapters against it from memory.
- The scripted ch.16-18 confrontation line has now leaked verbatim into
  THREE separate original chapters (4, 5, 6). Treat this as a
  high-probability recurring defect in any remaining unchecked chapter,
  not a one-off - search each chapter's text for it specifically before
  clearing the chapter.

## Progress log (append one line per chapter as you finish it)

- 2026-09-27: ch.1 em-dash strip done, genre confirmed keep, commit 761229040d773806521b7e15f32e87b8aa39ff3c
- 2026-09-27: ch.2 FULL REWRITE (wrong magic system, invented lore, front-loaded plot all fixed), commit 26e8ec17b19c620edba38cb550073701727c8cab
- 2026-09-27: ch.3 FULL REWRITE (Thorne name continuity break, front-loaded plot fixed), commit f9c72347023dc8f0f6125eee1b9dbc581e57c6e1
- 2026-09-27: discovered structural defects go deeper than cosmetic em-dash issues; workstream priority changed to structural-check-first, see CRITICAL section above
- 2026-09-27: ch.4 FULL REWRITE (verbatim ch.16-18 scripted line used 3 days into story, plus full premature resolution of the Kael-pattern arc), commit 9e10b3250e00cea2973a7d3a31ef9ed0874e1d8f
- 2026-09-27: ch.5 FULL REWRITE (scripted line again + premature resolution + corrupted character), commit 3ae56edfffd60c119a1786b7b14d202e92aae8c0
- 2026-09-27: ch.6 FULL REWRITE (scripted line a third time + invented unestablished "vision" mechanic + Ward Deed of Succession named 14 chapters early), commit 87c3c65c9bbf149cbcc49334f2276a30ce9f96f9
- 2026-09-27: scripted line confirmed as a recurring cross-chapter generation artifact (3 for 3 so far) - added explicit search instruction to CRITICAL section and every remaining UNCHECKED row

## Protocol for any session picking this up

1. Read this file in full before opening any chapter, especially the
   CRITICAL section above. Re-fetch brief.txt fresh, do not rely on a
   remembered summary of it.
2. For any chapter marked UNCHECKED: read the actual chapter text first.
   Check it against chapter_01.md through chapter_06.md (the
   confirmed-correct chapters) for magic-system consistency, character
   name/lineage consistency, and against brief.txt's locked beat for
   THAT SPECIFIC chapter number - including an explicit text search for
   the ch.16-18 scripted line and for "Ward Deed of Succession" in any
   chapter before ch.13.
3. If broken: full rewrite, matching the locked beat, correct magic
   system, correct names, and no em-dashes in the same pass.
4. If genuinely fine: strip only the em-dashes.
5. Either way: update this chapter's row (structural check, verdict,
   em-dash done, genre call, notes) and append one line to the Progress
   log with the commit sha, in the same commit as the chapter edit.
6. Do not mark `continuity_voice_canon_review_complete: true` in
   `book_config.json` until every row above shows a structural check.
