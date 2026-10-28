# Warm Enough: humanizer pass method (2026-10-28, v2)

Every profile runs the SAME check. Do not retype the method; run the script.

## Command (repo root)
- One chapter: `python scripts/humanizer_pass.py novels/warm-enough/chapters/chapter_NN.md --n NN`
- Whole book table: `python scripts/humanizer_pass.py --book warm-enough`
- Tool self-check: `python scripts/humanizer_pass.py --selftest`
- It only reads. First run downloads a human baseline (4 MB) and caches it.

## Score
- HUMAN SCORE 0 to 100, higher is more human-like. `humanizer.py` score is the opposite (lower is cleaner). Both are printed.
- Weights (max points lost): repo scan 14, pronoun openings 14, stock fiction gestures 10, stated feeling or theme 8, same-opening runs 8, tic phrases 7, short sentences 6, sentence-length variation 6, negative parallelism 6, dialogue share 5, simile frames 4, vocabulary variety 3, repeated 4-word phrases 3, zinger paragraph endings 3, blocklist names 3.
- Baseline measures cost points only outside the human 10th to 90th percentile band (nine public-domain novels, 2,300-word windows, same windows as the first version so stamped numbers stay comparable).
- Sources: Wikipedia "Signs of AI writing", StoryScope (arXiv 2604.03136), stylometry papers, public AI-name lists.
- Checked 2026-10-28: stock AI sample scores 14.6, held-out human novel windows median 84.1 (min 69.9, max 89.0), ch01 73.3 before its edit and 77.3 after.
- Book baseline on 2026-10-28: mean 59.7, repo scan mean 21.3, lowest ch10, ch20, ch11, ch30, ch21.

## Per chapter, strict order
1. Run the script. Read the FIX LIST.
2. Edit the listed sentences for voice first. No canon change, locked endings kept, no dashes, no digits.
3. Re-run. Run `write_warm_enough.py --check`.
4. Push, confirm the live blob SHA matches.
5. One-line stamp in `PROOFREAD_TRACKER.md`: chapter, commit, HUMAN SCORE before to after, repo scan before to after, pronoun-opening rate.
6. Do not tick DONE. DONE still needs the separate 10-point continuity check.

## Honest limits
- No tool proves human authorship. Answer the KDP AI-content question truthfully.
- Baseline is 19th-century prose, so sentence length is not scored. Pronoun openings stay high until the whole book is worked.
- Zinger endings, tic phrases and stock-gesture lists are heuristics, not calibrated on Voxel books.
- 'The way ...' frames are shown but not scored: no source found that supports them as an AI tell.
- The name blocklist is partial (Elara, Elena, Elias, Aris, Kael, Voss, Vex, Vance, Thorne, Erebus, Eldora, Whispering).
