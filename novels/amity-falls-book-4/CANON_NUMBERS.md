# Book 4 canon numbers — single source of truth
_Merged from CANON_NUMBERS.md and DATES_BIBLE.md, 2026-09-22, because having
two overlapping reference files let them silently disagree with each other
(see PROOFED_LOG.md STAMP 2). This is now the only canon-numbers file for
this book. Do not create a second one._

Read this before touching any date, age, or name in any chapter. Every
number below was checked against the live chapter text (not memory, not a
prior handoff). Where a number is still unresolved, it says so and points
to `PROOFED_LOG.md` for the open question. Update this file, not just the
log, whenever a number gets newly confirmed or changed.

## Locked (verified in multiple chapters, do not change without re-verifying)
- Present day: autumn 2024.
- Harriet Marsh: born 1949, age 75. Lost decade 1997-2007 (ages 48-58).
  Husband Thomas Marsh died 2003, inside the lost decade.
- Theo Marsh: born 1997. Confirmed 26 in ch.1 and ch.15 ("I'm twenty-six
  now"). NOTE: 1-year mismatch against 2024-1997=27, not fixed - low
  priority, see Open Questions.
- Drake's first (Millbrook) attempt: 2005, nineteen years before present.
  Confirmed in ch.5, ch.19, ch.21.
- Millbrook <-> valley drive: two hours. Confirmed/fixed in ch.5, 13, 15,
  28, 38, 44.
- Wren Castellano: 21 years old. Confirmed twice in ch.20.
- **Warden succession and the Josiah/Ambrose question — DECIDED
  2026-09-22, Option B (see PROOFED_LOG.md STAMP 2 for the full trail):**
  Josiah Whitlock (role active 1847, still active 1863, tried and failed
  to end the bargain, hid the complete terms) → his son **Ambrose
  Whitlock** (Warden 1872-1901, tried again 1889, hid Adelaide's letter,
  taught Adelaide the renewal) → Sarah Voss/Mara's family (Menders,
  1901-1947) → Weathers line → Caller line → vacant after prior Warden
  died 1987 → Yusuf (Warden through the ring-ritual era) → role passes to
  Wren by custody of the ledger, not blood (ch.9 - "whoever holds the
  ledger holds the duty"). Two Whitlocks, father and son, each
  independently tried to end the bargain and failed - this is the book's
  actual recurring-pattern theme, matching ch.3's own list of forgotten
  attempts (Caleb, Denise, Ambrose). Fixed in ch.9 (`c77f8f4`) to state the
  father relationship explicitly instead of the vaguer "generations
  before." Ch.2, 6, 7, 12, 13, 15 (Josiah) and ch.3, 5, 14, 19, 21
  (Ambrose) all stay as they are - both names are correct, referring to
  different people. **Do not collapse these into one name.**
- **Ambrose Kell** (a DIFFERENT, later person - not to be confused with
  either Whitlock): the antagonist who forced Dev to redirect tolls and
  spread the "valley is cursed" lie a generation before Drake. Confirmed
  distinct in ch.19.
- Ring ritual: 2023. Denise's split-the-weight ritual freeing her: March
  2022, ending 50 years of secret renewals (1972-2022).
- Elena Castellano (Wren's grandmother, died when Wren was 12-14, found
  the missing Miller girl in 1985): distinct from Clara Castellano
  (great-great-grandmother, signed folios 1870-1895, renamed from a
  collision with "Elena" in ch.3, fixed `61225b8`). Family line: Clara →
  [unnamed great-grandmother] → Elena → [Wren's unnamed mother] → Wren.
- Drake is arrested: see CONFLICT below - NOT locked.

## CONFLICT - genuine duplicate scenes, not date typos (need Zia's decision)
These need a structural decision (which scene stays, which is cut or
merged) before any date can be "fixed." A numeric patch alone would just
make two contradictory scenes internally consistent with each other while
still being two contradictory scenes.

1. **Drake's arrest is told twice, incompatibly.** Ch.21: a deputy tells
   Wren Millbrook County picked Drake up at a motel, "three days" from
   print. Ch.41: Drake is arrested at home at 6:45am, no resistance,
   triggered by "the gap" collapsing his hold. Ch.37, 39, 40 all treat
   Drake as free/active, which fits before ch.41's arrest but would
   contradict ch.21's arrest already having happened. Ch.41's version is
   what the rest of the book is built around. Ch.39/40 already fixed
   (`c77f8f4` and earlier) to not claim custody before ch.41. **Ch.21's
   motel arrest is NOT yet fixed** - still needs cutting or downgrading to
   something short of arrest.
2. **First kiss is told twice, both in full.** Ch.17: complete,
   undisturbed first-kiss scene. Ch.21: another full kiss, framed as
   "Interrupted... Again," implying a prior interruption that ch.17
   doesn't have. Ch.26 adds a third version, recalling an interruption by
   Priya that appears in neither ch.17 nor ch.21. Three-way mismatch, not
   two-way. Needs Zia's read of which detail should change. NOT applied.
3. **The accelerate-the-timeline council scene happens at least four
   times** (ch.16, 18, 19, 20) with the same shape and overlapping
   dialogue. Read as one continuous escalation, the countdown works:
   ch.16 "two weeks/the fifteenth" (14 days) → ch.18 "ten days" → ch.19
   "one week" (7 days) → ch.21 "three days." Ch.20 is the outlier: it
   independently lands on "two weeks" again, matching ch.16 exactly rather
   than compressing further - the signature of a duplicated scene, not a
   date needing adjustment. Ch.20's actual content (Wren's arc, the
   Marta/Hal objection) is worth keeping; the countdown number and vote
   structure is what's suspect. NOT applied - needs Zia.

## Still open, lower priority
- Archive building has 3+ different physical descriptions across chapters
  (tall-windows library, cold-storage shed, municipal building, converted
  barn "behind the general store" per ch.18).
- Calendar/season references still don't form one consistent year across
  the whole book (see PROOFED_LOG.md Q7).
- Denise's "grandson's husband" line (ch.16) vs. Mara+Caleb as the couple -
  unverified whose grandchild Mara is.
- Martha Whitlock's relation to Ambrose (daughter vs. granddaughter,
  ch.22) - see PROOFED_LOG.md Q22, still needs Zia.
- Theo's age: 26 stated vs. 27 by birth-year math (1997 to 2024). Low
  priority.
- 1942 renewal gap (ch.10): mentioned in passing, not yet explored.
- Fading-memory thread (ch.11): Wren's own search debt is eroding rather
  than staying fixed, unlike every other documented debt. Track whether
  later chapters pay this off.
- 1893 ledger vs. oral-tradition Mender-toll contradiction (ch.12): this
  one is INTENTIONAL, not an error - ledger shows variable tolls, oral
  tradition claims a clean formula, chapter explicitly resolves this as
  "both true in different registers." Do not "fix" if seen again.
- Archive building flooded twice (1922, 1957); council sealed the 1893
  ledger in 1998 under then-chair Yusuf - no conflict with his later
  Warden appointment, ~26 years apart, different roles.

## Read progress
Sequential manual read: ch.1-26 done (per PROOFED_LOG.md). Ch.27-45 not yet
read this pass - do not assume they are clean.

## How to keep this file honest
Every entry above was read from the live chapter text, not from memory or
a prior version of this file. When you read a new chapter, add any new
number here BEFORE updating PROOFED_LOG.md's chapter status, so the two
files never disagree about what's confirmed. If you find this file
disagreeing with PROOFED_LOG.md or with live chapter text, stop and stamp
the conflict in PROOFED_LOG.md rather than picking a side silently - this
exact failure (two files disagreeing, nobody catching it) is why this file
was merged with DATES_BIBLE.md in the first place.
