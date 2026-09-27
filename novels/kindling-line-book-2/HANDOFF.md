# HANDOFF — Kindling Line Book 2 Polish Pass

STATUS AS OF 2026-09-27: All 45 chapters exist and are pushed. This file
tracks a cross-session polish pass authorized by Zia with no budget
constraint — quality is the only priority. ANY session picking up this
work must read this file FIRST, before touching a chapter, and must
UPDATE this file's table in the SAME commit as any chapter edit, before
ending its turn. Do not batch updates for later — if a session ends
without updating this file, the next session has no way to know what was
actually finished versus attempted.

## The four workstreams, in priority order

1. **Em-dash strip (ALL 45 chapters).** Locked rule from both books'
   architecture/brief: no em dashes. Verified violated in every chapter
   sampled so far (chapter_09.md had 25, chapter_34.md had 40). This is
   mechanical — replace each em dash with a period, comma, or parenthetical
   rephrase depending on what reads best in context. Not a judgment call
   on whether to do it, only how to phrase each fix.

2. **Genre-balance rebalance (chapters flagged "rebalance" in the table
   below only, not all 45).** Zia's core concern: the book reads as
   political-procedural in long stretches (council votes, legal clauses,
   contract-chain-of-custody analysis) rather than romantasy-forward
   (romance, physical stakes, sensory/magic-forward action). The fix is
   NOT uniform padding. Each chapter marked "rebalance" needs: legal/
   procedural exposition trimmed, replaced with interiority, sensory
   detail, physical stakes, or relationship beats. Chapters marked "keep"
   are already doing their job (tight, romance/action-forward, or
   legitimately short-by-design like ch.32) and should NOT be touched
   for length or content, only for em-dashes.

3. **Continuity/voice/canon review (`continuity_voice_canon_review_complete`
   in book_config.json, currently `false`).** A full read of all 45
   chapters against `architecture.md`, `brief.txt`, and Book 1's actual
   text, checking for contradictions the beat map didn't already catch
   (name spellings, timeline math, mechanic consistency, voice drift
   between Sol's and Kael's POV chapters). Do this AFTER em-dash strip and
   rebalance are done, since edits will change the text being reviewed.

4. **Chapter 13 missing date header.** One-line fix: add
   `<!-- chapter_date: 21 Sunspire, Year 3 of the Reckoning Accord -->`
   to the top of `chapter_13.md`, matching the beat map's locked date for
   that chapter. Trivial, do it whenever convenient.

## Chapter table

Columns: chapter / word count (from generation log) / em-dash count (from
generation log) / genre-balance call / em-dash strip done? / rebalance
done? / notes.

Genre-balance calls below are a FIRST PASS based on beat-map content only
(procedural set pieces vs. romance/action set pieces), not a full read of
each chapter's actual prose. Any session doing the rebalance work should
re-confirm the call against the actual chapter text before deciding to
leave a chapter alone or trim it - the table's call is a starting
hypothesis, not a verdict.

| Ch | Words | Em-dashes | Genre call | Em-dash done | Rebalance done | Notes |
|----|-------|-----------|------------|---------------|-----------------|-------|
| 01 | 2598 | 14 | rebalance (Contract reading, public/political opening) | no | no | |
| 02 | 2907 | 16 | rebalance (Council vote, appointment) | no | no | |
| 03 | 3019 | 12 | rebalance (petition/audit procedure) | no | no | |
| 04 | 2355 | 16 | rebalance (sealed report, archive procedure) | no | no | |
| 05 | 1770 | 3 | keep (Thorne's proposal speech - check if thin from missing beat or by design) | no | no | verify against 2300w floor note |
| 06 | 2737 | 8 | rebalance (unilateral audits, seal-memorization) | no | no | |
| 07 | 1922 | 7 | keep (confrontation beat, likely tight by design) | no | no | verify against floor note |
| 08 | 3168 | 4 | keep (entry pass discovery, relationship-forward) | no | no | |
| 09 | 2595 | 25 | rebalance (heavy legal/deposition analysis, confirmed by direct read) | no | no | confirmed via direct read 2026-09-27 |
| 10 | 2925 | 21 | rebalance (joint ledger review) | no | no | |
| 11 | 3503 | 9 | keep (infiltration prep, action-adjacent) | no | no | |
| 12 | 3163 | 0 | keep | no | no | |
| 13 | 1802 | 13 | keep (infiltration set piece, action-forward) | no | no | ALSO needs date header fix |
| 14 | 2486 | 17 | keep (escape set piece, action-forward) | no | no | |
| 15 | 3373 | 9 | rebalance (procedural postponement) | no | no | regenerated once (meta-leak) |
| 16 | 2661 | 17 | keep (the named-pattern confrontation, core relationship beat) | no | no | |
| 17 | 3366 | 4 | rebalance (archive verification explanation) | no | no | |
| 18 | 3098 | 11 | rebalance (hearing scheduled, procedural) | no | no | |
| 19 | 3619 | 27 | rebalance (solo audit report, injury-as-procedure) | no | no | |
| 20 | 4215 | 25 | rebalance (Deed reading, legal cross-reference - very long, check for trim not just rebalance) | no | no | longest chapter, priority check |
| 21 | 2381 | 0 | rebalance (Council argument, joint-audit order) | no | no | |
| 22 | 1845 | 0 | keep (Kael's solo-audit decision, relationship-forward) | no | no | regenerated once (unfinished sentence) |
| 23 | (unknown - generated late) | (unknown) | keep (Embervein infiltration, action set piece) | no | no | generated on retry run, needs word/em-dash check |
| 24 | 1589 | 6 | keep (immediate aftermath, emotional) | no | no | |
| 25 | 2703 | 2 | keep (infirmary, propaganda fallout - mixed, verify) | no | no | |
| 26 | 1838 | 15 | rebalance (Council debate over stripping Kael's status) | no | no | |
| 27 | 3064 | 30 | rebalance (provisional ruling, nomination procedure) | no | no | |
| 28 | 2044 | 5 | keep (the "I love you" chapter, core relationship beat) | no | no | |
| 29 | 1879 | 0 | rebalance (counter-proposal drafting) | no | no | |
| 30 | 2860 | 8 | rebalance (public forum, spokesperson) | no | no | |
| 31 | 2626 | 13 | rebalance (censure vote) | no | no | |
| 32 | 1493 | 4 | keep - confirmed via direct read, well-executed tight scene, DO NOT pad | no | no | confirmed via direct read 2026-09-27 |
| 33 | 2393 | 12 | keep (the rupture, core relationship beat) | no | no | |
| 34 | 3735 | 40 | keep (rupture continues) BUT highest em-dash count in the book - priority strip | no | no | |
| 35 | 3006 | 24 | keep (rupture aftermath) | no | no | |
| 36 | 3932 | 15 | rebalance (formal renunciation, Council censure) | no | no | |
| 37 | 1853 | 3 | rebalance (Council decree accepted) | no | no | |
| 38 | 2294 | 1 | keep (first intimate scene, core relationship beat) | no | no | |
| 39 | 2266 | 4 | rebalance (joint report finalized) | no | no | |
| 40 | 2950 | 24 | keep (Accord ceremony opens, ritual/magic-forward) | no | no | regenerated once (meta-leak) |
| 41 | 2027 | 1 | keep (the ward-taker trial itself, magic/physical) | no | no | |
| 42 | 2581 | 7 | keep (trial completes, exposure of Thorne) | no | no | |
| 43 | 4442 | 30 | rebalance (Accord votes to reject Thorne - very long, check for trim) | no | no | longest along with ch.20, priority check |
| 44 | 1985 | 4 | keep (aftermath walk, relationship-forward) | no | no | |
| 45 | 1842 | 4 | keep (final line, Keeper reveal - must stay institutional-not-personal per locked rule) | no | no | |

## Additional known issues to fix as encountered (not chapter-specific)

- `chapters_date_report.md` in this folder has a fuller date-consistency
  report from generation - check it before marking the continuity review
  gate complete.
- Every chapter carries a `<!-- WARNING: chapter N rewrite dropped a fact
  - kept original text -->`-type log note from generation (not visible in
  the files themselves, only in the run log) - this means the automated
  humanizer pass failed on nearly every chapter and the pipeline fell back
  to pre-humanizer text. Worth knowing this text has NOT been through a
  successful automated smoothing pass; manual polish carries more weight
  here than usual.

## Protocol for any session picking this up

1. Read this file in full before opening any chapter.
2. Pick the next unfinished row(s) in whichever workstream you're doing.
3. Before rebalancing a chapter, actually read it (don't rely solely on
   this table's genre call - it's a first-pass hypothesis from beat-map
   content only, confirm or overturn it against the real prose).
4. After finishing a chapter (either workstream), update that chapter's
   row in this file - mark done, add a note if the genre call changed
   after reading the real text.
5. Commit the chapter edit AND this file's update together, or as close
   together as possible, so progress is never invisible to the next
   session.
6. Do not mark `continuity_voice_canon_review_complete: true` in
   `book_config.json` until every row above shows both em-dash and
   rebalance columns as done.
