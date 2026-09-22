# Book 4 proofed log

## STAMP 2 (2026-09-22, same session): Josiah/Ambrose is a REAL two-chapter
## conflict, not a one-sided naming error. NOTHING is live-fixed. Needs Zia.
Correcting my own STAMP 1 below, which reverted 6 chapters to Ambrose based
on reading ch.3 alone. Since then I also directly read all of ch.9 in full
(not summarized, the actual paragraphs), and the picture changed:

- **Ch.3 (the anchor):** only ever says Ambrose Whitlock. Held the role
  1872-1901, tried to end the bargain in 1889, failed, hid the complete
  terms. Josiah is never mentioned anywhere in ch.3.
- **Ch.9 (read in full just now):** independently tells the SAME shaped
  story — tried to end the bargain, failed, hid the complete terms rather
  than destroy them — but names the person **Josiah Whitlock, "a Warden
  generations before" Ambrose**, and dates two of his signed items 1847 and
  1863. The phrasing echoes ch.3 closely enough ("hid the complete terms
  rather than destroy them" vs. ch.3's "hid the complete terms") that this
  reads like it could be the same event misattributed, or a genuine
  parallel-generations theme (two Whitlocks, two failed attempts) that the
  book intends. Ch.9's text alone does not resolve which.
- Two of this project's canon files disagree on this exact point:
  `DATES_BIBLE.md` calls it an intentional two-Whitlocks theme and says so
  explicitly ("NOT a duplication error"). `CANON_NUMBERS.md` calls Josiah
  Ambrose's father who only signed the earlier documents, crediting the
  bargain-ending attempt to Ambrose alone. Neither file's claim should be
  trusted over the actual chapter text (rule zero), and the chapter text
  itself (ch.3 vs ch.9) is what actually conflicts — the two summary files
  are just downstream of that same unresolved conflict, not new evidence
  either way.
- **STAMP 1's revert never reached the chapters.** Checked live text for
  ch.2, 6, 7, 12, 13, 15 just now: all still read Josiah, unchanged. The
  mechanical fixer had not run yet. I pulled every Josiah->Ambrose entry
  out of `scripts/book4_fixes.json` (`3c0b806`) before it could run. **Do
  not re-add these fixes without Zia's decision below.**
- Ch.14 remains correctly Ambrose (separate, earlier fix, `bfeee2c`,
  verified live) and is not affected either way this needs deciding.
- What's actually still live and unchanged right now: ch.2, 6, 7, 12, 13,
  15 all say Josiah for this. Ch.3, 5, 19, 21 say Ambrose. Ch.9 says both,
  naming them as two different people.

**This needs Zia's call, framed as two real options, not a mechanical
fix:**
- **Option A — one person, naming error.** Josiah is a mistake; every
  Josiah reference in ch.2, 6, 7, 9, 12, 13 becomes Ambrose, and ch.9's
  "a Warden generations before him" line gets cut or rewritten since it
  wouldn't make sense once there's only one Whitlock.
  - Costs of A: **removes ~1,200 words** of independently-invented content
    in ch.9 (the 1847 marginal note and 1863 letter, two evocative
    period-voice passages), the "trend one) reduces the book's oldest
    dated document from 1847 to 1889 (fixed with Ambrose alone), and
    loses the "he kept trying, decades before Ambrose" beat that ch.9
    builds toward.
- **Option B — two people, intended parallel.** Josiah (1847, 1863) and
  Ambrose (1889) are both real, distinct Wardens who each independently
  tried and failed. Nothing in ch.9 or ch.3 changes. This needs a couple
  of connective sentences added somewhere (likely ch.9, since it's the
  chapter making the claim) to explicitly state the family relationship
  (is Josiah Ambrose's father, grandfather, a Warden with no blood tie
  before the role "passed outside the bloodline" language ch.3 uses?) so
  a reader doesn't read it as a slip.
  - Costs of B: needs a genealogy decision (Josiah's relation to Ambrose)
    that no chapter currently states outright; `CANON_NUMBERS.md`'s
    guess ("Ambrose's father") is not confirmed by any chapter text.

Neither option is a guess I'm making here — this is exactly the kind of
call the editorial charter says is Zia's, not a same-session mechanical
patch. Recommend presenting both to him plainly rather than picking one.

Only what was read from live `main` is stamped. Never stamp from memory or a
handoff claim. Condensed 2026-09-22 — detail trimmed, no findings dropped.

Legend: FIXED = edit read back live. READ = manual read, no change needed.
NOT PROOFED = mechanical pass only, no manual read yet.

**LAST CHAPTER STAMPED: ch.26.** Ch.1-26 read/fixed. Ch.27-45 not yet read
this pass.

## STAMP 1 (SUPERSEDED BY STAMP 2 ABOVE — kept for the audit trail only,
## do not act on this section)
Read ch.3 live directly. Concluded Ambrose alone was correct and queued a
revert of ch.2, 6, 7, 12, 13, 15 to Ambrose. This was based on ch.3 alone,
before reading ch.9 in full. See STAMP 2: the revert never reached the
chapters and has been withdrawn pending Zia's decision between the two
real options above. Also fixed this session and NOT superseded: ch.39,
ch.40 (removed premature Drake-in-custody claims, still correct, see
Decisions section below) and Q22 confirmed still open (Martha in ch.22).

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
1. **Josiah vs Ambrose: NOT DECIDED. See STAMP 2 at the top of this file
   for the real two-option framing.** Do not add or remove any Josiah or
   Ambrose reference anywhere until Zia picks Option A or B.
2. **Chapter order: not renumbering files.** "The fifteenth" is the one
   publication deadline. Ch.26's "summer solstice" line FIXED to match
   (`4175ca7`). Ch.18-23 countdown-number mismatches still unresolved.
3. **Drake's arrest: ch.41's early-morning home arrest is canon.** Ch.25 is
   FIXED (`f9e01f5`): Drake's lawyer makes contact, no custody, "custody
   hearing" line in ch.26 also fixed (`4175ca7`). Ch.39/40 also fixed this
   session (`3c0b806`). **Ch.21's motel-pickup arrest is NOT YET FIXED**
   — still needs downgrading when the read reaches it.
4. **REVERSED — see correction above. Do not cut ch.17.**
5. **Drake's em-dash note: kept, the one deliberate exception to house
   style.** FIXED in ch.25 (`f9e01f5`).
6. **Ch.26 pacing: no longer settled** now that Decision 4 is reversed —
   depends on how the kiss-sequence question above gets resolved.

Related, lower-stakes, not decided: **Ambrose Kell** vs **Ambrose Whitlock**
naming collision (ch.19).

## Fixed and locked (do not re-touch without new evidence)
- Folio gap: 1887-1891. (ch.3, `207db70`)
- Anachronisms (trial/leverage as past): fixed ch.8, ch.12. Ch.24-26 clean.
- ch.11: Odette Reynolds → Reyes; age/decade fix (`3c0b806`). ch.22: Harriet
  is Theo's grandmother. ch.23 & ch.25: Harriet's age fixed to seventy-five
  (locked: born 1949, present 2024).
- ch.12: truncated sentence, ledger-finder attribution, 2 anachronisms.
- ch.15: full rewrite verified. (Josiah/Ambrose line in ch.15 UNCHANGED,
  see STAMP 2 — do not touch pending Zia.)
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
- ch.39, ch.40: FIXED this session (`3c0b806`) — removed premature Drake
  custody claims (independent of the Josiah/Ambrose question).

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
- Q10 Kiss/rupture beat map: three-way mismatch, needs Zia's read (see
  CORRECTION above).
- Q11 Archive building: still 5-6 competing descriptions.
- Q12 Two "Silas" characters: unresolved.
- Q13 Spaced hyphens as em-dash substitutes: still open generally; the
  ch.25 plot-point case is fixed.
- Q14 Line-edit style: not urgent.
- Q15 Denise's "grandson's husband" line: unresolved.
- Q16 Ambrose Kell vs Ambrose Whitlock: unresolved (distinct question from
  Q21 — Kell is confirmed a different, later character in ch.19).
- Q17 "The house on the ridge": unresolved.
- Q18 M. Harrow / Harlan & Associates thread: self-contained so far.
- Q19 Search-cost mechanic: confirmed consistent.
- Q20 Shell company names ("Holloway & Finch" vs "Meridian Consulting"):
  presented as two different shells, not necessarily a conflict.
- Q21 SUPERSEDED by STAMP 2 above — this is now the main Josiah/Ambrose
  question, framed as Option A vs Option B, not a simple "which chapter is
  wrong" question. See STAMP 2, don't treat this as a smaller side item.
- Q22 CONFIRMED STILL OPEN (verified live): ch.22 still reads "Martha
  Whitlock. Ambrose Whitlock's daughter." Ambrose held the role 1872-1901;
  ch.22 places Martha as town clerk in 1978, which fits a granddaughter
  better than a daughter, but this is unfixed and needs Zia's confirmation
  before anyone changes it. Note: if Zia picks Option B on Q21 (two
  Whitlocks), this doesn't change — Martha's ambiguity is about Ambrose's
  own descendants, not about Josiah.

## Not done
- Get Zia's call on Q21 (Option A vs B) before touching ch.2, 6, 7, 9, 12,
  13, 15 again in any direction.
- Resolve the three-way kiss-sequence mismatch (ch.17/21/26) — needs Zia,
  do not force-fix.
- Apply Decision 3 to ch.21 (downgrade the motel-pickup arrest).
- Sequential read of ch.27-45 (17 chapters remaining).
- Full season/countdown/Archive-naming reconciliation pass (Q7) — needs
  Zia's decisions on the specific dates, not a same-session guess.
- Cross-check against Books 1-3 (Q1, Q15).
- Decide Q22 (Martha's relation to Ambrose).
- Once Q21 is decided, reconcile `DATES_BIBLE.md` and `CANON_NUMBERS.md`
  so they stop disagreeing with each other on this point.
