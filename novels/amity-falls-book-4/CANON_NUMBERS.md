# Book 4 canon numbers — single source of truth

Read this before touching any date, age, or countdown in any chapter. Every
number below was checked against the live chapter text (not memory, not a
prior handoff). Where a number is still unresolved, it says so and points to
`PROOFED_LOG.md` for the open question. Update this file, not just the log,
whenever a number gets newly confirmed or changed.

## Locked (verified in multiple chapters, do not change without re-verifying)
- Present day: autumn 2024.
- Harriet Marsh: born 1949, age 75. Lost decade 1997-2007 (ages 48-58).
- Theo Marsh: born 1997. Confirmed 26 in ch.1 and ch.15 ("I'm twenty-six
  now" - sixteen, plus ten years searching). NOTE: this is a 1-year mismatch
  against 2024-1997=27, not fixed - see PROOFED_LOG Q12, low priority.
- Harriet's husband, Thomas Marsh: died 2003, inside the lost decade.
- Drake's first (Millbrook) attempt: 2005 - "nineteen years ago" from 2024.
  Confirmed independently in ch.5, ch.19, ch.21 (twelfth-redirect timing).
- Millbrook <-> valley drive: two hours. Fixed in ch.5, 28, 38, 44 via
  book4_fixes.json; ch.13, ch.15 independently confirm "two hours" in
  live text with no fix needed.
- Wren Castellano: 21 years old. Confirmed twice in ch.20 ("the words she'd
  swallowed for twenty-one years"; "For the first time in twenty-one years").
- Ambrose Whitlock: Warden of the first debt 1872-1901. Failed attempt to
  end the bargain: 1889 (ch.3's anchor - never change). Taught Adelaide,
  hid the complete terms after failing. Correctly named in ch.5, 15, 19, 21.
- Josiah Whitlock (Ambrose's father, invented for this book): signed the
  1847 marginal note and 1863 hidden letter, both predating Ambrose's
  1872-1901 tenure. Fixed in ch.6, 7, 9, 12.
- Ambrose Kell (a DIFFERENT, later person - not to be confused with Ambrose
  Whitlock): the antagonist who forced Dev to redirect tolls and spread the
  "valley is cursed" lie a generation before Drake. Confirmed as a distinct
  character in ch.19 and ch.37's fix ("Not Ambrose Kell, who was alive and
  difficult" was cut but the name itself is legitimate - see ch.19).
- Ring ritual: 2023. Denise's split-the-weight ritual freeing her: March
  2022, ending 50 years of secret renewals (1972-2022).
- Drake is arrested: see CONFLICT below - this is NOT locked.

## UNRESOLVED - genuine duplicate scenes, not date typos
These need a structural decision (which scene stays, which is cut or merged)
before any date can be "fixed." Applying a numeric patch without resolving
the duplication would just make two contradictory scenes internally
consistent with each other while still being two contradictory scenes.

1. DRAKE'S ARREST is told twice, incompatibly:
   - Ch.21: a deputy tells Wren "Millbrook County picked him up at a motel
     on Route 9," triggered by Dev's substation evidence reaching the
     prosecutor. Print is "three days" out at this point.
   - Ch.41 (already logged): Drake is "taken into custody at six forty-five
     this morning at his residence on Elm Street," triggered by "the gap"
     collapsing his hold - no resistance, described as a clean early-morning
     arrest.
   Ch.37, 39, 40 all still treat Drake as free/active, which fits AFTER
   ch.21's version but BEFORE ch.41's - i.e. if ch.21's arrest were canon,
   ch.37/39/40 would be contradicting an arrest that already happened. So
   ch.41's version is the one the rest of the book is actually built around;
   ch.21's arrest is the one that doesn't fit anywhere else. Recommend: ch.41
   stays, ch.21's arrest scene needs to be cut, replaced, or its "custody"
   framing walked back to something short of arrest (e.g. "brought in for
   questioning, released"). NOT applied - deletes real prose, needs Zia's
   call.

2. FIRST KISS is told twice, both in full:
   - Ch.17: complete, undisturbed first-kiss scene at midnight over
     sandwiches and proof pages.
   - Ch.21: another full kiss, explicitly framed as "Interrupted... Again" -
     implying a previous interruption, not a previous completed kiss. This
     line only makes sense if ch.17's kiss is NOT canon, or if ch.21 is
     describing a second kiss the text doesn't otherwise acknowledge.
   The inherited beat map said "first kiss ch.21" (see PROOFED_LOG Q10) -
   that assumption was wrong or the manuscript drifted from it; ch.17
   already delivers a full first kiss. Recommend: decide which chapter's
   kiss is canon and cut or reframe the other. NOT applied.

3. THE ACCELERATE-THE-TIMELINE COUNCIL SCENE happens at least four times
   (ch.16, 18, 19, 20), each with the same shape (crisis -> emergency
   session -> debate -> vote -> countdown announced) and overlapping
   dialogue beats (Yusuf calling the vote, someone objecting, a show of
   standing/hands). The countdown numbers, read as one continuous
   escalation across ch.16 -> 18 -> 19 -> 21, form a clean decreasing
   sequence:

   | Chapter | Stated countdown | Days remaining |
   |---|---|---|
   | ch.16 | "two weeks... the fifteenth" | 14 |
   | ch.18 | "ten days" | 10 |
   | ch.19 | "one week" | 7 |
   | ch.21 | "three days" (arrest chapter, print imminent) | 3 |

   That's a real, working countdown - 14 to 10 to 7 to 3 tracks a
   tightening crisis correctly and should NOT be touched.

   Ch.20 is the outlier: it independently arrives at "two weeks" (14 days) -
   the same number as ch.16, not a further compression. Two different
   chapters landing on the exact same "two weeks" figure, via two different
   council sessions, is the signature of a duplicated scene rather than a
   date that needs adjusting. Ch.20's content (Wren's arc about no longer
   apologizing, the Marta/Hal privacy objection) is worth keeping - the
   countdown number and the redundant vote structure is what's suspect.
   Recommend: read ch.22+ to see which countdown they assume is current
   (this will show whether ch.20 chronologically belongs before ch.16, or
   is a straight duplicate to be cut). NOT applied - no date patch here
   would fix the actual problem.

## Still open, lower priority (see PROOFED_LOG.md for full detail)
- Archive building has 3+ different physical descriptions across chapters
  (tall-windows library, cold-storage shed, municipal building, converted
  barn "behind the general store" per ch.18).
- Calendar/season references still don't form one consistent year.
- Ch.14's Josiah/Ambrose mixup in its own central reveal (HIGH PRIORITY in
  PROOFED_LOG.md) - unrelated to the above, still needs Zia's decision.
- Denise's "grandson's husband" line (ch.16) vs. Mara+Caleb as the couple -
  unverified whose grandchild Mara is.

## How to keep this file honest
Every entry above was read from the live chapter text this session (chapters
1-21 and 37 have been read in full; 22-36 and 38-45 have not yet been read
this pass - do not assume they are clean). When you read a new chapter, add
any new number to the right section here BEFORE updating PROOFED_LOG.md's
chapter status, so the two files never disagree about what's confirmed.
