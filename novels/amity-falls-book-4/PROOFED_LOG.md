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
- ⚠️ AUDIT DISCREPANCY found during sequential read (ch.3): the corrected
  audit states "Ambrose Whitlock: 'Warden 1872–1901... died 2009' —
  unsupported; none of those figures appear" anywhere in the manuscript.
  chapter_03 explicitly states "He held the role from 1872 to 1901" — that
  figure DOES appear, verbatim, contradicting the audit's claim. The "died
  2009" half may still be unsupported (not yet independently re-checked),
  but the audit's blanket claim about the 1872-1901 figure is wrong. Not a
  chapter error — an audit-file error. Needs reconciling once more chapters
  are read (may be more Whitlock date mentions elsewhere).
- OPEN QUESTION FOR ZIA (raised at ch.4, applies book-wide): chapter_04 uses
  spaced hyphens (" - ") as dash substitutes, roughly 14 instances, with zero
  true em dashes. The mechanical passes count only U+2014, so they cannot
  see this. Not changed in ch.4 alone, because fixing one chapter would
  make it inconsistent with the rest if " - " is the pipeline's convention.
  Needs a decision: treat " - " as an em-dash dodge and sweep the whole
  book, or accept it as the house form. Check whether ch.1-3 and later
  chapters use it too as the read continues.
- Strict sequential manual read of all 45 chapters: IN PROGRESS. ch.1-4 done,
  ch.5 next.
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
- chapter_03: PROOFED (sequential manual read), 2026-09-21. No hard
  violations, no em dashes, no staged constructions. Repeated "Memory
  surrendered: X, Y, Z" folio format is an intentional in-world document
  convention, not a tell. No fix needed. See whole-book AUDIT DISCREPANCY
  note above re: Whitlock 1872-1901 dates — this chapter is the source of
  that figure and is internally consistent on its own terms. New continuity
  info: Warden succession Whitlock (1872-1901) -> Sarah Voss/Mara's family
  (1901-1947) -> Weathers line -> Caller line -> vacant after prior Warden
  died 1987 -> Yusuf (current). Elena Castellano (Wren's great-great-
  grandmother) was Finder 1870-1895. Missing folios 1887-1891 (5 yrs) is
  this chapter's core plot point, not a proofing error.
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
  Continuity to CHECK later (not errors yet):
  a. Doris says Harriet still visits every few months asking for the gap,
     yet Theo describes her as in assisted living, unable to remember the
     decade. Plausible but unexplained. Author call.
  b. Cold-case review "every ten years, next review is next month": with a
     2005 case and a present around 2024 this does not obviously land next
     month. Cannot resolve without the book's calendar date. Fold into the
     season/month pass.
  c. Folio ledger here lists an 1891 entry (Eleanor Whitlock), while ch.3
     says folios 1887-1891 are missing. Probably different documents (the
     county folio vs. the valley's ledger), but confirm.
  d. This chapter titles Josiah Whitlock "Warden of the First Debt" in
     1847, while ch.3's succession begins with Whitlock in 1872, and the
     hidden note says "I was the Warden" without saying which Whitlock.
     Live ch.4 has exactly one "Josiah" occurrence; the log's earlier
     "2 hits" was not reconciled and whether the queued Josiah fix is
     applied was not verified. Reconcile when the read reaches ch.9
     ("J. Whitlock, 1847").
- chapter_05: one entry SKIPPED (duplicate text). Other Batch 2 entries: not re-read.
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
