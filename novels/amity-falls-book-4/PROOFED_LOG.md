# Book 4 proofed log

Only what was read from live `main` is stamped. Update this file every time a
chapter is verified. Never stamp from memory or from a handoff claim.

Legend: APPLIED = fix read back from the live chapter. QUEUED = in
`scripts/book4_fixes.json`, not yet in the chapter. SEEN = seen in an earlier
grep, not re-read. SKIMMED = mechanical/grep sweep only, not the full
sequential manual read. NOT PROOFED = no continuity check done.

## Whole book
- 2026-09-21 15:42 UTC: mechanical proofread pass, all 45 chapters. 0 hard
  violations, 0 em dashes. Advisory flags only. This is NOT a continuity or
  read-through proof. Only skipped fix: chapter 5 "She was the Warden before
  him. She tried to end the bargain." (2 matches).
- 2026-09-21 15:50 UTC: second automated pass, commit `f8551915`. Auto-fixed
  tell-phrases in chapter_15 (3) and chapter_37 (6) — diffed against live
  `main` and confirmed below.
- 2026-09-21 16:04 UTC: DONE — Drake countdown-clock item from
  `PRE_PUBLISH_AUDIT_2026-09-21_CORRECTED.md` reconciled. Grepped all 45 live
  chapter files (not the concatenated manuscript, which has no chapter
  markers) for every deadline phrase. Result: four separate, internally
  consistent deadline threads (Drake's ch4 "thirty days" ultimatum; the
  court's ch5/ch9 "four days" evidence deadline; the council's ch18→ch28/31
  "ten days"→"nine days" accelerated publication vote; the final
  ch31/37/38 "ten days"→"six days" injunction-response/print deadline). No
  contradiction, no chapter text changed. See audit file for the full
  chapter-by-chapter trace. Math/dates thread is CLOSED.
  (Ch.5 re-read note: the "four days" thread is fine as a deadline thread,
  but the day COUNT inside ch.5 itself is inconsistent. See ch.5 entry.)
- ⚠️ AUDIT DISCREPANCY (ch.3, extended at ch.5): the corrected audit states
  "Ambrose Whitlock: 'Warden 1872–1901... died 2009' — unsupported; none of
  those figures appear" anywhere in the manuscript. Wrong on both halves.
  chapter_03 states "He held the role from 1872 to 1901" verbatim, and
  chapter_05 states "He died in 2009" (Wren) and "He died four years later"
  after a 2005 sealing (Theo). So the figures DO appear. The real problem is
  that they contradict each other: a Warden active 1872-1901 cannot be
  alive in 2005 or die in 2009. That is a chapter error (ch.5 vs ch.3), not
  only an audit error. See ch.5 entry.
- OPEN QUESTION FOR ZIA (raised at ch.4, applies book-wide): chapters 3, 4
  and 5 use spaced hyphens (" - ") as dash substitutes (ch.3 ~8, ch.4 ~14,
  ch.5 many), with zero true em dashes. The mechanical passes count only
  U+2014, so they cannot see this. Looks like the pipeline's house form.
  Not changed anywhere. Decision needed: treat " - " as an em-dash dodge
  and sweep the whole book, or accept it as house form. Ch.6-12 skim adds
  more data: ch.6 (~3), ch.7 (~9), ch.8 (~3), ch.9 (0), ch.10 (~6),
  ch.11 (~11), ch.12 (~22). Rising, not falling. Still unresolved.
- DECIDED AND APPLIED (2026-09-21): canonical missing-folio gap is
  1887-1891 (five years). Last volume present before the gap: 1886. First
  volume back: 1892. Basis: Priya's explicit statement in ch.3, the
  figure the log/audit already carried, 3 suspended years (1887-89) plus 2
  resumed (1890-91) making exactly 5, and Ambrose's 1889 attempt landing
  inside it. Applied to ch.3 in commit `207db70` (see ch.3 entry). Every
  later chapter that cites the gap years must be checked against this as
  the read reaches it.
- ⚠️ NEW MAJOR CONFLICT, ch.6-12 skim (2026-09-22): re-opens the Elena
  question the ch.3 fix was based on. **The ch.3 fix (Elena Castellano ->
  Clara Castellano for the 1870s ancestor, keeping "Elena" as the
  grandmother) was made on ch.11's evidence alone** ("Elena Castellano...
  my grandmother," a dead Finder who did a 1985 search and stopped singing
  afterward). A grep sweep of ch.6-10 and ch.12 (not yet the full
  sequential read — this was a skim, done out of order because ch.13 was
  already in progress) finds EIGHT separate passages across SIX chapters
  that consistently use a different split:
    - "Elena Castellano" = Wren's living MOTHER. Introduced by name in
      ch.7 (baker, fifty-three, kneading dough), called "Mama" by Wren
      (ch.7 twice), present-tense and alive throughout ch.6-9, arguing
      with Wren about publication.
    - "your/my grandmother" (never named "Elena" in these chapters) =
      already DEAD, was a Finder, died when Wren was fourteen (ch.7, ch.9),
      found the 1893 ledger and brought it to the council in 1998 (ch.12),
      never told Wren the full terms (ch.8, ch.9).
  This matches ch.5's "Elena = mother" and ch.4's "grandmother = a Finder"
  — NOT ch.11's "Elena = grandmother." Ch.11 is now the outlier (1 chapter)
  against ch.4/5/6/7/8/9/12 (7 chapters). **Not reversing the ch.3 fix
  yet** — that would be flipping it twice on partial evidence again, and
  ch.11's own passage is a real, specific scene (the lullaby/1985 search)
  that has to be reconciled, not just outvoted. CONFIRMED FURTHER by
  ch.7's real read (2026-09-22): Elena is named and present in the scene
  eleven times as Wren's living mother (kneading dough, crying, called
  "Mama"), and the chapter separately references "your grandmother," dead,
  four more times, never once calling her Elena. The mother-reading is now
  extremely solid for ch.6-9. Possibilities, undecided: (a) ch.11's "Elena"
  is the error and should be renamed to whatever the grandmother is
  actually called elsewhere (possibly "Adelaide" — see ch.12's "my
  grandmother... Adelaide's letter" juxtaposition, still ambiguous); (b)
  there are genuinely two Castellano women a generation apart and ch.11
  needs a different surname/first name for the 1985-search Finder,
  distinct from mother-Elena; (c) something else. FLAGGING FOR ZIA, not
  deciding. Do not touch ch.3, ch.7, or ch.11 further until this is
  resolved — the real read reaching ch.11 should treat this as the top
  item.
- ⚠️ NEW MAJOR CONFLICT, ch.6 vs ch.7 real read (2026-09-22): **the ch.6
  fix I just made (changed "Ambrose Whitlock wrote that he hid the terms"
  -> "Josiah Whitlock," on the basis that ch.6's OWN manuscript is
  explicitly signed "Josiah Whitlock... 1847") is now contradicted by
  ch.7, read immediately after.** Ch.7 independently and repeatedly (4x:
  lines 15, 17, 89, 117) attributes this exact story — tried to end the
  bargain, failed, hid the complete terms rather than destroy them — to
  **Ambrose** Whitlock, not Josiah. Ch.7 even distinguishes "Ambrose Kell"
  (a different, already-faced antagonist) from "Ambrose Whitlock" in the
  same paragraph (line 17), which reads as a deliberate authorial choice
  to keep the Whitlock name Ambrose, not a slip. This means my ch.6 fix
  may have gone the wrong direction — same shape of problem as the ch.3
  Elena fix: I corrected ch.6 for internal-chapter consistency without
  yet knowing what the surrounding chapters actually use. **NOT reverting
  ch.6 again yet** — need at minimum ch.8/9's usage before touching it a
  third time; ch.9's "J. Whitlock, 1847" and "J. Whitlock, 1863" (two
  dated signatures, same initial) may mean Josiah signed twice across 16
  years, or may mean there were two Whitlocks who each tried and failed
  (Josiah 1847, Ambrose 1872-1901) and ch.6's manuscript excerpt and ch.7's
  spoken references are simply talking about two different men who did
  the same thing a generation apart — which would mean NEITHER ch.6 nor
  ch.7 is wrong, and my ch.6 edit was actually unnecessary. FLAGGING FOR
  ZIA. Do not touch ch.6's Josiah/Ambrose line again until ch.8, ch.9 (real
  read) are checked for which name attaches to the "hid the terms, tried
  and failed" story there.
- CARRY-FORWARD CHECKS for the rest of the read (raised by ch.3-5):
  1. Ambrose Whitlock dates: anchor is 1872-1901 (ch.3). Flag every later
     mention of him alive in 2005 or dying 2009 (ch.5 has both). Also now
     tangled with the ch.6/ch.7 Josiah-vs-Ambrose conflict above.
  2. Who Adelaide is: ch.4 = Wren's grandmother, a Finder, "For my
     granddaughter." Ch.3 = she "found" Ambrose's letter. Ch.5 = "Adelaide
     Whitlock," Ambrose's student and the Warden after him. Ch.9/10/12
     (skim) = author of an undated 1960s letter, "Warden of the first
     debt (role, not bloodline)," taught by Ambrose Whitlock, tried and
     failed to end the bargain like Whitlock did — this matches ch.5's
     "Ambrose's student, Warden after him," not ch.4's "grandmother, a
     Finder." Ch.12:7 has an ambiguous juxtaposition ("my grandmother
     taught me" right next to a line from Adelaide's letter) that could
     imply Adelaide = grandmother, or could just be two separate
     thoughts in the same line. UNRESOLVED — now tangled with the Elena
     conflict above, since both questions turn on who Wren's grandmother
     actually is. Count which version later chapters use.
  3. Elena Castellano: see NEW MAJOR CONFLICT above — superseded by the
     ch.6-12 finding, this line item is now the summary, not the flag.
  4. Warden succession: ch.3 = Whitlock -> Voss (1901-47) -> Weathers ->
     Caller -> vacant after 1987 -> Yusuf, current Warden. Ch.5 (typed
     record) says the role "is currently vacant" and puts Adelaide directly
     after Ambrose. Ch.6-12 skim: Yusuf referred to consistently as
     current/active (authorizes the box transfer, council chair, "backs
     your publication") — matches ch.3, not ch.5's "vacant." No fix
     needed, just confirms ch.3's line.
  5. Drake's status: ch.4 = active threat, thirty-day ultimatum. Ch.5 late
     scene = "in custody," charges filed, "not coming back." Ch.6-12
     skim: Drake is an active, ongoing threat throughout (threatening to
     publish his own partial record, "seen in Millbrook," the vetting/
     publication timeline is explicitly a race against him) — matches
     ch.4, not ch.5's "in custody." Grep for "in custody" and "vacant"
     across ch.6-12 returned zero hits. Confirms ch.4's version is the
     one later chapters build on; ch.5's "in custody" scene looks like
     the actual error in that chapter, not ch.4.
  6. Mara's gift: ch.3 says Sarah Voss (Mara's great-grandmother) was a
     Mender; ch.5 calls Mara "a Finder" while describing structural
     Mender-type work. Ch.6-9 skim: Mara referenced only by name at the
     orchard with Caleb, no gift-type stated in these chapters. Ch.10
     lists "The Menders" as a distinct lineage group from "The Wardens/
     Callers/Weathers/Finders" but doesn't tie Mara to one. Still open.
  7. Season/month: ch.5 is late summer (apples heavy, peaches early).
     Record for the season pass.
  8. NEW (ch.10 skim): "a gap in the 1942 renewal that doesn't match the
     ledger Dev found" — second numeric discrepancy, separate from the
     1887-91 folio gap, still unexplored (same item already logged from
     the earlier ch.10 pass, confirmed still open on this skim).
- Strict sequential manual read of all 45 chapters: IN PROGRESS. ch.1-7
  now have a real read (ch.3 amended and fixed; ch.5 read with OPEN canon
  conflicts, text unchanged; ch.6 read and edited, see ch.6/ch.7 conflict
  above; ch.7 read, text unchanged). **ch.8-12 still only SKIMMED**
  (mechanical grep sweep, not the real read) — ch.8 next for the real
  read. ch.13+ not yet started (real or skim).
- Season/month progression read-through: NOT DONE.
- Check against Books 1 to 3: NOT DONE.

## Chapters
- chapter_01: PROOFED (sequential manual read), 2026-09-21. No hard
  violations, no lexical/structural/rhythm tells found (no em dashes, no
  staged "not X, it's Y," no vague-emotion hedges, one single rule-of-three
  instance — not used as a default crutch). No fix needed. Continuity note:
  Theo Marsh stated as twenty-six here, with a five-year professional
  background (Millbrook State degree, 3yr county records, 2yr special
  collections) — internally consistent with a 1997 birth year if present-day
  aligns with the audit's 2023 reference point. This means chapter_15's
  "age 36" line is the one in error, not chapter 1 — carry this forward when
  the read reaches ch.15.
- chapter_02: PROOFED (sequential manual read), 2026-09-21. No hard
  violations, no em dashes, no staged constructions, no vague-emotion
  hedges. Near-verbatim repeated line ("Because I found the list... Because
  I'm a Finder...") appears twice — intentional callback (Theo re-asks,
  Wren repeats her own explanation), not accidental repetition; not a tell.
  "Toll"/"redirected" repeat heavily but are the chapter's actual subject
  matter (a documentary/legal investigation), not filler-word density. No
  fix needed. Continuity: confirms Harriet Marsh's lost decade as 1997-2007,
  matching the audit. Introduces Theo as Harriet's grandson.
- chapter_03: PROOFED (sequential manual read), 2026-09-21; AMENDED and FIXED
  later the same day. Original stamp: no hard violations, no em dashes, no
  staged constructions; repeated "Memory surrendered: X, Y, Z" folio format
  is an intentional in-world document convention, not a tell. Continuity
  info from this chapter: Warden succession Whitlock (1872-1901) -> Sarah
  Voss/Mara's family (1901-1947) -> Weathers line -> Caller line -> vacant
  after prior Warden died 1987 -> Yusuf (current). Elena Castellano (Wren's
  great-great-grandmother) was Finder 1870-1895.
  **AMENDMENT (re-read of live `main`, blob SHA `37879b06`): the original
  "no fix needed / internally consistent" was too generous. Found and
  fixed:**
  1. GAP YEARS were stated inconsistently (opening put the gap between the
     1892 and 1897 renewals; the 1887 volume was read as "last before the
     gap" while also listed as missing; Wren's note said 1887-1892; Priya
     said 1887-1891 and also 1892 missing). APPLIED: canonical gap 1887-1891,
     last present 1886, first back 1892. Edits: opening renewal years,
     volumes on the table (1892 set down, 1886 pulled closer and read),
     Wren's note and closing note, Priya's sign-off range (now 1892 through
     1897), Wren's "1887 to 1891," Priya's "1892: folio present," Wren's
     three-years-suspended recap, Priya's confirmation line, and removal of
     "He doesn't have 1892. He has 1893 forward" from Wren's line.
  2. RELATIONSHIP LABEL: "Her grandmother" for Elena Castellano (4 spots)
     -> "great-great-grandmother." APPLIED. **See ch.6-12 skim finding
     above (Whole book section) — this fix is now in question and should
     not be assumed final until the Elena conflict is resolved.**
  Verified via diff of commit `207db70`: 19 lines changed, all intended,
  plus a trailing newline added at end of file (harmless). No other text
  changed.
  3. Spaced-hyphen dashes (~8) left as is (see Whole book OPEN QUESTION).
- chapter_04: PROOFED (sequential manual read of live `main`, blob SHA
  `aca0a058`), 2026-09-21. NO CHAPTER TEXT CHANGED. Read in full by eye, not
  machine-scanned. Chapter contains earlier "Josiah" fixes (see SEEN note
  below), so edits were held to zero pending decisions. No true em dashes,
  no "particular", no "the specific ___". No factual/mechanical error found
  that required an in-file fix. Findings surfaced, not fixed, each a
  judgment call for Zia:
  1. Spaced-hyphen dash substitutes (~14). See OPEN QUESTION in Whole book.
  2. Repetition density: "nineteen years" ~11x, "thirty days" ~13x,
     "standing arrangement" ~9x. These are plot-anchor refrains, but at that
     count they exceed the charter's 8+ threshold. Left as is.
  3. Staged/tell constructions are noticeably denser here than ch.1-3:
     staccato fragment stacks ("Names. Dates. Amounts of memory taken.";
     "Complete. True. Every name."; "No name. No date. No authority
     cited."), pivot lines ("That's not protection. That's trust."; "The
     memory isn't suppressed. It's gone. Taken."), scene-ending theme
     restatement (the closing notebook line "We are the ones who find what
     was lost..." and "Two grandmothers. Two Finders. Two gaps."), and
     exposition delivered as dialogue between people who already know it
     (Theo reciting Harriet's history and the Priya/Dev roles to Wren). A
     line-edit pass would be voice work, not mechanical, so not done.
  Continuity CONFIRMED: Harriet's lost decade 1997-2007 matches ch.2; 2005
  Drake attempt falls inside it; Harriet 75, wedding 1971; Theo "fifteen
  years ... since you were eleven" gives age 26, matching ch.1, which
  further supports that ch.15's "age 36" is the error. "Castellano"
  spelling matches ch.3.
  Continuity checks, status:
  a. OPEN. Doris says Harriet still visits every few months asking for the
     gap, yet Theo describes her as in assisted living, unable to remember
     the decade. Plausible but unexplained. Author call; later Harriet
     scenes (ch.15) may explain it. (Ch.5 has Harriet gardening and reading
     mysteries, not in a facility, which adds to this.)
  b. OPEN. Cold-case review "every ten years, next review is next month":
     with a 2005 case and a present around 2024 this does not obviously
     land next month. Fold into the season/month pass.
  c. RESOLVED, no conflict. Ch.4's 1891 Eleanor Whitlock entry is in the
     county-held Whitlock folio ("Terms of the First Debt", Box 47), a
     different document from the valley Archive's annual renewal folios that
     ch.3 says are missing.
  d. ch.3 HALF RESOLVED, no conflict. Ch.3 says Ambrose held the role
     1872-1901 and that it "passed outside the bloodline" after he stepped
     down, which implies earlier Whitlock Wardens, so Josiah Whitlock as
     Warden in 1847 fits. STILL OPEN: the earlier "2 hits" on "Josiah" in
     ch.4 was never reconciled (live ch.4 has exactly one), and whether the
     queued Josiah fix is applied is unverified. Ch.5 has no "Josiah." ch.6
     real read: has 1 "Josiah" hit (manuscript signed "Josiah Whitlock...
     1847"), matching ch.9's "J. Whitlock, 1847" note — but see the new
     ch.6/ch.7 Josiah-vs-Ambrose conflict in Whole book section: ch.7 uses
     Ambrose for the same "hid the terms" story. Unresolved.
  e. OPEN. "Standing arrangement" is used two ways. Ch.3 (Priya): a
     notation in the county ledger every year the valley renews, with 1887-89
     marked "suspended" and 1890-91 "resumed." Ch.4 (Theo): a
     restricted-record seal on the 2005 Drake investigation. Ch.5 follows
     the ch.4 meaning (a pointer to the sealed 2005 box). Author call; watch
     later chapters.
- chapter_05: READ (sequential manual read of live `main`, blob SHA
  `7e3cf48d`), 2026-09-21. NOT CLEARED. NO CHAPTER TEXT CHANGED. Read in
  full by eye. Word count is far above any floor. This chapter carries the
  book's heaviest canon conflicts so far. Deliberate decision: do NOT
  rewrite it yet. Every fix here (who Adelaide is, who Elena is, who sealed
  the 2005 box, Drake's status) changes a fact that chapters 6-45 may
  already depend on, and a wrong pick would break them. Rule I am applying:
  earlier, already-anchored canon (ch.3-4, plus dates verified in the
  audit) wins on conflict, but the exact rewrite waits until the sequential
  read shows which version the later chapters use. Findings:
  HARD CONTINUITY CONFLICTS (author-level, need the read to finish):
  1. Ambrose Whitlock in modern times. Ch.5 says the 2005-sealed box holds
     his journal (last entry 2005), that "Whitlock was still alive" in
     2005, and that "He died in 2009." Ch.3 fixes him as Warden 1872-1901.
     Same error class as the ch.37 fix (Ambrose Whitlock -> Silas Harker),
     which suggests prior sessions already met this and resolved it there
     by renaming a modern figure.
  2. Adelaide. Ch.4 = Wren's grandmother, a Finder. Ch.5 = "Adelaide
     Whitlock," Ambrose's student, Warden after him, letter "decades ago,
     maybe fifty years." Also contradicts ch.3 (Voss line is the Warden
     after Ambrose, 1901-1947) and the ch.5 letter's claim that Ambrose
     taught her (a 1901-era Warden cannot teach a 1970s one). **Ch.6-12
     skim: matches ch.5, not ch.4 — see Whole book section, item 2.**
  3. Elena Castellano. Ch.3 = Wren's great-great-grandmother (Finder
     1870-95). Ch.5 = Wren's living mother, peeling peaches. **Ch.6-12
     skim, and ch.7's real read, strongly confirm ch.5's version (Elena =
     living mother) — see Whole book section, NEW MAJOR CONFLICT.**
  4. Warden role. Ch.5's typed record says it "is currently vacant";
     ch.3 says Yusuf is the current Warden. **Ch.6-12 skim confirms ch.3
     — Yusuf is active/current throughout. Ch.5's "vacant" line looks
     like this chapter's own error.**
  5. Drake. Late in ch.5 Wren says he is "in custody," facing charges, "not
     coming back," yet the same chapter has his attorney filing an
     emergency motion that morning, and ch.4 has him issuing a live
     ultimatum. Later deadlines (ch.31/37/38 injunction) need him active.
     **Ch.6-12 skim confirms ch.4/ch.31/37/38 — Drake active throughout,
     zero "in custody" hits. Ch.5's "in custody" scene looks like this
     chapter's own error, not ch.4.**
  6. Timeline inside ch.5: opens Tuesday, court date Friday is called "four
     days" (Tue to Fri is three); on the Thursday at the courthouse it is
     still "four days"; at midnight it is "Four days" then "Three now."
     Elena also says "Diaz is logging the inventory tomorrow" after Diaz
     has already logged it on the spot.
  7. Mara is called "a Finder" while doing Mender-type structural work
     (ch.3: Voss line = Menders). Ch.6-12 skim: no gift-type for Mara found
     in these chapters. Still open.
  8. Ch.5 says Wren has made the Millbrook trip "six times now"; ch.4
     reads as her first visit to the county records.
  MECHANICAL/LINE-LEVEL (not fixed, held with the rest):
  9. Skipped-fix string: live ch.5 has "She was the Warden after him. She
     tried to end the bargain." twice (Theo's line and Wren's line to
     Elena). The logged fix string says "before him," so it no longer
     matches; unclear whether a fix already changed "before" to "after."
     Confirm against `scripts/book4_fixes.json` at fix time.
  10. Markdown glitches: "*To the one who finds this - *" and "* - A.W.*"
      (stray space inside the italics).
  11. Wording: Harriet "doesn't remember the son she raised for ten years"
      (she raised him 1972-1990, not in the lost decade); Wren tells Theo
      "nineteen years caring for a woman," vs. his fifteen years since age
      eleven in ch.4. Muddled sentence: the kiss "interrupted by a phone
      call from Yusuf - Drake's attorney, the motion to compel."
  STYLE (Zia's call, not fixed): spaced-hyphen dashes throughout; staccato
  fragment lists and pivot lines ("Publish with care. That's the choice.
  Not publish or don't."); speeches that explain their own subtext (Elena
  on the bargain as a margin); theme-restating scene endings; heavy
  repetition of "truth," "publish," "four days," "Drake."
  Confirmed fine: Harriet 56 in 2005 and her son 33 (wedding 1971 fits);
  ring ritual "a year ago" (2023) with a 2024 present; "nineteen years"
  since 2005.
- chapter_06: READ (sequential manual read of live `main`, blob SHA
  `de90408b`), 2026-09-22. TEXT CHANGED, commit `f9495fc`. Found and fixed:
  the archive manuscript in this chapter is explicitly signed "Josiah
  Whitlock... 1847" (established at the top of the chapter), but 140
  lines later the same document's "hid the terms" warning was attributed
  to "Ambrose Whitlock" — a same-chapter, same-document name slip.
  Changed "Ambrose Whitlock" -> "Josiah Whitlock" at that line. **THIS FIX
  IS NOW IN QUESTION — see the ch.6/ch.7 Josiah-vs-Ambrose conflict in the
  Whole book section.** Ch.7, read immediately after, uses Ambrose 4x for
  this exact story. Do not touch this line again until ch.8-9 are read.
  Other findings: 0 em dashes, ~3 spaced hyphens (confirms skim). A
  call-and-echo dialogue tic (line repeated verbatim as the next line —
  "Until now."/"Until now.", "Or accepts."/"Or accepts.", "Because the
  Whitlocks buried it." x2, "He doesn't have the Warden clause." x2,
  "Which means he cannot control it." x2, "Yusuf knows." x2, "Walt Pruitt
  will have opinions." x2, "And for the dead." x2) appears 9 times in one
  chapter — reads as intentional rhythm individually, but the density is
  a real structural tell per the charter. Not fixed — voice/line-edit
  call, flagged for Zia. Also: line 47 stacks four "He has X." fragments
  in a row (renewals/names/dates/amounts) — same staccato-list pattern
  noted in ch.4. "A hundred and seventy years" since 1847 (line 151):
  should be closer to 177 given the audit's ~2024 present-day anchor;
  minor, likely just rounded phrasing, not flagged as an error. Continuity
  confirmed: unnamed grandmother (dead, was a Finder) distinct from "my
  mother" — consistent with the mother-reading of the Elena conflict, not
  ch.11's.
- chapter_07: READ (sequential manual read of live `main`), 2026-09-22.
  NO CHAPTER TEXT CHANGED. 0 em dashes, ~9 spaced hyphens. Central chapter
  for the Elena conflict — see Whole book NEW MAJOR CONFLICT above; Elena
  Castellano named and present as Wren's living mother throughout (baker,
  53, called "Mama" twice), clearly distinguished from "your grandmother"
  (dead, never named Elena here, died when Wren was fourteen). Also
  central to the new ch.6/ch.7 conflict: uses "Ambrose Whitlock" 4x (lines
  15, 17, 89, 117) for the "tried to end the bargain, hid the terms"
  story, and explicitly distinguishes him from "Ambrose Kell" (a different,
  already-faced antagonist) in the same breath — reads like a deliberate
  choice to keep the name Ambrose, making ch.6's Josiah signature the more
  likely odd one out, though not confirmed yet (see Whole book conflict).
  No other hard violations. Staged/tell density here is moderate: a few
  pivot lines ("It's not about won't. It's about -"), one theme-restating
  closing ("The split loyalty didn't resolve... She drove through it
  anyway.") — not flagged as excessive, in line with the book's established
  house style rather than unusual for this chapter specifically. Continuity
  notes: confirms Theo's grandmother is Harriet Marsh, lost decade before
  2007, matching ch.1/2/4/6. Confirms Wren is twenty-one (matches ch.7's
  own dialogue, "You're twenty-one years old," said twice, once by Elena
  once by narration) — consistent with prior chapters.
- chapter_08: SKIMMED (grep sweep only), 2026-09-22. 0 em dashes, ~3 spaced
  hyphens. "said" dialogue tag count high (41) — worth a variety check on
  the real read. Continues the ch.6-7 grandmother/mother split; "my
  grandmother never told me the full terms... she died before the time
  came." Real sequential read still owed — next up.
- chapter_09: SKIMMED (grep sweep only), 2026-09-22. 0 em dashes, 0 spaced
  hyphens (only ch.6-12 chapter with none). Contains "J. Whitlock, 1847"
  and a second Whitlock signature "J. Whitlock, 1863" — two dated
  signatures from the same initials, not yet checked against whether
  that's one long-lived Whitlock or two different Whitlocks with the same
  initial. This is now directly relevant to the ch.6/ch.7 Josiah-vs-
  Ambrose conflict (see Whole book section) and should be the next
  priority after ch.8's real read. Adelaide material here (taught by
  Ambrose, the role, not bloodline) matches ch.5, not ch.4 — see Whole
  book item 2. Real sequential read still owed.
- chapter_10: SKIMMED (grep sweep only), 2026-09-22. 0 em dashes, ~6
  spaced hyphens. Confirms the 1942-renewal-gap open item (Whole book
  item 8). Lists lineage types (Wardens/Menders/Callers/Weathers/Finders)
  without tying Mara to one. Real sequential read still owed.
- chapter_11: SKIMMED (grep sweep only), 2026-09-22. 0 em dashes, ~11
  spaced hyphens, 1 "the specific" hit (only one across ch.6-12).
  Contains the "Elena Castellano... my grandmother" passage that
  originally drove the ch.3 fix — see Whole book NEW MAJOR CONFLICT. "said"
  count 31. Real sequential read still owed, and is now the priority
  chapter for the Elena question once the real read resumes.
- chapter_12: SKIMMED (grep sweep only), 2026-09-22. 0 em dashes, ~22
  spaced hyphens (highest of any chapter skimmed so far). "said" count 26.
  Confirms Yusuf as active council chair as of 1998 (grandmother brought
  him the 1893 ledger then). Ambiguous "my grandmother taught me" line
  sitting next to an Adelaide's-letter quote — see Whole book item 2.
  Real sequential read still owed.
- chapter_15: APPLIED, verified via diff of commit `f8551915` — "your father"
  (was "your mother"), 2003 heart-failure rewrite (was "died six months
  later. Heart attack."), "two hours" (was "two hundred miles"). All three
  former QUEUED items now confirmed live. Still spotted, not fixed: Theo age
  36 vs born 1997 (see chapter_01 note above — confirmed a real error, ch.15
  needs the fix, not ch.1).
- chapter_37: APPLIED, verified via diff of commit `f8551915` — Weather/Silas
  Harker rewrite landed: "Warden" → "Weather" (role name, 2x), "Ambrose
  Whitlock" → "Silas Harker" (name, throughout), added "Not Old Man Harker,
  who was alive and difficult" distinction line. All 6 tell-phrase edits
  confirmed live.
- All other chapters: NOT PROOFED (mechanical pass only).
