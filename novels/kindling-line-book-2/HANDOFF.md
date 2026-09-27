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
   mechanical — replace each em dash with a period, comma, colon, or
   parenthetical rephrase depending on what reads best in context. Not a
   judgment call on whether to do it, only how to phrase each fix.

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
   CORRECTION (2026-09-27, after reading ch.1 directly): the first-pass
   genre calls below were built from beat-map summaries only and are
   proving too pessimistic. Ch.1 was flagged "rebalance" but on direct
   read is actually well-balanced: the Thorne/Council material is
   backdrop, the chapter's real weight is Sol/Kael relationship tension.
   Re-flagged "keep" below. Treat every "rebalance" call in this table as
   unconfirmed until read directly - do not trim a chapter's political
   content on the strength of the table alone.

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
generation log, PRE-STRIP - will read 0 after strip, not re-counted) /
genre-balance call / em-dash strip done? / rebalance done? / notes.

Genre-balance calls below are a FIRST PASS based on beat-map content only
(procedural set pieces vs. romance/action set pieces), not a full read of
each chapter's actual prose, EXCEPT where marked "confirmed via direct
read." Any session doing the rebalance work should re-confirm the call
against the actual chapter text before deciding to leave a chapter alone
or trim it - the table's call is a starting hypothesis, not a verdict.

| Ch | Words | Em-dashes (pre-strip) | Genre call | Em-dash done | Rebalance done | Notes |
|----|-------|-----------|------------|---------------|-----------------|-------|
| 01 | 2598 | 14 | keep - confirmed via direct read 2026-09-27, political content is backdrop, chapter's real weight is Sol/Kael tension, well-balanced | yes | yes (no rebalance needed) | em-dashes stripped 2026-09-27, 6 found on direct read (log's 14 not fully reconciled, worth a second look if a session has time) |
| 02 | 2907 | 16 | rebalance (Council vote, appointment) - UNCONFIRMED | no | no | |
| 03 | 3019 | 12 | rebalance (petition/audit procedure) - UNCONFIRMED | no | no | |
| 04 | 2355 | 16 | rebalance (sealed report, archive procedure) - UNCONFIRMED | no | no | |
| 05 | 1770 | 3 | keep (Thorne's proposal speech) - UNCONFIRMED, verify against 2300w floor note | no | no | |
| 06 | 2737 | 8 | rebalance (unilateral audits, seal-memorization) - UNCONFIRMED | no | no | |
| 07 | 1922 | 7 | keep (confrontation beat) - UNCONFIRMED, verify against floor note | no | no | |
| 08 | 3168 | 4 | keep (entry pass discovery, relationship-forward) - UNCONFIRMED | no | no | |
| 09 | 2595 | 25 | rebalance (heavy legal/deposition analysis) - CONFIRMED via direct read 2026-09-27, romance beat strong at top but back half is procedural | no | no | |
| 10 | 2925 | 21 | rebalance (joint ledger review) - UNCONFIRMED | no | no | |
| 11 | 3503 | 9 | keep (infiltration prep, action-adjacent) - UNCONFIRMED | no | no | |
| 12 | 3163 | 0 | keep - UNCONFIRMED | no | no | |
| 13 | 1802 | 13 | keep (infiltration set piece, action-forward) - UNCONFIRMED | no | no | ALSO needs date header fix |
| 14 | 2486 | 17 | keep (escape set piece, action-forward) - UNCONFIRMED | no | no | |
| 15 | 3373 | 9 | rebalance (procedural postponement) - UNCONFIRMED | no | no | regenerated once (meta-leak) |
| 16 | 2661 | 17 | keep (the named-pattern confrontation, core relationship beat) - UNCONFIRMED | no | no | |
| 17 | 3366 | 4 | rebalance (archive verification explanation) - UNCONFIRMED | no | no | |
| 18 | 3098 | 11 | rebalance (hearing scheduled, procedural) - UNCONFIRMED | no | no | |
| 19 | 3619 | 27 | rebalance (solo audit report, injury-as-procedure) - UNCONFIRMED | no | no | |
| 20 | 4215 | 25 | rebalance (Deed reading, legal cross-reference) - UNCONFIRMED, very long, check for trim not just rebalance | no | no | longest chapter, priority check |
| 21 | 2381 | 0 | rebalance (Council argument, joint-audit order) - UNCONFIRMED | no | no | |
| 22 | 1845 | 0 | keep (Kael's solo-audit decision, relationship-forward) - UNCONFIRMED | no | no | regenerated once (unfinished sentence) |
| 23 | ? | ? | keep (Embervein infiltration, action set piece) - UNCONFIRMED | no | no | generated on retry run, needs word/em-dash check |
| 24 | 1589 | 6 | keep (immediate aftermath, emotional) - UNCONFIRMED | no | no | |
| 25 | 2703 | 2 | keep (infirmary, propaganda fallout) - UNCONFIRMED, mixed, verify | no | no | |
| 26 | 1838 | 15 | rebalance (Council debate over stripping Kael's status) - UNCONFIRMED | no | no | |
| 27 | 3064 | 30 | rebalance (provisional ruling, nomination procedure) - UNCONFIRMED | no | no | |
| 28 | 2044 | 5 | keep (the "I love you" chapter, core relationship beat) - UNCONFIRMED | no | no | |
| 29 | 1879 | 0 | rebalance (counter-proposal drafting) - UNCONFIRMED | no | no | |
| 30 | 2860 | 8 | rebalance (public forum, spokesperson) - UNCONFIRMED | no | no | |
| 31 | 2626 | 13 | rebalance (censure vote) - UNCONFIRMED | no | no | |
| 32 | 1493 | 4 | keep - CONFIRMED via direct read 2026-09-27, well-executed tight scene, DO NOT pad | no | no | |
| 33 | 2393 | 12 | keep (the rupture, core relationship beat) - UNCONFIRMED | no | no | |
| 34 | 3735 | 40 | keep (rupture continues) - UNCONFIRMED, highest em-dash count in the book, priority strip | no | no | |
| 35 | 3006 | 24 | keep (rupture aftermath) - UNCONFIRMED | no | no | |
| 36 | 3932 | 15 | rebalance (formal renunciation, Council censure) - UNCONFIRMED | no | no | |
| 37 | 1853 | 3 | rebalance (Council decree accepted) - UNCONFIRMED | no | no | |
| 38 | 2294 | 1 | keep (first intimate scene, core relationship beat) - UNCONFIRMED | no | no | |
| 39 | 2266 | 4 | rebalance (joint report finalized) - UNCONFIRMED | no | no | |
| 40 | 2950 | 24 | keep (Accord ceremony opens, ritual/magic-forward) - UNCONFIRMED | no | no | regenerated once (meta-leak) |
| 41 | 2027 | 1 | keep (the ward-taker trial itself, magic/physical) - UNCONFIRMED | no | no | |
| 42 | 2581 | 7 | keep (trial completes, exposure of Thorne) - UNCONFIRMED | no | no | |
| 43 | 4442 | 30 | rebalance (Accord votes to reject Thorne) - UNCONFIRMED, very long, check for trim | no | no | longest along with ch.20, priority check |
| 44 | 1985 | 4 | keep (aftermath walk, relationship-forward) - UNCONFIRMED | no | no | |
| 45 | 1842 | 4 | keep (final line, Keeper reveal) - UNCONFIRMED, must stay institutional-not-personal per locked rule | no | no | |

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
- The log's em-dash counts and a direct manual count of the same chapter
  do not fully reconcile (ch.1 logged as 14, manual count found 6 before
  stripping). Do not treat the log count as exact - use it only to
  prioritize which chapters to check first, and always verify zero
  em-dashes remain by actually re-reading the stripped chapter, not by
  trusting the original count was fully addressed.

## Progress log (append one line per chapter as you finish it)

- 2026-09-27: ch.1 em-dash strip done, genre call corrected keep, commit 761229040d773806521b7e15f32e87b8aa39ff3c

## Protocol for any session picking this up

1. Read this file in full before opening any chapter.
2. Pick the next unfinished row(s) in whichever workstream you're doing.
3. Before rebalancing a chapter, actually read it (don't rely solely on
   this table's genre call - it's a first-pass hypothesis from beat-map
   content only, confirm or overturn it against the real prose).
4. After finishing a chapter (either workstream), update that chapter's
   row in this file - mark done, add a note if the genre call changed
   after reading the real text, and append one line to the Progress log
   above with the commit sha.
5. Commit the chapter edit AND this file's update together, or as close
   together as possible, so progress is never invisible to the next
   session.
6. Do not mark `continuity_voice_canon_review_complete: true` in
   `book_config.json` until every row above shows both em-dash and
   rebalance columns as done.
