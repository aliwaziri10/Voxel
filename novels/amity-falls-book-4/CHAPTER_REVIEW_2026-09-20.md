# Book 4 chapter review - 2026-09-20 (branch book4-progress-saving)

Chapters on this branch: 1, 2, 3, 4, 5, 7, 9, 11, 12 (6, 8, 10 are absent).
Checked with humanizer.scan, proofread_novel.py (auto-fix off, on a copy),
word_repetition_fixer (on a copy), manuscript_qa, and grep for leaks.

## Status per chapter

| Ch | Words | Em dashes | Humanizer | Verdict |
|----|-------|-----------|-----------|---------|
| 1 | 2,309 | 0 | 20 | DONE (proofread and fixed 2026-09-20) |
| 2 | 2,935 | 17 | 32 | Rewrite: leaked bible line (Wren writes "Wound: grandmother's missing decade. Competence: high."), "particular", "the kind of" |
| 3 | 3,632 | 38 | 100 | Rewrite: over length, leak ("Since Book 3." said in dialogue) |
| 4 | 2,580 | 19 | 20 | Proofread only (cleanest chapter) |
| 5 | 4,508 | 27 | 24 | Rewrite: over length; characters say "Book 3", "Book 1 protagonist" aloud |
| 7 | 2,158 | 27 | 100 | Proofread + real content to reach 2,300 |
| 9 | 3,799 | 55 | 100 | Rewrite: bible text read out as dialogue ("No persuasion arc needed... Book 2 he hesitated"); "Yusef" misspelled |
| 11 | 2,517 | 30 | 100 | Rewrite: the bible entry is pasted into the prose ("Book 4: his procedural evidence work...") |
| 12 | 5,654 | 53 | 100 | Rewrite/split: over length by double; says "Before Book 3"; invents 2019 Drake meeting that contradicts the bible |

## Root cause (fix this BEFORE regenerating anything)

The story bible fields are written as author notes ("Book 4: ...",
"No persuasion arc needed", "Book 1 protagonist") and are injected into the
chapter prompt. The model copies them into the prose. `proofread_novel.py`
already flags these as `meta_leaks_VIOLATION`, but `voxel_cli.py novel` saves
the chapter anyway.

Fix in three parts:
1. Rewrite `story_bibles/amity-falls.json` entries as neutral in-world facts
   (no "Book N", no notes to the author, no "arc" language).
2. Add one rule to the chapter prompt: never mention "Book 1-4", "chapter"
   of this novel, "the series", or anything about the author's plan.
3. Extend the existing broken-chapter guard in `voxel_cli.py` to also reject
   and regenerate a chapter that trips the meta-leak check, instead of saving
   it. (Read the current `voxel_cli.py` first; it changed on 2026-09-19.)

## Run problems seen in the workflow log (2026-09-20)

- Resume works: chapters 1-5 already existed and were kept, so the edited
  chapter 1 is safe from overwrite.
- OpenRouter free tier hit its 50 requests per day limit on chapter 6. The
  limit resets 2026-09-21 00:00 UTC (05:30 IST). Adding OpenRouter credit is
  Zia's decision.
- The workflow's own commit was rejected (`fetch first`) because this branch
  had a newer commit. The workflow needs `git pull --rebase` before `git
  push`. Workflow files must be pasted by Zia; give the full file.

## Open canon items from chapter 1

1. Wren's mother is alive in Book 1 and lives in the valley. Chapter 1's
   mother and grandmother backstory does not contradict this, but the
   grandmother and father details are unverified. Confirm or trim.
2. Denise is alive and warm at Book 3's end. Chapter 1 leaves her chair
   empty without saying why. Zia to choose a reason (proposed: she stepped
   back from the council after the ring; add one line to chapter 1).
3. The bible gives Theo a wound (his grandmother's missing decade). Chapter 1
   gives him an index gap. Chapter 2 and 3 already mention the grandmother,
   so they cover it; keep chapter 1 as is.
