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
(2026-09-22). A follow-up verification/decision pass this same day re-read
ch.16, 18, 19, 20, 21, 28, 29, 31, 37 in full (not from memory) to map the
countdown cluster, then made and applied three editorial decisions per
Zia's handoff ("it's your call, fix everything, but not without
diligence, review critically"). All three were done as targeted,
diff-verified edits — no chapter was cut or rewritten wholesale. See below.
Two further follow-up sessions (2026-09-22, later) fixed Q19 (`11cd9f0`),
closed the ch.28/29/31/37 day-count cross-check (reconciled, not fixed —
no contradiction found once read together), and fixed Q9 (`c4dbf27`).

## Decisions made and applied this pass (2026-09-22)

**Decision A — Drake's arrest / custody status (conflict #1). CLOSED.**
- Ch.21's motel-arrest line was already fixed in an earlier part of this
  session (`beb46da`) — the log's "NOT yet fixed" note had simply gone
  stale; the chapter itself was fine. Verified live via commit diff: the
  deputy now says Drake is "not in custody - not yet," consistent with
  ch.41 as the actual arrest.
- Ch.34's three custody lines ("sat in a county jail cell," "the
  experimenter was in custody," "Drake in his cell") were still live.
  FIXED this pass (`866eb6b`) using the exact wording pattern already
  established in ch.21 ("cornered," "the case built and building,"
  "facing real charges in real courts") rather than inventing new
  phrasing, so the two fixes read as one consistent authorial choice.
  Diff-checked: 4 lines changed, nothing else touched.
- Ch.21, ch.25, ch.26, ch.34, ch.39, ch.40 now all read consistently with
  ch.41 as the one canonical arrest. No chapter cut or rewritten to get
  here — every fix was a same-scene wording swap.

**Decision B — Ch.20's timeline reset (part of conflict #3). FIXED.**
- Re-read ch.16, 18, 19, 20, 21 in full to map the actual countdown
  chain: ch.16 teaser leak -> 14 days ("the fifteenth"); ch.18 Gazette
  deadline -> 10 days; ch.19 fabricated transcripts -> 1 week; ch.20 -> an
  independent re-vote landing back on 2 weeks, breaking the chain; ch.21
  -> 3 days. Ch.16/18/19/21 form a genuine escalating sequence, each
  triggered by a distinct new Drake threat. Ch.20 was the confirmed
  outlier: real, non-duplicate prose (new characters Hal Brenner/Marta
  Cortes, Wren's "stopped apologizing" arc) wrapped around a vote that
  contradicted ch.19's number for no in-story reason.
- Zia's instruction was explicit: find a solution without deleting or
  rewriting the chapter. FIXED (`da6ebe0`) by swapping "two weeks" ->
  "one week" in the 6 places the number appears, and adjusting a
  half-dozen surrounding words (Wren: "I'm not asking for more time. I'm
  asking you to hold the line on it"; Yusuf: "The deadline stands") so
  the scene now reads as the council *defending* the existing one-week
  deadline against Hal and Marta's pushback, rather than re-voting a
  longer one. Every character beat, every line of dialogue not touching
  the number, and the full Hal/Marta objection stayed exactly as
  written. Diff-checked: 6 lines changed (numeral + minimal adjacent
  wording), nothing else touched.

**Decision C — Ch.31's rupture scene vs. ch.19's (part of conflict #3).
FIXED.**
- Ch.31 (Drake leaks a full draft + 10-day ultimatum) contains a second
  full Wren/Theo rupture-and-reconciliation scene that is structurally
  very close to ch.19's (same core disagreement: control the narrative
  vs. trust the valley with it; same resolution shape: "together," on
  our terms). As written, ch.31 gave no sign the two of them had already
  had this exact fight and resolved it in ch.19 - it read as their first
  time, not their second, deeper one.
- Zia's instruction: same as Decision B, no deletion or rewrite. FIXED
  (`0963500`) by inserting one paragraph, right where Theo's silence
  turns into the start of the argument, in which Wren explicitly
  recognizes the recurrence: they'd had this fight the night the
  fabricated transcripts arrived, found a third way, sealed it with
  "together" - and she'd believed that word had settled it. The
  insertion frames Drake's new leverage (the dead-drop offer to Theo
  from ch.29, tied to Harriet Marsh) as reopening a wound they thought
  was closed, rather than the book forgetting it was ever closed. Not
  one word of the existing argument, resolution, or dialogue was cut,
  reordered, or reworded. Diff-checked: exactly 1 paragraph (3 lines)
  added, nothing else touched.
- This resolves the acute duplication problem without removing either
  chapter's content.

**Countdown data — RECONCILED (2026-09-22, follow-up pass):**
ch.16 (14d) -> ch.18 (10d) -> ch.19 (7d) -> ch.20 (7d, reaffirmed, was
14d) -> ch.21 (3d): one clean chain tracking the original "publish next
Friday, the 11th, four days ahead of Drake's the-15th deadline" plan
(ch.28/29 confirm this Friday-the-11th target explicitly: ch.28 "nine
days before his deadline" for the press run, ch.29 "we beat it by four
days... next Friday"). Ch.31 (10d ultimatum, "we publish in 9") opens a
SEPARATE, later countdown, triggered by Drake's new full-draft leak — not
a contradiction of the Friday-the-11th plan but a second crisis with its
own clock, consistent with Decision C's finding that ch.31 is a
deliberate second rupture rather than an unacknowledged repeat of ch.19.
Ch.37 ("ten days total / six days for lineage signatures") lands 3 days
into that new 9-day countdown, with 6 of a 10-day total print/signature
cycle remaining — arithmetically consistent with ch.31's clock. No
chapter text needed changing; the cluster reads as two sequential
crises, each internally consistent, not one broken timeline. CLOSED.

**Q9 — kiss/rupture beat map. FIXED (`c4dbf27`).**
- Read ch.17, ch.21 (already current from this session's own Q19 edit),
  and ch.26 in full. Found the true chronology: ch.17 is the real first
  kiss (Wren's mother's kitchen table, late-night proofing session,
  uninterrupted, midnight). Ch.21 is a later kiss, explicitly narrated as
  a repeat ("Interrupted... Again"), in the study, cut short by the
  deputy's arrival at the gate. Ch.26 is later still — the deepest
  commitment scene (Theo missing his train to stay).
- The actual defect was narrower than "three-way mismatch": two lines
  inside ch.26 itself described "the first kiss" as happening "in the
  records room," interrupted by "Priya's knock at the door" — a scene
  that was never written anywhere and matches neither ch.17 nor ch.21.
- FIXED by correcting those two ch.26 lines to point at the real ch.21
  scene (deputy at the gate, Dev's twelfth-redirect discovery) instead of
  the phantom records-room scene. Nothing added, nothing cut; ch.17 and
  ch.21 untouched. Diff-checked: 2 lines changed, nothing else touched.

## Decisions locked (do not re-touch without new evidence)
1. Josiah/Ambrose: DECIDED — confirmed through the full sequential read.
2. Chapter order: not renumbering files. "The fifteenth" is the one
   original publication deadline (`4175ca7`). Countdown chain
   ch.16/18/19/20/21 CLOSED (Decision B). Ch.28/29/31/37 now also
   CLOSED — reconciled as two sequential crisis-clocks, not one broken
   chain (see Countdown data above).
3. Drake's arrest: ch.41's early-morning home arrest is canon. Ch.21,
   ch.25, ch.26, ch.34, ch.39, ch.40 all now fixed to match. **CLOSED
   (Decision A).**
4. Ch.17 kiss stays; do not cut. Ch.19 and ch.31's rupture scenes both
   stay; ch.31 now explicitly references ch.19 rather than duplicating
   it unacknowledged (Decision C). Kiss chronology is ch.17 (first,
   uninterrupted) -> ch.21 (interrupted, deputy at gate) -> ch.26
   (deepest commitment scene). **CLOSED (Q9, `c4dbf27`).**
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
- Ch.16: RE-READ in full 2026-09-22. Clean. Confirms 14-day figure ("the
  fifteenth"), first link in the countdown chain. No fix needed.
- Ch.17: READ in full. Clean, complete prose, not a duplicate. The real
  first kiss — see Q9 above. No change.
- Ch.18: internal day-count contradiction fixed. RE-READ in full
  2026-09-22: clean, confirms 10-day figure, fits the chain.
- Ch.19: RE-READ in full 2026-09-22. Clean. Confirms 1-week figure and
  the first Wren/Theo rupture-and-resolution ("together," testimony not
  ledger). No fix needed to this chapter itself - it's the anchor
  Decision C points back to.
- Ch.20: FIXED (`da6ebe0`, Decision B). Timeline reset resolved without
  cutting the Hal/Marta scene.
- Ch.21: READ in full, FIXED (`beb46da`, Decision A; `11cd9f0`, Q19).
  Confirmed a real second kiss scene interrupted by Dev/the deputy at the
  gate — this is the scene ch.26 now correctly references (Q9). Also
  confirms: Wren's age 21 (matches ch.7); "three days" to publication,
  the last link in the ch.16/18/19/21 chain. Q19 fixed: deputy's "your
  brother-in-law's evidence" (unsupported relationship claim) -> "Dev's
  evidence" — Dev is Priya's brother, not Wren's, per ch.13/14; no
  marriage link between Wren and Priya/Dev exists anywhere in the book.
- Ch.24: READ, clean, confirms the ch.45 large-debt fix.
- Ch.25: Harriet's age, Drake's custody status, em dash fixed (`f9e01f5`).
- Ch.26: "Summer solstice" and "custody hearing" lines fixed (`4175ca7`,
  earlier session); kiss-recollection lines fixed (`c4dbf27`, Q9, this
  session — see above). Deepest-commitment kiss scene (Theo misses his
  train) confirmed as chronologically last of the three.
- Ch.28: READ in full 2026-09-22. Clean. Proof copy finished, press run
  "nine days before deadline." Cross-checked against ch.29/31/37 this
  pass — see Countdown data. No conflict.
- Ch.29: READ in full 2026-09-22. Clean. Drake's dead-drop offer to Theo
  (trade Harriet's Millbrook record for a 3-week delay); Theo goes to the
  drop, doesn't leave an answer, tells Wren. Confirms "the fifteenth" as
  the locked deadline ("we beat it by four days," publish "next
  Friday"). This chapter is the setup Decision C's ch.31 insertion refers
  back to, and the anchor for the Friday-the-11th leg of the countdown
  cross-check.
- Ch.31: READ in full, FIXED (`0963500`, Decision C). Second
  Wren/Theo rupture, now explicitly framed as a recurrence of ch.19's,
  reopened by Drake's leaked draft and the temptation planted in ch.29.
  Its "we publish in nine days" opens the second countdown clock — see
  Countdown data.
- Ch.34: READ in full, FIXED (`866eb6b`, this pass, Decision A).
  Otherwise clean.
- Ch.37: READ in full 2026-09-22. Clean. Confirms Silas Harker rename is
  holding correctly ("Not Old Man Harker, who was alive and difficult").
  References the ch.31 rupture as already resolved, confirming it sits
  after ch.31 in-story. Its "ten days total / six days for signatures"
  cross-checked against ch.28/29/31 this pass — see Countdown data. No
  conflict.
- Ch.39, ch.40: FIXED — custody claims removed (checked against ch.37-41
  directly).
- Ch.27, 30, 32, 33, 35, 36, 38, 40, 42-45: READ in full (earlier
  sequential pass), no hard violations, no fix needed beyond what's
  logged above.
- Ch.41: READ in full, FIXED (age). Otherwise clean; the arrest scene
  itself (6:45am, home, no resistance) matches Decision A exactly — this
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
  chapters. Needs Zia's specific date decisions, not a guess. The
  ch.28/29/31/37 leg of this is now closed (see Countdown data); the rest
  of Q6 (season progression across the full 45 chapters) is still open.
- Q7 Wren's mother's job: unresolved.
- Q8 Harriet's home terminology: unresolved.
- Q10 Archive building: 3+ competing physical descriptions.
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

## Not done
- Full season/Archive-naming reconciliation pass (Q6 remainder, Q10).
- Cross-check against Books 1-3 (Q1, Q13).
- Decide Q17 (Martha's relation to Ambrose).
- Mechanical/lexical/tell-density pass (em dashes, repetition, staged
  constructions) for ch.27-45 specifically — this pass was a continuity
  read, not the full lexical sweep the earlier chapters got.
