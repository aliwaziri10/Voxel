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

Chapters 2 and 3 were found to be badly broken on direct read, not
cosmetically but structurally, and have been FULLY REWRITTEN (not just
em-dash stripped). Two categories of defect found so far, both serious
enough that every remaining unconfirmed chapter must be checked for
them before any em-dash work is done on it:

1. **Wrong magic system.** Some generated chapters describe a "burner's
   brand," "ward-crew," "flare-back" system where workers physically
   bear ward-loads and carry visible burn scars. This is NOT the
   established mechanic. Book 1 and the locked architecture establish
   the Kindling: an involuntary flame that steals YEARS OF LIFE,
   transferred to whoever stands nearest, leaving a silver tracer mark
   on skin. If a chapter uses burns/brands/physical load-bearing instead
   of years-of-life cost-transfer, it is not a style problem, it is
   using a different magic system and must be rewritten.
2. **Character name drift.** Chapter 1 (correct) establishes Lord
   Malrik Thorne as House Thorne's head, with grandfather/father/himself
   as the three generations of ward service. The original chapter 3 had
   invented a different person, "Lord Corvin Thorne," with a different
   family lineage (grandfather/mother/brother), giving nearly the same
   speech. ANY chapter featuring Thorne must be checked against
   chapter_01.md's actual text for name and lineage consistency, not
   against the beat map summary alone.
3. **Plot front-loading.** The original chapters 2 and 3 both jumped
   straight to full confrontation, full naming of Kael's pattern, and a
   resolved "together" agreement, days into the story. The locked beat
   map spaces this out deliberately: Sol notices and privately files the
   pattern away at ch.3, it's formally confronted at ch.9, the entry-pass
   discovery lands at ch.16, and the real rupture is ch.33-35. If an
   early chapter already delivers the full confrontation/resolution,
   later chapters that are supposed to escalate it will read as
   repetitive or redundant. Check every early chapter (roughly 2-20)
   against the locked beat/brief for its specific chapter, not just its
   general subject, before assuming it's fine.

Given this, the workstream priority has changed from the original plan:
**structural/continuity correctness comes before em-dash stripping, on
every chapter, not after.** Do not spend time stripping em-dashes from a
chapter you have not confirmed is structurally sound. A full rewrite
already includes a clean em-dash-free draft, so those two tasks collapse
into one for a broken chapter, and stay separate only for a chapter that
turns out to be genuinely fine.

## Chapter table

Columns: chapter / structural check done? / structural verdict / em-dash
done? / genre call / notes.

| Ch | Structural check | Verdict | Em-dash done | Genre call | Notes |
|----|-------------------|---------|---------------|------------|-------|
| 01 | yes | fine, no rewrite needed | yes | keep, confirmed well-balanced | em-dashes stripped 2026-09-27 |
| 02 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to locked Council-vote/appointment beat | wrong magic system (burner's brand) removed, invented Vane council-seat/signet-ring lore removed, front-loaded rupture content removed. Commit 26e8ec17b19c620edba38cb550073701727c8cab |
| 03 | yes | BROKEN - full rewrite done | yes (rewrite is clean) | keep, restored to locked "notices and files away" beat | Thorne name fixed Corvin to Malrik, front-loaded confrontation/resolution removed. Commit f9c72347023dc8f0f6125eee1b9dbc581e57c6e1 |
| 04 | no | UNCHECKED | no | unknown | check for both defect categories above before anything else |
| 05 | no | UNCHECKED | no | unknown | also verify against 2300w floor note |
| 06 | no | UNCHECKED | no | unknown | |
| 07 | no | UNCHECKED | no | unknown | also verify against 2300w floor note |
| 08 | no | UNCHECKED | no | unknown | |
| 09 | partial (read for genre only, not for the two defect categories) | needs re-check | no | rebalance suspected, unconfirmed for structural issues | re-open and check against defect categories 1-3 above, not just genre balance |
| 10 | no | UNCHECKED | no | unknown | |
| 11 | no | UNCHECKED | no | unknown | |
| 12 | no | UNCHECKED | no | unknown | |
| 13 | no | UNCHECKED | no | unknown | ALSO needs date header fix regardless of structural check outcome |
| 14 | no | UNCHECKED | no | unknown | |
| 15 | no | UNCHECKED | no | unknown | regenerated once during original run (meta-leak) |
| 16 | no | UNCHECKED | no | unknown | this is the locked entry-pass discovery chapter, check especially carefully that it hasn't already happened in an earlier broken chapter |
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
| 33 | no | UNCHECKED | no | unknown | this is the locked rupture chapter, check it hasn't already happened earlier |
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
  possibly stale now that chapters 2 and 3 have been substantially
  rewritten with corrected dates carried over unchanged (both kept their
  original chapter_date headers, 10 Sunspire and 11 Sunspire, which are
  still correct).
- Every chapter, before rewrite, carried a generation-log warning that
  the automated humanizer pass failed and fell back to pre-humanizer
  text. This means NOTHING in this book has been through a successful
  automated smoothing pass. Manual review carries more weight than usual
  on every remaining chapter.
- The original generation log's em-dash counts do not reliably match a
  direct manual count of the same chapter. Do not trust the log number;
  always verify by reading the actual current chapter text.

## Progress log (append one line per chapter as you finish it)

- 2026-09-27: ch.1 em-dash strip done, genre confirmed keep, commit 761229040d773806521b7e15f32e87b8aa39ff3c
- 2026-09-27: ch.2 FULL REWRITE (wrong magic system, invented lore, front-loaded plot all fixed), commit 26e8ec17b19c620edba38cb550073701727c8cab
- 2026-09-27: ch.3 FULL REWRITE (Thorne name continuity break, front-loaded plot fixed), commit f9c72347023dc8f0f6125eee1b9dbc581e57c6e1
- 2026-09-27: discovered structural defects go deeper than cosmetic em-dash issues; workstream priority changed to structural-check-first, see CRITICAL section above

## Protocol for any session picking this up

1. Read this file in full before opening any chapter, especially the
   CRITICAL section above.
2. For any chapter marked UNCHECKED: read the actual chapter text first.
   Check it against chapter_01.md, chapter_02.md, and chapter_03.md
   (the three confirmed-correct chapters) for magic-system consistency,
   character name/lineage consistency, and against `brief.txt`'s locked
   beat for THAT SPECIFIC chapter number, not just its general subject.
3. If broken: full rewrite, matching the locked beat, correct magic
   system, correct names, and no em-dashes in the same pass.
4. If genuinely fine: strip only the em-dashes.
5. Either way: update this chapter's row (structural check, verdict,
   em-dash done, genre call, notes) and append one line to the Progress
   log with the commit sha, in the same commit as the chapter edit.
6. Do not mark `continuity_voice_canon_review_complete: true` in
   `book_config.json` until every row above shows a structural check.
