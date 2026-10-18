# Proof of Home: second-round proofread log

Started by Zia on 2026-10-17. The book is complete (chapters 1 to 32 live). The second round is a full read of each chapter in order, fixing every flag inside the chapter file itself, pushing, and verifying the pushed blob SHA against the local text. This log is the record of where the second round stands. The first-round tracker (`PROOFREAD_TRACKER.md`) is unchanged and still shows the first round.

Rules for this round: fix flags in the file, not just in the log. American spelling. Curly quotes only. No em dashes. No banned hedges. Point of view stays inside its own character. Baking comparisons only in Sarah's chapters, water and boat comparisons only in Jack's. A chapter never goes below 2,300 words and never gets there by padding. Never trust a stored hash: check the live blob SHA from the directory listing.

| Ch | Second round | Notes |
|---|---|---|
| 1 to 10 | DONE (Zia's record, 2026-10-18) | Spelling and quote clean-ups were pushed on 2026-10-17, for example chapter 10 commit `1476ff98` |
| 11 | DONE | Rewritten by an earlier session (commit `54daf935`). Then fixed here: removed the invented thumb-on-cheek line (his thumb never touched her), grey spelling. Commit `f36004a49c7487f8b3e603909808cd59c7c1bfe8`, blob `5cb6a91b`, 2386 words |
| 12 | DONE | American spelling (fiber), cut repeated basket and rain, removed a contradictory line (he said nothing, right after he spoke). Commit `b73fdb5ed416670a27d3f002d36cf40c4a8cf822`, blob `1de7c3b5`, 2309 words |
| 13 | DONE | Rewritten to the beat map: she fixes his collar at the landing while he talks to a fisherman. Removed the tiller in his hand on shore, the invented cheek touch, a banned phrase and heavy repetition. Commit `a4ed70fa21db5f9754a04820450a9dbba4d308bc`, blob `8617e9dd`, 2336 words |
| 14 | DONE | Rewritten to the beat map: one hand on the tiller while the other holds her, the held moment broken by a gust and not by Nell, loaf crushed between them, passenger business cut from three repeats to one. Commit `349b31750400af8721ebe6da4b2751fc39117570`, blob `1d92323b`, 2316 words |
| 15 | DONE | Done by an earlier session, see the git history of `chapter_15.md` |
| 16 | DONE | Read in full. Only change: grey spelling (one "gray"). Commit `dea656269a4f9343019dbe95d191f05d1e2aafc2`, blob `6413092c`, 2330 words |
| 17 | DONE | Read in full in this session, mechanical scan clean, no change needed. Blob `4821b034` series, 2352 words |
| 18 | DONE | Read in full; earlier fix this session (baking comparison removed from Jack's point of view, repeated word) is live, commit `5c6697d5`, 2336 words |
| 19 | DONE | Read in full. Clean, no change needed. 2451 words |
| 20 | DONE | Read in full. Clean, no change needed. 2325 words |
| 21 | DONE | Read in full this session before pushing it. Clean. 2369 words, blob `67acfbea` |
| 22 | DONE | Read in full this session before pushing it. Clean. 2355 words, blob `7f676806` |
| 23 | DONE | Read in full. Clean, no change needed. 2350 words |
| 24 | DONE | Read in full. Clean, no change needed. 2504 words |
| 25 | DONE | Read in full. Clean. The line about Odalys circling the word "birthday" looks stray but is a deliberate plant for chapter 26, leave it. 2595 words |
| 26 | DONE | Read in full. Clean, no change needed. 2428 words |
| 27 to 32 | NOT DONE | Next: chapter 27 |

All of chapters 17 to 32 pass the mechanical scan (no em dashes, no straight quotes, no British spellings, no banned hedges, no digits).

## Open items found during this round (not yet fixed)

- Helm term is mixed across the book. Chapters 2, 4, 6, 13, 14 and 20 say tiller (chapter 2 also says wheel once), chapters 10, 11, 16, 18, 22 to 25, 27, 28, 30 and 32 say wheel. Decide one term for the Heron and make it consistent. Both can stand if the Heron has a wheel in the wheelhouse and a tiller used in the open, but the book never says so.
- Chapters 5 and 6, 9, 10: Jack sleeps in the ferry cabin bunk, chapter 16 gives him a cottage at the end of the water road. Already listed in the HANDOFF known issues.
- Chapter 5: banned phrase "a kind of trap", and Sarah's point of view slip about Jack never asking anyone to remain. Not yet touched in this round; if Zia's record for chapters 1 to 10 is wrong, check first.
- Chapter 1 and chapter 9: straight quotes. Check they were cleaned in the chapters 1 to 10 pass before trusting the HANDOFF note.
- Fenna's years of baking: chapter 19 says "Sixty years of bread", earlier sessions said fifty. Check chapters 16, 25 and 30 and pick one.
