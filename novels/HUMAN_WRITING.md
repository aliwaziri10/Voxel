# Human Writing (Voxel novels only)

Applies to every Voxel Publications novel. Read it with `novels/EDITORIAL_CHARTER.md`. The charter wins on any conflict.

AI fiction gets flagged by density, not by any single habit. One em dash or one triplet is fine. Five of them on a page is the tell. So write each scene from its real point and its character's voice, then check the list below before saving.

Run `python scripts/novel_guard.py --config novels/<book>/writer_config.json --chapter <file> --n <N>` after drafting and fix every HARD finding.

## Sentence shapes to avoid

- **Negative parallelism.** "It wasn't fear, it was something older." "Not just X but Y." Say the true thing directly.
- **Triple negation.** "Not a lie. Not a truth. Something between." Never build to a reveal by knocking down two things first.
- **Rule of three.** Three adjectives, three actions or three images by reflex, and several triplets in a row. Use as many items as the moment has. Two is fine. Four is fine.
- **Self-posed questions.** "The answer? Nothing." Just give the answer.
- **Self-echo.** Reusing a striking word or image from earlier in the chapter as a callback. Repeat a phrase only when the plan lists it as an ECHO.
- **Fragment paragraphs for fake emphasis.** One-line paragraphs stacked like a poem.
- **Anaphora.** Three sentences in a row opening the same way.
- **Trailing analysis.** A sentence ending in "-ing" commentary: "...reflecting everything she had lost."
- **Comma-clipped tails.** A short phrase hung off a comma as a pseudo-punchline.
- **Quotable one-liners and forced similes** that sound wise and add nothing.
- **Scene-ending theme paragraphs.** End on the last real beat, not a line that restates the meaning.
- **Same resolution every time.** The same embrace, breath or gesture closing each scene.
- **Dialogue that explains its own subtext.** Trust the reader.

## Punctuation and format

- No em dashes or en dashes. Use a comma, a full stop or a colon. No spaced hyphen standing in for one.
- No markdown in chapter text: no headings, bold, bullets or "Scene/Part" labels. Use the book's scene break only.
- Straight quotes in, balanced double quotes out. No decorative symbols or emoji.

## Words and phrases to cut

- Hedge fillers: some, something, someone, somewhere, somehow, kind of, particular, "the specific", "the kind of". Name the feeling or thing precisely.
- Stock phrases: something shifted, let out a breath she didn't know, heart hammered, shivers down, orbs, ministrations, palpable, electric, etched, bustling, a mix of, the weight of, woven, tapestry, testament to, unwavering, seamless, intricate, delve, a dance of.
- Fancy copulas: "served as", "stood as", "marked", where "was" does the job.
- Synonym cycling: do not rename the same object three ways in a paragraph.
- Any ordinary word used eight or more times in one chapter.

## Fiction rules from past failures

- **No planning text in the prose.** No PROPOSED, UNSET, "beat map", "sub-beat", "word count", "protagonist", "Wound:", "Competence:", and no "Here is the chapter".
- **The narrator never mentions the machinery.** No "Book Two", "this series", "chapter nine", "the reader", "the author".
- **Tell time by light, weather and season.** No digits, clock times, bells as hours, month or weekday names, or arithmetic on the page. No counted spans or ages unless the chapter's FIGURES allow them.
- **Stay in point of view.** Only the POV character thinks, wonders or realizes. Keep metaphors inside that character's own trade (an engineer's chapter does not borrow a baker's comparisons).
- **Keep each voice distinct.** Do not sand every character down to one clean style.
- **Rhythm.** Mix long and short sentences unevenly, and let length and word choice shift with tension. Even sentence lengths across a chapter read as machine-made.
- **One spelling standard** per book (American unless the book says otherwise, and "gray" or "grey" consistently).
- **No padding.** A chapter with one clean beat stays short. Lengthen only by adding a real sub-beat: a relationship shift, an interior admission, a concrete stake, a callback. Never stretch existing sentences.

## Before saving a chapter

Scan the draft for: em dashes (zero), "not X but Y" lines (zero), triple negations (zero), triplets (only where the content has three), self-echoes, hedge fillers, and stock phrases. If three or more of these show up in one paragraph, rewrite that paragraph from its point instead of swapping words.
