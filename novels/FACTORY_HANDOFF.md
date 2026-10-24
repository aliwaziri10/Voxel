# Novel Factory: HANDOFF (50+ novels, same method as Warm Enough)

Written 2026-10-22, corrected 2026-10-24. Read `novels/EDITORIAL_CHARTER.md` first. Repo: `aliwaziri10/Voxel` (not Wazzaboyzz). Zia is browser-only.

## Request (Zia, 2026-10-22)
GitHub must do, for at least 50 novels (3 or 4 per series), everything done by hand for Warm Enough, without missing a point. Free tier only.

## Verified live (CONFIRMED; corrected 2026-10-24)
- Warm Enough has: HANDOFF.md, WRITER_COMMAND.md, VOICE_GUIDE.md, book_config.json, PROOFREAD_TRACKER.md, canon/CANON_LOCK.md, canon/HEAT_LADDER.md, canon/STATUS.md, briefs/ch01..ch40.md. No chapters yet as of 2026-10-24.
- `scripts/write_warm_enough.py` EXISTS (strict order, hard/soft checks, locked lines, name whitelist, 2 calls per chapter, --auto, --checkpoint, --audit). Hard-coded to Warm Enough (ALLOWED names, LOCKED lines, CHAR_RANGES, BANNED_NAMES are constants in the file). Pinned by Zia on 2026-10-24 to `nvidia/nemotron-3-ultra-550b-a55b:free` through OpenRouter only (no fallback models). Tested with a mock model on 2026-10-24; not yet run on the real writer.
- `.github/workflows/write-warm-enough.yml` EXISTS (created by Zia 2026-10-22, run by hand). A version with a daily schedule (four runs a day) was drafted on 2026-10-24 and waits for Zia to paste it. `.github/workflows/write-kindling.yml` was the template (Kindling Line is frozen, never run it).
- The repo is PUBLIC, so scheduled Actions runs do not use a private-repo minute limit.
- Reusable: `content_provider.call_raw` (NVIDIA then OpenRouter keys, free models only), `scripts/languagetool_pass.py` + `proofread-languagetool.yml`, `scripts/pipeline.py`, `scripts/manuscript_qa.py`, `scripts/kdp_metadata.py`, `novels/BOOK_CONFIG_TEMPLATE.json`, `novels/VOICE_GUIDE_TEMPLATE.md`, `novels/BEAT_MAP_PROTOCOL.md`, `novels/HUMAN_WRITING.md`.
- Workflow files are refused by the connector (403). Zia pastes them via the web editor.

## Warm Enough method to automate (every point)
1. Readiness verdict: brief thickness vs BEAT_MAP_PROTOCOL (15 to 20 lines per chapter).
2. Closed-world CANON_LOCK: cast, places, objects (exact wording), magic rules, NOT list, locked lines with chapter, time rules, style bans, hidden-fact seed/reveal schedule, conflicts-resolved list.
3. Name audit against every Voxel novel (banned: Wren Pell Bram Hale Oakes Corrin Voss Marius Mara Renn plus every name in existing books).
4. Chapter plan with tempo level per chapter; tempo audit (cold opening, sag zones, flat peak, undefined release); heat ladder with BODY line per chapter.
5. Briefs: PLOT, PRESENT, SETTING, MAGIC, OBJECTS, LOCKED, WITHHOLD, SEED, INTERIOR, STAKES, CALLBACK, ENDS ON, plus HEAT/BODY line.
6. Genre check (heat level, word count, first-kiss position) per pen name: Elif Kessler = slow burn closed door; Ivy Cassel = romantic.
7. STATUS.md, HANDOFF.md, book_config.json, VOICE_GUIDE.md, WRITER_COMMAND.md per book.
8. Writer: canon + brief + real previous chapter + voice sample; reject invented names, banned words, em dashes, digits, wrong-chapter locked lines; retry; never save a broken chapter; commit each chapter.
9. Proofread: banned words, em dashes, word count, name check, LanguageTool; audit report.
10. Daily cron workflow.

## Build plan (not built yet, in order)
1. `factory/ROADMAP.json`: 51 novels (12 new series x 4 + Larkmere books 3 to 5), pen name, genre profile, seed premise.
2. `scripts/novel_factory.py`: stages spec -> canon (json + md) -> name audit -> plan -> tempo audit -> briefs -> readiness gate -> STATUS.
3. `scripts/novel_writer.py`: write_warm_enough.py generalized to read `novels/<id>/canon/canon.json`.
4. `.github/workflows/novel-factory.yml`: cron plus manual, matrix over books, time-boxed, checkpoint per file.
5. Test with a mock model in a sandbox before pushing.
(Where `FACTORY_ADDENDUM.md` disagrees, the addendum wins: extend `pipeline.py`, queue 3 to 4 books ahead, publish at most one title a week per format.)

## Honest limits
- 50 novels is about 2,000 chapters and about 4,000 model calls. Free-tier quotas make this weeks of runs, not one book a day. The free writer gives about 50 requests a day per key, so one finished book a day needs about three keys.
- Nothing in this plan has been run on the real writer. Verify by a real triggered run.
