"""
canon_data.py - single source of truth for the next series (small-town cozy
fantasy romance). PART 1 OF 3: core facts.
Part 2 (to add): chapter plan with ISO dates and sub-beats (CHAPTERS list).
Part 3 (to add): hidden-fact schedule.

RULES
- Everything is data. No weekday, age, total or formatted date is typed by hand.
  build_canon.py computes them from the ISO dates and numbers below.
- Text fields are in-world facts only. Never write: Book N, the series,
  protagonist, sub-beat, Wound:, Competence:, [End of Chapter.
- Placeholders allowed in text, resolved by build_canon.py: {opening} {vote}
  {threshold} {counted} {ferry_loaves} {final_total} {fare} {loaf_price}
  {shortfall} {margin}.
- Edit this file, never the generated files.

GENRE: slow-burn small-town cozy fantasy romance. The love story is the book.
See ROMANCE_RULES at the bottom of this file; they are sent to the writing model.

STATUS: DRAFT. Pen name, genre and all proposals below are NOT yet approved by
Zia. See PLAN_AND_STATUS.md. Validated by build_canon.py (names, dates, totals).
"""

SERIES_SLUG = "larkmere"
BOOK_TITLE = "Proof of Home"
PEN_NAME = "Elif Kessler"  # proposal only; canon does not depend on it
TOWN = "Larkmere"          # working name; fictional lakeside town
LAKE = "Larkmere Water"    # working name of the lake
CHAPTER_COUNT = 32
WORDS_MIN, WORDS_MAX = 2300, 2700

# ---------- Calendar (real Gregorian) ----------
OPENING_DATE = "2027-04-03"      # bakery reopens, Saturday
VOTE_DATE = "2027-06-29"         # council lease vote, Tuesday
COUNT_CLOSES = "2027-06-26"      # last sales day counted for the vote
SALES_WEEKDAYS = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
CLOSED_WEEKDAYS = ["Sunday", "Monday"]
# The ferry runs Tuesday to Sunday; no Monday service.
FERRY_WEEKDAYS = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# ---------- Money and counts (US dollars) ----------
LOAF_PRICE = 7.00
ROLL_PRICE = 2.00
FERRY_FARE = 4.00
MONTHLY_RENT = 1150.00
THRESHOLD = 1500   # whole loaves sold, counted from OPENING_DATE through COUNT_CLOSES

# Loaves sold in the shop, per period. Opening Saturday, then 12 full
# Tuesday-to-Saturday weeks. The validator checks week dates and the total.
OPENING_DAY_LOAVES = 40
WEEKLY_LOAVES = [90, 96, 102, 108, 112, 118, 124, 130, 136, 140, 146, 155]
# Loaves sold on the ferry by Jack from a cash box and never written in the
# shop ledger. Found in the ledger check; they push the count over THRESHOLD.
FERRY_LOAVES_UNLEDGERED = 6
# Expected by design (validator asserts these):
EXPECT_LEDGER_TOTAL = 1497
EXPECT_FINAL_TOTAL = 1503

# ---------- Cast ----------
# dob is ISO. Age is computed as of each chapter date.
CAST = {
    "Zoya Quill": {
        "role": "baker, heroine, point of view in odd chapters",
        "dob": "1994-09-12",
        "desc": "Runs the bakery on Lantern Street. Came back to Larkmere after her great-aunt Fenna Quill died and left her the shop lease. Her bread carries the feeling she had while shaping it.",
    },
    "Jack Mercer": {
        "role": "ferryman, hero, point of view in even chapters",
        "dob": "1991-02-20",
        "desc": "Pilots the ferry Heron across Larkmere Water. Quiet, dry humor. Knows when a passenger is carrying an unspoken worry.",
    },
    "Gideon Teague": {
        "role": "council chair",
        "dob": "1955-12-19",
        "desc": "Chairs the Larkmere council. Careful with rules. Grandfather of Lotte Teague.",
    },
    "Ines Okafor": {
        "role": "town clerk",
        "dob": "1972-06-08",
        "desc": "Keeps the council records and counts the vote. Precise, kind, never rushed.",
    },
    "Bertrand Fisk": {
        "role": "owner of Fisk Provisions",
        "dob": "1969-03-14",
        "desc": "Sells packaged bread from the grocery on Quay Road. Friendly on the surface, competitive underneath.",
    },
    "Izma Haddad": {
        "role": "bookshop owner, Zoya's friend",
        "dob": "1993-01-25",
        "desc": "Runs the bookshop next door to the bakery. Loud laugh, loyal, bad at secrets.",
    },
    "Milo Sutter": {
        "role": "ferry deckhand",
        "dob": "2005-05-30",
        "desc": "Jack's deckhand. Eager, forgetful about paperwork.",
    },
    "Lotte Teague": {
        "role": "child, Gideon's granddaughter",
        "dob": "2017-08-02",
        "desc": "Visits the bakery after school. Asks direct questions.",
    },
    "Fenna Quill": {
        "role": "Zoya's great-aunt, deceased",
        "dob": "1951-07-09",
        "dod": "2026-11-14",
        "desc": "Ran the bakery for decades. Died 2026-11-14. Appears only in memory and in her recipe cards.",
    },
}

# Pre-made minor names. If a scene needs a new named person, use the next
# unused name here. Never invent one.
EXTRAS_POOL = [
    ("Anselm Rudd", "owns the hardware store"),
    ("Perpetua Ostrow", "retired schoolteacher"),
    ("Tobias Alder", "mail carrier"),
    ("Linnea Eklund", "nurse at the lakeside clinic"),
    ("Hollis Lindgren", "fisherman"),
    ("Cosima Duarte", "runs the flower stall"),
]

# ---------- Magic: one small knack per named resident, with limits ----------
KNACKS = {
    "Zoya Quill": {
        "does": "Bread she shapes by hand carries the feeling she has while shaping it. Whoever eats it feels a mild echo of that feeling.",
        "limits": [
            "Only bread she shapes by hand. Machine-made or bought bread carries nothing.",
            "The echo is mild and lasts that day only.",
            "It cannot create a feeling she does not have, and cannot be aimed at a person.",
            "If she bakes to hurt someone, the bread simply tastes flat.",
        ],
    },
    "Jack Mercer": {
        "does": "He knows when a person within the length of his ferry is carrying a worry they have not said aloud.",
        "limits": [
            "Only aboard the Heron, within the length of the boat.",
            "He learns that a worry exists, never what it is or who it concerns.",
            "It works only on worries, not on joy, anger or lies.",
        ],
    },
    "Ines Okafor": {
        "does": "She always knows the exact time without a clock.",
        "limits": ["Time only. It tells her nothing else."],
    },
    "Gideon Teague": {
        "does": "Anything he writes in ink on council paper stays dry and readable in any weather.",
        "limits": ["Ink on paper only."],
    },
    "Bertrand Fisk": {
        "does": "Packaged goods on his shelves stay fresh a few days longer than they would elsewhere.",
        "limits": ["A few days only. It does not work on bread baked by hand."],
    },
    "Izma Haddad": {
        "does": "She can find any book in her shop by thinking of its title.",
        "limits": ["Inside her own shop only."],
    },
    "Milo Sutter": {
        "does": "He ties knots that hold until he chooses to undo them.",
        "limits": ["Rope and cord only."],
    },
    "Lotte Teague": {
        "does": "No knack yet. Larkmere children receive theirs at age ten.",
        "limits": [],
    },
}
MAGIC_RULES = [
    "Every resident has exactly one small, everyday knack. It does exactly what is written and nothing more.",
    "A knack fails if used to hurt someone.",
    "There are no spells, rituals, curses, hidden groups or dangers beyond ordinary life in a small town.",
]

# ---------- Places ----------
LOCATIONS = {
    "Lantern Street": "Main street of Larkmere. The bakery and the bookshop stand side by side on it.",
    "Quill's Bakery": "The bakery on Lantern Street. Leased from the council. Front counter, one oven, a back room with a flour bin.",
    "Haddad Books": "The bookshop next to the bakery on Lantern Street.",
    "Quay Road": "Road along the water. Fisk Provisions and the ferry landing are on it.",
    "Fisk Provisions": "The grocery on Quay Road.",
    "Heron Landing": "The ferry landing at the foot of Quay Road. Home dock of the ferry Heron.",
    "Council Hall": "Stone hall at the top of Lantern Street. The vote is held here.",
    "Larkmere Water": "The lake. The ferry crosses it between Heron Landing and the far shore landing at Reedbank.",
    "Reedbank": "Small landing on the far shore. Ferry destination.",
}
# Ferry crossing time in minutes. Fixed. Do not invent others.
FERRY_CROSSING_MINUTES = 18

# ---------- Closed-world rules for the model ----------
CLOSED_WORLD_RULES = [
    "Everything that may be named is listed in this canon. The people, places, businesses, dates, prices and numbers given here are complete.",
    "If a scene needs a minor person who is not in the cast, use a role such as the woman at the counter, or use the next unused name from the extras list. Never make up a new name.",
    "If a scene needs a place, price, distance, date or count that is not given, write the scene so it is not needed. Do not make one up.",
    "Do not add history, relatives, past events or town rules that are not listed.",
    "Do not do arithmetic in the prose. Use only the numbers given for that chapter.",
    "Magic follows the written rules exactly, with their limits. It never does anything not listed.",
]

# ---------- Genre rules: slow-burn romance comes first ----------
ROMANCE_RULES = [
    "This is a slow-burn romance. The love story between Zoya Quill and Jack Mercer is the main story of every chapter. The shop, the lease and the town are light pressure in the background.",
    "Every chapter moves Zoya and Jack closer emotionally by one small, specific step: a thing said, a thing given, a thing noticed, a hand not taken.",
    "Wanting is shown through attention and restraint: where they stand, what they notice about each other's hands and voices, what they almost say.",
    "Physical contact stays small and charged until late: a brushed hand, a bag handed across a gap, shoulders close on a bench. The first kiss happens in chapter 27 and not before. Before it there are near-moments that end because of something the characters themselves feel or fear.",
    "After the first kiss the closeness grows to embraces and kisses. Heat is closed door: a scene ends at the door.",
    "The low point is emotional and personal, caused by what the two of them feel or fear. It is not caused by the town or by a villain.",
    "The ending is a complete happy ending: they choose each other openly and stay in Larkmere.",
    "Mention the town, the shop and the lease only as far as a scene needs them.",
    "The tone is warm, funny and comforting.",
]
FIRST_KISS_CHAPTER = 27

# Physical tension ladder. Each stage may appear only in its chapters. The
# wanting grows long before anything is allowed to happen. Closed door always.
TENSION_LADDER = [
    "Chapters 1 to 6: no touch except Jack handing her bag across the gap at the dock, where their fingers meet on the strap for a moment.",
    "Chapters 7 to 12: small accidents. Hands brush over a flour sack. They pass each other in a narrow doorway with their shoulders touching. Each notices and says nothing.",
    "Chapters 13 to 18: nearness. They stand at the counter so close that her chest almost meets his arm. He steadies her on the dock with a hand at her waist and takes it away too fast. They each remember it afterward.",
    "Chapters 19 to 24: heat under restraint. She brushes flour from his collar and her fingers stay a second too long. His palm guides her through a door, rests low on her back, drifts a little lower and stops. They hold a look too long and are interrupted or step apart.",
    "Chapters 25 and 26: a near kiss, close enough to feel breath, stopped by what they themselves fear. They want each other and still do not act.",
    "Chapter 27: the first kiss, earned and a relief.",
    "Chapters 28 to 32: kisses and embraces, growing bolder. Heat is closed door: a scene ends at the door.",
]
ROMANCE_RULES = ROMANCE_RULES + [
    "Follow the physical tension ladder by chapter number. " + " ".join(TENSION_LADDER),
    "Between touches, the longing shows in small details: noticing the other's hands, voice, scent of flour or lake water, a pulse, a held breath, the memory of the last touch replayed.",
]
CLOSED_WORLD_RULES = CLOSED_WORLD_RULES + ROMANCE_RULES
