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

Six defect categories found so far, all serious enough that every
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
2. **Invented Sol/Kael soulbond mechanic.** Some chapters invent a
   "bond" where injuries mirror or double between Sol and Kael
   specifically ("the bond doesn't divide it, it doubles it"). This
   directly violates brief.txt rule 15: no ward-binding, no chosen
   buffer role between Sol and Kael, ever - the involuntary
   cost-transfer mechanic from Book 1 must stay uncontrollable and
   non-redirectable, never a private two-person bond.
3. **Character/lore name drift.** Chapter 1 (correct) establishes Lord
   Malrik Thorne as House Thorne's head. The original chapter 3 invented
   "Lord Corvin Thorne." Original chapter 8 independently described the
   Thorne house seal as "a hound's head crowned with thorns" - WRONG;
   the correct, established Thorne mark (set in ch.5-7) is a three-strand
   unbroken knot with a drop/flame/feather sigil at each terminus, in
   violet-and-copper house colors, wax dark and near-black. ANY chapter
   describing the Thorne seal or Thorne colors must match this exactly,
   not reinvent it. Kael's father is Valerius Ashworth, confirmed
   consistent through ch.8.
4. **Plot front-loading - now SIX variants confirmed, the most damaging
   being the ch.16-18 beat leaking wholesale into ch.8:**
   - Original ch.2/3: full confrontation + full resolution, days in.
   - Original ch.4, 5, 6, 7, AND 8 (FIVE separate chapters): each used
     the EXACT scripted confrontation line locked for ch.16-18 verbatim
     ("I'm not asking you to tell me everything. I'm asking you to stop
     deciding what I don't need to know"). 5 for 5 so far - CHECK EVERY
     REMAINING CHAPTER FOR THIS EXACT SENTENCE.
   - Original ch.6 invented a Sol "vision/gift" mechanic to reveal "Ward
     Deed of Succession" by name 14 chapters early. Original ch.7 named
     it again unprompted.
   - **Original ch.8 was the worst case yet: it staged the ENTIRE ch.16-18
     set piece verbatim, eight chapters early** - Sol finding a
     Thorne-sealed entry pass hidden in Kael's coat, for a site he hadn't
     mentioned, followed by the full scripted confrontation and a
     "co-lead auditor" resolution. This is not a variation, it IS the
     locked ch.16-18 scene, just moved. When you reach the real ch.16-18,
     confirm it hasn't already been "used up" by an earlier broken
     chapter's leak - if a later chapter's own content looks thin or
     redundant, check whether an earlier chapter (now fixed) had stolen
     its material, and confirm the later chapter still delivers ITS
     locked beat in full.
   The locked beat map spaces the Kael-pattern arc out deliberately:
   ch.3 = Sol notices and privately files away one instance. ch.4-8 (as
   rewritten) = further small instances, noticed, named quietly, never
   with the scripted line, never resolved - by ch.8 this should be
   dramatic irony (reader knows something Sol doesn't, or vice versa),
   NOT a discovery scene. ch.9 = pattern formally named. ch.13-15 =
   infiltration set piece, Ward Deed discovered but not understood.
   ch.16-18 = entry-pass discovery + the scripted confrontation line
   belongs HERE, nowhere earlier. ch.20 = Ward Deed fully understood.
   ch.26-28 = solo handling backfires, injury, first "I love you."
   ch.33-35 = the real rupture, UNRESOLVED. ch.36-39 = repair, Kael
   formally cedes unilateral authority.
5. **Corrupted/non-Latin stray characters** from bad generation passes
   (found once in original ch.5). Skim for this even in chapters that
   otherwise check out structurally.
6. **Word count floor.** Original ch.7 and ch.8 both ran short before
   rewrite; rewrites were expanded with additional in-scene material
   (not padding) to clear the 1,800-word floor. Check word count on
   every remaining chapter, not just the ones flagged "also verify
   against floor note."

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
| 04 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to a second small "noticed, not confronted" beat | original used the ch.16-18 scripted line verbatim + fully resolved the arc 3 days in. Commit 9e10b3250e00cea2973a7d3a31ef9ed0874e1d8f |
| 05 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to locked ch.5-8 Thorne-public-proposal beat | scripted line again + premature resolution + corrupted character. Commit 3ae56edfffd60c119a1786b7b14d202e92aae8c0 |
| 06 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to a quiet escalation of Sol's private noticing | scripted line a third time + invented Sol "vision" mechanic + Ward Deed named 14 chapters early. Commit 87c3c65c9bbf149cbcc49334f2276a30ce9f96f9 |
| 07 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to Thorne-petition-gathering-signatures beat | scripted line a fourth time + invented mirrored-injury soulbond (violates rule 15) + premature Ward Deed naming. Commit e5ba08ae83bc0ab085e8a0b500ee085df44785a0 |
| 08 | yes | BROKEN - full rewrite done, WORST CASE SO FAR | yes (rewrite is clean) | keep, restored to a dramatic-irony beat (both leads separately noticing, neither confronting) | original staged the ENTIRE ch.16-18 entry-pass-discovery set piece verbatim, 8 chapters early - Sol found a hidden Thorne pass in Kael's coat, full scripted confrontation, resolved into "co-lead auditor" arrangement. Also reinvented the Thorne seal as "a hound's head crowned with thorns," contradicting the established three-strand knot from ch.5-7. Rewrite: Thorne courier delivers a sealed pass for Anchor Seven to Kael's office (seal corrected to match established knotwork/violet-copper), Kael doesn't mention it that evening, Sol separately finds a discrepancy in the Accord's decommissioning register for the same anchor and also doesn't mention it, both hold back, unresolved, ends on Kael's private resolve to check the archive "before" telling her, undercut by his own doubt. NO entry-pass discovery, NO scripted line, NO co-lead resolution. Commit ee2f2f4421878f6b9d920bc02af48d667b643f18 |
| 09 | partial (read for genre only, not for the two defect categories) | needs re-check | no | rebalance suspected, unconfirmed for structural issues | re-open and check against defect categories 1-6 above; this IS the correct chapter for the pattern to be formally named (not the confrontation line itself, that's still ch.16-18); ALSO check whether ch.9's own material was stolen by the original (now-fixed) ch.8's front-loading and needs restoring |
| 10 | no | UNCHECKED | no | unknown | |
| 11 | no | UNCHECKED | no | unknown | |
| 12 | no | UNCHECKED | no | unknown | |
| 13 | no | UNCHECKED | no | unknown | ALSO needs date header fix regardless of structural check outcome; this is where "Ward Deed of Succession" may FIRST be named (discovered, not understood) - if it was already named in an earlier chapter, that earlier chapter has the defect, not this one |
| 14 | no | UNCHECKED | no | unknown | |
| 15 | no | UNCHECKED | no | unknown | regenerated once during original run (meta-leak) |
| 16 | no | UNCHECKED | no | unknown | this is the locked entry-pass discovery chapter AND the correct home for the scripted confrontation line - that scene has now leaked into FIVE earlier chapters (4,5,6,7,8), all fixed; confirm THIS chapter still has its own full, undamaged version, and that Anchor Seven / the anchor status discrepancy set up in ch.8's rewrite pays off here or later, not wasted |
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
| 32 | partial (read for genre only) | genre confirmed good, structural defect categories NOT yet checked | no | keep, confirmed well-executed, do not pad | re-open and check against defect categories 1-6 above |
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
  possibly stale now that chapters 2-8 have been substantially rewritten
  with corrected dates carried over unchanged (10 through 16 Sunspire,
  all still correct and sequential).
- Every chapter, before rewrite, carried a generation-log warning that
  the automated humanizer pass failed and fell back to pre-humanizer
  text. Manual review carries more weight than usual on every remaining
  chapter.
- The original generation log's em-dash counts do not reliably match a
  direct manual count. Do not trust the log number; verify by reading.
- brief.txt holds the full locked beat map (all 15 numbered rules) and
  should be re-fetched at the start of any session before checking
  chapters against it from memory.
- The scripted ch.16-18 confrontation line has now leaked verbatim into
  FIVE separate original chapters (4, 5, 6, 7, 8). Treat this as a
  near-certain recurring defect in any remaining unchecked chapter.
- A mirrored-injury "bond" mechanic between Sol and Kael (found once,
  ch.7) directly violates brief.txt rule 15.
- Anchor Seven (Lower Reach, disused ropewalk site) and its status
  discrepancy (Thorne calls it "decommissioned," the Accord register
  calls it "unresolved"/"contested") were introduced in ch.8's rewrite
  as a planted thread. Whichever session reaches the chapters where this
  should pay off (likely ch.9, possibly folded into ch.13-15's
  infiltration site) should either use it or consciously decide to let
  it resolve quietly - don't let it dangle unaddressed past ch.15.

## Progress log (append one line per chapter as you finish it)

- 2026-09-27: ch.1 em-dash strip done, genre confirmed keep, commit 761229040d773806521b7e15f32e87b8aa39ff3c
- 2026-09-27: ch.2 FULL REWRITE (wrong magic system, invented lore, front-loaded plot all fixed), commit 26e8ec17b19c620edba38cb550073701727c8cab
- 2026-09-27: ch.3 FULL REWRITE (Thorne name continuity break, front-loaded plot fixed), commit f9c72347023dc8f0f6125eee1b9dbc581e57c6e1
- 2026-09-27: discovered structural defects go deeper than cosmetic em-dash issues; workstream priority changed to structural-check-first
- 2026-09-27: ch.4 FULL REWRITE (verbatim ch.16-18 scripted line, full premature resolution), commit 9e10b3250e00cea2973a7d3a31ef9ed0874e1d8f
- 2026-09-27: ch.5 FULL REWRITE (scripted line again + premature resolution + corrupted character), commit 3ae56edfffd60c119a1786b7b14d202e92aae8c0
- 2026-09-27: ch.6 FULL REWRITE (scripted line a third time + invented "vision" mechanic + Ward Deed named 14 chapters early), commit 87c3c65c9bbf149cbcc49334f2276a30ce9f96f9
- 2026-09-27: ch.7 FULL REWRITE (scripted line a fourth time + invented mirrored-injury soulbond violating rule 15 + premature Ward Deed naming), commit e5ba08ae83bc0ab085e8a0b500ee085df44785a0
- 2026-09-27: ch.8 FULL REWRITE (scripted line a fifth time + the ENTIRE ch.16-18 entry-pass set piece staged 8 chapters early + wrong Thorne seal description), commit ee2f2f4421878f6b9d920bc02af48d667b643f18

## Protocol for any session picking this up

1. Read this file in full before opening any chapter, especially the
   CRITICAL section above. Re-fetch brief.txt fresh, do not rely on a
   remembered summary of it.
2. For any chapter marked UNCHECKED: read the actual chapter text first.
   Check it against chapter_01.md through chapter_08.md (the
   confirmed-correct chapters) for magic-system consistency, character
   name/lineage/seal consistency, and against brief.txt's locked beat for
   THAT SPECIFIC chapter number - including an explicit text search for
   the ch.16-18 scripted line, for "Ward Deed of Succession" in any
   chapter before ch.13, and for any mirrored-injury/soulbond language
   between Sol and Kael.
3. If broken: full rewrite, matching the locked beat, correct magic
   system, correct names/seals, and no em-dashes in the same pass.
4. If genuinely fine: strip only the em-dashes.
5. Either way: update this chapter's row (structural check, verdict,
   em-dash done, genre call, notes) and append one line to the Progress
   log with the commit sha, in the same commit as the chapter edit.
6. Do not mark `continuity_voice_canon_review_complete: true` in
   `book_config.json` until every row above shows a structural check.
