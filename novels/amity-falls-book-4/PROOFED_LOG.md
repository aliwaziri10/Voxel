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
- Strict sequential manual read of all 45 chapters: IN PROGRESS. ch.1-3 done,
  ch.4 next.
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
- chapter_04: SEEN "Josiah" fixes (2 hits).
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
