# Proof of Home: HANDOFF

THE BOOK IS COMPLETE. All 32 chapters are written, proofread on the 10 points and live on GitHub (verified 2026-10-18). A second round of reading and proofreading has also been finished for all 32 chapters on 2026-10-18; its chapter-by-chapter record is `novels/proof-of-home/SECOND_ROUND_LOG.md`. Do not write or regenerate any chapter. Do not run the GitHub workflow "Voxel Novel (one command)" for this book.

Read `novels/EDITORIAL_CHARTER.md` first, always. Then read this file. Then open `novels/proof-of-home/PROOFREAD_TRACKER.md`, which is the live record of what is finished. Nothing marked DONE there is ever proofread again.

Repo: `aliwaziri10/Voxel` (not `Wazzaboyzz/Voxel`, which is a different, unrelated repo).
Zia works in the browser only, by voice dictation and copy/paste. He is not technical.

## What this book is

A standalone slow-burn cozy fantasy romance, 32 chapters. Sarah Quill, a baker whose bread carries what she feels, and Jack Mercer, the ferryman, in the lakeside town of Larkmere. Sarah's point of view in odd chapters, Jack's in even chapters, close third person, past tense. First kiss in chapter 27. The longing keeps rising after the kiss and is released only in chapter 32, where Jack asks her to stay on the last run, she says she has been staying since the first loaf, and they kiss in plain light at the last lantern with the whole town watching.

Zia's standing instruction, stated 2026-10-16: the two leads want each other physically and are denied it, and that denial must be felt in the prose through the body. Every chapter must raise the ache by one notch over the chapter before.

Single source of truth for plot and canon: `novels/proof-of-home-canon/canon_data.py`. Each chapter's plan is in `novels/proof-of-home/beat_map.md`, and the scenes are in `novels/proof-of-home-canon/canon_scenes.py`. Never edit the generated canon files by hand.

## Who wrote what

Zia said on 2026-10-17 that part of the book was written by Claude sessions and part by ChatGPT. He did not say which chapters. This probably explains the differences in spelling, quotation marks and voice in chapters 2 to 15 (see KNOWN ISSUES IN FINISHED CHAPTERS). Chapters 17 to 18, 19 to 20 (hand rewrites), 23 to 26, and 27 to 32 (hand written) are the strongest, most consistent voice in the book: match that voice, not the weakest chapters. Several sessions have worked in parallel. Always list the latest commits and check a chapter's current blob SHA before pushing anything.

## STATE (verified live on 2026-10-18, seventh session)

- Second round, 2026-10-17 and 2026-10-18 (full record in `SECOND_ROUND_LOG.md`). Chapters 1 to 10 were done by Zia and earlier sessions; a fresh scan of the live files confirms they are clean (no em dashes, no straight quotes, no British spellings, no banned hedges). Chapter 15 had its second round earlier on 2026-10-17 (commit `19171d2b`). In this session chapters 11 to 14 and 16 to 32 were each read in full. Changes made: chapter 11 lost an invented line (his thumb on her cheek, which never happened) and got grey spelling; chapter 12 got American spelling and cuts to repeated words; chapters 13 and 14 were rewritten to the beat map (collar at the landing; one hand on the tiller while the other holds her, loaf crushed between them); chapter 16 got grey spelling; chapters 17 to 32 needed no other change. Chapter 25's line about Odalys circling the word "birthday" looks stray but is a deliberate plant for chapter 26, leave it.

- Chapters 1 to 32 are live and DONE in the tracker. Chapters 1 to 4 and 16 to 22 were rewritten from the canon, chapters 5 to 15 were line-edited, chapters 19 and 20 were rewritten by hand, chapters 23 to 26 were written from the canon in an earlier session, chapters 27 to 32 were written by hand. Do not reopen any of them unless a specific continuity issue is found.
- Chapters 24 to 26 were stamped in the tracker on Zia's word that everything up to 26 is finished. They were read in full and scanned mechanically (clean), not re-proofread line by line.
- Chapter 30: 2659 words, blob `3bb0a737`, commit `f69bb2912a448487d6c72529021113fc4e3b69bd`.
- Chapter 31: 2675 words, blob `eaaa1526`, commit `a81c7746dee5ee6d4d071b9a301368e1a0db6a30`.
- Chapter 32: 2673 words, blob `527393de`, commit `3d00bd74eccf25350a9130bfc871fd7944b89e77`.
- Lesson: never trust a hash in the tracker without a `get_commit` call.
- Zia's decision, 2026-10-18: every novel gets its own ending, and the next novel will be a different story with different protagonists and a different setup. Nothing from Proof of Home carries into it. Give it its own canon folder, its own tracker and its own handoff. Do not mix craft, names or logic across books (see the voxel-guardrails rule).
- Standing instruction from Zia: push chapters directly through the aliwaziri10 GitHub connector, stamp each chapter in the tracker, do not stop to ask him for input on straightforward next steps, and fix every proofreading flag rather than leaving it open. Verification method that works: after each push, compute the git blob SHA of the local text and compare it with the SHA the connector returns. The sandbox shell is plain `sh`: wrap anything that uses process substitution in `bash`. The `gh` CLI and `git push` have no write access in this sandbox; use the connector.
- What remains: only Zia's decisions (see OPEN DECISIONS), the optional clean-up of the known issues below, and the manual gates in `book_config.json`. A final cross-chapter read of the whole book in order has not been done.

### Continuity facts established in chapters 16 to 32 (use them, never contradict them)

- Chapter 16: Gideon keeps a flat tin with a heel of Fenna's unsold yearly loaf, which tastes of leaving. Jack's memory is a grey wool coat going up the gangplank, a brass button hanging by a thread, his grandfather's hand on his shoulder. Jack has a cottage at the end of the water road.
- Chapter 17: iron hook by the bakery window where Fenna hung a lantern early at midsummer. Sarah's lantern buns made couples stand closer. Jack buttoned a split bun with two thumb dents into his coat pocket. Nell steered them to the same lantern; Gideon had counted that lantern in advance.
- Chapter 18: crowded market-day crossing, her shoulder against his arm the whole way, he talked about the weather. Nine grey loaves, one taken to Jack by Odalys.
- Chapter 19: eight grey loaves remain on the cellar shelf. Sarah baked one plain loaf, brought it to the dock in the last light with two fishermen mending a net six feet away, said "I miss you, and I did not expect to, and you are standing right in front of me." Jack answered with a speech about autumn and "your own people". She left the lantern unlit, the first dark night since midsummer.
- Chapter 20: Jack laid the stone-hard bun on the counter (it stays there). He said "I cannot make you stay, Sarah, and I am afraid of how much I want to." She said "Stop deciding for me." Reveal: his mother went up the plank of the Heron in the rain in a grey wool coat when he was a boy small enough that the pier rail came to his eyes; his grandfather stood behind him with a hand on his shoulder. On the narrow cellar stair, one inch of air. Sarah promised to tell him her decision to his face when she knows. She relit the lantern after he left.
- Chapter 21: Sarah's coat is Fenna's long waxed canvas coat with horn buttons. Jack's first real question: "Will you let me walk you home?" Downpour, shared coat, six rolls in the basket stayed dry and warm.
- Chapter 22: Jack has asked nineteen small questions, none the big one. The last run of the season is on the harbor clerk's board, six weeks off. Nell steered them down the Net Sheds stair. Reveal: Nell has steered since the first loaf. Nell calls Jack "Uncle".
- Chapter 23: they held hands the whole dusk crossing; he asked "May I?" (his twentieth small question). The loaf on her knee warmed while he held her hand and cooled when he let go. Sarah wrapped the standing loaf in a blue cloth.
- Chapter 24: the Heron's engine stopped mid-lake and would not start until dawn. A grey wool blanket that smelled of tar and old rain. Sarah said: "Nobody is keeping me. I am sitting here."
- Chapter 25: Fenna's card: "He said it would be selfish to want me to stay, and kind to go before I could ask. He took the last run of the season. I let him call it kind." Fenna's last loaf was behind two stone jars of caraway. Forehead to forehead, one inch between their mouths.
- Chapter 26: Jack's brick of a loaf ("armored", "a lifeboat"), his twenty-first question, "May I", cut off by Nell's knock. Jack has an old rope scar across the back of his left hand.
- Chapter 27: the first kiss, mid-lake on the Heron at dusk, Sarah asked for it. The Heron ran true for the first time all season. The loaf rule: a kiss given in love sets a loaf's feeling for good.
- Chapter 28: the day after the kiss, the town knows from her bread. A second kiss on the cellar stair cut short by Odalys. He thought "Stay" and could not say it. Two lamps burning, his and hers, facing each other across the harbor.
- Chapter 29: Jack's cottage is one room and a lean-to with a black stove, a bench built for one and the grey blanket. She stopped the kiss herself ("I will not give you the half of me"). He said "As long as it takes." Reveal: the man in the city, not cruel, only large; she made herself small and left with a coat and the shop key. He fears the yes. Her dawn loaf said "yours" and then "not yet".
- Chapter 30: Fenna's letter (written the winter after the ferryman went, kept by Gideon): "He should have asked ... A lantern is not a question. Do not hang one in a window and call it patience ... Whichever of you is reading this, ask. Do not wait to be asked. Say it badly, say it once, say it in the rain. Then bear the answer." Jack fears his wanting is the weather she ran from. On the frozen pier she kissed him desperately; he stepped back; she gripped the lantern post and did not follow; her shadow stopped a yard short of his boots. The Heron "has a cough" (Nell's cover story). The chalk on the clerk's board was nearly gone.
- Chapter 31: the clerk had rubbed the chalk to one dot. Sarah found her decision already made in her own order book: twelve sacks of rye and wheat from the north shore mill delivered every fortnight through the first week of February, a cord of beech, a longer peel, a second crock. She wrote her first card in the margin language: a spiral, the ferry mark, and a square with a roof and the door open. She baked one loaf, wrapped it in the blue cloth, and told Jack on the pier before he could ask: "I am not leaving." He sat down on a coil of rope. He gave her Fenna's letter to read; she read "A lantern is not a question" aloud. He asked to ask her tomorrow on the last run, the one the old ferryman took, so the Heron carries it the other way. They shared Fenna's coat, kissed and stopped three times, and kept the last inch for the morning. His heel of the loaf tasted of yes and of walking in at the end of a long day.
- Chapter 32: the rain came in overnight. The Heron started on the first turn and ran true all day. The clerk chalked LAST RUN. DUSK. The whole town rode the dusk crossing; Odalys wore a hat from its box; Gideon sat in the stern; Nell stayed on the pier. Sarah gave the town a great round loaf that tasted of home. Mid-lake Jack lashed the wheel and asked: "Stay ... Will you stay, Sarah?" She answered "I have been staying since the first loaf." The Heron moved by herself and ran true. A woman came down the plank and stayed. At the last lantern the wick caught, they kissed in plain light, the lamps came on along the harbor wall, and the book ends on the Heron lying level at her lines.

## KNOWN ISSUES IN FINISHED CHAPTERS (re-checked against the live files 2026-10-18)

Fixed in the second round and confirmed by a scan of all 32 chapters: British spellings, straight quotation marks, the point-of-view slips in chapters 5 and 11, the banned phrase in chapter 5, and where Jack lives (chapter 6 now makes the ferry cabin the place he sleeps aboard before the early run, and the cottage at the end of the water road is home).

Still open, for Zia to decide:

- The helm of the Heron is called a tiller in some chapters and a wheel in others. Tiller: chapters 1, 2, 4, 5, 6, 7, 9, 10, 14, 20. Wheel: chapters 2, 4, 10, 11, 16, 18, 22 to 25, 27, 28, 30, 32. Pick one word for the whole book, or state once that the Heron has a wheel in the wheelhouse and a tiller used in the open.

## Why the generated chapters failed (read before touching any old chapter)

1. Each chapter's plan was only four or five lines about one scene, so the model had nothing to dramatise and filled space.
2. Free fallback models wrote many chapters and ignored the word floor.
3. The long chapters reached length by looping the same sentences or drifting into recap. Hitting the number there meant padding, not story.
4. The model pasted planning notes into the prose, and the repo's leak guard does not catch these.
5. Point of view broke in several chapters, and canon broke in a few (an early decision to stay, an invented first kiss).
6. Baking comparisons leaked into Jack's chapters (voice guide forbids this) and em dashes remained in several chapters.

## THE METHOD (reuse it for any future book, in strict numeric order)

1. Read the chapter's entry in the beat map and canon, plus the voice guide, plus the chapter before it. Continuity comes from its real text, not from its plan.
2. Write a beat sheet first: 5 to 6 genuine sub-beats with a word budget each. A sub-beat must add something a reader would miss if it were cut. Never stretch one event.
3. Write the full chapter, 2,300 to 2,700 words, in the right point of view and voice.
4. Run the mechanical checks with a shell: `wc -w`, em dashes (must be 0), digits, banned words (some, something, someone, somewhere, somehow, particular, the specific, the kind of, kind of, unwavering, woven, seamless, testament, tapestry, protagonist, sub-beat, chapter, book, series, "days later", weekday names), and repeats of ordinary words (eight or more is a problem). Check that every name, place and object already exists in the book.
5. Read the draft against all 10 points in the tracker.
6. Check the latest commits and the file's current blob SHA, push with the GitHub connector, compare the local blob SHA with the one the push returns.
7. Tick the chapter in the tracker with its real word count and commit hash.
8. Update the handoff every two or three chapters.

## Rules that never bend

- Free models only for anything automated. Nothing in this pipeline may cost money.
- No em dashes. No dates, weekdays, years or ages in digits (write ages as words). Time is told by season, light, weather and the bread.
- Nell never appears in any intimate beat; she only meddles around the edges.
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
- He does not want memory or a handoff trusted over the live repo. Say what you are about to do before you do it, and read the files before writing.
- Do not wait for an instruction to do the obvious next step. He said on 2026-10-17 and again on 2026-10-18: keep going and finish.

## KNOWN LIMITS

- The GitHub connector is refused (403) when it tries to create anything under `.github/workflows/`.
- Name-collision audit run 2026-10-17 by cloning the repo and scanning both ways (gate `name_collision_audit_complete` in `book_config.json` is left for Zia to flip). Result: none of Sarah Quill, Jack Mercer, Odalys, Nell, Gideon, Fenna, Heron, Lamplight, Lantern Street or Larkmere appears in any other book. One overlap: the first name Sarah is used in the frozen Amity Falls book 4 for two minor characters (Sarah Voss, a past warden mentioned in chapter 3, and Sarah Kline, a third-grade teacher in chapter 40). Different series and surnames, so low risk, but Zia decided on 2026-10-18 that this does not matter (accepted). The audit only covered chapters 1 to 23 of this book; chapters 24 to 32 were not scanned.
- Clean-up done 2026-10-17: the early draft folder `novels/next-series-canon/` was deleted. Never revive it. `book_config.json` and `brief.txt` stay because the generation workflow reads them.
- The saved `story_bibles/larkmere.json` and `novels/proof-of-home/beat_map.md` are older than the scenes in `canon_scenes.py`. They are not used for chapters written by hand. Regenerate and save them only if the automated generator is ever used again.
- `content_provider.py` was changed on 2026-10-17 (commit `91c98305`) to send OpenRouter a "models" array with free fallback models. It has not been tested by a live run.

## OPEN DECISIONS (for Zia)

- Pen name: Elif Kessler, confirmed by Zia 2026-10-18. Amity Falls and Kindling Line are by other novelists; Proof of Home is a separate set of books.
- Genre label, series name "Larkmere" and the town name are working names only.
- Whether to add more books in Larkmere later. Zia said on 2026-10-18 that the next novel will be a different story with different protagonists and setup, so the default is no.
- DECIDED by Zia 2026-10-18: the first name Sarah is fine. Amity Falls and Kindling Line were written by other novelists; Proof of Home is a separate set of books by Elif Kessler, so name overlaps do not matter. Do not raise it again.
- Whether to make the helm word consistent (tiller or wheel), see KNOWN ISSUES IN FINISHED CHAPTERS.
- Whether to flip the manual gates in `book_config.json` and publish.

## To regenerate the canon files after any canon change

Run from `novels/proof-of-home-canon/`: `python3 build_canon.py` then `python3 build_bible.py`. Then save `story_bibles/larkmere.json` and `novels/proof-of-home/beat_map.md` to the repo.
