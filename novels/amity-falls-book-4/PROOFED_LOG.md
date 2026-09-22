# Book 4 proofed log

Only what was read from live `main` is stamped. Never stamp from memory or a
handoff claim. Condensed 2026-09-22 — detail trimmed, no findings dropped.

Legend: FIXED = edit read back live. READ = manual read, no change needed.
NOT PROOFED = mechanical pass only, no manual read yet.

**LAST CHAPTER STAMPED: ch.22.** Ch.1-22 read/fixed. Ch.23-45 not yet read
this pass (ch.37 has an earlier tell-phrase fix only, no full read).

## ZIA DECISIONS NEEDED (4) — do not guess-fix any of these
1. **Ch.14 Josiah vs Ambrose.** The "tried to end the bargain, hid the
   terms" story is attributed to Josiah in ch.14's key reveal but to
   Ambrose everywhere else that matters (ch.3 anchor, ch.5, ch.15, ch.18,
   ch.21). This log itself has contradicted itself on which is correct
   (see old ch.9 commit note). Need: which Whitlock actually tried and
   failed — Josiah or Ambrose — then ch.14 gets fixed to match.
2. **Ch.18/19/20 duplicate council scene.** Three near-identical "accelerate
   the publication" council votes in a row: ch.18 → ten days, ch.19 → one
   week, ch.20 → two weeks with zero awareness of the other two (framed
   around a milder threat than either). Reads like ch.20 is either
   out-of-order or a leftover duplicate draft. Need: keep/cut/reorder call.
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
  fixed ch.8, ch.12. Clear through ch.22; ch.23+ not checked yet.
- Countdown escalation ch.16(14d) → ch.18(10d) → ch.19(7d) → ch.21(3d) is a
  clean, correct sequence — don't touch. Ch.20's "two weeks" is the outlier
  (duplicates ch.16's exact figure) — see Decision #2.
- ch.11: Odette Reynolds → Reyes (4x). ch.22: "Dev's grandmother, Harriet
  Marsh" → "Theo's grandmother" (Harriet is Theo's grandmother everywhere
  else — ch.1,4,6,7,8,11,13,15,21). Both plain misattributions, fixed
  directly, not judgment calls.
- ch.12: truncated sentence, ledger-finder attribution, 2 anachronisms — fixed.
- ch.15: full rewrite verified (`ffe3562`) — "your father" not "your
  mother," husband died 2003, "two hours" not "two hundred miles," Theo's
  age 36→26, grandmother detail fixed.
- ch.18: internal "ten days" vs "thirteen days" contradiction fixed.

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
  outlier.
- **Q5 Ch.5 is broadly unreliable**: internally contradicts the Whitlock
  death date, Warden vacancy, Drake's custody status, day-count, and trip
  count — whole chapter needs a pass, not itemized fixes.
- **Q6 Lineage roster**: Mara's lineage label conflicts 3 ways (Finder /
  Mender / Wardens rep). Dev=Finder and Priya=Caller are now confirmed
  clean across multiple chapters.
- **Q7 Calendar**: no single consistent season/month thread across all 22
  chapters read so far (spring in ch.16, autumn implied in ch.20-22, others
  unstated). Needs one full-book pass once the rest is read.
- **Q8 Wren's mother's job**: baker / clinic / store — 3 different jobs, unresolved.
- **Q9 Harriet's home**: "nursing home" vs "care facility" vs "assisted
  living" — used inconsistently, no clear single term yet.
- **Q10 Kiss/rupture beat map is stale**: see Zia Decision #4. Beat map's
  ch.30 rupture placement doesn't match ch.19-21's already-settled
  relationship either — may need the beat map itself corrected, not just chapters.
- **Q11 Archive building**: 5 different physical descriptions across ch.9,
  12, 13/14, 16, 18, 19. Needs one settled description.
- **Q12 Small continuity**: two unrelated characters both named "Silas"
  (Kettering ch.11, Harker ch.37) — check for reader confusion. Everything
  else in this bucket (Theo's age math, "eight months," Drake's name) is
  now internally consistent, no action needed.
- **Q13 Spaced hyphens (" - ")** used as em-dash substitutes throughout —
  invisible to automated em-dash checks. Decide house style: keep or sweep.
- **Q14 Line-edit style patterns** (not factual errors): staccato fragments,
  "Not X. Y" pivots, theme-restating endings, litany-style closings
  (ch.19, ch.20), heavy "said" tags. Worth a dedicated style pass, not
  urgent.
- **Q15 Denise's "grandson's husband" line** (ch.16) doesn't obviously fit
  Mara+Caleb as the established couple — whose grandchild is Mara? Not
  checked against ch.1-12/Books 1-3 yet.
- **Q16 Ambrose Kell vs Ambrose Whitlock** — see Zia Decisions section above.
- **Q17 "The house on the ridge"** (ch.22): Dev's closing scene implies he
  shares a home with Theo and Wren, but no chapter has established this
  household or its location relative to Wren's family home. Flag for ch.23+.

## Not done
- Sequential read of ch.23-45.
- Full season/countdown/Archive-naming reconciliation pass (needs the rest
  of the book read first).
- Cross-check against Books 1-3 (Q1, Q15).
- The 4 Zia decisions above — nothing past them should be force-fixed by guessing.
