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

Three defect categories found so far, all serious enough that every
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
   Ashworth, confirmed consistent through ch.4.
3. **Plot front-loading.** This is the most common and most damaging
   defect and now includes a THIRD variant discovered in chapter 4:
   - Original ch.2/3: jumped straight to full confrontation, full
     naming of Kael's pattern, and a resolved "together" agreement,
     days into the story.
   - Original ch.4: used the EXACT scripted confrontation line locked
     for ch.16-18 ("I'm not asking you to tell me everything. I'm
     asking you to stop deciding what I don't need to know") verbatim,
     three days into the story, then fully resolved it with a
     negotiated agreement that preempted the ch.36-39 repair beat.
   The locked beat map spaces the Kael-pattern arc out deliberately:
   ch.3 = Sol notices and privately files away one instance. ch.4 (as
   rewritten) = a second small instance, still not confronted. ch.5-8 =
   Kael's first small unilateral act as auditor, not yet named as a
   problem. ch.9 = pattern formally named. ch.13-15 = infiltration set
   piece. ch.16-18 = entry-pass discovery + THIS is where the scripted
   confrontation line belongs, not earlier. ch.20 = Ward Deed fully
   understood. ch.26-28 = solo handling backfires, injury, first "I
   love you." ch.33-35 = the real rupture, left UNRESOLVED. ch.36-39 =
   repair, Kael formally cedes unilateral authority. Check every early
   chapter (roughly 2-20) against brief.txt's locked beat for its
   SPECIFIC chapter number, not just its general subject or whether the
   scripted lines "sound right" - a scripted line appearing early is
   itself a defect even if every other detail checks out.

Given this, the workstream priority is: **structural/continuity
correctness comes before em-dash stripping, on every chapter, not
after.** Do not spend time stripping em-dashes from a chapter you have
not confirmed is structurally sound. A full rewrite already includes a
clean em-dash-free draft, so those two tasks collapse into one for a
broken chapter, and stay separate only for a chapter that turns out to
be genuinely fine.

## Chapter table

Columns: chapter / structural check done? / structural verdict / em-dash
done? / genre call / notes.

| Ch | Structural check | Verdict | Em-dash done | Genre call | Notes |
|----|-------------------|---------|---------------|------------|-------|
| 01 | yes | fine, no rewrite needed | yes | keep, confirmed well-balanced | em-dashes stripped 2026-09-27 |
| 02 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to locked Council-vote/appointment beat | wrong magic system (burner's brand) removed, invented Vane council-seat/signet-ring lore removed, front-loaded rupture content removed. Commit 26e8ec17b19c620edba38cb550073701727c8cab |
| 03 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to locked "notices and files away" beat | Thorne name fixed Corvin to Malrik, front-loaded confrontation/resolution removed. Commit f9c72347023dc8f0f6125eee1b9dbc581e57c6e1 |
| 04 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to a second small "noticed, not confronted" beat building toward ch.5-8 | original ch.4 used the ch.16-18 scripted confrontation line verbatim and fully resolved the Kael-pattern arc 3 days into the story, preempting ch.9, ch.16-18, and ch.36-39. Rewrite: Kael solo-surveys Lower Spine anchor, finds an unexplained cut seam, doesn't report it same-day; Sol independently finds a network diagram showing a diversion route with a missing appendix; both notice the other's small unilateral choice, name it once, do not resolve it, agree only to walk the diversion route together next. Ends on open hook (unnamed site at end of dotted line). Names/magic system verified consistent with ch.1. Commit 9e10b3250e00cea2973a7d3a31ef9ed0874e1d8f |
| 05 | no | UNCHECKED | no | unknown | check for all three defect categories above, especially verbatim/near-verbatim use of the ch.16-18 confrontation line or any full resolution of the pattern before ch.36-39 |
| 06 | no | UNCHECKED | no | unknown | |
| 07 | no | UNCHECKED | no | unknown | also verify against 2300w floor note |
| 08 | no | UNCHECKED | no | unknown | |
| 09 | partial (read for genre only, not for the two defect categories) | needs re-check | no | rebalance suspected, unconfirmed for structural issues | re-open and check against defect categories 1-3 above, not just genre balance; this is the LOCKED "pattern formally named" chapter, confirm it isn't redundant with ch.4's rewritten "noticed, not confronted" beat |
| 10 | no | UNCHECKED | no | unknown | |
| 11 | no | UNCHECKED | no | unknown | |
| 12 | no | UNCHECKED | no | unknown | |
| 13 | no | UNCHECKED | no | unknown | ALSO needs date header fix regardless of structural check outcome |
| 14 | no | UNCHECKED | no | unknown | |
| 15 | no | UNCHECKED | no | unknown | regenerated once during original run (meta-leak) |
| 16 | no | UNCHECKED | no | unknown | this is the locked entry-pass discovery chapter AND the correct home for the scripted confrontation line ("I'm not asking you to tell me everything...") - if that line already appears in an earlier chapter, that earlier chapter needs re-review even if already marked fixed |
| 17 | no | UNCHECKED | no | unknown | |
| 18 | no | UNCHECKED | no | unknown | |
| 19 | no | UNCHECKED | no | unknown | |
| 20 | no | UNCHECKED | no | unknown | longest chapter, check for trim as well as structure |
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
| 32 | partial (read for genre only) | genre confirmed good, structural defect categories NOT yet checked | no | keep, confirmed well-executed, do not pad | re-open and check against defect categories 1-3 above |
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
  possibly stale now that chapters 2, 3, and 4 have been substantially
  rewritten with corrected dates carried over unchanged (10, 11, and 12
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

## Progress log (append one line per chapter as you finish it)

- 2026-09-27: ch.1 em-dash strip done, genre confirmed keep, commit 761229040d773806521b7e15f32e87b8aa39ff3c
- 2026-09-27: ch.2 FULL REWRITE (wrong magic system, invented lore, front-loaded plot all fixed), commit 26e8ec17b19c620edba38cb550073701727c8cab
- 2026-09-27: ch.3 FULL REWRITE (Thorne name continuity break, front-loaded plot fixed), commit f9c72347023dc8f0f6125eee1b9dbc581e57c6e1
- 2026-09-27: discovered structural defects go deeper than cosmetic em-dash issues; workstream priority changed to structural-check-first, see CRITICAL section above
- 2026-09-27: ch.4 FULL REWRITE (found and fixed a new front-loading variant: verbatim ch.16-18 scripted line used 3 days into story, plus full premature resolution of the Kael-pattern arc), commit 9e10b3250e00cea2973a7d3a31ef9ed0874e1d8f

## Protocol for any session picking this up

1. Read this file in full before opening any chapter, especially the
   CRITICAL section above. Re-fetch brief.txt fresh, do not rely on a
   remembered summary of it.
2. For any chapter marked UNCHECKED: read the actual chapter text first.
   Check it against chapter_01.md through chapter_04.md (the four
   confirmed-correct chapters) for magic-system consistency, character
   name/lineage consistency, and against brief.txt's locked beat for
   THAT SPECIFIC chapter number - including checking whether any later
   chapter's scripted dialogue (e.g. the ch.16-18 line) has leaked into
   an earlier chapter.
3. If broken: full rewrite, matching the locked beat, correct magic
   system, correct names, and no em-dashes in the same pass.
4. If genuinely fine: strip only the em-dashes.
5. Either way: update this chapter's row (structural check, verdict,
   em-dash done, genre call, notes) and append one line to the Progress
   log with the commit sha, in the same commit as the chapter edit.
6. Do not mark `continuity_voice_canon_review_complete: true` in
   `book_config.json` until every row above shows a structural check.
