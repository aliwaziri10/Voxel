# Proofreading upgrade - handoff (2026-10-20)

Owner: Zia. Applies to NEW books only. Published books are frozen (novels/FROZEN_DO_NOT_EDIT.md): never scan, edit or rebuild them.

## Goal (Zia)
World-standard proofreading through GitHub, fast and correct, for the American and European markets with universal appeal. Judged on his "10 parameters".

## OPEN QUESTION
No list of 10 parameters exists in any repo. Candidates: the 10 check_ functions in scripts/proofread_novel.py (ai_tells, meta_leaks, repeated_openers, overused_words, dialogue_tags, paragraph_outliers, duplicate_sentences_within, dialogue_ratio, sentence_rhythm, filename) or the 10 roles in novels/EDITORIAL_CHARTER.md. Zia must confirm or paste his list.

## Verified findings (read from live files 2026-10-20)
- Proofreading code exists only in aliwaziri10/Voxel: scripts/proofread_novel.py, scripts/manuscript_qa.py, proofreader.py, humanizer.py, scripts/word_repetition_fixer.py, scripts/continuity_extract.py, voxel_cli.py audit, .github/workflows/proofread.yml.
- Wazzaboyzz/Voxel has an older humanizer.py only. Marius, Nova, upgraded-journey, elif-kessler-books, ivy-cassel-books have no manuscript proofreading. ADAM is empty.
- Conflicting settings: proofread.yml word band 1900-2500, charter says 2300-2700. manuscript_qa.py has no block for Book 4 or Kindling books.
- proofreader.grammar_scan parses model output with json.loads (same trailing-text crash already fixed in content_provider.py).
- proofread.yml still targets Books 2 and 3, runs a daily cron, can commit auto-fixes to main.
- No tests existed for proofread_novel, manuscript_qa or proofreader.
- manuscript_qa.py INVISIBLE_CHARS has no soft hyphen (U+00AD).
- NOT fully read: scripts/proofread_novel.py body and humanizer.py body (only header and function list).

## Research basis
Chicago Manual of Style 18th ed (dialogue, numbers, hyphens, AI disclosure 4.51/4.76), KDP content-quality page (Critical / Destructive / Distracting; Critical removes a book from sale; US/UK spelling not an error), LanguageTool vs Vale vs Harper vs nabokov, ideas from whh110112/human-writing-skills and seba-cascardo/book-factory (both MIT). Amazon's quality page says nothing about AI disclosure: verify on KDP's own AI help page.

## Plan
1. DONE: scripts/proofread_core.py (read-only, deterministic, frozen-book guard, KDP tiers, one verdict) plus scripts/test_proofread_core.py.
2. NEXT: dry run proofread_core on one genuinely new, unpublished book folder (read-only). Confirm status with Zia first; novels/proof-of-home status is unknown.
3. Add LanguageTool once per book with a per-chapter hash cache. Test Harper as a fast pre-pass.
4. Add Chicago-18 checks (numbers and ages, dialogue punctuation, hyphen compounds) and a US/UK Britishism list review.
5. Add continuity ledger entries that must quote their location, plus a check that earlier fixes stay fixed.
6. Fix proofreader.grammar_scan JSON parsing. Unify word bands and frozen list across scripts.
7. Hand Zia a replacement proofread.yml as a full file (Claude cannot edit .github/workflows).

## Rules
- Do not push to novels/ for any frozen book. Auto-fix stays off by default.
- Never pad a short chapter to hit a number (charter).
- Re-fetch files from GitHub before trusting this note.

## Run
python scripts/proofread_core.py --chapters novels/<new-book>/chapters --min-words 2300 --max-words 2700
Exit codes: 0 PASS, 1 NEEDS-REVISION, 2 BLOCKED, 3 REFUSED (frozen), 4 no files.

## Status
Step 1 pushed 2026-10-20. 23 local tests passed before push. CI result not yet checked.
