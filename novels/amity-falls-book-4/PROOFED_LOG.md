# Book 4 proofed log

Only what was read from live `main` is stamped. Update this file every time a
chapter is verified. Never stamp from memory or from a handoff claim.

Legend: APPLIED = fix read back from the live chapter. QUEUED = in
`scripts/book4_fixes.json`, not yet in the chapter. SEEN = seen in an earlier
grep, not re-read. SKIMMED = mechanical/grep sweep only, not the full
sequential manual read. NOT PROOFED = no continuity check done.

🔒 ch.13-16 claimed by Claude (chat session), 2026-09-21 20:58 UTC. Chapters
1-12 are DONE (real read, stamped below). Do not redo them. Remove this claim
when ch.13-16 are stamped.

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
  **RE-OPENED 2026-09-21 20:58 UTC by the ch.8-12 real read:** ch.9 already
  has the Millbrook printer confirmed ("first run, five hundred copies...
  final files by Friday") and ch.10, the next chapter, restarts publication
  planning from zero (eight-week timeline, council in three days to approve
  press funding); ch.37 repeats the "printer needs final files by Friday"
  line. The "closed" verdict above did not test this. Season/countdown pass
  must re-check it.
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
  and sweep the whole book, or accept it as house form. Real-read counts
  so far: ch.6 (~3), ch.7 (~9), ch.8 (3), ch.9 (0), ch.10 (6), ch.11 (11),
  ch.12 (22). Rising, not falling. Still unresolved.
- DECIDED AND APPLIED (2026-09-21): canonical missing-folio gap is
  1887-1891 (five years). Last volume present before the gap: 1886. First
  volume back: 1892. Basis: Priya's explicit statement in ch.3, the
  figure the log/audit already carried, 3 suspended years (1887-89) plus 2
  resumed (1890-91) making exactly 5, and Ambrose's 1889 attempt landing
  inside it. Applied to ch.3 in commit `207db70` (see ch.3 entry). Every
  later chapter that cites the gap years must be checked against this as
  the read reaches it.
- ⚠️ MAJOR CONFLICT, Elena Castellano (raised by the ch.6-12 skim, 2026-09-22,
  now CONFIRMED by the real reads of ch.7 and ch.11): **the ch.3 fix (Elena
  Castellano -> Clara Castellano for the 1870s ancestor, keeping "Elena" as
  the grandmother) was made on ch.11's evidence alone** ("Elena Castellano...
  my grandmother," a dead Finder who did a 1985 search and stopped singing
  afterward). Ch.5 and ch.7 (real reads) use a different split:
    - "Elena Castellano" = Wren's living MOTHER. Introduced by name in
      ch.7 (baker, fifty-three, kneading dough), called "Mama" by Wren
      (ch.7 twice), present-tense and alive throughout ch.5-9, arguing
      with Wren about publication.
    - "your/my grandmother" (never named "Elena" in these chapters) =
      already DEAD, was a Finder, died when Wren was fourteen (ch.7, ch.9),
      found the 1893 ledger and brought it to the council in 1998 (ch.12),
      never told Wren the full terms (ch.8, ch.9).
  Ch.11 (real read, 2026-09-21 20:55 UTC) has Dev say "Elena Castellano. She
  found the girl [1985]... Elena never sang that lullaby again" and Wren
  answer "My grandmother." So ch.11 is the outlier (1 chapter) against
  ch.5/6/7/8/9/12. **NOT reversing the ch.3 fix and NOT touching ch.11's
  Elena line** — the lullaby scene is real and specific and has to be
  reconciled, not just outvoted. Possibilities, undecided: (a) ch.11's
  "Elena" should be renamed to a different name for the grandmother (the
  grandmother is never named anywhere else); (b) two Castellano women a
  generation apart; (c) something else. FLAGGING FOR ZIA, not deciding.
- ✅ RESOLVED, ch.9 real read (2026-09-21): the Josiah-vs-Ambrose conflict
  (ch.6 vs ch.7) is CLOSED. Ch.9's own primary-source documents settle it:
  the marginal note (signed "J. Whitlock, 1847") and the complete hidden
  letter (signed "J. Whitlock, 1863," found later in the SAME chapter) are
  both the "tried to end the bargain, could not, hid the terms" document,
  and both predate Ambrose's own established Warden tenure of 1872-1901
  (ch.3). The third signature, "A.W." (newer, darker ink, a pointer arrow
  to the letter's location), is a later annotation, Ambrose Whitlock.
  APPLIED and read back live: ch.9's opening paragraph keeps Ambrose as
  Adelaide's teacher and attributes the failed-bargain/hidden-letter story
  to Josiah, "a Warden generations before him" (commit `0041d89`); ch.7's
  four "Ambrose Whitlock" mentions for this story are now "Josiah Whitlock"
  (commit `b98711c`, "Ambrose Kell" untouched); ch.6's earlier fix stands.
  Follow-on found at ch.12 and FIXED (commit `0553dba`): ch.12's metadata for
  the hidden letter still said "Author: Ambrose Whitlock"; now "Josiah
  Whitlock ... (signed J. Whitlock, 1863)". Ch.37's Ambrose -> Silas Harker
  rewrite is unrelated. Later chapters still need checking as the read
  reaches them (any "Ambrose Whitlock" tried/failed/hid-the-terms mention).
- ⚠️ OPEN CANON QUESTIONS FOR ZIA, raised by the ch.8-12 real reads
  (2026-09-21 20:58 UTC). None touched. Each needs a decision before the text
  is changed:
  1. WHO IS "WARDEN OF THE FIRST DEBT" NOW? Ch.3 says Yusuf is the current
     Warden (since Denise was freed). Ch.9 has Wren conclude "I'm the Warden
     of the first debt... since I took charge of the documentation project.
     Maybe since I was born." Ch.11 has Yusuf as the WEATHERS
     representative and Mara Voss as the WARDENS representative. Ch.10 has
     "the Warden elder" as a separate person. Also "Wardens" is both a
     lineage (ch.10/11) and the office of the first debt (ch.3/9). Later
     chapters that say "Warden" (ch.31, ch.37) must be checked against
     whichever is chosen.
  2. DREW'S 2005 MILLBROOK ATTEMPT, WHO WAS COERCED? Ch.5 typed record:
     "coercing a Whitlock descendant to take Harriet Marsh's memory." Ch.11:
     Drake coerced a FINDER, Silas Kettering (served two years, out in '09),
     with Harriet as the "source memory." Pick one.
  3. LINEAGE ROSTER. Ch.11 has SIX lineages (Wardens, Menders, Callers,
     Weathers, Finders, Wicks) with Mara/Aris Thorne/Priya/Yusuf/Dev/Odette
     as reps; ch.37 says "six lineages"; ch.10 says "five of seven." Dev is
     the Finders rep in ch.11 and is listed among Finders in ch.10, but ch.8
     says Dev "maintained" the Caller field at the ring. Mara is a "Finder"
     in ch.5 and the Wardens rep in ch.11 (ch.3: Voss line = Menders).
  4. NOTEBOOK/CALENDAR FRAME (ch.8 vs ch.11). Ch.8 has Wren read Nov 3-12
     notebook entries (Drake's letter, council vote to publish) as events of
     "a year ago" while the same beats are the book's present (ch.4, ch.18).
     Ch.11 (three days after Nov 3, "cold bright morning") puts the present
     at about Nov 6; ch.8 reads entries through Nov 12 as past. Ch.9 says
     "July." Ch.10 (bare apple trees, "winter geometry") and ch.12
     (November, bare branches, "recorded last spring") are winter. Ch.9 is
     the odd one out. Belongs in the season pass; needs one calendar.
  5. WREN'S MOTHER'S JOB. Baker (ch.7, ch.5 peaches), "gone to the clinic"
     (ch.8), "at the store by nine, Odette's back room" (ch.10).
  6. HARRIET'S LIVING SITUATION. Assisted living (ch.4), gardening and
     mysteries (ch.5), "tends her roses" at home (ch.8), "Millbrook nursing
     home" (ch.9), "care facility in Millbrook" (ch.12). Plausible as one
     facility with a garden; never stated.
  7. THE KISS AND THE RUPTURE ARE EARLY. Ch.5 and ch.9 both refer to the kiss
     interrupted by Yusuf's call ("three weeks ago" in ch.9) and ch.9 says
     "The rupture. It was here." The beat map puts the first kiss at ch.21
     and the rupture at ch.30.
  8. ARCHIVE BUILDING. Ch.9: tall windows, oak table, locked cabinet, spring
     under the floor. Ch.12: "a converted cold-storage shed Mara and Caleb
     had insulated." Ch.3-4 also need a look. One description needed.
  9. TWO SILASES: Silas Kettering (ch.11) and Silas Harker (ch.37 rewrite).
  10. THEO'S "NINETEEN YEARS" vs "FIFTEEN YEARS" of searching: fifteen in
      ch.4 and ch.11; nineteen in ch.10 and ch.12.
- CARRY-FORWARD CHECKS for the rest of the read (raised by ch.3-5):
  1. Ambrose Whitlock dates: anchor is 1872-1901 (ch.3). Flag every later
     mention of him alive in 2005 or dying 2009 (ch.5 has both). The
     Josiah/Ambrose split is resolved through ch.12 (see above).
  2. Who Adelaide is: ch.4 = Wren's grandmother, a Finder, "For my
     granddaughter." Ch.3 = she "found" Ambrose's letter. Ch.5 = "Adelaide
     Whitlock," Ambrose's student and the Warden after him. Ch.9 and ch.12
     (real reads) = author of an undated 1960s letter, "Adelaide, Warden of
     the first debt (role, not bloodline)," taught by Ambrose Whitlock,
     tried and failed to end the bargain like the Whitlocks did. Ch.12's
     "my grandmother taught me" line is about the Mender's toll story and
     is separate from the Adelaide's-letter line (the grandmother is a
     Finder, Adelaide is a Warden). So Adelaide is NOT the grandmother in
     ch.5-12; ch.4's "grandmother, a Finder, 'For my granddaughter'" is the
     outlier. Still to decide and fix at ch.4 (text unchanged).
  3. Elena Castellano: see MAJOR CONFLICT above.
  4. Warden succession: ch.3 = Whitlock -> Voss (1901-47) -> Weathers ->
     Caller -> vacant after 1987 -> Yusuf, current Warden. Ch.5 (typed
     record) says the role "is currently vacant" and puts Adelaide directly
     after Ambrose. Ch.6-12: Yusuf referred to consistently as active
     (authorizes the box transfer, council chair, sealed the 1893 ledger in
     1998). But see OPEN QUESTION 1 above (ch.9 makes Wren the Warden).
  5. Drake's status: ch.4 = active threat, thirty-day ultimatum. Ch.5 late
     scene = "in custody," charges filed, "not coming back." Ch.6-12: Drake
     is an active, ongoing threat throughout. Ch.5's "in custody" scene
     looks like the actual error in that chapter, not ch.4.
  6. Mara's gift: ch.3 says Sarah Voss (Mara's great-grandmother) was a
     Mender; ch.5 calls Mara "a Finder"; ch.11 makes her the Wardens
     representative. Still open (OPEN QUESTION 3).
  7. Season/month: ch.5 is late summer (apples heavy, peaches early); ch.9
     is July; ch.10 and ch.12 are winter/November. See OPEN QUESTION 4.
  8. "A gap in the 1942 renewal that doesn't match the ledger Dev found"
     (ch.10) is a second numeric discrepancy, separate from the 1887-91 folio
     gap, still unexplored. (Ch.11's 1942 "lost Watkins boy" search is a
     different item.)
- ANACHRONISM PATTERN (ch.8 and ch.12, both FIXED): early chapters speak of
  the Drake trial, the court testimony, Drake's "leverage collapsing," and
  Dev "proving the gap was deliberate" as already past. Those are ch.36-45
  events. Watch for more in ch.13-35, especially Dev/Priya lines.
- Strict sequential manual read of all 45 chapters: IN PROGRESS. **ch.1-12
  now have a real read and are stamped below.** ch.13 is next (claimed at
  the top of this file). ch.15 and ch.37 have applied fixes but no real read.
- Season/month progression read-through: NOT DONE (data collected above).
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
     -> "great-great-grandmother." APPLIED. **See the Elena MAJOR CONFLICT
     in Whole book — this fix is in question and should not be assumed
     final until that is resolved.**
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
     mysteries, not in a facility, which adds to this.) See OPEN QUESTION 6.
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
     Warden in 1847 fits. Josiah is now used consistently in ch.4, 6, 7, 9
     and 12 (see the RESOLVED note in Whole book).
  e. OPEN. "Standing arrangement" is used two ways. Ch.3 (Priya): a
     notation in the county ledger every year the valley renews, with 1887-89
     marked "suspended" and 1890-91 "resumed." Ch.4 (Theo): a
     restricted-record seal on the 2005 Drake investigation. Ch.5 follows
     the ch.4 meaning (a pointer to the sealed 2005 box). Ch.11 and ch.12
     follow the ch.4 meaning too ("the standing arrangement notation" in the
     Millbrook index). Author call.
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
     taught her (a 1901-era Warden cannot teach a 1970s one). **Ch.9 and
     ch.12 real reads match ch.5, not ch.4 — see Whole book, CARRY-FORWARD
     item 2.**
  3. Elena Castellano. Ch.3 = Wren's great-great-grandmother (Finder
     1870-95). Ch.5 = Wren's living mother, peeling peaches. **Ch.7's real
     read confirms ch.5 (Elena = living mother); ch.11 is the outlier — see
     the Elena MAJOR CONFLICT in Whole book.**
  4. Warden role. Ch.5's typed record says it "is currently vacant";
     ch.3 says Yusuf is the current Warden. **Ch.6-12 confirm Yusuf is
     active/current (but see OPEN QUESTION 1). Ch.5's "vacant" line looks
     like this chapter's own error.**
  5. Drake. Late in ch.5 Wren says he is "in custody," facing charges, "not
     coming back," yet the same chapter has his attorney filing an
     emergency motion that morning, and ch.4 has him issuing a live
     ultimatum. Later deadlines (ch.31/37/38 injunction) need him active.
     **Ch.6-12 confirm Drake active throughout. Ch.5's "in custody" scene
     looks like this chapter's own error, not ch.4.**
  6. Timeline inside ch.5: opens Tuesday, court date Friday is called "four
     days" (Tue to Fri is three); on the Thursday at the courthouse it is
     still "four days"; at midnight it is "Four days" then "Three now."
     Elena also says "Diaz is logging the inventory tomorrow" after Diaz
     has already logged it on the spot.
  7. Mara is called "a Finder" while doing Mender-type structural work
     (ch.3: Voss line = Menders). See OPEN QUESTION 3.
  8. Ch.5 says Wren has made the Millbrook trip "six times now"; ch.4
     reads as her first visit to the county records.
  9. NEW (ch.11 real read): ch.5's typed record says Drake coerced "a
     Whitlock descendant"; ch.11 says he coerced the Finder Silas Kettering.
     See OPEN QUESTION 2.
  MECHANICAL/LINE-LEVEL (not fixed, held with the rest):
  10. Skipped-fix string: live ch.5 has "She was the Warden after him. She
      tried to end the bargain." twice (Theo's line and Wren's line to
      Elena). The logged fix string says "before him," so it no longer
      matches; unclear whether a fix already changed "before" to "after."
      Confirm against `scripts/book4_fixes.json` at fix time.
  11. Markdown glitches: "*To the one who finds this - *" and "* - A.W.*"
      (stray space inside the italics).
  12. Wording: Harriet "doesn't remember the son she raised for ten years"
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
  `de90408b`), 2026-09-21. TEXT CHANGED, commit `f9495fc`. Found and fixed:
  the archive manuscript in this chapter is explicitly signed "Josiah
  Whitlock... 1847" (established at the top of the chapter), but 140
  lines later the same document's "hid the terms" warning was attributed
  to "Ambrose Whitlock" — a same-chapter, same-document name slip.
  Changed "Ambrose Whitlock" -> "Josiah Whitlock" at that line. **CONFIRMED
  CORRECT by the ch.9 real read (see the RESOLVED note in Whole book).**
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
- chapter_07: READ (sequential manual read of live `main`), 2026-09-21.
  TEXT CHANGED later the same day by commit `b98711c` (4x "Ambrose
  Whitlock" -> "Josiah Whitlock" for the tried-to-end/hid-the-terms story;
  read back live: lines 15, 17, 89, 117 now Josiah, "Ambrose Kell" on line 17
  untouched). 0 em dashes, ~9 spaced hyphens. Central chapter for the Elena
  conflict — see Whole book MAJOR CONFLICT; Elena Castellano named and
  present as Wren's living mother throughout (baker, 53, called "Mama"
  twice), clearly distinguished from "your grandmother" (dead, never named
  Elena here, died when Wren was fourteen). No other hard violations.
  Staged/tell density here is moderate: a few pivot lines ("It's not about
  won't. It's about -"), one theme-restating closing ("The split loyalty
  didn't resolve... She drove through it anyway.") — in line with the
  book's established house style. Continuity notes: confirms Theo's
  grandmother is Harriet Marsh, lost decade before 2007, matching
  ch.1/2/4/6. Confirms Wren is twenty-one ("You're twenty-one years old,"
  said twice) — consistent with prior chapters.
- chapter_08: READ (sequential manual read of live `main`), 2026-09-21
  20:50 UTC. TEXT CHANGED, commit `46bd7e8` (read back: pushed file equals
  the intended edit plus a trailing newline). Three anachronisms removed,
  no other text changed: (1) "the day Dev had shown them the gap in Drake's
  account. The day the leverage had collapsed." -> "the day Dev had first
  pulled the substation logs. The day the numbers started to make sense.";
  (2) "the only reason the substation evidence held up in court. Dev found the
  gap. Priya made sure the testimony stuck." -> "the reason the substation
  logs are usable at all. Dev found the pattern. Priya made sure the chain
  of custody held."; (3) "The county hired him on contract after the trial.
  ... the Drake case is being adapted for three other cold cases." -> "The
  county asked him to consult on contract. ... the logs is being adapted for
  three cold cases." The trial, the court testimony and the collapse of
  Drake's leverage are ch.36-45 events. NOT FIXED, logged: the notebook
  frame and calendar (OPEN QUESTION 4); Wren's mother "had gone to the
  clinic" (OPEN QUESTION 5); "Drake's letter... by the solstice" (deadline
  wording, season/countdown pass). 0 em dashes, 3 spaced hyphens. Style:
  staccato lists ("The pauses. The corrections."), "Keys. Jacket. Door.",
  "It was not her calm. It was borrowed.", theme-restating close ("The
  shield grew."), heavy "said" tags. Continuity CONFIRMED: Denise's husband
  "dead forty-three years" fits 1981; "nineteen years since Drake's first
  attempt" fits 2005; Theo "six months" matches ch.9; Priya's session math
  (six sessions, three hours recovery) is right.
- chapter_09: READ (sequential manual read of live `main`), 2026-09-21
  20:52 UTC. NO NEW TEXT CHANGE by this read. The opening-paragraph
  Josiah/Ambrose fix (commit `0041d89`) was read back and is live. 0 em
  dashes, 0 spaced hyphens. Date arithmetic verified: ledger 1823 -> "J.
  Whitlock, 1847" is 24 years; 1847 -> 1863 is 16 years. NOT FIXED, logged:
  MAJOR canon conflict, Wren declares herself "the Warden of the first debt"
  by custody while ch.3 says Yusuf is Warden (OPEN QUESTION 1); setting is
  July ("cool even in July") against winter in ch.10 and November in ch.12
  (OPEN QUESTION 4); the kiss "three weeks ago" and "The rupture. It was
  here." are much earlier than the beat map (OPEN QUESTION 7); Harriet in a
  "Millbrook nursing home" (OPEN QUESTION 6); printer already confirmed and
  "final files by Friday" (re-opens the countdown item); Yusuf reports
  Drake's lawyer wants a meeting and "has a proposal" (check the follow-up
  in ch.13+). Style: theme-restating lines ("The truth was a heavy thing to
  carry. But she wasn't carrying it alone."), "Not X but Y" pivots, "cost"
  repeated heavily.
- chapter_10: READ (sequential manual read of live `main`), 2026-09-21
  20:53 UTC. NO CHAPTER TEXT CHANGED. 0 em dashes, 6 spaced hyphens.
  NOT FIXED, logged: winter setting (bare apple trees) against ch.9's July
  (OPEN QUESTION 4); publication planning restarts from zero (eight-week
  timeline, council in three days for press funding) although ch.9 already
  confirmed the printer (Whole book countdown note); "five of seven" lineage
  leads against six lineages elsewhere, and "the Warden elder" as a separate
  person (OPEN QUESTIONS 1, 3); Dev listed among Finders although ch.8 has
  him maintain the Caller field (OPEN QUESTION 3); Wren's mother "at the
  store by nine, Odette's back room" (OPEN QUESTION 5); Theo's "nineteen
  years" vs fifteen (OPEN QUESTION 10); the 1942 renewal gap (Whole book
  CARRY-FORWARD 8). Style: dense pivot/staged lines ("It doesn't change the
  timeline. It *is* the timeline."; "That's not a strategy. That's a
  surrender." / "It's a boundary."), theme-restating close, "timeline"
  repeated heavily.
- chapter_11: READ (sequential manual read of live `main`), 2026-09-21
  20:54 UTC. TEXT CHANGED, commit `8d63946` (read back: pushed file equals
  the intended edit plus a trailing newline): "Odette Reynolds" -> "Odette
  Reyes" in 4 places (Reyes appears 16 other times in the book, plus Caleb
  Reyes and Reyes Orchard). NOT FIXED, logged: the Elena outlier (Whole book
  MAJOR CONFLICT: Dev names "Elena Castellano" as Wren's grandmother, Wren
  agrees); Drake coerced Finder Silas Kettering vs ch.5's "Whitlock
  descendant" (OPEN QUESTION 2); lineage roster (OPEN QUESTION 3); Wren's
  "first search... the first one" against "She had paid small debts before"
  in the same chapter; present-day date about Nov 6 ("fading since November
  3," noticed "three days ago") against ch.8 reading Nov 4-12 entries as past
  (OPEN QUESTION 4); "Silas" used twice (OPEN QUESTION 9). 0 em dashes, 11
  spaced hyphens. "the specific" on "The bargain takes the specific, not the
  general" is a legitimate noun use and was left. Style: staccato lists,
  "Not unity. Not forgiveness. Something simpler:", theme-restating close.
  Continuity CONFIRMED: Harriet "Born 1949. Lost 1997-2007" (fix landed),
  "born in 1997", Harriet 2005 attempt "nineteen years ago" fits.
- chapter_12: READ (sequential manual read of live `main`), 2026-09-21
  20:56 UTC. TEXT CHANGED, commit `0553dba` (read back: pushed file equals
  the intended edit plus a trailing newline; 5 changed lines): (1) last line
  "Now it. The scanner whirred again" was a truncated sentence -> "Now it
  did."; (2) Theo's "the one Mara found in the false bottom of the archive
  cabinet" contradicted Wren's "my grandmother... was the Finder who located
  it in the false bottom... 1998" -> "the one recovered from the false
  bottom"; (3) metadata "Author: Ambrose Whitlock" for the hidden letter ->
  "Josiah Whitlock, former Warden of the first debt (signed J. Whitlock,
  1863)" to match ch.9; (4) and (5) two anachronisms: "Dev's evidence work
  collapsed Drake's advantage by proving the gap was deliberate" -> "keeps
  narrowing Drake's advantage by showing the gaps were deliberate"; "Since
  Dev's evidence work proved the gap was deliberate" -> "started showing the
  gaps were deliberate". NOT FIXED, logged: archive as "converted
  cold-storage shed" vs ch.9's archive (OPEN QUESTION 8); November and bare
  branches vs ch.9's July (OPEN QUESTION 4); "care facility in Millbrook"
  (OPEN QUESTION 6); Theo's "nineteen years" (OPEN QUESTION 10). Adelaide
  read: "Adelaide, Warden of the first debt (role, not bloodline)" is
  separate from the grandmother (see CARRY-FORWARD 2). 0 em dashes, 22
  spaced hyphens (highest so far). Style: heavy theme lines ("Information
  wasn't a weapon. It was a wound. The story was the bandage. The ledger was
  the scar."), "Not X. Y" pivots, theme-restating close ("Because the valley
  had always known. It just hadn't had the words."). Odette Reyes 78 years
  and "recorded 2024" fit a 2024 present.
- chapter_15: APPLIED, verified via diff of commit `f8551915` — "your father"
  (was "your mother"), 2003 heart-failure rewrite (was "died six months
  later. Heart attack."), "two hours" (was "two hundred miles"). All three
  former QUEUED items now confirmed live. Still spotted, not fixed: Theo age
  36 vs born 1997 (see chapter_01 note above — confirmed a real error, ch.15
  needs the fix, not ch.1). Real read: still owed (ch.13-16 claimed).
- chapter_37: APPLIED, verified via diff of commit `f8551915` — Weather/Silas
  Harker rewrite landed: "Warden" → "Weather" (role name, 2x), "Ambrose
  Whitlock" → "Silas Harker" (name, throughout), added "Not Old Man Harker,
  who was alive and difficult" distinction line. All 6 tell-phrase edits
  confirmed live. Real read: still owed. (Live text at 20:00 UTC still had
  Drake "in a county holding cell" in ch.37 while the arrest is in ch.41;
  re-check when the read reaches ch.37.)
- All other chapters: NOT PROOFED (mechanical pass only).
