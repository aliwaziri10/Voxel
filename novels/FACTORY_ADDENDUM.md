# Novel Factory: ADDENDUM after reading GENRE_DECISION.md (2026-10-22)

Read after `FACTORY_SESSION_HANDOFF.md`. This corrects parts of `FACTORY_HANDOFF.md` and `FACTORY_DECISIONS.md`. Where they disagree, this file wins until Zia overrules.

## Verified in `GENRE_DECISION.md` (updated 2026-10-16, root of the repo)
- The repo is PUBLIC. Scheduled and manual Actions runs do not use the private-repo minute limit. (Earlier open question closed.)
- KDP LIMIT: 2 new titles per format per week, reset Sunday 12:00 AM UTC (Sunday 5:30 AM IST). So publishing 32 new books takes at least 16 weeks. Plan launches one book at a time. The earlier idea of many books a day is wrong.
- Zia decided 2026-10-16: two pen names, two separate reader promises, never mixed. Ivy Cassel = romantasy (Kindling Line, 3 books live). Elif Kessler = slow-burn small-town romance (Amity Falls, 4 books, frozen). Frozen books are never edited (`novels/FROZEN_DO_NOT_EDIT.md`).
- Zia's working view then: connected standalones in a shared world, committing to later books only if Book 1 sells. Sales and read-through numbers from the KDP dashboard are NOT recorded yet and were to decide the next steps.
- Round 1 market research exists there (cozy fantasy best ratio, romance highest ceiling, catalog size correlates with income but partly survivorship, readers wary of AI books, Hachette pulled "Shy Girl"). Round 2 (live Amazon bestseller pages, ranks, page counts, hybrid test) is NOT done. This is the "study the best sellers" request.
- A pipeline state machine already exists (`novels/PIPELINE_SPEC.md`, `scripts/pipeline.py`, `scripts/book_config.py`). The genre file says: do NOT build a second system beside it; extend it with stages `genre_contract` and `story_bible` and Zia-only gates. The factory plan must follow that, so `novel_factory.py` becomes an extension of pipeline.py, not a separate system.
- Existing humanizer chain to verify and reuse: `humanizer.py` (25 KB), `test_humanizer.py`, `proofreader.py`, `PROOFREAD_RULES.md`, `novels/HUMAN_WRITING.md`, `scripts/novel_guard.py`.

## Changes to the plan
1. Pace: release at most one new title a week per format. Writing can run ahead; publishing cannot.
2. Scale: write the next book only after the previous one's sales and read-through are recorded, as Zia decided on 2026-10-16. The 20-per-pen-name target stays the long-term goal, not a batch order. Queue 3 to 4 books ahead at most.
3. Build by extending `pipeline.py` and `BOOK_CONFIG_TEMPLATE.json`, not a parallel factory.
4. Do round 2 market research before locking any new series.

## Open for Zia
- Record Kindling Line and Amity Falls per-book sales and read-through from the KDP dashboard.
- Confirm: factory writes ahead 3 to 4 books, publishing one a week, scaling only on sales.
