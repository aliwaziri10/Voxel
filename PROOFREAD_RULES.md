# The 10 proofreading rules (adopted by Zia, 2026-10-20)

Apply to NEW books only. Frozen books (novels/FROZEN_DO_NOT_EDIT.md) are never touched. Market: American first, European second, universal appeal. Sources: EDITORIAL_CHARTER.md, Amazon KDP content-quality tiers, Chicago Manual of Style 18th edition.

Mode: auto = scripts/proofread_core.py does it. partial = script covers part. human = needs a read.

1. **Published books are never touched.** Checks only read and report. A fix goes into a chapter file only after Zia approves it. (auto: frozen-book guard)
2. **Every finding gets a severity.** Critical, Destructive, Distracting (plus Review for human judgment). Any Critical blocks release. (auto)
3. **Clean characters and markup first.** Soft hyphens, zero-width characters, digits inside words, leaked tags or placeholders, in-line page numbers, empty or corrupted files. (auto)
4. **One American English standard per book.** US spelling, Britishisms flagged for review, a/an. Dialect in dialogue is not an error. No region-locked slang. (partial)
5. **Punctuation and dialogue follow Chicago 18.** Balanced quotes, comma before a tag, lowercase tag after a comma, one ellipsis style, no dash stand-ins (house rule), spacing, spelled-out numbers. (partial; hyphen compounds not built yet)
6. **Repetition is counted, then judged in context.** Doubled words by script. Overused words, filler hedges and AI tells are counted by the older scripts and judged by a person. Never mass-delete. (partial)
7. **Continuity is checked against the fact record, in chapter order.** Names, ages, dates, timelines. Each flag quotes its location. (human)
8. **Voice and rhythm are checked per character.** Sentence-length variety, each character's own voice, tone that shifts with tension. (human; scripts may supply numbers)
9. **Never pad.** Word floor is a review flag only. A short chapter stays short unless a real scene is missing. (auto: review flag only)
10. **Every pass leaves proof.** One verdict per book, a dated stamp per chapter, full re-scan after every edit, earlier fixes re-checked, files re-read live from GitHub before trusting any note. (partial: verdict done; stamps, re-scan, regression not built)

## Considered and dropped
Readability score (Flesch/ARI) as a pass/fail gate. Fiction varies by scene and suitability for novels is unconfirmed. May be added as an advisory number only.

## Not built yet
LanguageTool grammar pass with per-chapter cache. Hyphen-compound checks. Continuity ledger. Fixed-defect regression. Replacement proofread.yml (must be pasted by Zia; Claude cannot edit workflows).
