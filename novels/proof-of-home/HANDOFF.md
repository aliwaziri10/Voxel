# Proof of Home: HANDOFF

Read `novels/EDITORIAL_CHARTER.md` first, always. Then read this file. Then open `novels/proof-of-home/PROOFREAD_TRACKER.md`, which is the live record of what is finished. Nothing marked DONE there is ever proofread again.

Repo: `aliwaziri10/Voxel` (not `Wazzaboyzz/Voxel`, which is a different, unrelated repo).
Zia works in the browser only, by voice dictation and copy/paste. He is not technical.

## What this book is

A standalone slow-burn cozy fantasy romance, 32 chapters. Sarah Quill, a baker whose bread carries what she feels, and Jack Mercer, the ferryman, in the lakeside town of Larkmere. Sarah's point of view in odd chapters, Jack's in even chapters, close third person, past tense. First kiss in chapter 27. The longing keeps rising after the kiss and is released only in chapter 32.

Zia's standing instruction, stated 2026-10-16: the two leads want each other physically and are denied it, and that denial must be felt in the prose through the body. Every chapter must raise the ache by one notch over the chapter before. Told feelings ("the ache", "longing") are not enough. Show it: a held breath, a locked grip, eyes fixed on one point, the distance between two shoulders, a word not said.

Single source of truth for plot and canon: `novels/proof-of-home-canon/canon_data.py`. Each chapter's plan (touch level, space, contact, restraint, bread magic) is in `novels/proof-of-home/beat_map.md`. Never edit the generated canon files by hand.

## STATE (verified live on 2026-10-17, third session)

- Chapters 1 to 23 are live and DONE in the tracker. Chapters 1 to 4 and 16 to 23 were rewritten from the canon, chapters 5 to 15 were line-edited. Do not reopen any of them unless a specific continuity issue is found.
- Chapter 23 was written this session (2350 words, blob SHA `ca00537aa0806e68085b725eab840d83454582f9`, commit `fd1b99275babddb3e7b71c39319038f958890ec4`). The tracker's chapter 13 commit hash was wrong (it did not exist on GitHub) and was corrected to `b9bbee5bf6af62fe1b8d6dd2b5f4dc5a05c9f501`. Lesson: never trust a hash in the tracker without a `get_commit` call.
- Standing instruction from Zia, 2026-10-17: push chapters directly through the aliwaziri10 GitHub connector (confirmed authenticated, write access works, no 403), stamp each chapter in the tracker, continue in strict order to chapter 32, and update this HANDOFF before the session ends. Verification method that works: after each push, compute the git blob SHA of the local text and compare it with the SHA the connector returns. Do not trust `raw.githubusercontent.com` straight after a push on the branch name; fetch by the commit SHA instead.
- Next: write chapter 24, Jack POV, late summer, touch 6. The Heron stops mid-lake after dark and will not move until dawn. Jack and Sarah wait it out in the cramped wheelhouse under one blanket, shoulder to shoulder, hands joined. Neither sleeps. He feels every breath she takes. He stares at the black water and says her name once, softly; she does not answer, only tightens her hold. The loaf they share goes cold and neither cares. At dawn the Heron starts as if nothing happened. Water comparisons only, no baking comparisons in his head. Nell must not be aboard.

### Continuity facts established in chapters 16 to 23 (use them, never contradict them)

- Chapter 16: Gideon keeps a flat tin with a heel of Fenna's unsold yearly loaf, which tastes of leaving. Jack's memory is a grey wool coat going up the gangplank, a brass button hanging by a thread, his grandfather's hand on his shoulder.
- Chapter 17: iron hook by the bakery window where Fenna hung a lantern early at midsummer. Sarah's lantern buns made couples stand closer. Jack buttoned a split bun with two thumb dents into his coat pocket. Nell steered them to the same lantern; Gideon had counted that lantern in advance.
- Chapter 18: crowded market-day crossing, her shoulder against his arm the whole way, he talked about the weather. Nine grey loaves, one taken to Jack by Odalys.
- Chapter 19: eight grey loaves remain on the cellar shelf. Odalys told Sarah about the bun. The grocer's wife tasted a biscuit and remembered a lonely winter. Sarah baked one plain loaf, brought it to the dock, said "I miss you, and I did not expect to, and you are standing right in front of me." Jack answered with a speech about autumn and "your own people". Her raised hand lowered. She left the lantern unlit. Hint planted: in another city she learned to make herself small (reveal is chapter 29).
- Chapter 20: dark window two nights. Jack laid the stone-hard bun on the counter (it stays there). He said "I cannot make you stay, Sarah, and I am afraid of how much I want to." She said "Stop deciding for me." Reveal: his mother left on the Heron in the rain when he was a boy small enough that the rail came to his eyes. On the narrow cellar stair, one inch of air. The cellar is warm now and smells of yeast and warm wood; the eight grey loaves still sit there. Sarah promised to tell him her decision to his face when she knows. She told him to go home and find a question. She relit the lantern after he left.
- Chapter 21: Sarah's coat is Fenna's long waxed canvas coat with horn buttons. Jack's first real question: "Will you let me walk you home?" Downpour, shared coat, six rolls in the basket stayed dry and warm. At her door she said goodnight to his chin. First cool air, first smell of the turn.
- Chapter 22: Jack has asked nineteen small questions, none the big one. The last run of the season is on the harbor clerk's board, six weeks off. Late-summer lantern night, every household hangs a lantern on the pier rail. Nell steered them down the Net Sheds stair, her back against his chest the whole way, he gripped the iron rail and counted lanterns. Reveal: Nell has steered since the first loaf (flour sent by the Heron, early crossing moved to pass Lantern Street, stern line tied short, told Gideon where to stand). Nell calls Jack "Uncle". Odalys tasted the next morning's rolls and brought him one.
- Chapter 23: the wax is scraped off the pier rail by afternoon. Odalys ate a roll at the back door at first light and left humming. Sarah shaped the standing loaf for the far shore on the dusk run, said to the dough "I am not going to hide it", wrapped it cool in a blue cloth. Six passengers sat forward with their backs to the stern (three fishermen, three women with baskets). Nell was absent, "has a cough", though Sarah saw her healthy at noon outside the chandler's. Jack lashed the wheel with a turn of line and left it; the Heron slowed. He asked "May I?" (his twentieth small question) and she said "Yes." They held hands the whole crossing, thigh to thigh on the stern bench, eyes on the single lamp at the far landing. His thumb crossed her knuckles once; "Tell me if you want me to stop." "I do not." The loaf on her knee warmed while he held her hand and cooled when he let go at the far dock. His empty hand closed on nothing. She still has not told him her decision. Sarah has been pressed against him by a market-day crowd, a downpour and a lantern stair, and this is the first time she has held his hand.

## Why the generated chapters failed (read before touching any old chapter)

1. Each chapter's plan was only four or five lines about one scene, so the model had nothing to dramatise and filled space.
2. Free fallback models wrote many chapters and ignored the word floor.
3. The long chapters reached length by looping the same sentences or drifting into recap. Hitting the number there meant padding, not story.
4. The model pasted planning notes into the prose: "touch level three of ten", "the kiss in chapter twenty-seven", "yesterday's chapter", and the canon's own labels. The repo's leak guard does not catch these.
5. Point of view broke in several chapters.
6. Canon broke: a chapter had Sarah decide to stay too early, another invented an earlier first kiss, another said Jack inherited the shop.
7. Touch level jumped past the plan in some chapters and fell short in others, so the ache did not rise one notch at a time.
8. Baking comparisons leaked into Jack's chapters (voice guide forbids this) and em dashes remained in several chapters.

Chapters 24 onward, if any generated text exists, must be REWRITTEN from the canon, not extended. Chapters 24 to 32 are not written yet.

## THE METHOD (do this for every chapter, in strict numeric order)

1. Read the chapter's entry in `beat_map.md` and `canon_data.py`, plus `VOICE_GUIDE.md`, plus the chapter before it. Do not skip the previous chapter. Continuity comes from its real text, not from its plan.
2. Write a beat sheet first: 5 to 6 genuine sub-beats with a word budget each. Cover the plot beat, a relationship beat, an interior beat, a stakes or world beat, and a callback or plant. Plan the body-level restraint and the one notch of ache this chapter adds. A sub-beat must add something a reader would miss if it were cut. Never stretch one event.
3. Write the full chapter, 2,300 to 2,700 words, in the right point of view and voice. Sarah: warm, sensory, baking comparisons. Jack: dry, spare, watchful, water and tiller comparisons. Plant secrets quietly per the canon's hidden-fact schedule.
4. Run the mechanical checks on the draft with a shell: `wc -w` for the word count, `grep -c "—"` for em dashes (must be 0), and a case-insensitive grep for some, something, someone, somewhere, somehow, particular, the specific, the kind of, kind of, unwavering, woven, seamless, testament, tapestry, protagonist, sub-beat, chapter, book, series, "days later", weekday names and any digit. Fix every hit. Also count repeats of ordinary words (hand, hands, stood, dough and the like): eight or more in one chapter is a problem unless the word is the chapter's subject.
5. Read the draft once against all 10 points in the tracker, including the points a script cannot check: point of view, metaphor discipline, touch level, ache rising, grammar and dialogue punctuation, rhythm, ending on an image.
6. Push the chapter with the GitHub connector (get the file's current SHA from the directory listing first), then compare the blob SHA of the local text with the SHA returned by the push.
7. Only then tick the chapter in the tracker with its real word count and the commit hash, and confirm the hash exists with a `get_commit` call.
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

- He is non-technical. Maximum three or four steps at a time. Exact button labels. The full GitHub edit link in the same message as the step, put first, whenever he has to do something by hand.
- Every URL, file path and all copyable text goes in its own code block. Paste complete replacement files, never diffs or line-by-line edits.
- Check things yourself first through the tools before asking him to look anything up.
- Whenever he says "committed", verify on GitHub before moving on, every time.
- Do not describe finished work at length. Move straight to the next step.

## KNOWN LIMITS

- The GitHub connector is refused (403) when it tries to create anything under `.github/workflows/`.
- Name-collision audit run 2026-10-17 by cloning the repo and scanning both ways (gate `name_collision_audit_complete` in `book_config.json` is left for Zia to flip). Result: none of Sarah Quill, Jack Mercer, Odalys, Nell, Gideon, Fenna, Heron, Lamplight, Lantern Street or Larkmere appears in any other book. No other-book character name appears in chapters 1 to 23. One overlap: the first name Sarah is used in the frozen Amity Falls book 4 for two minor characters (Sarah Voss, a past warden mentioned in chapter 3, and Sarah Kline, a third-grade teacher in chapter 40). Different series and surnames, so low risk, but Zia should decide whether to accept it.
- Clean-up done 2026-10-17: the early draft folder `novels/next-series-canon/` (a Tamsin Quill / Matteo Garrick plot about a council vote and a loaf count, rejected by Zia) was deleted. Never revive it. `book_config.json` and `brief.txt` stay because the generation workflow reads them.

## OPEN DECISIONS (for Zia)

- Pen name: `Elif Kessler` is a proposal only. Not decided.
- Genre label, series name "Larkmere" and the town name are working names only.
- Whether to add more books in Larkmere later.
- Whether the first name Sarah is acceptable given the two minor Sarahs in Amity Falls book 4.

## To regenerate the canon files after any canon change

Run from `novels/proof-of-home-canon/`: `python3 build_canon.py` then `python3 build_bible.py`. Then save `story_bibles/larkmere.json` and `novels/proof-of-home/beat_map.md` to the repo.
