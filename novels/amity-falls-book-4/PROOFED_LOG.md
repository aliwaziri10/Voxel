# Book 4 proofed log

Only what was read from live `main` is stamped. Update this file every time a
chapter is verified. Never stamp from memory or from a handoff claim.

Legend: APPLIED = fix read back from the live chapter. QUEUED = in
`scripts/book4_fixes.json`, not yet in the chapter. SEEN = seen in an earlier
grep, not re-read. NOT PROOFED = no continuity check done.

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
  and sweep the whole book, or accept it as house form. Check ch.1-2 and
  later chapters as the read continues.
- DECIDED AND APPLIED (2026-09-21): canonical missing-folio gap is
  1887-1891 (five years). Last volume present before the gap: 1886. First
  volume back: 1892. Basis: Priya's explicit statement in ch.3, the
  figure the log/audit already carried, 3 suspended years (1887-89) plus 2
  resumed (1890-91) making exactly 5, and Ambrose's 1889 attempt landing
  inside it. Applied to ch.3 in commit `207db70` (see ch.3 entry). Every
  later chapter that cites the gap years must be checked against this as
  the read reaches it.
- CARRY-FORWARD CHECKS for the rest of the read (raised by ch.3-5):
  1. Ambrose Whitlock dates: anchor is 1872-1901 (ch.3). Flag every later
     mention of him alive in 2005 or dying 2009 (ch.5 has both).
  2. Who Adelaide is: ch.4 = Wren's grandmother, a Finder, "For my
     granddaughter." Ch.3 = she "found" Ambrose's letter. Ch.5 = "Adelaide
     Whitlock," Ambrose's student and the Warden after him. Count which
     version later chapters use.
  3. Elena Castellano: ch.3 = Wren's great-great-grandmother, Finder
     1870-1895. Ch.5 = Wren's living mother, at the farmhouse. Same name,
     two people. Count what later chapters call Wren's mother.
  4. Warden succession: ch.3 = Whitlock -> Voss (1901-47) -> Weathers ->
     Caller -> vacant after 1987 -> Yusuf, current Warden. Ch.5 (typed
     record) says the role "is currently vacant" and puts Adelaide directly
     after Ambrose.
  5. Drake's status: ch.4 = active threat, thirty-day ultimatum. Ch.5 late
     scene = "in custody," charges filed, "not coming back." Later chapters
     (ch.18 onward, ch.31/37/38 injunction) need Drake active. Check.
  6. Mara's gift: ch.3 says Sarah Voss (Mara's great-grandmother) was a
     Mender; ch.5 calls Mara "a Finder" while describing structural
     Mender-type work. Check how later chapters label Mara.
  7. Season/month: ch.5 is late summer (apples heavy, peaches early).
     Record for the season pass.
- Strict sequential manual read of all 45 chapters: IN PROGRESS. ch.1-5 read
  (ch.3 amended and fixed; ch.5 read with OPEN canon conflicts, text
  unchanged), ch.6 next.
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
     -> "great-great-grandmother." APPLIED.
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
     queued Josiah fix is applied is unverified. Ch.5 has no "Josiah."
     Reconcile the rest at ch.6 and ch.9 ("J. Whitlock, 1847").
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
     taught her (a 1901-era Warden cannot teach a 1970s one).
  3. Elena Castellano. Ch.3 = Wren's great-great-grandmother (Finder
     1870-95). Ch.5 = Wren's living mother, peeling peaches.
  4. Warden role. Ch.5's typed record says it "is currently vacant";
     ch.3 says Yusuf is the current Warden.
  5. Drake. Late in ch.5 Wren says he is "in custody," facing charges, "not
     coming back," yet the same chapter has his attorney filing an
     emergency motion that morning, and ch.4 has him issuing a live
     ultimatum. Later deadlines (ch.31/37/38 injunction) need him active.
  6. Timeline inside ch.5: opens Tuesday, court date Friday is called "four
     days" (Tue to Fri is three); on the Thursday at the courthouse it is
     still "four days"; at midnight it is "Four days" then "Three now."
     Elena also says "Diaz is logging the inventory tomorrow" after Diaz
     has already logged it on the spot.
  7. Mara is called "a Finder" while doing Mender-type structural work
     (ch.3: Voss line = Menders).
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
- chapter_06: SEEN "Josiah" fix.
- chapter_09: SEEN "J. Whitlock, 1847".
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
