# HANDOFF — Kindling Line Book 2 Polish Pass

STATUS AS OF 2026-09-28 (updated): All 45 chapters exist and are pushed.
This file tracks a cross-session polish pass authorized by Zia with no
budget constraint - quality is the only priority, and Zia has explicitly
said do NOT strip em-dashes on a chapter that is structurally broken.
Fix the chapter completely first. ANY session picking up this work must
read this file FIRST, before touching a chapter, and must UPDATE this
file's table in the SAME commit as any chapter edit, before ending its
turn. Do not batch updates for later.

## CRITICAL UPDATE 2026-09-28 — chapters 9-15 audited, found catastrophically broken

A full read-through of chapters 9-15 (previously all marked UNCHECKED)
found the SAME defect categories from chapters 2-8 recurring at massive
scale, plus a new defect. Ch.8 itself remains correctly fixed and is not
part of this problem. Full findings:

- **Ch.9 is the only clean chapter in this range.** Well-executed,
  matches the locked "pattern formally named" beat. No rewrite needed,
  em-dash pass still outstanding.
- **Ch.10, 11, 12, 13, 14, 15 are ALL broken**, and not with minor
  variations - each independently reinvents the Thorne seal WRONG, and
  the "find the Ward Deed" set piece (locked for ch.13-15 ONLY, discovered
  but not understood) has been staged FOUR SEPARATE, MUTUALLY
  CONTRADICTORY times, at three or four different disused ward sites
  (ch.11's Lower Ward Annex, ch.12's site three miles north, ch.14's
  unnamed shaft site, ch.15's Graywater Hollow), each time treating the
  Deed's full legal meaning (the clause 7/12/19 chain locked for ch.20)
  as already fully understood. The story currently has no single canon
  version of how or where the Deed was found.
- **The locked ch.16-18 scripted line** ("I'm not asking you to tell me
  everything. I'm asking you to stop deciding what I don't need to
  know.") appears VERBATIM in ch.12 and ch.15 in addition to the five
  original chapters (4,5,6,7, orig-8) already fixed. That is 7 confirmed
  verbatim instances total across the manuscript's history, 2 of them
  still live and unfixed (ch.12, ch.15).
- **Thorne seal has now been described 9 DIFFERENT WRONG WAYS** across
  ch.10 ("thorn-and-crown"), ch.11 ("vine-and-key"), ch.12 ("hawk's
  head/talon/chain"), ch.13 ("thorned crown/Endure and Bind" motto),
  ch.14 ("thorne branches intertwined with a key"), ch.15 ("coiled
  viper"), plus the three earlier wrong variants already fixed. NONE of
  these match the established canon: three-strand unbroken knot,
  drop/flame/feather sigil at each terminus, violet-and-copper house
  colors, wax dark and near-black (locked ch.5-7, confirmed consistent
  through the fixed ch.8).
- **NEW defect category 7: literal fourth-wall / meta-reference break.**
  Ch.14 contains the sentence "Sol had found it in chapter 8, had held it
  up to the light and asked him what it meant" - the model referencing
  its own chapter numbering INSIDE the story's prose. This is live in
  the current chapter file, not a stale-artifact issue. Any remaining
  chapter must also be scanned for literal "chapter [number]" references
  inside narrative text, not just for plot/seal/line defects.
- **Ch.15 also has a plain continuity/grammar bug**, independent of the
  structural issues: "She did not tell him... She did not tell her..."
  in the same sentence pattern - a pronoun swap error.
- The Anchor Seven planted thread from ch.8's rewrite has NOT paid off
  in any of ch.9-15 - ch.9 mentions Anchor Seven only as one candidate
  site among several, never followed up. Still dangling as of ch.15.

**Conclusion: chapters 10-15 all require full rewrites**, coordinated as
a set so they don't re-collide (i.e. don't just fix ch.10 in isolation
and let ch.11 stage the same stolen beat again - decide the ONE correct
version of the ch.13-15 infiltration/discovery before rewriting any of
them). Do not trust "UNCHECKED" as "probably fine, just not yet read" -
past ch.9, assume broken until confirmed otherwise; the base rate in
this manuscript is now over 90% broken for any chapter not yet verified.

Six ORIGINAL defect categories (still valid, see full descriptions
further below in file history / commit diffs if needed):
1. Wrong magic system (burns/brands instead of years-of-life Kindling
   cost-transfer with silver tracer marks).
2. Invented Sol/Kael soulbond (violates brief.txt rule 15).
3. Character/lore name drift (Thorne seal/name, now 9 wrong variants
   found, see above).
4. Plot front-loading (scripted ch.16-18 line and/or Ward Deed
   discovery/understanding staged early).
5. Corrupted/non-Latin stray characters.
6. Word count floor (1,800 words minimum).
7. NEW: literal chapter-number meta-references inside narrative prose.

Given this, workstream priority remains: **structural/continuity
correctness before em-dash stripping, every chapter, no exceptions.**

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
| 08 | yes | BROKEN - full rewrite done, WORST CASE (superseded, see ch.10-15) | yes (rewrite is clean) | keep, restored to a dramatic-irony beat (both leads separately noticing, neither confronting) | original staged the ENTIRE ch.16-18 entry-pass-discovery set piece verbatim, 8 chapters early. Rewrite: Thorne courier delivers a sealed pass for Anchor Seven, Kael doesn't mention it, Sol separately finds a discrepancy in the decommissioning register, both hold back, unresolved. Confirmed still correct 2026-09-28, re-verified against user-pasted copy twice. Commit ee2f2f4421878f6b9d920bc02af48d667b643f18 |
| 09 | yes (2026-09-28) | CONFIRMED CLEAN, no rewrite needed | no | keep, well-executed pattern-formally-named beat | matches locked beat correctly, no wrong seal, no scripted line, no premature Deed content. Only outstanding task is the em-dash pass. |
| 10 | yes (2026-09-28) | BROKEN - full rewrite NEEDED, not yet done | no | pending - depends on coordinated ch.10-15 plan | wrong Thorne seal ("thorn-and-crown"); stages the ch.16-18 entry-pass-in-coat discovery almost verbatim, 6 chapters early; front-loads Deed's full clause-chain legal meaning (belongs ch.20) |
| 11 | yes (2026-09-28) | BROKEN - full rewrite NEEDED, not yet done | no | pending | wrong Thorne seal ("vine-and-key"); stages an entire, independent version of the ch.13-15 infiltration/discovery at a different site (Lower Ward Annex); repeats the naming-the-pattern confrontation a 3rd time near-verbatim |
| 12 | yes (2026-09-28) | BROKEN - full rewrite NEEDED, not yet done | no | pending | wrong Thorne seal ("hawk's head/talon/chain"); contains the locked ch.16-18 scripted line VERBATIM, 7 chapters early; sets up yet another different infiltration/site, contradicting ch.11's |
| 13 | yes (2026-09-28) | BROKEN - full rewrite NEEDED, not yet done | no | pending | wrong Thorne seal ("thorned crown/Endure and Bind" motto); scripted line verbatim; Ward Deed fully explained AND resolved via full confrontation, 7 chapters early; needs date header fix too |
| 14 | yes (2026-09-28) | BROKEN - full rewrite NEEDED, not yet done, WORST CASE IN THIS BATCH | no | pending | wrong Thorne seal; contains literal fourth-wall break "Sol had found it in chapter 8" (see new defect category 7 above); directly contradicts the confirmed-correct ch.8 (which has no entry-pass discovery scene at all); another independent version of the infiltration set piece at a third/unnamed site |
| 15 | yes (2026-09-28) | BROKEN - full rewrite NEEDED, not yet done | no | pending | wrong Thorne seal ("coiled viper"); scripted line verbatim; a FOURTH independent version of "finding the Deed," at Graywater Hollow; also has an unrelated pronoun-swap grammar bug ("she did not tell him... she did not tell her...") |
| 16 | no | UNCHECKED | no | unknown | this is the locked entry-pass discovery chapter AND the correct home for the scripted confrontation line - that scene has now leaked into AT LEAST SEVEN earlier chapters (4,5,6,7,orig-8,12,15); confirm THIS chapter still has its own full, undamaged version, and that Anchor Seven (still dangling, unaddressed through ch.15) pays off here or is consciously resolved |
| 17 | no | UNCHECKED | no | unknown | |
| 18 | no | UNCHECKED | no | unknown | |
| 19 | no | UNCHECKED | no | unknown | |
| 20 | no | UNCHECKED | no | unknown | longest chapter, check for trim as well as structure; this is where Ward Deed of Succession should be FULLY UNDERSTOOD for the first time - but its full legal meaning has now ALREADY been explained in ch.10, 12, 13, and 14 (all broken/unfixed), so when this is rewritten, check nothing genuine is left for ch.20 to reveal and rebuild the escalation from scratch if needed |
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
| 32 | partial (read for genre only) | genre confirmed good, structural defect categories NOT yet checked | no | keep, confirmed well-executed, do not pad | re-open and check against all 7 defect categories above, including the new meta-reference check |
| 33 | no | UNCHECKED | no | unknown | this is the locked rupture chapter, check it hasn't already happened earlier, and that it stays UNRESOLVED per brief.txt rule 8 |
| 34 | no | UNCHECKED | no | unknown | highest em-dash count in original generation, but do not strip until structurally checked |
| 35 | no | UNCHECKED | no | unknown | |
| 36 | no | UNCHECKED | no | unknown | |
| 37 | no | UNCHECKED | no | unknown | |
| 38 | no | UNCHECKED | no | unknown | this is the locked first-intimate-scene chapter |
| 39 | no | UNCHECKED | no | unknown | |
| 40 | no | UNCHECKED | no | unknown | regenerated once during original run (meta-leak) - given the ch.14 meta-reference finding above, check this one especially carefully for literal chapter-number references |
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
  all still correct and sequential). Ch.13 still needs its date header
  fixed regardless of its rewrite.
- Every chapter, before rewrite, carried a generation-log warning that
  the automated humanizer pass failed and fell back to pre-humanizer
  text. Manual review carries more weight than usual on every remaining
  chapter.
- The original generation log's em-dash counts do not reliably match a
  direct manual count. Do not trust the log number; verify by reading.
- brief.txt holds the full locked beat map (all 15 numbered rules) and
  should be re-fetched at the start of any session before checking
  chapters against it from memory.
- `kindling-line-book-2_full_manuscript.md` (the combined single-file
  manuscript) is NOT reliably in sync with the individual chapter files
  in `chapters/` - it should NOT be used as a reference for continuity
  checks. Rebuild it from the individual chapter files only after all
  45 chapters pass their structural check.
- The scripted ch.16-18 confrontation line has now leaked verbatim into
  SEVEN separate chapters (4,5,6,7,orig-8 - all fixed; 12,15 - still
  broken). Treat this as a near-certain recurring defect in any
  remaining unchecked chapter, especially ch.16-19.
- A mirrored-injury "bond" mechanic between Sol and Kael (found once,
  ch.7, fixed) directly violates brief.txt rule 15.
- Anchor Seven (Lower Reach, disused ropewalk site) and its status
  discrepancy, planted in ch.8's rewrite, is STILL DANGLING as of ch.15
  - mentioned once in ch.9 as a candidate site, never followed up.
  Whichever session rewrites ch.16-20 should either pay this off or
  consciously and explicitly resolve it - don't let it disappear
  silently.
- Given how many independent, contradictory "we found the Deed" scenes
  have been generated (now four, across ch.11/12/14/15, all wrong), the
  session that tackles ch.10-20 should FIRST decide and write down the
  one true version of: where the Deed is found (site name), how the
  infiltration goes (physical danger per rule 4), what "discovered but
  not understood" actually looks like on the page for ch.13-15, and what
  new information ch.20 reveals that ISN'T already given away earlier -
  before rewriting any of ch.10-20 prose, to avoid a fifth contradictory
  version.

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
- 2026-09-28: AUDITED ch.9-15 (no rewrites done yet, documentation only). Ch.9 confirmed clean. Ch.10-15 ALL confirmed broken: 6 more wrong Thorne seal variants (9 total now), scripted line found verbatim in ch.12 and ch.15 (7 total instances), FOUR independent contradictory "found the Deed" scenes across ch.11/12/14/15, and a new defect category (literal in-narrative "chapter 8" meta-reference in ch.14). No commit - findings only, table and CRITICAL section updated to reflect this. Full rewrite of ch.10-15 as a coordinated set is the next work needed, ideally planned as one continuity decision before any prose is written.
