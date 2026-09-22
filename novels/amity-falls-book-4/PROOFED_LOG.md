# Book 4 proofed log
_Rewritten clean 2026-09-22 — old stamps and superseded sections removed.
See git history for the full trail if needed; nothing here contradicts
itself anymore. `CANON_NUMBERS.md` now merges what used to be a second,
disagreeing file (`DATES_BIBLE.md`, deleted). Read that file for all
dates/ages/names; this file is for open editorial questions and chapter
read-progress only._

Legend: FIXED = edit read back live. READ = manual read, no change needed.
NOT PROOFED = mechanical pass only, no manual read yet.

**LAST CHAPTER STAMPED: ch.45. FULL SEQUENTIAL READ OF THE BOOK COMPLETE**
(2026-09-22). A follow-up verification pass this same day re-read ch.16,
18, 19, 20, 21 in full (not from memory) to map the countdown cluster, and
fixed the two remaining custody-conflict instances (ch.21, ch.34) since
Zia handed off decision authority. See below.

## Resolved 2026-09-22 (verification/decision pass, after full read complete)
- **Ch.21's motel arrest: FIXED** (`beb46da`) — this was done in an
  earlier session pass than the log previously reflected; the log's "NOT
  yet fixed" note was stale, not the chapter. Verified live: the deputy
  now says Drake is "not in custody - not yet," matching ch.41 as the
  actual arrest. Diff-checked, 3 lines changed, nothing else touched.
- **Ch.34's three custody lines: FIXED** (`866eb6b`), decided and applied
  per Zia's handoff ("it's your call, fix everything, but not without
  diligence"). Wording matched to the ch.21 precedent exactly ("cornered,"
  "case built and building," "facing real charges in real courts")
  instead of inventing new phrasing, so the two fixes read as one
  consistent choice rather than two different patches. Diff-checked: 4
  lines changed (2 custody lines plus 2 downstream references to Drake's
  status later in the same chapter), nothing else touched, verified
  against the live commit patch.
- **Conflict #1 (Drake's arrest) is now CLOSED.** Ch.21, ch.34, ch.39,
  ch.40 all read consistently with ch.41 as the one canonical arrest.
- **Countdown cluster: read ch.16, 18, 19, 20, 21 in full (not skimmed).**
  Confirmed the actual shape, not just the day-counts:
  - Ch.16: Drake's teaser document leaks. Emergency session. Council votes
    to accelerate to **14 days** ("the fifteenth").
  - Ch.18: separate emergency session, triggered by a Millbrook Gazette
    print deadline. Council commits to **10 days**.
  - Ch.19: nine fabricated transcripts arrive by mail (different threat).
    Council votes to open the Archive to outsiders in **1 week**.
  - Ch.20: another full emergency council-vote scene, new characters (Hal
    Brenner, Marta Cortes), independently lands back on **2 weeks** -
    matching ch.16's number exactly rather than compressing further from
    ch.19's 1 week. This is the outlier.
  - Ch.21: **3 days** to print (deputy scene).
  Read in full, ch.16/18/19/21 form a genuine escalating sequence, each
  triggered by a distinct new Drake threat (14 -> 10 -> 7 -> 3). Ch.20 is
  a real, independently-written scene with its own cast and its own
  emotional arc (Wren's "stopped apologizing" beat), not a copy-paste
  duplicate - but its timeline machinery (the vote, the "two weeks"
  number) resets the countdown for no in-story reason and doesn't fit
  the sequence. NOT YET fixed - see Not done below for the specific
  proposed edit.
  Ch.28, 29, 31, 37 (more "nine days"/"ten days" data points per
  `CANON_NUMBERS.md`) not yet re-read this pass to confirm they fit the
  same chain - still open.

## Decisions locked (do not re-touch without new evidence)
1. Josiah/Ambrose: DECIDED — confirmed through the full sequential read.
2. Chapter order: not renumbering files. "The fifteenth" is the one
   publication deadline (`4175ca7`). Countdown chain ch.16/18/19/21
   confirmed to escalate cleanly (14/10/7/3 days). Ch.20 is the confirmed
   outlier - fix proposed, not yet applied. Ch.28/29/31/37 still
   unverified against the chain.
3. Drake's arrest: ch.41's early-morning home arrest is canon. Ch.21,
   ch.25, ch.26, ch.34, ch.39, ch.40 all now fixed to match. **CLOSED.**
4. Ch.17 kiss stays; do not cut.
5. Drake's em-dash note: kept, the one deliberate house-style exception
   (`f9e01f5`).

Related, lower-stakes, not decided: Ambrose Kell vs. either Whitlock —
already confirmed distinct in ch.19, and reconfirmed distinct in ch.27-45,
not actually a conflict, just a name worth double-checking on sight since
three "Ambrose/Whitlock"-adjacent names exist in this book (Josiah
Whitlock, Ambrose Whitlock, Ambrose Kell).

## Fixed and locked (do not re-touch without new evidence)
- Folio gap: 1887-1891 (ch.3, `207db70`).
- Anachronisms (trial/leverage as past): fixed ch.8, ch.12. Ch.24-26 clean.
- Ch.11: Odette Reynolds → Reyes; age/decade fix. Ch.22: Harriet is Theo's
  grandmother. Ch.23, ch.25: Harriet's age fixed to seventy-five. Ch.41:
  same fix applied (`29be7e8`).
- Ch.12: truncated sentence, ledger-finder attribution, 2 anachronisms.
- Ch.15: full rewrite verified.
- Ch.18: internal day-count contradiction fixed. RE-READ in full
  2026-09-22: clean, confirms 10-day figure, fits the escalation chain.
- Ch.24: READ, clean, confirms the ch.45 large-debt fix.
- Ch.25: Harriet's age, Drake's custody status, em dash fixed (`f9e01f5`).
- Ch.26: "Summer solstice" and "custody hearing" lines fixed (`4175ca7`).
- Ch.17: READ in full. Clean, complete prose, not a duplicate. No change.
- Ch.16: RE-READ in full 2026-09-22. Clean. Confirms 14-day figure ("the
  fifteenth"), first link in the countdown chain. No fix needed.
- Ch.19: RE-READ in full 2026-09-22. Clean. Confirms 1-week figure, third
  link in the chain (nine fabricated transcripts as the trigger). No fix
  needed.
- Ch.20: RE-READ in full 2026-09-22. Clean prose, real scene, not clutter
  - but its 2-week vote duplicates ch.16's timeline rather than advancing
    it. See Not done.
- Ch.21: READ in full, FIXED (`beb46da`, verified this pass via commit
  diff). Confirmed a real second kiss scene interrupted by Dev. Also
  confirms: Wren's age 21 (matches ch.7); "three days" to publication,
  the last link in the ch.16/18/19/21 chain.
- Ch.34: READ in full, FIXED (`866eb6b`, this pass). Otherwise clean.
- Ch.39, ch.40: FIXED — custody claims removed (checked against ch.37-41
  directly).
- Ch.27-33, 35-40, 42-45: READ in full, no hard violations, no fix
  needed beyond what's logged above.
- Ch.41: READ in full, FIXED (age). Otherwise clean; the arrest scene
  itself (6:45am, home, no resistance) matches Decision 3 exactly — this
  chapter is the canonical arrest, everything else measures against it.

## Open questions
- Q1 Elena Castellano: three different ages given for when the grandmother
  died (fourteen/sixteen across chapters).
- Q2 Drake's 2005 Millbrook target: unresolved.
- Q3 Adelaide's exact relationship to Ambrose (student/successor/other):
  unresolved. Do not guess — a prior pass tried and reverted it.
- Q4 Ch.5 unreliable/anachronistic (Ambrose alive 2005-2009): unresolved.
- Q5 Lineage roster: unresolved.
- Q6 Calendar: still cycles through all four seasons inconsistently across
  chapters. Needs Zia's specific date decisions, not a guess.
- Q7 Wren's mother's job: unresolved.
- Q8 Harriet's home terminology: unresolved.
- Q9 Kiss/rupture beat map: three-way mismatch (ch.17/21/26), needs a
  decision on which detail to change. Not yet re-read this pass.
- Q10 Archive building: 3+ competing physical descriptions. Ch.18's
  "converted barn behind the general store" confirmed this pass as one
  more data point in this open list.
- Q11 Two "Silas" characters: unresolved.
- Q12 Spaced hyphens as em-dash substitutes: open generally; the ch.25
  plot-point case is fixed.
- Q13 Denise's "grandson's husband" line vs. Mara+Caleb: unresolved.
- Q14 "The house on the ridge": unresolved.
- Q15 M. Harrow / Harlan & Associates thread: self-contained so far.
- Q16 Shell company names ("Holloway & Finch" vs "Meridian Consulting"):
  presented as two different shells, not necessarily a conflict.
- Q17 Martha Whitlock's relation to Ambrose (daughter vs. granddaughter,
  ch.22): unfixed, needs confirmation, not an assumption.
- Q18 Theo's age: 26 stated vs. 27 by birth-year math. Low priority.
- Q19 (new, low priority) Ch.21's deputy scene calls Dev "your
  brother-in-law" to Wren. No established relationship supports this
  (Dev is not married into Wren's family anywhere else in the book,
  including ch.6-9 where he's introduced as a colleague/Finder). Spotted
  during the ch.21 diff-check, not fixed — the "in custody" fix touched
  an adjacent sentence but this one is untouched and may predate it.
  Worth a look, low stakes.

## Not done
- **Ch.20's timeline reset:** proposed fix, not yet applied — trim the
  vote's specific number so it doesn't restate "two weeks" (which
  duplicates ch.16), while keeping the scene's actual content (Hal/Marta
  objection, Wren's growth beat) intact. Likely approach: have the
  council shorten further from ch.19's one week rather than re-lengthen,
  or make ch.20 explicitly about *holding* the one-week deadline against
  pushback rather than re-voting a new number. Needs the exact wording
  decided before editing, same as the custody fix was.
- Confirm ch.28, 29, 31, 37 fit the ch.16/18/19/21 chain (or identify
  where they actually belong) - not yet re-read this pass.
- Resolve the three-way kiss-sequence mismatch (ch.17/21/26).
- Full season/countdown/Archive-naming reconciliation pass (Q6, Q10).
- Cross-check against Books 1-3 (Q1, Q13).
- Decide Q17 (Martha's relation to Ambrose).
- Check Q19 (Dev "brother-in-law" line, ch.21).
- Mechanical/lexical/tell-density pass (em dashes, repetition, staged
  constructions) for ch.27-45 specifically — this pass was a continuity
  read, not the full lexical sweep the earlier chapters got.
