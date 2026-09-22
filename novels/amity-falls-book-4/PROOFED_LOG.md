# Book 4 proofed log

Only what was read from live `main` is stamped. Never stamp from memory or a
handoff claim. Condensed 2026-09-22 — detail trimmed, no findings dropped.

Legend: FIXED = edit read back live. READ = manual read, no change needed.
NOT PROOFED = mechanical pass only, no manual read yet.

**LAST CHAPTER STAMPED: ch.23.** Ch.1-23 read/fixed. Ch.24-45 not yet read
this pass (ch.37 has an earlier tell-phrase fix only, no full read).

🔒 ch.24-28 claimed by Claude (chat session), 2026-09-22 07:20 UTC.

## ZIA DECISIONS NEEDED (4) — do not guess-fix any of these
1. **Ch.14 Josiah vs Ambrose.** The "tried to end the bargain, hid the
   terms" story is attributed to Josiah in ch.14's key reveal but to
   Ambrose everywhere else that matters (ch.3 anchor, ch.5, ch.15, ch.18,
   ch.21). This log itself has contradicted itself on which is correct
   (see old ch.9 commit note). Need: which Whitlock actually tried and
   failed — Josiah or Ambrose — then ch.14 gets fixed to match.
2. **Chapter-ordering problem, now spanning ch.18-23.** Three near-identical
   "accelerate the publication" council votes in a row (ch.18 → ten days,
   ch.19 → one week, ch.20 → two weeks, the last with zero awareness of the
   other two). NEW (ch.23): ch.23's own countdown math ("today's the third,
   twelve days to the fifteenth") places it chronologically BEFORE ch.18's
   day-5, ch.19's day-8, and ch.21's day-12 in the same countdown to the
   15th - meaning ch.23, despite its chapter number, depicts an earlier
   story-day than four chapters that precede it in the manuscript. This
   isn't just a ch.18-20 problem anymore; ch.23 may belong earlier too (near
   ch.16, which shares its "today=day 1, 14 days out" starting point). Do
   not resolve by guessing which chapter is misplaced - needs Zia's read of
   the intended order.
3. **Ch.21 vs ch.41 — Drake's arrest happens twice**, incompatibly (motel
   pickup vs. early-morning home arrest). Ch.37/39/40 only make sense if
   ch.41's version is real. Recommend cutting/downgrading ch.21's version,
   but it's real prose — needs your sign-off.
4. **Ch.17 vs ch.21 — first kiss happens twice**, both written as complete
   scenes. Ch.21 calls it "Interrupted... Again," which only makes sense if
   ch.17's kiss didn't already land clean. Need: which chapter keeps it.

Related, lower-stakes naming collision: **Ambrose Kell** (ch.19, a past
antagonist) vs. **Ambrose Whitlock** (the Warden in dispute above) — two
different people sharing a first name, real reader-confusion risk even
once #1 is resolved.

## Fixed and locked (do not re-touch without new evidence)
- Folio gap: 1887-1891. (ch.3, `207db70`)
- Josiah signed 1847/1863; Ambrose is 1872-1901, "A.W." in newer ink. Fixed
  ch.2, 6, 7, 9, 12, 13, 14(partial), 15. (Separate from Decision #1 above —
  that's about who *tried to end it*, this is just about signatures.)
- Anachronisms (trial/leverage treated as past when it's ch.36-45 material):
  fixed ch.8, ch.12. Clear through ch.23; ch.24+ not checked yet.
- ch.11: Odette Reynolds → Reyes (4x). ch.22: "Dev's grandmother, Harriet
  Marsh" → "Theo's grandmother" (Harriet is Theo's grandmother everywhere
  else — ch.1,4,6,7,8,11,13,15,21,23). ch.23: Harriet's age "eighty-seven"
  → "seventy-five" (locked canon: born 1949, present-day 2024, confirmed
  independently in ch.20's "twenty-one years" Wren-age math and elsewhere).
  All three are plain misattributions/arithmetic slips, fixed directly, not
  judgment calls.
- ch.12: truncated sentence, ledger-finder attribution, 2 anachronisms — fixed.
- ch.15: full rewrite verified (`ffe3562`) — "your father" not "your
  mother," husband died 2003, "two hours" not "two hundred miles," Theo's
  age 36→26, grandmother detail fixed.
- ch.18: internal "ten days" vs "thirteen days" contradiction fixed.
- Countdown chain ch.16(14d)/ch.18(10d)/ch.19(7d)/ch.21(3d) is internally
  consistent as arithmetic, but is NO LONGER treated as "settled" now that
  ch.23 shows the same 15th-deadline countdown may not be in chapter order
  - see Decision #2. Don't touch any individual number; the open question
  is ordering, not arithmetic.

## Open questions (not fixed, tracked, no chapter guessed at)
- **Q1 Elena Castellano**: named as both Wren's living mother (ch.5,7) and
  dead grandmother (ch.11). Ch.3's ancestor rename to "Clara" may need
  revisiting.
- **Q2 Warden of the first debt**: at least 4 different succession/office
  mechanisms across ch.3/9/10/11/14/20 (blood vs. custody vs. consensus vs.
  "council chair"). Needs one settled mechanism.
- **Q3 Drake's 2005 Millbrook target**: 3 different accounts of what/who he
  took (a Whitlock descendant / Silas Kettering / the renewal-ceremony
  memory via the "twelfth redirect," ch.21) — may all be compatible, not
  yet reconciled.
- **Q4 Adelaide**: ch.4 calls her Wren's own grandmother; ch.5/9/12 call her
  Adelaide Whitlock, an unrelated historical Warden. Ch.4 looks like the
  outlier. NEW (ch.23): confirms Adelaide Whitlock's bloodline "runs through
  Mara, through Caleb, through their kids" - i.e. Mara and Caleb are
  established descendants of Adelaide Whitlock. Useful for Q6/Q15 but
  doesn't resolve Q4's separate Wren's-grandmother-Adelaide conflict.
- **Q5 Ch.5 is broadly unreliable**: internally contradicts the Whitlock
  death date, Warden vacancy, Drake's custody status, day-count, and trip
  count — whole chapter needs a pass, not itemized fixes.
- **Q6 Lineage roster**: Mara's lineage label conflicts 3 ways (Finder /
  Mender / Wardens rep). Dev=Finder and Priya=Caller are now confirmed
  clean across multiple chapters. Ch.23's new "descendant of Adelaide
  Whitlock" fact for Mara/Caleb (see Q4) is genealogy, not a lineage-gift
  label, so it doesn't settle this by itself.
- **Q7 Calendar**: ch.23 explicitly sets its own scene in "late autumn"
  turning to "winter" ("fields turning brown for winter," "the winter
  light") - consistent with the autumn drift already noted in ch.20-22, and
  the "converted barn" Archive description (see Q11) also matches ch.18.
  Still no single full-book calendar confirmed; needs the ch.24-45 read.
- **Q8 Wren's mother's job**: baker / clinic / store — 3 different jobs, unresolved.
- **Q9 Harriet's home**: "nursing home" vs "care facility" vs "assisted
  living" — used inconsistently. Ch.23 just says "the home," no new term.
- **Q10 Kiss/rupture beat map is stale**: see Zia Decision #4. Beat map's
  ch.30 rupture placement doesn't match ch.19-21's already-settled
  relationship either — may need the beat map itself corrected, not just chapters.
- **Q11 Archive building**: 5 different physical descriptions across ch.9,
  12, 13/14, 16, 18, 19. Ch.23 repeats ch.18's "converted barn" description
  exactly - the first internal AGREEMENT found between two of the five
  competing descriptions, worth noting for whichever description is chosen.
- **Q12 Small continuity**: two unrelated characters both named "Silas"
  (Kettering ch.11, Harker ch.37) — check for reader confusion. Everything
  else in this bucket (Theo's age math, "eight months," Drake's name) is
  now internally consistent, no action needed.
- **Q13 Spaced hyphens (" - ")** used as em-dash substitutes throughout —
  invisible to automated em-dash checks. Ch.23 count: ~4. Decide house
  style: keep or sweep.
- **Q14 Line-edit style patterns** (not factual errors): staccato fragments,
  "Not X. Y" pivots, theme-restating endings, litany-style closings
  (ch.19, ch.20), heavy "said" tags. Worth a dedicated style pass, not urgent.
- **Q15 Denise's "grandson's husband" line** (ch.16) doesn't obviously fit
  Mara+Caleb as the established couple — whose grandchild is Mara? Ch.23's
  Adelaide-descent fact (Q4) doesn't resolve this specifically. Not checked
  against ch.1-12/Books 1-3 yet.
- **Q16 Ambrose Kell vs Ambrose Whitlock** — see Zia Decisions section above.
- **Q17 "The house on the ridge"** (ch.22): Dev's closing scene implies he
  shares a home with Theo and Wren, but no chapter has established this
  household or its location relative to Wren's family home. Ch.23 doesn't
  touch this - still open.
- **Q18 NEW (ch.23) M. Harrow / Harlan & Associates thread**: a new
  investigative subplot (an anonymous 2003 donor restricted access to
  Adelaide Whitlock's folio via a law firm). Self-contained so far, no
  contradiction with anything else - just note it as a new open thread to
  watch for a payoff or dangling end by ch.45.

## Not done
- Sequential read of ch.24-45.
- Full season/countdown/Archive-naming reconciliation pass (needs the rest
  of the book read first).
- Cross-check against Books 1-3 (Q1, Q15).
- The 4 Zia decisions above — nothing past them should be force-fixed by guessing.
