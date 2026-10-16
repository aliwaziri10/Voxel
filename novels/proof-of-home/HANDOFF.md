# Proof of Home: HANDOFF

Read `novels/EDITORIAL_CHARTER.md` first, always. Then read this file. Then open `novels/proof-of-home/PROOFREAD_TRACKER.md`, which is the live record of what is finished. Nothing marked DONE there is ever proofread again.

Repo: `aliwaziri10/Voxel` (not `Wazzaboyzz/Voxel`, which is a different, unrelated repo).
Zia works in the browser only, by voice dictation and copy/paste. He is not technical.

## What this book is

A standalone slow-burn cozy fantasy romance, 32 chapters. Sarah Quill, a baker whose bread carries what she feels, and Jack Mercer, the ferryman, in the lakeside town of Larkmere. Sarah's point of view in odd chapters, Jack's in even chapters, close third person, past tense. First kiss in chapter 27. The longing keeps rising after the kiss and is released only in chapter 32.

Zia's standing instruction, stated 2026-10-16: the two leads want each other physically and are denied it, and that denial must be felt in the prose through the body. Every chapter must raise the ache by one notch over the chapter before. Told feelings ("the ache", "longing") are not enough. Show it: a held breath, a locked grip, eyes fixed on one point, the distance between two shoulders, a word not said.

Single source of truth for plot and canon: `novels/proof-of-home-canon/canon_data.py`. Each chapter's plan (touch level, space, contact, restraint, bread magic) is in `novels/proof-of-home/beat_map.md`. Never edit the generated canon files by hand.

## STATE (verified live on 2026-10-17)

- The GitHub workflow "Voxel Novel (one command)" drafted chapters 1 to 22 and produced thin, flawed text. It finished its run on 2026-10-16 and made a last commit "Add Proof of Home (32 chapters, auto-generated)". The folder `novels/proof-of-home/chapters/` holds chapters 1 to 22 only. Chapter 7 does not exist. Chapters 23 to 32 were never saved.
- DO NOT run that workflow again for this book. Chapters are now written by hand, one at a time, by whoever holds this session.
- Chapter 1 has been rewritten under the method below and is live. See the tracker for the current count of finished chapters.

## Why the generated chapters failed (read before touching any old chapter)

1. Each chapter's plan was only four or five lines about one scene, so the model had nothing to dramatise and filled space.
2. Free fallback models wrote many chapters and ignored the word floor.
3. The long chapters (9, 10, 16, 19) reached length by looping the same sentences or drifting into recap. Hitting the number there meant padding, not story.
4. The model pasted planning notes into the prose: "touch level three of ten", "the kiss in chapter twenty-seven", "yesterday's chapter", "the feeling he wanted to leave the reader with", and the canon's own labels such as "held, and neither lets go first". The repo's leak guard does not catch these.
5. Point of view broke: chapters 14 and 16 (Jack's) are told from Sarah's side, and chapter 22 mixes both.
6. Canon broke: chapter 16 has Sarah decide to stay (that belongs to chapter 31). Chapter 17 invents an earlier first kiss. Chapter 22 says Jack inherited the shop.
7. Touch level jumped past the plan in chapters 17, 19 and 21 and fell short in 9 and 12, so the ache did not rise one notch at a time.
8. Baking comparisons leaked into Jack's chapters (voice guide forbids this) and em dashes remain in several chapters.

Old chapters 2 to 22 are therefore REWRITTEN from the canon, not extended. Keep only lines that truly work. Known good material: the end of chapter 4 ("he wished it were wider"), the narrow back passage in chapter 15, the crowded crossing in chapter 18, the doorway scene in chapter 3.

## THE METHOD (do this for every chapter, in strict numeric order)

1. Read the chapter's entry in `beat_map.md` and `canon_data.py`, plus `VOICE_GUIDE.md`, plus the chapter before it. Do not skip the previous chapter. Continuity comes from its real text, not from its plan.
2. Write a beat sheet first: 5 to 6 genuine sub-beats with a word budget each. Cover the plot beat, a relationship beat, an interior beat, a stakes or world beat, and a callback or plant. Plan the body-level restraint and the one notch of ache this chapter adds. A sub-beat must add something a reader would miss if it were cut. Never stretch one event.
3. Write the full chapter, 2,300 to 2,700 words, in the right point of view and voice. Sarah: warm, sensory, baking comparisons. Jack: dry, spare, watchful, water and tiller comparisons. Plant secrets quietly per the canon's hidden-fact schedule.
4. Run the mechanical checks on the draft with a shell: `wc -w` for the word count, `grep -c "—"` for em dashes (must be 0), and a case-insensitive grep for some, something, someone, somewhere, somehow, particular, the specific, the kind of, kind of, unwavering, woven, seamless, testament, tapestry, protagonist, sub-beat, chapter, book, series, "days later", weekday names and any digit. Fix every hit.
5. Read the draft once against all 10 points in the tracker, including the points a script cannot check: point of view, metaphor discipline, touch level, ache rising, grammar and dialogue punctuation, rhythm, ending on an image.
6. Give the finished chapter to Zia with the direct edit link `https://github.com/aliwaziri10/Voxel/edit/main/novels/proof-of-home/chapters/chapter_NN.md` stated first (for a new chapter use the `new/main/novels/proof-of-home/chapters?filename=chapter_NN.md` form). Zia pastes the full text over the file and commits.
7. When Zia says "committed", fetch the file from GitHub and confirm the live text matches. Only then tick the chapter in the tracker, with its real word count and the commit hash, and give Zia the updated full tracker file to paste and commit. Verify that commit too.
8. Update this HANDOFF every two or three chapters.

## Rules that never bend

- Free models only for anything automated. Nothing in this pipeline may cost money.
- No em dashes. No dates, weekdays, years or ages in digits (write ages as words). Time is told by season, light, weather and the bread.
- No kiss before chapter 27. Nell never appears in any intimate beat; she only meddles around the edges.
- Names are fixed: Sarah Quill, Jack Mercer, Odalys Pike, Nell Mercer, Gideon Teague, Fenna Quill, the ferry Heron, Larkmere Water, Lantern Street, the Lamplight Inn. Wren belongs to another Voxel series and must never appear.
- The obstacle is never a procedure (meeting, vote, debt, count). Interruptions come from feeling, weather, magic, or a person who loves them.
- Never write chapter numbers, touch levels, the word reader, or any canon label inside the story text.
- Never edit the frozen older books. Do not mix craft or logic across Voxel's sub-projects.

## How to work with Zia

- He is non-technical. Maximum three or four steps at a time. Exact button labels. The full GitHub edit link in the same message as the step, put first.
- Every URL, file path and all copyable text goes in its own code block. Paste complete replacement files, never diffs or line-by-line edits.
- Check things yourself first through the tools before asking him to look anything up.
- Whenever he says "committed", verify on GitHub before moving on, every time.
- Do not describe finished work at length. Move straight to the next step.

## KNOWN LIMITS

- The GitHub connector is refused (403) when it tries to create anything under `.github/workflows/`.
- The name-collision check was only done against the story bibles, not the other books' chapter text (gate `name_collision_audit_complete` in `book_config.json` is still open).

## OPEN DECISIONS (for Zia)

- Pen name: `Elif Kessler` is a proposal only. Not decided.
- Genre label, series name "Larkmere" and the town name are working names only.
- Whether to add more books in Larkmere later.

## To regenerate the canon files after any canon change

Run from `novels/proof-of-home-canon/`: `python3 build_canon.py` then `python3 build_bible.py`. Then save `story_bibles/larkmere.json` and `novels/proof-of-home/beat_map.md` to the repo.
