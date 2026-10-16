# Voice Guide - Proof of Home

Standing style rules for this book, referenced during every editorial_review
pass and every mechanical_qa run. Every rule below comes from the canon in
`novels/proof-of-home-canon/canon_data.py` or from `novels/EDITORIAL_CHARTER.md`.
If a rule changes, change it in canon_data.py first, then rebuild with
`build_bible.py`, then update this file.

Read `novels/EDITORIAL_CHARTER.md` before touching any chapter.

## Locked filler/tell-word rules

- No "some" or "something" hedges standing in for a precisely named feeling (someone, somewhere, somehow are caught by the same check). Name the feeling.
- "particular", "the specific ___" and "the kind of ___" are cut.
- "one beat too long" is cut.
- No em dashes anywhere. Use a period, a comma or a colon.
- No tidy summary sentences at the end of a chapter. Let the last image carry the feeling.

## Banned / flagged text for this book

These are checked by the banned-text scan in build_canon.py and must never appear in a chapter:

- Years in digits (any 19xx or 20xx), weekday names, the phrase "days later".
- Ages in digits. Time is told by season, light, weather and the bread.
- The word "protagonist", the word "sub-beat", the labels "Wound:" and "Competence:", the text "[End of Chapter", and the pattern "Book " followed by a number.
- Procedure as obstacle: no meeting, ruling, debt, count, ledger, vote or any process may be the thing keeping them apart. Interruptions come from feeling, weather, magic, or a person who loves them.

## Narrator voice notes

- Close third person, past tense, throughout. Odd chapters are Sarah Quill's point of view. Even chapters are Jack Mercer's.
- Sarah's voice is warm and sensory. She notices heat, hands, flour and rising dough. Her comparisons come from baking.
- Jack's voice is dry, spare and watchful. He notices what people carry and never says it first. His comparisons come from water, lines, current and the tiller.
- Metaphor discipline: baking comparisons stay out of Jack's chapters. Water comparisons stay out of Sarah's.
- Desire lives in small physical detail: the weight of a hand, the distance between two shoulders, breath on a collar, the pause before a sentence, the effort of staying still.
- Pressed closeness (touch level 4 and up) is built from restraint. Show what the body does to hold back: a locked grip, a held breath, eyes fixed on a point, a word not said. Sensual, never explicit.
- Show the bread magic in every chapter, small and specific. Sarah's bread carries what she feels while shaping it.
- Every chapter raises the ache by one notch. After the first kiss in chapter 27 the longing does not ease. It is released only in the final chapter.
- Nell never appears in any intimate beat. She only meddles around the edges.
- Names are fixed: Sarah Quill, Jack Mercer, Odalys Pike, Nell Mercer, Gideon Teague, Fenna Quill, the ferry Heron, Larkmere Water, Lantern Street, the Lamplight Inn. Wren is used by another Voxel series and must not appear here.

## Promotion to series-wide rules

A rule here gets promoted into `novels/EDITORIAL_CHARTER.md` (i.e. applied
to ALL future Voxel novels, not just this one) only after it's held true
across 2+ separate books. Don't promote off a single book's pattern.
