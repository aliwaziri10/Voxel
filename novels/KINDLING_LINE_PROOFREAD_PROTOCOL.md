# KINDLING LINE PROOFREAD PROTOCOL (Books 1, 2, 3)

v1, written 2026-10-07 at Zia's request. Applies to every session and every profile that proofreads Kindling Line. Read this file, then `novels/KINDLING_LINE_PROOFED_LOG.md`, before opening any chapter. Authority: this file governs proofreading. `novels/EDITORIAL_CHARTER.md`, `novels/kindling-line-book-3/READER_FIX_LIST.md` and each book's `CANON_LOCK.md` stay in force; where they differ on proofreading, this file wins.

Sources this protocol was built from: the repo's EDITORIAL_CHARTER.md (what to check every pass; what NOT to do), READER_FIX_LIST.md (what a reader feels vs what only a checker finds), the Amity Falls Book 4 AI-tell checklist (read only, as a reference list; Amity Falls is never edited), Book 3 CANON_LOCK.md and WRITER_COMMAND.md (banned words, locked facts), and the real damage found live on 2026-10-07 (see section 8).

## 1. SCOPE: FIX ONLY WHAT A READER WOULD FEEL
This is a normal proofread, not a rewrite. Do not overcorrect.
- Fix: a block of text pasted twice, plan or outline text leaked into the prose ("Ch.31 you forget in panic"), a fact that contradicts another chapter or book, a premature reveal that breaks the beat map, a broken sentence, a typo, an AI tell a reader would notice, a stray `---` glued to a sentence.
- Do NOT fix: chapter length (a clean 5,900-word chapter stays 5,900), anything the READER_FIX_LIST marks group C (bell numbers, hold counts, awning days, sigil colours, Kael's title variants, and the other items listed there), a sentence that is merely plain, a character's distinct voice.
- Do NOT mechanically delete a flagged word. Read it in context. "Something" in a precise sentence is fine; "something in her chest loosened" is the tell.
- Do NOT sand every character down to one clean style. Voices must stay distinct.
- Do NOT pad. Do NOT trim for length. Do NOT rewrite a paragraph on a hunch.
- A fix is the smallest edit that removes the problem. If the problem needs a real rewrite of a scene (for example a chapter with its second half missing), FLAG it for Zia (section 5) instead of rewriting silently.

## 2. ORDER OF WORK
Strict order: Book 1 chapters 1 to 45, then Book 2 chapters 1 to 45, then Book 3 chapters 1 to 45. Within a book, strictly in chapter order, no skipping, no jumping to the worst chapters first. Reason: continuity is learned in story order, and a Book 3 fact can only be judged against what Books 1 and 2 actually say. While reading, add every locked fact (names, ages, years, who knows what and when, the cost rule, deaths, places) to the LOCKED FACTS section of the log, with chapter citation, so the next session does not re-derive it.

Paths:
```
novels/kindling-line-book-1/chapters/chapter_NN.md
```
```
novels/kindling-line-book-2/chapters/chapter_NN.md
```
```
novels/kindling-line-book-3/chapters/chapter_NN.md
```

## 3. THE SEVEN PARAMETERS (run all seven on every chapter, in one full read)

### P1. Lexical (word choice)
- Banned: em dashes and en dashes (zero allowed in prose), "particular", the month name Frostveil, "aye", and any word CANON_LOCK.md or WRITER_COMMAND.md bans for that book.
- AI vocabulary: tapestry, testament to, underscore(s), delve, navigate (figurative), landscape (figurative), myriad, unwavering, poignant, resonate, robust, seamless, boasts, elevate, harness, and hedge openers ("it is worth noting", "in many ways", "at its core").
- Vague hedges standing in for a named feeling: "some/something/someone/somewhere ___". Count per chapter; fix the ones that dodge a precise image.
- "the kind of ___", "the specific ___", "exactly the kind of".
- Overused ordinary words: 8 or more repeats of one ordinary word in a chapter is a real problem even if the word is not banned.
- Invented names: any capitalised name not in the canon records or earlier chapters. Dead or absent people stay unnamed in Book 3 (see WRITER_COMMAND.md).

### P2. Grammar and mechanics
- Spelling, doubled words, doubled punctuation (`..`, `,,`, `.,`), unclosed quotation marks, a quote that starts but never ends, tense slips inside a scene, pronoun with no clear owner, subject-verb disagreement, run-ons that are not deliberate.
- Section break hygiene: a `---` break must sit on its own line with a blank line either side. A `---` glued to the end of a sentence is a defect.
- Chapter header comment `<!-- chapter_date: Day N -->` must be present and untouched.
- Do not change dialogue dialect or deliberate fragments.

### P3. Syntax and rhythm
- Repeated pivot construction: "Not X. Y." / "not X, but Y" used as a default shape. Fine once or twice a chapter; a tell when it recurs.
- Tricolon crutch: "X. Y. Z." three-beat fragments used as a rhythm default.
- Present-participle openers ("Turning to face him," "Standing there,") as the default transition.
- Clause-stacked sentence openings, reflexive trailing qualifiers, suspiciously uniform paragraph lengths, and sentence lengths that never vary.
- Real prose clusters unevenly. Fix only where the sameness is something a reader would hear.

### P4. Structure and scene
- Duplicated blocks: a paragraph or whole scene present twice (the 2026-10-07 chapter 3 defect). Check by comparing every long paragraph against the rest of the chapter and against the neighbouring chapters' endings and openings.
- Leaked planning text: chapter numbers ("Ch.8", "Ch.43"), "Day 29" style bookkeeping spoken as dialogue, beat-map or canon-file wording, instructions, bracket notes, markdown headings inside prose.
- Seams: the chapter begins and ends cleanly; the last paragraph of chapter N does not repeat the first of N+1.
- Premature reveals: a secret the beat map says lands in a later chapter must not appear early. Check against BEAT_MAP and CANON_LOCK "Locked" lines.
- Repeated identical beat resolutions (same gesture, same embrace, every chapter), dialogue that explains its own subtext, scene endings that restate the theme. Also watch recurring closers such as "held its breath".
- A scene that stops mid-sentence or a chapter whose second half is missing is a DAMAGE finding (section 5).

### P5. Voice and POV
- Each POV character keeps a distinct voice. Do not leak one character's metaphor domain or habits into the other's narration.
- No POV break inside a scene unless the book already does that deliberately.
- Same bodily-sensation shorthand for emotion ("something in her chest loosened", "the knot eased") reused across different characters flattens voice. Vary or cut.
- Dialogue sounds like the speaker, not like a summary of the plot.

### P6. Continuity (cross-book canon)
- Check each fact against the LOCKED FACTS section of the log and the book's CANON_LOCK.md, never against memory of what "should" be true.
- Names, ages, years, relationships, who knows what and when, the cost rule, physical details, places, objects (the pegs, the plates, the line), day counts in Book 3 (the custodian's order is dated Day 0, served Day 16).
- Where two books disagree and a reader would feel it, do not choose silently. Use section 5.
- Open known items (from READER_FIX_LIST.md, group A and B) are tracked in the log.

### P7. Pacing, emotion and human register
- Emotional register shifts with tension: a chase does not sit at the same simmering pitch as a quiet kitchen scene.
- Conflicts should not resolve completely in one scene through a clean vow exchange every time.
- Chapter-ending thematic one-liners: acceptable occasionally, a tell when nearly every chapter ends on one.
- The romance scenes carry weight (the repo's romance-first rule): a gesture is not a scene. Do not cut romance beats while proofreading.
- Overall test: would an ordinary reader think a person wrote this? If a passage reads like a summary of itself, fix that passage only.

## 4. HOW TO PROOFREAD ONE CHAPTER (the exact sequence)
1. Claim it in the log (section 6) before reading. If someone else holds the claim and it is under 3 hours old, take the next chapter in order.
2. Fetch the live chapter from `main` (GitHub file read, not a remembered copy). Note its blob SHA. Raw CDN copies can be stale right after a push; use the GitHub file read when in doubt.
3. Read the WHOLE chapter once, start to finish, before changing anything.
4. Run P1 to P7. Quote the live text for every finding. Mechanical greps (dashes, banned words, doubled punctuation, repeated paragraphs) are a map, not a substitute for reading.
5. Classify each finding: FIX (safe, small), FLAG (needs Zia), or IGNORE (group C or only a checker would find it).
6. Apply FIX items as targeted edits on that chapter file. Never use force or the writer workflow to re-generate a chapter during proofreading.
7. Re-read the file live after the push to confirm the edit landed and nothing else changed. Note the new blob SHA and commit SHA.
8. Write the stamp (section 6). One chapter, finish it, stamp it, then move on.

## 5. FLAG PROCEDURE (Zia decides, you do not)
Flag, do not fix, when: two versions of a fact are both plausible and the choice changes the story, a scene is damaged and needs rewriting, a reveal must move chapters, or a published book would change. Log the flag with chapter, the exact quoted lines, the two options, and a one-line recommendation. Status FLAGGED. A flagged chapter is not STAMPED until Zia answers and the fix is applied. Do not stop the whole pass: continue with the next chapter.

Known flagged items waiting for Zia (from READER_FIX_LIST.md group A): the ward's death told several ways in Book 1; Sol's mother's name and ward and Kael's father's status varying in Book 1; Auda Ashworth appearing from nowhere in Book 2 ch.44 to 45; Kael's father stripped and exiled (Book 1 ch.44) vs buried (Book 2). Group B cheap fixes are applied during the pass in a single small edit each, and logged.

## 6. THE STAMP (so no other profile repeats the work)
All stamps live in one file, append only:
```
novels/KINDLING_LINE_PROOFED_LOG.md
```
Stamp line format (one line per chapter, written immediately after finishing that chapter, never batched):

`B<book>-ch<NN> | <STATUS> | <YYYY-MM-DD> | <session or profile name> | blob <sha at stamp time> | fixes: <commit sha(s) or none> | checks: P1-P7 | notes: <flags, open items>`

Status values:
- STAMPED-CLEAN: read in full, all seven checks run, nothing needed fixing.
- STAMPED-FIXED: read in full, all seven checks run, fixes pushed and re-read live.
- FLAGGED: read in full, needs Zia's decision; not complete.
- SKIPPED: not read (give the reason). Never counts as proofread.

Rules:
- Never stamp a chapter you did not read in full in the same session. A pasted summary, an earlier session's claim or a script report is not a read.
- A stamp is valid only while the chapter file's blob SHA still equals the stamped blob SHA. If the file has changed since (by the writer workflow, a force run, or anyone), the stamp is void and the chapter goes back to the queue.
- Do not re-read or re-verify a stamped chapter with a matching blob SHA. If you find a new real problem in a stamped chapter while reading a neighbour, log it as a new finding under that chapter and fix it, then add a new stamp line that supersedes the old one.
- Claim line format at the top of the log while working: `LOCK B<book> ch<X>-<Y> | <session> | <YYYY-MM-DD HH:MM UTC>`. Remove the lock line when the batch is stamped. A lock older than 3 hours is stale.
- Update the COVERAGE lines at the top of the log after each stamp (next unstamped chapter per book).
- Do not touch Amity Falks or any other series from this protocol. Amity Falls is published and closed. Reading it for reference is allowed; editing it is never allowed.

## 7. SESSION START AND END
Start: read this file, read the log (COVERAGE, LOCKED FACTS, open FLAGS), then list the live chapters folder for the book in progress and confirm the next unstamped chapter exists and its blob SHA is not already stamped. Do not trust any summary, including this one, for the current state of the repo.
End: update COVERAGE, release locks, and make sure every chapter you touched has a stamp line. If you run out of context mid-chapter, do not stamp it; release the lock and say where you stopped.

## 8. DAMAGE FOUND LIVE ON 2026-10-07 (starting condition)
- Book 3 chapter 3 on GitHub: the scene beginning "Sol stood in the doorway of Ansa's room" appears twice, plan text ("Ch.1 you asked. Ch.8 ... Ch.31 ... Ch.43") is spoken in dialogue, a `---` is glued to the end of the previous paragraph, and the works steward's reveal is made far too early. An earlier session's sandbox cleanup was never pushed, so none of that was fixed.
- An earlier session's report listed chapters 3, 4, 6, 10, 11, 15, 16 and 38 as having removable copied text. Treat that list as unverified leads, not facts. Verify each live when you reach it.
- Book 3 batch notes from 2026-10-06 (chapter 10 at about 5,900 words, chapter 8 with a paragraph pasted twice) are leads too. Length is not a defect; the pasted paragraph is.
