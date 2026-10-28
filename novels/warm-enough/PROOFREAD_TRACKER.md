# Warm Enough: chapter tracker

A chapter is DONE only when written, checked on the 10 points in `novels/proof-of-home/PROOFREAD_TRACKER.md` (same points, with Ansel odd and Hester even, grey spelling, no kiss before chapter 33, Tilda and Gran never in an intimate beat), pushed, and confirmed live. Read `novels/warm-enough/HANDOFF.md` and `VOICE_GUIDE.md` first. Write in strict order. Record real word count and commit hash.

No chapters written yet (2026-10-22). Plan is 40 chapters (revision 2).

All 40 chapters exist as of 2026-10-28. The DONE column below stays open until each chapter also passes the 10-point check. The humanizer pass is a separate stamp, logged under the table.

| Ch | POV | Touch | DONE | Notes |
|---|---|---|---|---|
| 1 | Ansel | 0 | ⬜ | Humanizer pass stamped 2026-10-28 (HUMANIZER-PASS-A, see log below). 10-point check still open. |
| 2 | Hester | 0 | ⬜ |  |
| 3 | Ansel | 1 | ⬜ |  |
| 4 | Hester | 2 | ⬜ |  |
| 5 | Ansel | 0 | ⬜ |  |
| 6 | Hester | 1 | ⬜ |  |
| 7 | Ansel | 1 | ⬜ |  |
| 8 | Hester | 3 | ⬜ |  |
| 9 | Ansel | 3 | ⬜ |  |
| 10 | Hester | 2 | ⬜ |  |
| 11 | Ansel | 2 | ⬜ |  |
| 12 | Hester | 4 | ⬜ |  |
| 13 | Ansel | 3 | ⬜ |  |
| 14 | Hester | 4 | ⬜ |  |
| 15 | Ansel | 1 | ⬜ |  |
| 16 | Hester | 2 | ⬜ |  |
| 17 | Ansel | 2 | ⬜ |  |
| 18 | Hester | 2 | ⬜ |  |
| 19 | Ansel | 4 | ⬜ |  |
| 20 | Hester | 3 | ⬜ |  |
| 21 | Ansel | 4 | ⬜ |  |
| 22 | Hester | 4 | ⬜ |  |
| 23 | Ansel | 3 | ⬜ |  |
| 24 | Hester | 3 | ⬜ |  |
| 25 | Ansel | 5 | ⬜ |  |
| 26 | Hester | 6 | ⬜ |  |
| 27 | Ansel | 2 | ⬜ |  |
| 28 | Hester | 5 | ⬜ |  |
| 29 | Ansel | 4 | ⬜ |  |
| 30 | Hester | 3 | ⬜ |  |
| 31 | Ansel | 7 | ⬜ |  |
| 32 | Hester | 8 | ⬜ |  |
| 33 | Ansel | 9 | ⬜ | First kiss |
| 34 | Hester | 10 | ⬜ |  |
| 35 | Ansel | 10 | ⬜ |  |
| 36 | Hester | 10 | ⬜ |  |
| 37 | Ansel | 10 | ⬜ |  |
| 38 | Hester | 10 | ⬜ |  |
| 39 | Ansel | 10 | ⬜ |  |
| 40 | Hester | 10 | ⬜ | Release, "Stay." |

## Humanizer pass log (strict chapter order, 2026-10-28 onward)

Standards used for this pass, from several independent sources, not one: (1) Wikipedia "Signs of AI writing" and its talk-page analysis; (2) the repo's own `humanizer.py` (`scan` and `scan_narrative`); (3) academic stylometric detector research (sentence-length variation, vocabulary diversity, sentence openings, repeated phrases), measured against a human baseline of nine public-domain novels in 2,300-word windows (`metrics.py` method, baseline is 19th-century prose so gaps are read with care); (4) community blocklists of overused AI character and place names; (5) `novels/HUMAN_WRITING.md` and the Editorial Charter. No tool can certify a text as human written. Detector tools give probabilities only. The KDP AI-generated-content question must still be answered truthfully in the dashboard.

### HUMANIZER-PASS-A, chapter 1, 2026-10-28 (stamped)
- Read in full, paragraph by paragraph, against Ansel's voice and brief 01. No canon change. Locked ending kept (Hester's mouth thinning, first lantern behind her).
- Edits (5, all in the file, commit `8c58123bf4436e147ee97814b7ff6dc24a4b59b4`): two runs of three sentences opening "He" varied (paragraphs 4 and 28); "It came... It entered" and "He felt it... He felt it" merged (paragraph 9); one "He tried" opening restructured (paragraph 26).
- Live file blob `be3dd408584c58b2ccc8e41da18ece7445133534` (matches the tested local copy byte for byte). 2,307 words (floor 2,300).
- `write_warm_enough.py --check`: HARD none, SOFT none. Em and en dashes 0. Digits 0. Banned words and hedges none.
- `humanizer.scan` score 20 to 16 (tricolon 1, repeated openings 4 to 3). `scan_narrative`: no flags.
- Same-opening runs (3+) per 1,000 words 1.29 to 0.87 (human median 0.43). Sentence-length variation 0.73 (human range 0.58 to 0.93, in range). Sentences opening with he/she/they/her/his 38% to 34% (human median 10%, still high).
- Character and place names on the AI-name blocklists: none.
- STILL OPEN for chapter 1: pronoun-opening rate remains above the human range (book-wide pattern, to be worked down across all chapters, not in one chapter); the 10-point continuity check; the external-detector caveat above.
