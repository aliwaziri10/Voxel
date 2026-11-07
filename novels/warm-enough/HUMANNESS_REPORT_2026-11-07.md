# Warm Enough: within-book comparison (2026-11-07, Claude chat for Zia)

READ-ONLY analysis. No chapter text was changed. Script: `scripts/within_book_compare.py` (commit 1c254cdcd9f5497be7b6b30337afda414c55c3fe). Re-run it before trusting any number here; chapters may have changed since.

## What was asked, and the decision
Zia asked for a modern comparison and NOT the 1906 to 1927 novels. There is no legal modern human fiction to use (copyright lasts about 95 years; free books stop near 1930, and downloading modern novels would be piracy). So the only modern human sample is Zia's hand-written chapters 1 to 6, and the only fair question is: do the other 34 chapters differ from those six by more than chance? This does NOT say "AI" or "human" and it is not a target to edit towards. Do not use the 1920s reference set (`scripts/humanness_bench.py`) as a headline measure of this book.

## A first attempt was wrong (kept here so nobody repeats it)
- It used Gemma's rejected drafts as "machine" examples. They were rejected for being broken (one runs about 11,800 words; the rest are short fragments with 6 to 10 word sentences against the book's 14.6), and several share the same brief. That says nothing about machine prose. Discarded.
- It counted chapters "outside the hand-written range". With six chapters, about 29 percent of new chapters from the same author fall outside that range by chance (about 10 of 34). Not evidence.

## Result (6 hand-written chapters vs 34 others; permutation test, 7 measures, Bonferroni threshold p < 0.0071)
| measure | hand-written | others | verdict |
|---|---|---|---|
| mean sentence length | 14.8 | 14.6 | no difference |
| sentence-length spread (CV) | 0.81 | 0.91 | differs beyond chance |
| sentences opening he/she/they | 28% | 35% | differs beyond chance |
| runs of 3+ same first word, per 1,000 words | 1.1 | 2.8 | differs beyond chance |
| lexical diversity (MATTR-500) | 0.449 | 0.434 | maybe (p about 0.02, not past the strict threshold) |
| very short sentences (5 words or fewer) | 26% | 30% | no clear difference |
| "It was not X. It was Y." per 1,000 words | 0.00 | 0.21 | no clear difference (p about 0.14) |

Confound checks inside the 34 others: early vs late chapters do not differ on any measure; Ansel (odd) vs Hester (even) chapters differ only on runs of repeated first words (Hester's higher, p about 0.02). So the gaps are not explained by point of view or by position in the book.

## What this does and does not mean
- The other chapters repeat sentence openings more, open more sentences with a pronoun, and vary sentence length more than the hand-written ones. That is a real difference between the two sets.
- It does NOT prove who wrote what, and it does NOT show the other chapters are worse. Only six chapters; ch2 and ch3 had beats added by Claude on 2026-10-28 (so "hand-written" is not pure); the measures are simple and mine, not validated detectors; two sets may also differ because of the scenes they contain.
- The one sensible use: when doing the human read, look at runs of repeated sentence openings, and edit a run only when it reads badly, never to move a number. This matches the frozen humanizer spec (B13, C5, C6), which forbids editing for pronoun openings alone.
- The KDP AI-disclosure question is unaffected by any of this and is still open.
