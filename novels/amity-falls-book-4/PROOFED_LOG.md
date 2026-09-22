# Book 4 proofed log

## CHAPTER STATUS — READ THIS TABLE FIRST, EVERY SESSION
DONE = verified clean or fixed and read back live. **Do not re-open a
DONE chapter without a specific new finding — cite it, don't re-read
"just to check."** This table exists because repeated sessions kept
re-verifying the same closed chapters. Stop doing that.

CORRECTION (2026-09-22, later same day): this table's ch.5 row
previously said "clean — Q4 closed, no fix" and Q2 below said "CLOSED,
no fix needed." Both were wrong. A session verified ch.5's LIVE text
directly (not from memory, not from this table) and found it said "a
Whitlock descendant" twice, naming Drake's coerced Millbrook Finder -
directly contradicting ch.11's grounded, cross-verified account (Dev's
substation research plus Theo's own interview), which names that same
person Silas Kettering with no Whitlock connection at all. FIXED
(`9e3991c`): both instances changed to the neutral "a Finder" - the
only detail Wren/Theo would have known at that point in the story,
since the name Kettering isn't learned until ch.11. This table is only
as good as the session that last touched a row - a "DONE / clean" entry
is a claim to verify against live text if you have a specific reason to
doubt it, not a guarantee.

| Ch | Status | Note |
|----|--------|------|
| 1  | DONE | clean |
| 2  | DONE | clean |
| 3  | DONE | FIXED — grandmother's age→14 (`268ae50`) |
| 4  | DONE | clean |
| 5  | DONE | FIXED — "a Whitlock descendant" → "a Finder", ×2 (`9e3991c`); previously mismarked clean, see CORRECTION above |
| 6  | DONE | clean (earlier full pass) |
| 7  | DONE | clean |
| 8  | DONE | FIXED — anachronisms |
| 9  | DONE | FIXED — "assisted living facility" (`e48fdeb`) |
| 10 | DONE | clean |
| 11 | DONE | FIXED — Reynolds→Reyes, age/decade; grandmother renamed Elena→Vivian (`ee44bbe`, Q21) |
| 12 | DONE | FIXED — truncated sentence, attribution, 2 anachronisms |
| 13 | DONE | clean |
| 14 | DONE | FIXED — Q3, teaching direction reversed (`b5d5d19`) |
| 15 | DONE | FIXED — full rewrite verified; Q18 (Theo's age) checked here 2026-09-23, clean, see Q18 below |
| 16 | DONE | clean — Q13 closed |
| 17 | DONE | clean — real first kiss |
| 18 | DONE | FIXED — day-count contradiction |
| 19 | DONE | clean — anchor chapter |
| 20 | DONE | FIXED — timeline reset (`da6ebe0`) |
| 21 | DONE | FIXED — custody (`beb46da`), Dev's evidence (`11cd9f0`) |
| 22 | DONE | clean — Q14 closed (Dev's shared home w/ Theo & Wren; see below), "assisted living facility" already fixed (`990a104`) |
| 23 | DONE | FIXED — Harriet's age; Q15 closed (Harrow/Harlan) |
| 24 | DONE | FIXED — grandmother's age→14 (`e82970a`); Q16 closed (Holloway & Finch) |
| 25 | DONE | FIXED — age, custody, em dash (`f9e01f5`) — the 2 literal em dashes here are the ONE deliberate, kept exception; see Q12 below. Also Q16 closed (Meridian Consulting) |
| 26 | DONE | FIXED — solstice/custody, kiss ref (`c4dbf27`) |
| 27 | DONE | clean — "Harlan" here is a place name, see Q15 |
| 28 | DONE | clean |
| 29 | DONE | clean |
| 30 | DONE | clean |
| 31 | DONE | FIXED — rupture-scene insert (`0963500`) |
| 32 | DONE | clean |
| 33 | DONE | clean |
| 34 | DONE | FIXED — custody (`866eb6b`) |
| 35 | DONE | clean |
| 36 | DONE | clean |
| 37 | DONE | clean |
| 38 | DONE | clean |
| 39 | DONE | FIXED — custody claims removed |
| 40 | DONE | FIXED — custody claims removed |
| 41 | DONE | FIXED — age (`29be7e8`); canonical arrest scene |
| 42 | DONE | clean |
| 43 | DONE | clean |
| 44 | DONE | clean |
| 45 | DONE | clean |

**All 45 chapters: DONE.** A "DONE" mark is not proof against re-reading
elsewhere in this file - see the CORRECTION above. Trust it as a
starting point, not a guarantee.

## Mechanical/lexical/tell-density pass, ch.27-45 — IN PROGRESS
Started 2026-09-23. This is a separate pass from the continuity table
above (all of ch.27-45 are continuity-DONE already). Scope: literal
em-dash count, repeated words/phrases, staged/parallel constructions,
general tell-density. Log one line per chapter as it's finished.

| Ch | Status | Note |
|----|--------|------|
| 27 | CLEAN | Zero literal em dashes (spaced-hyphen style used throughout, consistent with Q12). One repeated parallel construction ("Not because X. Not because Y. Because Z.") used twice near the end, in Wren's and Theo's mirrored declarations — read as a deliberate mirrored-vow device, not an accidental tic. No other repetition or tell-density issues found. |
| 28 | CLEAN | Zero literal em dashes. "Nine days" is repeated as a deliberate countdown refrain throughout (motif, not a tell). "There it is" repeated 3x in the Priya/Wren scene, also a deliberate rhythmic beat in that exchange, not accidental repetition. No new name/continuity conflicts (mentions "her father left" for the first time — doesn't contradict anything already logged, just a new detail). No mechanical issues found. |

## Open questions remaining (low priority / self-contained)
- Q20 "Castellan" vs "Castellano" — confirmed deliberate, do not fix.

Also not done: cross-check against Books 1-3; mechanical/lexical
tell-density pass for ch.27-45 specifically (now IN PROGRESS, see table
above — currently through ch.28).

## Closed this pass (Q2, Q3, Q5, Q6, Q7, Q10, Q12, Q14, Q15, Q16, Q18, Q19, Q21)
- **Q21 — "Elena Castellano" name collision. CLOSED, FIXED (`ee44bbe`,
  2026-09-22).** Grepped all 45 chapters for "Elena Castellano"/"Elena,".
  The name was used for two different people one generation apart:
  Wren's living mother (retired baker, ch.5/7/40 - 4 mentions across 3
  chapters) and Wren's dead grandmother (the 1985 Miller-girl search,
  ch.11 - 1 mention). No chapter ever acknowledges they share a name.
  Given a free hand to decide, fixed the lower-footprint side: renamed
  the grandmother to Vivian Castellano in her one appearance (ch.11).
  Same pattern already used earlier in the book for the identical
  problem one generation further back (the great-great-grandmother was
  renamed Clara Castellano to stop a different Elena collision, see
  Decision #13 note). Mother's name, all other family details,
  untouched.
- **Q19 — Early 14-day county-audit clock. CLOSED, resolved by reading,
  no fix needed (2026-09-23).** Ch.2 introduces "Notice of Records
  Audit" (Ordinance 44-12): a fourteen-day clock after which the county
  can copy/transfer restricted-index materials to its Millbrook
  repository, handing Drake leverage. Grepped all 45 chapters for
  "audit"/"Records Division"/"central repository"/"Ordinance 44-12" -
  this specific threat is never mentioned again after ch.2/3. It doesn't
  need a separate on-page resolution: ch.16's own fourteen-day plan
  ("target publication date: the fifteenth") is the team's direct
  answer to it, set in motion in the very same early stretch of the
  book. Once the complete true history is published, the county audit
  has nothing left to hand Drake - the race explicitly framed in ch.2
  ("we have fourteen days... before the county audit hands Drake the
  leverage he's been building for nineteen years") is the race the rest
  of the book runs and wins. No contradiction, no dangling thread - the
  audit clock is the inciting incident, not a separate plot line that
  needed its own ending.
- **Q2 — Drake's 2005 Millbrook target. CLOSED, FIXED (`9e3991c`).**
  Drake coerced Silas Kettering, a Millbrook Finder, into redirecting
  his toll — taking Harriet Marsh's memory of 1997-2007 to pay
  Drake's own debt. Ch.5 twice called this same Finder "a Whitlock
  descendant" before ch.11 ever named him - a genuine contradiction,
  since Kettering has no stated Whitlock connection and the story's
  other redirected-toll case (Kell/Dev) doesn't involve Whitlock
  lineage either. Fixed by removing the false qualifier in both
  spots. An earlier version of this log entry said "no fix needed" -
  that was wrong; see the CORRECTION note in the chapter table above.
- **Q3 — Adelaide/Ambrose relationship. CLOSED, FIXED (`b5d5d19`).**
  Ch.14 had the teaching direction backwards; fixed to match the
  established majority (Whitlock taught Adelaide).
- **Q5 — Lineage roster. CLOSED as far as the text supports.**
  Finders: Wren Castellano, her grandmother (Vivian, see Q21), her
  mother Elena Castellano, Dev Nair. Callers: Priya Nair. Menders: Mara
  Voss. Wardens: historically Whitlock line, now consensus-based.
  Weathers: three members, only Silas Harker named. Wicks: thinnest
  lineage, no members named on the page.
- **Q7 — Wren's mother's job. CLOSED, no fix needed.** Elena
  Castellano is a retired baker.
- **Q6 — Calendar/season. CLOSED, resolved by reading, no chapter
  edit needed.** "The frost line" scene at the very end is the
  bargain's permanent magical boundary marker (grass silver on the
  town side, green on the orchard side "since the first bargain was
  struck") — a fixed feature, not a literal winter-weather cue,
  confirmed by the same scene noting the air "should have been
  warmer by now." The "summer solstice" line (mid-book) is Yusuf's
  *original* publication target, stated before Drake's escalating
  threats forced the timeline to compress repeatedly (a pattern
  already established and locked — six months → ten days → nine
  days → days). The "Opening Spring" sign, seen with nine days left
  on the clock, is the actual final target that superseded it. Read
  in order, these aren't contradictory: an early, later-abandoned
  date, and the real one. No line needs to change.
- **Q10 — Archive building. CLOSED, decided (author's call, given
  free hand this session).** Canon going forward: the permanent,
  named "Amity Falls Archive" is the old Main Street library,
  gutted in the flood of '98, rebuilt with stones from the original
  foundation, sitting on the edge of the square where the old county
  records office also once stood (one site, two past uses — not a
  contradiction). This matches the three latest-in-story descriptions
  (ch. finale sequence). The earlier-story mentions of a "converted
  barn," "cold-storage shed," and "renovated room above the general
  store" are the *temporary workroom* the team used during the year
  the real building was still under renovation — consistent with the
  book's own repeated "the Archive project moved from Wren's kitchen
  table to the renovated room..." framing. No chapter's prose
  contradicts this reading as written; it did not require edits, only
  the decision recorded here. Future sessions: don't re-open this —
  treat early "barn/shed/room above the store" as workroom, late
  "old library on the square" as the real building.
- **Q12 — Spaced hyphens as em-dash substitutes. CLOSED, decided, NO
  SWEEP NEEDED, do not touch.** `novels/EDITORIAL_CHARTER.md` states an
  explicit, standing "em-dash ban" as one of the copy-editor's
  non-negotiable rules for every Voxel book. Verified directly against
  live text: grepped the literal em-dash character (—) across all 45
  raw chapter files. Result: exactly 2 occurrences in the entire book,
  both in ch.25 — and those 2 are already the one deliberate, logged
  exception (Decision #10, "Drake's em dash: kept"). Every other
  dash-style pause in all 45 chapters uses the spaced hyphen (" - ")
  instead. That is not inconsistent house style needing a sweep - it
  is the em-dash ban being enforced almost perfectly, with the spaced
  hyphen as its intentional, book-wide substitute. FUTURE SESSIONS:
  do not "fix" spaced hyphens to em dashes anywhere in this book, and
  do not treat a spaced hyphen as a proofreading error of any kind -
  it is correct as written, everywhere except the one already-logged
  Drake exception in ch.25.
- **Q14 — "The house on the ridge." CLOSED, decided, no fix needed.**
  Read ch.22 in full to check the source. Dev, riding his own
  established Honda, heads home at the end of a long day "toward the
  ridge, toward the house with... Theo's experimental lentil stew,
  Wren's terrible coffee... the chaos of two people learning how to
  share a space." Read in isolation this looks like a Dev/Theo mixup.
  But the same scene has Dev and Priya explicitly parting ways in
  separate vehicles (her truck, his bike) right before this line -
  staging that only makes sense if Dev's home isn't Priya's home.
  Checked every other Dev/Priya scene in the book (ch.4, 5, 8, 11, 14,
  21, 31, 38, 40-43): they're consistently paired as close partners
  everywhere else, which makes this one scene's deliberate separation
  meaningful rather than accidental. Read together, the passage is
  establishing that Dev has become part of Theo and Wren's household -
  a found-family arrangement distinct from his bond with Priya -
  consistent with the scene's own theme ("the chaos that had become,
  somehow, the shape of home"). No other chapter states or implies Dev
  lives elsewhere. Same category of call as Q10: a genuine ambiguity,
  resolved by reading, not a text error. No chapter edit made.
- **Q15 — M. Harrow / Harlan & Associates thread. CLOSED, no fix
  needed.** Grepped all 45 chapters for every mention. Margaret Harrow
  (retired 2011, former Processing Archivist) received a letter from
  "Law Offices of Harlan & Associates, Capital City" (ch.23), an
  estate/trusts/real-estate firm being investigated for possible ties
  to Drake. Separately, ch.27 mentions "Harlan" once, as a place name
  on a driving route ("the long way around through Harlan"). No
  chapter claims or implies these are the same entity - a law firm
  and a town sharing a name is not, by itself, a contradiction, and
  nothing else in the book connects them. Self-contained as the log
  already suspected; formally confirmed, no edit made.
- **Q16 — Shell company names. CLOSED, no fix needed.** Grepped all
  45 chapters. Holloway & Finch, Ltd. was incorporated 1995, dissolved
  2003 (three $5,000 payments in 1998, registered agent a Millbrook
  firm). Meridian Consulting is a separate, currently active shell
  (Delaware-registered, leasing storage units, "in the last eighteen
  months"). These read as sequential, not duplicate or conflicting:
  Drake rotated to a new shell once the older one was formally
  dissolved, consistent with a decades-long scheme (Holloway & Finch's
  1995 start even predates the established 2005 Millbrook incident).
  Two different shells at two different times is exactly what a
  long-running concealment operation would produce - not an error.
- **Q18 — Theo's age. CLOSED 2026-09-23, no fix needed.** Read ch.1 and
  ch.15 live in full. Ch.1: his credentials state "Theo Marsh,
  twenty-six." Ch.15: he says directly, "I was sixteen when I started
  looking for you, Grandma. Ten years ago. I'm twenty-six now" — 16+10=26,
  internally consistent, no birth year stated in either chapter. The
  supposed "born 1997, so should be 27" contradiction traced back to
  CANON_NUMBERS.md itself: an earlier version of that file asserted a
  birth year that was never quoted from the manuscript - a derived
  guess that only balances arithmetically if the present year is 2023,
  which directly contradicts that same file's own locked "present day:
  autumn 2024" entry. In other words, the two live chapters were never in
  conflict; a reference file's internal math error was mistaken for a
  manuscript contradiction. Fixed by correcting CANON_NUMBERS.md's entry
  (removed the false birth-year claim, documented why). No chapter text
  changed - none needed to. Also noted in passing: the stale
  `amity-falls-book-4_full_manuscript.md` concatenation file has an
  outdated version of the ch.15 scene reading "twenty-six... ten years
  ago... thirty-six now" - one more sign that concatenation predates
  several since-fixed chapters and should never be trusted over the
  individual chapter file (this was already documented for the
  Clara/Elena Castellano rename; now doubly confirmed).

## Rule for every session, no exceptions
1. Read the table above first.
2. If a chapter says DONE, that's a claim, not a guarantee (see the
   CORRECTION note) — open it again only with a specific new finding,
   cited against live text, not "just to check."
3. Work the open-question list instead. Pick the next unclosed item,
   verify it live, log the result in one line, move on.
4. Do not re-run a "fresh sequential read" of chapters already marked
   DONE without a specific reason. That loop is exactly what caused
   ch.5 to be redone repeatedly - though this time it turned out a
   real error was hiding under a "clean" mark, so the instinct to
   re-check was right; the fix is to cite a concrete reason, not to
   avoid re-checking altogether.
5. Q6, Q10, Q12, Q14, Q15, Q16, Q18, Q19, and Q21 are closed and
   decided — see above. Don't re-litigate any of them without a
   genuinely new, specific finding. In particular: NEVER convert a
   spaced hyphen to an em dash anywhere in this book (Q12) - that would
   violate the charter's own em-dash ban, not fix anything. And never
   "fix" Theo's age in ch.1 or ch.15 (Q18) - those chapters are
   correct; if a canon/reference file ever again disagrees with them,
   the reference file is wrong, not the chapters. And the grandmother
   in ch.11 is named Vivian, not Elena (Q21) - don't revert it.

## Decisions locked (facts, do not re-derive)
1. Josiah Whitlock (recorder, 1847) ≠ Ambrose Whitlock (Warden,
   1872-1901) — distinct people, confirmed repeatedly.
2. Countdown chain ch.16→18→19→20→21 = one deadline (Friday-the-11th).
   Ch.31→37 = a second, later clock. Two crises, not a broken timeline.
3. Ch.41 (home, 6:45am) is the one canonical arrest; ch.21/25/26/34/
   39/40 all match it.
4. Kiss order: ch.17 (first) → ch.21 (interrupted) → ch.26 (deepest).
5. Grandmother's death age = 14, standardized.
6. Harriet Marsh's home = "assisted living facility" / Willow Creek,
   standardized.
7. Silas Kettering ≠ Silas Harker — distinct, already differentiated.
8. Martha Whitlock = Ambrose's daughter, confirmed book-wide.
9. Denise's "granddaughter's husband" line (ch.16) is correct as is.
10. Drake's em dash (ch.25, ×2): kept, the ONE deliberate exception to
    the book-wide em-dash ban. See Q12 - do not add or "correct" any
    other em dash anywhere else in the book.
11. Ch.5's "-A.W." journal signature is a deliberate misdirection
    (Ambrose vs. Adelaide Whitlock, same initials). Closed (Q4).
12. Ambrose Whitlock taught Adelaide the bargain (not the reverse) —
    ch.14's reversed line fixed (Q3).
13. Elena Castellano (Wren's mother) is a retired baker (Q7). The
    grandmother previously also named "Elena Castellano" (ch.11) is now
    Vivian Castellano (Q21, fixed `ee44bbe`) - same collision pattern,
    same fix, as the earlier Clara/Elena great-great-grandmother rename.
14. Publication timeline: original target = summer solstice
    (superseded); actual target = spring, "Opening Spring" banner
    (Q6).
15. The Amity Falls Archive = the renovated old Main Street library
    (flood of '98, rebuilt on original foundation stones); earlier
    "barn/shed/room above the store" = the temporary workroom used
    before it (Q10).
16. Drake's Millbrook Finder is named Silas Kettering (ch.11); ch.5
    does not name or misname him as a Whitlock descendant (Q2, fixed
    `9e3991c`).
17. "The house on the ridge" (ch.22) is Theo and Wren's shared home,
    which Dev has also come to treat as home; Priya has her own,
    separate home. Not a contradiction (Q14).
18. Spaced hyphens (" - ") are the book-wide, deliberate substitute
    for the charter's banned em dash. Confirmed by direct count: 2
    literal em dashes exist in all 45 chapters combined, both already
    the logged Drake exception. Never "fix" a spaced hyphen (Q12).
19. "Harlan" is both a law firm name (Harlan & Associates, ch.23) and,
    separately, an unrelated place name (ch.27) - not shown to be the
    same entity, not a conflict (Q15).
20. Holloway & Finch (dissolved 2003) and Meridian Consulting (active,
    recent) are two sequential shell companies in Drake's long-running
    scheme, not duplicate or conflicting names for one company (Q16).
21. Theo Marsh is 26 years old in both ch.1 and ch.15, self-consistent
    (16 + 10 years = 26); no birth year is stated in the manuscript.
    Any future reference file that derives a conflicting birth year is
    the one with the error (Q18).
22. Ch.2's county-records-audit threat (Ordinance 44-12, 14 days) is the
    inciting incident for the whole book's publication race, not a
    separate thread needing its own on-page resolution; ch.16's
    publication plan answers it (Q19).
23. Wren's grandmother (1985 Miller-girl search, ch.11) is named Vivian
    Castellano, distinct from Wren's mother Elena Castellano (Q21).

_Older narrative version of this log (per-chapter rationale, quotes,
session-by-session play-by-play) is in git history if the reasoning
behind any line above is ever needed._
