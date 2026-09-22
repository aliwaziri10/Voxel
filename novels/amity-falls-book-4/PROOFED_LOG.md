# Book 4 proofed log
_Rewritten clean 2026-09-22 — old stamps and superseded sections removed.
See git history for the full trail if needed; nothing here contradicts
itself anymore. `CANON_NUMBERS.md` now merges what used to be a second,
disagreeing file (`DATES_BIBLE.md`, deleted). Read that file for all
dates/ages/names; this file is for open editorial questions and chapter
read-progress only._

Legend: FIXED = edit read back live. READ = manual read, no change needed.
NOT PROOFED = mechanical pass only, no manual read yet.

## SESSION 2026-09-22 (later) — honesty note on inherited claims

A pasted transcript fragment (source unclear, not from this file) claimed
Q4, Q7, Q8, Q11 were closed this session, including specific language like
"Q4 confirmed: this closes... no anachronism" and "Q7 is answered — Elena
is a retired baker." **That transcript does not match this book.** Book 4
has no character named "Elena," no "Silas Kettering vs. Silas Harker in
Millbrook/Weather" framing distinct from what's logged below, and Q4/Q7
were NOT independently re-verified by this session before that claim was
made. Rather than propagate an unverified claim, this session went back to
live `main` and checked only what could actually be confirmed against the
real chapter files. Result:

- **Q11 (two Silas characters) — genuinely CLOSED, independently verified
  this session**, by grepping the full live manuscript directly (not
  trusting the pasted claim): "Silas Kettering" (ch.5 area — the coerced
  Millbrook Finder, forced by Drake, confirmed via Dev's dialogue) and
  "Silas Harker" (the Weather who held the 2003 wind debt, ch.37/38 area)
  are two distinct, already-differentiated characters. Ch.38 explicitly
  narrates the distinction on the page: "Silas Harker... Not Old Man
  Harker, who was alive and difficult." No collision, no fix needed.
  Moved from Open to Closed below.
- **Q8 (Harriet's home terminology) — genuinely CLOSED, FIXED this
  session.** Grepped every one of the 45 live chapter files individually
  (not the concatenated manuscript, not GitHub's lagging code-search
  index) for "nursing home" and "assisted living." Found ch.4, ch.30,
  ch.34, ch.41 already said "assisted living facility" (ch.41 names it
  "Willow Creek Assisted Living"); ch.9 (2 instances) and ch.22
  (1 instance) said "nursing home" instead. Standardized ch.9 and ch.22
  to "assisted living facility" to match the majority and the named
  facility. Commits: `e48fdeb` (ch.9), `990a104` (ch.22). Both pushed to
  `main` and re-read back live to confirm. Moved from Open to Closed
  below.
- **Q4, Q7 — still genuinely OPEN.** Not touched this session beyond
  confirming they're still listed open below. The earlier pasted claim
  that Q4 was "closed as verified-clean" is NOT reflected here and should
  not be trusted until someone actually re-reads ch.5 and the relevant
  Ambrose/Kell chapters fresh and logs the result the way Q8/Q11 were
  just logged above, with a specific quote and a specific chapter.

## GENUINE FRESH SEQUENTIAL READ - IN PROGRESS (started 2026-09-22)

🔒 ch.1-10 claimed by Claude session, 2026-09-22 (IST). This is explicitly
NOT inheriting the "complete sequential read" claim below (see Session
Handoff) - every chapter here is being fetched fresh from live `main` and
read start to finish by this session, specifically because that claim had
never been independently re-verified and confusion over that exact point
caused real friction this session. Two spot-checks were run against this
log's other claims before starting (ch.16's "granddaughter's husband" line,
ch.20's Decision B "one week" fix) - both confirmed accurate against live
text, so the log's other entries are being treated as reliable, not
re-verified line by line.

- ch.1: READ FRESH, clean, no fix needed. Confirms (independently, not
  copied from any prior log entry): Theo Marsh's age is 26 ("twenty-six"
  stated directly in his intro). Priya is a Caller ("the low hum of a
  Caller, the calm that reached anyone within five feet"). "Nineteen years
  since Millbrook" (Drake's first attempt) matches the book's other
  nineteen-year references. "Twelve months since the ring" matches ch.20's
  identical phrasing exactly. This is the opening chapter: Wren proposes
  the Archive Project to the council, meets Theo Marsh for the first time
  the next morning. Establishes the county-index "standing arrangement"
  restriction (no classification code, "access restricted") that later
  chapters build on. No Ambrose/Josiah/Kell mention. No countdown numbers
  that conflict with anything (Odette's "two weeks, three if the weather
  turns" is about the archive building's roof, not publication - different
  clock, no conflict).
- ch.2: READ FRESH, clean, no fix needed. Independently confirms the
  Josiah/Ambrose split a THIRD time (after ch.15's letter, ch.18's Theo
  line): the 1847 ledger's recorder is named directly on the page -
  "Josiah Whitlock. The amount: seven years. The memory: his sister's
  face" - while Ambrose is separately named as the one who "held the
  Warden of the first debt role... tried to end the bargain... hid the
  complete terms... taught Adelaide how to renew it." Two different roles,
  two different Whitlocks, both consistent with the book's locked
  decision. Ambrose Kell also referenced again, consistent with earlier
  sightings, still clearly a separate person from either Whitlock.
  NEW (not previously logged, deliberate in-text plot device, not an
  error): a near-miss surname, "Castellan" (a Weather lineage, distinct
  from Wren's own "Castellano" family), appears in the same 1847 ledger
  attached to a redirected/blank toll entry. The text itself spells out
  the letter-by-letter distinction ("Castellan. Not Castellano.") rather
  than leaving it ambiguous, so this reads as an intentional mystery hook,
  not a typo - worth tracking for payoff in later chapters, not fixing.
  Also new: an early, SEPARATE 14-day countdown (a county records audit
  triggered by the "standing arrangement" restriction, distinct from the
  much-later ch.16-21 countdown chain over Drake's teaser/transcripts).
  Since "eight months" elapses before that later chain begins per ch.13/
  20, this earlier audit deadline must get resolved somewhere in ch.3-15 -
  flagging to watch for its resolution rather than assuming a conflict.
  Also confirms Wren's age 21 ("became the valley's lead documenter at
  twenty-one," Yusuf's line) - matches ch.7/21 exactly. New data, no
  conflict: Denise's age given as 78 here (not previously logged from any
  chapter read so far).
- ch.3: READ FRESH, clean, no fix needed. Wren's grandmother's death age
  ("She had been fourteen when her grandmother died") is live and matches
  the Q1 fix - fourteen is confirmed correctly in place, not reverted.
  This is the PAYOFF chapter for ch.1-2's setup, not a new, separate
  thread: the missing folios (1887-1891) are the "standing arrangement"
  mystery from ch.1-2's county-index restriction. Fourth independent
  confirmation this session of the Josiah/Ambrose split (Ambrose Whitlock,
  Warden 1872-1901, tried to end the bargain in 1889, hid the complete
  terms). RESOLVES a tension flagged earlier this session: the Warden of
  the first debt is explicitly a ROLE, not a bloodline, with a clean
  succession chain given on the page (Whitlock 1872-1901 -> Sarah Voss,
  a Mender, Mara's great-grandmother, 1901-1947 -> a Weathers line -> a
  Caller line -> vacant since a Warden's 1987 death -> Yusuf, appointed
  Warden only after Denise's freeing/the ring). This cleanly explains how
  Yusuf could be council "chair" during Denise's fifty secret years (ch.20
  dialogue) while the separate Warden office sat vacant - chair and Warden
  are different offices, exactly as suspected, now confirmed on the page.
  Also reinforces Mara's family as MENDERS (Voss line), consistent with
  the majority label from ch.19's "the Mender who healed the valley's
  wounds." Confirms Wren's age 21 a second time this session. New
  worldbuilding, not a conflict: standing arrangement was "suspended"
  1887-1889 and "resumed" 1890-1891 per county ledger notation; Drake's
  partial record has 1890-91 but not 1887-89, which the chapter treats as
  the live mystery driving the plot (connects directly to Q19/Q20 above -
  not a separate issue, the same one unfolding). No em dashes, no spaced
  hyphens seen. No new open questions raised - this chapter answers more
  than it asks.

## SESSION HANDOFF (2026-09-22, end of session)

**CONFIRMED this session (verified against live `main`, not memory):**
- Q13 closed — ch.16's "granddaughter's husband" line was already
  correct; an unsourced pasted claim said otherwise and was wrong.
- Q17 closed — fresh full-repo grep of all 45 live chapters found
  "Martha Whitlock" only in ch.22, consistently "Ambrose Whitlock's
  daughter," zero "granddaughter" hits anywhere. Fully confirmed, not
  just leaning.
- Q1 closed — grandmother's age at death was three-way inconsistent
  (ch.3: twelve, ch.7/ch.15: fourteen, ch.24: sixteen). Fourteen was the
  majority (2 of 4 chapters) and neither outlier carries plot weight tied
  to the specific number. FIXED ch.3 and ch.24 to "fourteen" (commits
  `268ae50`, `e82970a`). Ch.7 and ch.15 already said fourteen, untouched.
  RE-VERIFIED 2026-09-22 (fresh sequential read, ch.3): "fourteen" is
  live and correct.
- Q11 closed — two Silas characters (Kettering/Harker) independently
  verified distinct on the page, no fix needed.
- Q8 closed — FIXED. Harriet's home standardized to "assisted living
  facility" in ch.9 and ch.22 (commits `e48fdeb`, `990a104`).

**HYPOTHESIS / inherited, not independently re-verified this session:**
- Everything under "Fixed and locked" and "Decisions locked" below was
  read and fixed in *earlier* sessions today, not this one. This session
  did NOT do a fresh sequential read of ch.1-45 — it did targeted grep
  verification of specific flagged items only (Q1, Q8, Q11, Q13, Q17).
  The book-wide claim "full sequential read complete" is carried over
  from those earlier sessions and has not been independently re-confirmed
  here. A NEW session has now started an actual fresh read - see the
  section above this one (ch.1-3 done, all clean, and independently
  corroborating the locked decisions rather than contradicting them).
- Per the user's explicit instruction this session: continuing to close
  the Q2-Q18 list via targeted verification (not a full re-read) unless
  told otherwise.

**NEXT STEPS, in open-question order:** Q2 (Drake's 2005 Millbrook
target), Q3 (Adelaide/Ambrose relationship — do not guess, needs Zia),
Q4 (ch.5 anachronism — genuinely still open, see honesty note at top of
file), Q5 (lineage roster), Q6 remainder (season pass), Q7 (Wren's
mother's job — genuinely still open), Q10 (Archive description), Q12
(spaced hyphens, general), Q14 (house on the ridge), Q15/Q16
(self-contained, likely fine), Q18 (Theo's age, low priority). Then:
Books 1-3 cross-check, ch.27-45 lexical/tell-density pass (never done for
that stretch).

---

**LAST CHAPTER STAMPED: ch.45. FULL SEQUENTIAL READ OF THE BOOK COMPLETE**
(2026-09-22, earlier sessions). A follow-up verification/decision pass
re-read ch.16, 18, 19, 20, 21, 28, 29, 31, 37 in full (not from memory) to
map the countdown cluster, then made and applied three editorial
decisions per Zia's handoff ("it's your call, fix everything, but not
without diligence, review critically"). All three were done as targeted,
diff-verified edits — no chapter was cut or rewritten wholesale. See
below. Further follow-up sessions fixed Q19 (`11cd9f0`), closed the
ch.28/29/31/37 day-count cross-check (reconciled, not fixed — no
contradiction found once read together), fixed Q9 (`c4dbf27`), closed
Q13 (verified ch.16 was already correct), and this session closed Q1,
Q8, Q11, and Q17 (see Session Handoff above).

## Decisions made and applied (2026-09-22)

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
  wording), nothing else touched. VERIFIED AGAIN 2026-09-22 (fresh
  sequential read pass): live text confirmed - reads exactly as
  described, no drift.

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
Ch.2-3 (this session's fresh read) add an even EARLIER, separate 14-day
countdown (a county records audit over the missing 1887-91 folios) that
is the book's actual opening dramatic clock, resolved before the later
chain starts - not yet seen resolved on the page; watch ch.4-15.

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

**Q13 — Denise's "grandson's/granddaughter's husband" line. CLOSED, no
fix needed (2026-09-22).**
- A prior unverified claim (not from this log — surfaced via a pasted,
  unsourced transcript) asserted ch.16 read "grandson's husband," which
  would contradict Mara (Denise's granddaughter) being Caleb's wife.
- Re-fetched ch.16 directly from the live `main` branch (not from memory,
  not from the pasted claim) before touching anything. The actual live
  line reads: "I took two years from my granddaughter's husband." This
  is already correct — Caleb is Mara's husband, Mara is Denise's
  granddaughter. There was never an error here. The pasted claim was
  wrong about what the text says. RE-VERIFIED AGAIN 2026-09-22 (fresh
  sequential read pass): confirmed identical live text.
- No chapter edit made. Moved from Open Questions to Closed.

**Q17 — Martha Whitlock's relation to Ambrose. FULLY CLOSED (2026-09-22,
this session).**
- Re-fetched all 45 live chapters fresh from `main` and grepped the raw
  text directly (not GitHub's code-search index, which lags) for
  "martha" and for "whitlock" near "granddaughter" across the whole
  book. Zero matches anywhere outside ch.22 (8 mentions, all "Ambrose
  Whitlock's daughter"), zero "granddaughter" references at all in the
  entire book. No second, conflicting source exists. Confirmed, not
  leaning. See `CANON_NUMBERS.md`.

**Q1 — Elena/grandmother's age at death. CLOSED, FIXED (2026-09-22, this
session).**
- Grepped all 45 live chapters for "grandmother died" / "died when...
  was". Found three different ages: ch.3 "twelve", ch.7 "fourteen",
  ch.15 "fourteen", ch.24 "sixteen". Fourteen is the majority (2 of 4)
  and no plot point in ch.3 or ch.24 depends on the specific number.
  FIXED ch.3 (`268ae50`) and ch.24 (`e82970a`) to "fourteen". Ch.7 and
  ch.15 already correct, untouched. See `CANON_NUMBERS.md`.

**Q11 — Two "Silas" characters. CLOSED, no fix needed (2026-09-22, this
session).**
- Downloaded the full live manuscript and grepped directly for "Silas."
  Found exactly two hits, both distinct on the page: "Silas Kettering,"
  the coerced Millbrook Finder Drake threatened into silence (Dev's
  dialogue, ch.5 area — "He served two years. Got out in '09... Drake
  didn't ask. He told. Said he'd hurt Kettering's daughter"), and "Silas
  Harker," the Weather who held the 2003 wind debt (ch.37/38 area — "The
  Weather who held the wind debt in 2003... Not Old Man Harker, who was
  alive and difficult"). The text itself makes the distinction explicit
  on the page. No collision, no fix needed. Moved from Open to Closed.

**Q8 — Harriet's home terminology. CLOSED, FIXED (2026-09-22, this
session).**
- Grepped every one of the 45 individual live chapter files (not the
  concatenated manuscript, not GitHub's code-search index) for "nursing
  home" and "assisted living." Found ch.4, ch.30, ch.34, ch.41 already
  said "assisted living facility," with ch.41 naming it specifically:
  "Willow Creek Assisted Living." Ch.9 (2 instances) and ch.22 (1
  instance) said "nursing home" instead — the minority, and the term
  Theo's own dialogue never uses elsewhere.
- FIXED: standardized both instances in ch.9 and the one in ch.22 to
  "assisted living facility," matching the established majority and the
  named facility. Commits `e48fdeb` (ch.9) and `990a104` (ch.22), both
  pushed directly to `main` and re-read back live to confirm the exact
  wording landed. No other text in either chapter touched.

## Decisions locked (do not re-touch without new evidence)
1. Josiah/Ambrose: DECIDED — confirmed through the full sequential read,
   and independently reconfirmed a fourth time by this session's fresh
   ch.2-3 reads (see above).
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
6. Denise's granddaughter's-husband line (ch.16): correct as written,
   refers to Mara/Caleb. **CLOSED (Q13).**
7. Martha Whitlock is Ambrose's daughter, confirmed book-wide, no
   conflicting reference exists. **CLOSED (Q17).**
8. Grandmother's death age standardized to fourteen across ch.3, ch.7,
   ch.15, ch.24. **CLOSED (Q1).**
9. The Warden of the first debt is a ROLE, not a bloodline, distinct
   from council "chair" - succession given on the page in ch.3 (Whitlock
   -> Voss/Mender -> Weathers line -> Caller line -> vacant since 1987 ->
   Yusuf, appointed after Denise's freeing). **CONFIRMED, not previously
   locked explicitly - added this session from the ch.3 fresh read.**
10. Silas Kettering (Millbrook Finder) and Silas Harker (2003 Weather)
    are two distinct characters, already differentiated on the page.
    **CLOSED (Q11).**
11. Harriet Marsh's home is "assisted living facility" (Willow Creek
    Assisted Living), standardized across all mentions. **CLOSED (Q8,
    `e48fdeb`, `990a104`).**

Related, lower-stakes, not decided: Ambrose Kell vs. either Whitlock —
already confirmed distinct in ch.19, and reconfirmed distinct in ch.27-45,
not actually a conflict, just a name worth double-checking on sight since
three "Ambrose/Whitlock"-adjacent names exist in this book (Josiah
Whitlock, Ambrose Whitlock, Ambrose Kell).

## Fixed and locked (do not re-touch without new evidence)
- Folio gap: 1887-1891 (ch.3, `207db70`). RE-VERIFIED 2026-09-22 (fresh
  sequential read): this is not just a fixed date range, it's the live
  central mystery of ch.1-3 - do not "fix" the Castellan/Castellano near-
  miss or the standing-arrangement-suspended language, both are
  deliberate plot devices, not errors (see Q19/Q20).
- Anachronisms (trial/leverage as past): fixed ch.8, ch.12. Ch.24-26 clean.
- Ch.11: Odette Reynolds → Reyes; age/decade fix. Ch.22: Harriet is Theo's
  grandmother. Ch.23, ch.25: Harriet's age fixed to seventy-five. Ch.41:
  same fix applied (`29be7e8`).
- Ch.12: truncated sentence, ledger-finder attribution, 2 anachronisms.
- Ch.15: full rewrite verified.
- Ch.16: RE-READ in full 2026-09-22 (three times now — countdown pass,
  Q13 verification, and this session's fresh sequential read). Clean.
  Confirms 14-day figure ("the fifteenth"), first link in the countdown
  chain. Confirms Denise's "granddaughter's husband" line is correct
  (Q13). No fix needed.
- Ch.17: READ in full. Clean, complete prose, not a duplicate. The real
  first kiss — see Q9 above. No change.
- Ch.18: internal day-count contradiction fixed. RE-READ in full
  2026-09-22: clean, confirms 10-day figure, fits the chain.
- Ch.19: RE-READ in full 2026-09-22. Clean. Confirms 1-week figure and
  the first Wren/Theo rupture-and-resolution ("together," testimony not
  ledger). No fix needed to this chapter itself - it's the anchor
  Decision C points back to.
- Ch.20: FIXED (`da6ebe0`, Decision B). Timeline reset resolved without
  cutting the Hal/Marta scene. RE-VERIFIED 2026-09-22 (fresh sequential
  read): live text confirmed current, "one week" throughout.
- Ch.21: READ in full, FIXED (`beb46da`, Decision A; `11cd9f0`, Q19).
  Confirmed a real second kiss scene interrupted by Dev/the deputy at the
  gate — this is the scene ch.26 now correctly references (Q9). Also
  confirms: Wren's age 21 (matches ch.7); "three days" to publication,
  the last link in the ch.16/18/19/21 chain. Q19 fixed: deputy's "your
  brother-in-law's evidence" (unsupported relationship claim) -> "Dev's
  evidence" — Dev is Priya's brother, not Wren's, per ch.13/14; no
  marriage link between Wren and Priya/Dev exists anywhere in the book.
- Ch.24: READ, clean, confirms the ch.45 large-debt fix. Grandmother's
  death-age line FIXED this session (Q1, `e82970a`).
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
  itself (6:45am, home, no resistance) matches Decision A exactly - this
  chapter is the canonical arrest, everything else measures against it.
- Ch.9: FIXED — "nursing home" -> "assisted living facility", 2
  instances (`e48fdeb`, Q8, this session). Otherwise clean.
- Ch.22: FIXED — "nursing home" -> "assisted living facility", 1
  instance (`990a104`, Q8, this session). Otherwise clean.

## Open questions
- Q2 Drake's 2005 Millbrook target: unresolved.
- Q3 Adelaide's exact relationship to Ambrose (student/successor/other):
  unresolved. Do not guess — a prior pass tried and reverted it.
- Q4 Ch.5 unreliable/anachronistic (Ambrose alive 2005-2009): unresolved.
  NOT closed despite an earlier unverified transcript claim to the
  contrary this session — see honesty note at top of file.
- Q5 Lineage roster: unresolved.
- Q6 Calendar: still cycles through all four seasons inconsistently across
  chapters. Needs Zia's specific date decisions, not a guess. The
  ch.28/29/31/37 leg of this is now closed (see Countdown data); the rest
  of Q6 (season progression across the full 45 chapters) is still open.
- Q7 Wren's mother's job: unresolved. NOT answered despite an earlier
  unverified transcript claim ("Elena is a retired baker") — that name
  doesn't appear in this book's live text; see honesty note at top of
  file.
- Q10 Archive building: 3+ competing physical descriptions.
- Q12 Spaced hyphens as em-dash substitutes: open generally; the ch.25
  plot-point case is fixed.
- Q14 "The house on the ridge": unresolved.
- Q15 M. Harrow / Harlan & Associates thread: self-contained so far.
- Q16 Shell company names ("Holloway & Finch" vs "Meridian Consulting"):
  presented as two different shells, not necessarily a conflict.
- Q18 Theo's age: 26 stated vs. 27 by birth-year math. Low priority.
- Q19 (fresh-read, ch.2-3) The early county-audit 14-day countdown over
  the missing 1887-91 folios: this is the book's opening dramatic clock,
  not yet seen resolved on the page. Watch ch.4-15.
- Q20 (fresh-read, ch.2-3) "Castellan" (Weather) vs "Castellano" (Wren's
  Finder family) near-miss surname, tied to a redirected toll in the
  missing-folios mystery: confirmed deliberate across two chapters now -
  do not fix, watch for payoff.

## Not done
- Full season/Archive-naming reconciliation pass (Q6 remainder, Q10).
- Cross-check against Books 1-3.
- Mechanical/lexical/tell-density pass (em dashes, repetition, staged
  constructions) for ch.27-45 specifically — this pass was a continuity
  read, not the full lexical sweep the earlier chapters got.
- Genuine fresh sequential read of all 45 chapters: IN PROGRESS, see top
  of file (ch.1-3 done, ch.4-45 remaining).
- Q2, Q3, Q4, Q5, Q6 (remainder), Q7, Q10, Q12, Q14, Q15, Q16, Q18: still
  open, none touched this session beyond the honesty note above.