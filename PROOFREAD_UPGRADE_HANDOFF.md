# Proofreading upgrade - handoff (updated 2026-10-20, end of session)

Owner: Zia (browser only, no terminal). Applies to NEW books only. Frozen books (novels/FROZEN_DO_NOT_EDIT.md) are never scanned or edited. Only aliwaziri10/Voxel is used; Wazzaboyzz/Voxel is ignored for good (Zia's decision).

## Rules
The 10 rules in PROOFREAD_RULES.md are Zia's official parameters. Read EDITORIAL_CHARTER.md first, then this file. Re-read live files before trusting any note. Never pad. Auto-fix stays off. A fix goes into a chapter only after Zia approves it.

## Built and verified live
- scripts/proofread_core.py: deterministic read-only engine, tiers, one verdict, tags every finding to rules 1-10.
- scripts/languagetool_pass.py: LanguageTool en-US pass, per-chapter cache, never blocks a book (max tier DISTRACTING). Tests: 72 pass in the whole repo.
- .github/workflows/proofread-languagetool.yml: manual "Run workflow"; report appears in the run Summary. First real run on proof-of-home worked (LanguageTool 6.8): 32 chapters, 102 DISTRACTING, 8 REVIEW.
- Claude cannot edit .github/workflows (403): Zia pastes workflow files in the GitHub web editor. A one-off fix-proof-of-home-spelling.yml is still in that folder and can be deleted.
- novels/where-the-frost-doesnt-reach is complete on aliwaziri10 (HANDOFF.md, PRE_PUBLISH_CHECKLIST.md, progress.json added; frozen).

## proof-of-home (new book, 32 chapters, unpublished) - state
- proofread_core scan after fixes: no grey or fortnight left (commit 4c22095). One flag remains on purpose: ch31 line 113 "could not not" is deliberate voice. Zia said leave it.
- Zia chose to keep going with a full proofread of this book. Still to do: human read for continuity and voice (rules 7 and 8), and judging the LanguageTool list.
- LanguageTool list looks mostly noise: comma before "and" or "so", comma after "Instead", false hits on "boule", "square knot", "firm knot", "woodsmoke", "midmorning". Possible real ones to judge: ch2 "lay low", ch6 "damp", ch10 and ch16 "restraint", ch5 line 31 "it", ch3 line 39 "beside". Only 50 of 102 are listed in the report.

## Next
1. Tune languagetool_pass.py: switch off the comma rules and the "Instead" rule, add an ignore-words file for the book (boule, midmorning, woodsmoke, whitecaps, Mam), list all findings. Then rerun the workflow.
2. Walk Zia through the remaining LanguageTool findings one at a time (he wants it slow, one by one, with the whole paragraph shown). Fix only with his approval.
3. Human continuity and voice read of proof-of-home (use SECOND_ROUND_LOG.md and PROOFREAD_TRACKER.md in the book folder; do not reopen DONE chapters without a concrete issue).
4. Later: hyphen-compound checks, continuity ledger, fixed-defect regression, fix proofreader.grammar_scan JSON parsing, unify word bands (1900-2500 vs charter 2300-2700), replace proofread.yml.

## Run
python scripts/proofread_core.py --chapters novels/<new-book>/chapters --min-words 2300 --max-words 2700
python scripts/languagetool_pass.py --chapters novels/<new-book>/chapters  (needs Java; easiest through the workflow)
Exit codes: 0 PASS, 1 NEEDS-REVISION, 2 BLOCKED, 3 REFUSED (frozen), 4 no files, 5 LanguageTool unavailable.
