# Proofreading upgrade - handoff (updated 2026-10-20)

Owner: Zia. Applies to NEW books only. Published books are frozen (novels/FROZEN_DO_NOT_EDIT.md): never scan, edit or rebuild them.

## Goal (Zia)
World-standard proofreading through GitHub, fast and correct, American first then European, universal appeal.

## Decision
Zia adopted the 10 rules in PROOFREAD_RULES.md as his official parameters on 2026-10-20 ("use all those things"). The earlier question about where his "10 parameters" were is closed: no list existed in any repo, so these replace it.

## Verified findings (read from live files 2026-10-20)
- Proofreading code exists only in aliwaziri10/Voxel: scripts/proofread_novel.py, scripts/manuscript_qa.py, proofreader.py, humanizer.py, scripts/word_repetition_fixer.py, scripts/continuity_extract.py, voxel_cli.py audit, .github/workflows/proofread.yml.
- Wazzaboyzz/Voxel has an older humanizer.py only. Marius, Nova, upgraded-journey, elif-kessler-books, ivy-cassel-books have no manuscript proofreading. ADAM is empty.
- Conflicting settings: proofread.yml word band 1900-2500, charter says 2300-2700. manuscript_qa.py has no block for Book 4 or Kindling books.
- proofreader.grammar_scan parses model output with json.loads (same trailing-text crash already fixed in content_provider.py).
- proofread.yml still targets Books 2 and 3, runs a daily cron, can commit auto-fixes to main.
- manuscript_qa.py INVISIBLE_CHARS has no soft hyphen (U+00AD).
- NOT fully read: scripts/proofread_novel.py body and humanizer.py body (only header and function list).

## Research basis
Chicago Manual of Style 18th ed, KDP content-quality page (Critical / Destructive / Distracting; Critical removes a book from sale; US/UK spelling not an error), LanguageTool vs Vale vs Harper vs nabokov, ideas from whh110112/human-writing-skills and seba-cascardo/book-factory (both MIT). Amazon's quality page says nothing about AI disclosure: verify on KDP's own AI help page.

## Status
- DONE: scripts/proofread_core.py (read-only, deterministic, frozen guard, tiers, verdict, every check tagged to rules 1-10) plus scripts/test_proofread_core.py (28 tests passed locally).
- DONE: PROOFREAD_RULES.md in both repos.
- NOT CHECKED: GitHub Actions result for the push commits.
- NOT DONE: any real book scanned. novels/proof-of-home status (published or not) unknown; ask Zia before scanning.

## Next
1. Run proofread_core read-only on one confirmed-unpublished book.
2. LanguageTool once per book with per-chapter hash cache. Test Harper as a fast pre-pass.
3. Hyphen-compound checks (Chicago 18) and Britishism list review.
4. Continuity ledger (flags must quote location) plus fixed-defect regression.
5. Fix proofreader.grammar_scan JSON parsing. Unify word bands and frozen list across scripts.
6. Hand Zia a replacement proofread.yml as a full file (Claude cannot edit .github/workflows).

## Rules
- Do not push to novels/ for any frozen book. Auto-fix stays off by default.
- Never pad a short chapter to hit a number (charter).
- Re-fetch files from GitHub before trusting this note.

## Run
python scripts/proofread_core.py --chapters novels/<new-book>/chapters --min-words 2300 --max-words 2700
Exit codes: 0 PASS, 1 NEEDS-REVISION, 2 BLOCKED, 3 REFUSED (frozen), 4 no files.
