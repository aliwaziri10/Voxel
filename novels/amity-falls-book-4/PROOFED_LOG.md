# Book 4 proofed log

## STAMP (2026-09-22, this session): Decision 1 REVERSED. Ambrose is correct.
Read ch.3 live directly (not from the log, not from HANDOFF's claim). It is
unambiguous: **Ambrose Whitlock** tried to end the bargain in 1889 and hid
the complete terms. Josiah does not appear anywhere in ch.3.
- **Reverted to Ambrose** and pushed live: ch.2, ch.6, ch.7, ch.12, ch.13,
  ch.15 (`e14a5fc`). These 6 chapters now match ch.3.
- **Ch.14 CORRECTION: already fixed, by a parallel/earlier commit this
  same day** (`bfeee2c`, 08:22:28, before this stamp) — verified live just
  now, it correctly reads "Ambrose Whitlock's precise script." My earlier
  note in this stamp saying ch.14 was "not yet touched" was wrong; I was
  going off the log's stale claim instead of checking live. Correcting
  that here per rule zero.
- **Ch.9 deliberately left untouched.** Its own text reads "Ambrose himself
  had learned it from an older warning. Josiah Whitlock, a Warden
  generations before him, had held the role" — this frames Josiah as a
  separate, earlier ancestor, not as the one who tried the bargain. That
  may be intentional (two Whitlocks, not a naming error) or it may be
  another instance of the same mistake. NOT decided here — needs a direct
  read of ch.9 in full before anyone touches its "J. Whitlock, 1847/1863"
  signature lines.
- I also pushed and then pulled back a batch of guesses on Adelaide's
  relationship to Ambrose (ch.3, ch.5), Martha's relation (ch.22), the
  publication-date wording (ch.26), and season details (ch.34, ch.35,
  ch.37) — none of that landed live. Those are Q4/Q7/Q10-adjacent open
  questions in this log; they need Zia's read, not a same-session guess
  layered on top of the Josiah correction. Treat this session's only real
  edits as the 6-chapter Ambrose revert plus the two Drake-custody wording
  fixes below.
- Also fixed live: ch.39, ch.40 — both said Drake was already in custody,
  contradicting Decision 3 (ch.41's early-morning arrest is the actual
  arrest). Reworded to "hold is broken" / "fraud file opened" so nothing
  claims custody before ch.41.
- **Confirmed live just now: Q22 (Martha) is NOT stamped or fixed anywhere
  yet** — ch.22 still reads "Martha Whitlock. Ambrose Whitlock's daughter,"
  unchanged. Still needs Zia's call before anyone touches it.

Only what was read from live `main` is stamped. Never stamp from memory or a
handoff claim. Condensed 2026-09-22 — detail trimmed, no findings dropped.

Legend: FIXED = edit read back live. READ = manual read, no change needed.
NOT PROOFED = mechanical pass only, no manual read yet.

**LAST CHAPTER STAMPED: ch.26.** Ch.1-26 read/fixed. Ch.27-45 not yet read
this pass.

## CORRECTION (2026-09-22, same session): Decision 4 below was wrong and
## is REVERSED. Do not cut or rewrite ch.17.
The original Decision 4 ("keep ch.21's kiss, cut ch.17's") was made from
the log's summary, without reading ch.17 or ch.21 directly. On actually
reading both in full:
- **Ch.17 IS a complete, uninterrupted first kiss.** Nothing external stops
  it; Wren and Theo end it themselves and go back to proofreading. It is
  clean, finished prose — not a stray duplicate to be cut.
- **Ch.21 is a real second kiss**, genuinely interrupted when Dev walks back
  into the room. Theo calls it "Interrupted. Again" - which only makes
  sense if a first interruption already happened. But ch.17's kiss was
  never interrupted by anything, so "Again" doesn't have a clean referent
  in ch.17 either.
- **Ch.26 makes it worse**: it describes "the kiss that had been
  interrupted by Priya's knock at the door" as the first one - an
  interruption that appears in NEITHER ch.17 nor ch.21.

So this is not a two-way duplicate with an obvious chapter to cut. It's a
three-way mismatch in how the couple's kiss history is described (ch.17:
no interruption; ch.21: interrupted, calls itself "again"; ch.26: recalls
an interruption by Priya that isn't in either prior scene). The likely real
shape is three escalating moments (ch.17 -> ch.21 -> ch.26 landing), which
needs a few words changed in ch.21 and/or ch.26 to match what actually
happens on the page - not a chapter deletion. NO CHAPTER TOUCHED. This
needs Zia's read of which detail (the "Again," or the "Priya's knock" line
in ch.26) should change, since both are small enough to fix once decided
but neither should be guessed.

## Decisions applied this session (2026-09-22, made without further
## checking with Zia — he delegated this call)
1. **Josiah vs Ambrose: SUPERSEDED by the STAMP at the top of this file.**
   Reverted to Ambrose in ch.2, 6, 7, 12, 13, 15. Ch.14 already correct
   (separate earlier fix). Do not re-add Josiah anywhere.
2. **Chapter order: not renumbering files.** "The fifteenth" is the one
   publication deadline. Ch.26's "summer solstice" line FIXED to match
   (`4175ca7`). Ch.18-23 countdown-number mismatches still unresolved.
3. **Drake's arrest: ch.41's early-morning home arrest is canon.** Ch.25 is
   FIXED (`f9e01f5`): Drake's lawyer makes contact, no custody, "custody
   hearing" line in ch.26 also fixed (`4175ca7`). Ch.39/40 also fixed this
   session (see STAMP above). **Ch.21's motel-pickup arrest is NOT YET
   FIXED** — still needs downgrading when the read reaches it.
4. **REVERSED — see correction above. Do not cut ch.17.**
5. **Drake's em-dash note: kept, the one deliberate exception to house
   style.** FIXED in ch.25 (`f9e01f5`).
6. **Ch.26 pacing: no longer settled** now that Decision 4 is reversed —
   depends on how the kiss-sequence question above gets resolved.

Related, lower-stakes, not decided: **Ambrose Kell** vs **Ambrose Whitlock**
naming collision (ch.19).

## Fixed and locked (do not re-touch without new evidence)
- Folio gap: 1887-1891. (ch.3, `207db70`)
- Josiah/Ambrose signatures: REVERTED to Ambrose in ch.2, 6, 7, 12, 13, 15
  this session (`e14a5fc`) — see STAMP at top. Ch.14 already correct
  (`bfeee2c`, separate fix, verified live). Ch.9 still open (Q21).
- Anachronisms (trial/leverage as past): fixed ch.8, ch.12. Ch.24-26 clean.
- ch.11: Odette Reynolds → Reyes. ch.22: Harriet is Theo's grandmother.
  ch.23 & ch.25: Harriet's age fixed to seventy-five (locked: born 1949,
  present 2024).
- ch.12: truncated sentence, ledger-finder attribution, 2 anachronisms.
- ch.15: full rewrite verified; Ambrose reversion applied on top this
  session.
- ch.18: internal day-count contradiction fixed.
- ch.24: READ, clean, confirms the ch.45 large-debt fix.
- ch.25: Harriet's age, Drake's custody status, em dash — FIXED (`f9e01f5`).
- ch.26: "Summer solstice" and "custody hearing" lines FIXED (`4175ca7`).
- ch.17: READ in full (this correction). Clean, complete prose. NOT a
  duplicate to cut. No text changed.
- ch.21: READ in full (this correction). Clean, complete prose, confirmed
  a real (not duplicate) second kiss scene, interrupted by Dev. No text
  changed. Also independently confirms: Drake's motel-pickup arrest (still
  needs the Decision 3 downgrade when the read reaches it in order);
  Wren's age twenty-one (matches ch.7); "three days" to publication
  (matches the ch.16/18/19 countdown chain, not ch.23's "twelve days" -
  another data point for the still-open chapter-ordering problem).
- ch.39, ch.40: FIXED this session (`e14a5fc`) — removed premature Drake
  custody claims, see STAMP above.

## Open questions (mostly unchanged; new items marked NEW)
- Q1 Elena Castellano: still open; three different ages given for when the
  grandmother died (fourteen/sixteen across chapters).
- Q2 Warden of the first debt: unresolved.
- Q3 Drake's 2005 Millbrook target: unresolved.
- Q4 Adelaide's exact relationship to Ambrose (student/successor/other):
  unresolved — do not guess, this session tried and reverted it.
- Q5 Ch.5 unreliable: unresolved.
- Q6 Lineage roster: unresolved.
- Q7 Calendar: still cycling through all four seasons across chapters;
  this session sketched a possible fix for ch.26/34/35/37/38 but did not
  push any of it — needs Zia, not a guess.
- Q8 Wren's mother's job: unresolved.
- Q9 Harriet's home terminology: unresolved.
- Q10 Kiss/rupture beat map: NEW, see correction above — three-way mismatch,
  not two-way, needs Zia's read.
- Q11 Archive building: still 5-6 competing descriptions.
- Q12 Two "Silas" characters: unresolved.
- Q13 Spaced hyphens as em-dash substitutes: still open generally; the
  ch.25 plot-point case is fixed.
- Q14 Line-edit style: not urgent.
- Q15 Denise's "grandson's husband" line: unresolved.
- Q16 Ambrose Kell vs Ambrose Whitlock: unresolved.
- Q17 "The house on the ridge": unresolved.
- Q18 M. Harrow / Harlan & Associates thread: self-contained so far.
- Q19 Search-cost mechanic: confirmed consistent.
- Q20 Shell company names ("Holloway & Finch" vs "Meridian Consulting"):
  presented as two different shells, not necessarily a conflict.
- Q21 NEW: ch.9's "Josiah Whitlock, a Warden generations before him" — is
  this a second, real Whitlock ancestor, or the same naming error in a
  different shape? Needs a direct read of ch.9 in full before any fix.
- Q22 NEW, CONFIRMED STILL OPEN (verified live): ch.22 still reads "Martha
  Whitlock. Ambrose Whitlock's daughter." Ambrose held the role 1872-1901;
  ch.22 places Martha as town clerk in 1978, which fits a granddaughter
  better than a daughter, but this is unfixed and needs Zia's confirmation
  before anyone changes it.

## Not done
- Read ch.9 in full and decide Q21 before touching its Whitlock lines.
- Resolve the three-way kiss-sequence mismatch (ch.17/21/26) — needs Zia,
  do not force-fix.
- Apply Decision 3 to ch.21 (downgrade the motel-pickup arrest).
- Sequential read of ch.27-45 (17 chapters remaining).
- Full season/countdown/Archive-naming reconciliation pass (Q7) — needs
  Zia's decisions on the specific dates, not a same-session guess.
- Cross-check against Books 1-3 (Q1, Q15).
- Decide Q22 (Martha's relation to Ambrose).
