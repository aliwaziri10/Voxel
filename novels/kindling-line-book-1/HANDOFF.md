# Book 1 — HANDOFF (Kindling Line, "What the Gift Demands")

**Read this first**, then `architecture.md` in full, then `VOICE_GUIDE.md`.
Do not generate the beat map or any chapter until both are read.
Standing rule: re-verify everything below against live GitHub before trusting it.

## Verified live 2026-09-25 (end of session)
CONFIRMED:
- `voxel_cli.py` compiles. All 3 edits are in: `if getattr(args, "beat_map_only", False):` sits at 4 spaces, `chapter_date=(raw_entry or {}).get("chapter_date"),` is passed to `generate_novel_chapter`, and `novel_p.add_argument("--beat-map-only", action="store_true")` exists.
- `content_provider.py` compiles. `generate_novel_chapter()` accepts `chapter_date`. `generate_beat_map()` requires `chapter_date`.
- `.github/workflows/voxel-novel.yml` fixed and committed by Zia, verified via the GitHub API (blob SHA `b11b8ff9b794d9ba33542fe15902b097699ee9b5`): has a `beat_map_only` boolean input passed as `--beat-map-only`, and the word range is 2300/2700. (`raw.githubusercontent.com` served the old copy for a while after the commit: CDN cache, use the API to verify.)
- No chapters exist. `story_bibles/` only has `amity-falls.json`, so no Kindling beat map exists yet.
- `CONSENSUS_LOG.md` is referenced by `architecture.md` but is NOT in this folder.
- Assistant GitHub write to `.github/workflows/` returns 403. Workflow edits must be pasted by Zia.

WORKFLOW INPUTS for the beat-map-only run (workflow "Voxel Novel (one command)"):
- series: `kindling-line`
- book: `Kindling Line Book 1` (slugs to `novels/kindling-line-book-1/`, matching the existing folder; do NOT use the title "What the Gift Demands" or it writes to `novels/what-the-gift-demands/`)
- chapters: `45`
- brief: the condensed brief below
- beat_map_only: ticked

NOT YET DONE: the beat-map-only run has not been triggered. Next session: verify the run and the beat map per "After the beat map is generated".

## Current state (2026-09-25)
- `architecture.md`: revised via two-session Claude consensus. Climax
  contradiction fixed, chapter maps unified around 6 set pieces, Kael has
  a real committed wrong act, cost/knowledge/promises ledgers specified,
  ward system added, all decisions synced with `book_config.json`.
- `VOICE_GUIDE.md`: created. Heat level set (open-door, 2-3 scenes,
  not erotica — Zia confirmed this explicitly). POV voice rules set.
- `book_config.json`: pen name Ivy Cassel, House Corrin antagonist,
  trilogy (3 books) all LOCKED. Stage is still `outline` — **no
  chapters exist yet.**
- `../../content_provider.py` and `../../proofreader.py`: both updated
  2026-09-25 so `generate_beat_map()` now requires a `chapter_date`
  field per chapter, and `generate_novel_chapter()` writes it into each
  chapter as a `<!-- chapter_date: ... -->` metadata header when passed.
  This is NEW — built specifically to stop the date/continuity drift
  that happened in Book 4, where dates lived only in prose and
  `CANON_NUMBERS.md` with nothing cross-checking them. See
  `proofreader.py`'s module docstring for the full mechanism.

## Next step
**Generate the real 45-chapter beat map**, now that the schema supports
dates. This must run through the `voxel-novel.yml` GitHub Actions
workflow (browser "Run workflow" button — Zia is browser-only, no
terminal), NOT executed by an assistant session directly: it needs the
NVIDIA/OpenRouter API keys stored as repo secrets, which a chat session
does not have access to. Use the WORKFLOW INPUTS above.

**Brief to pass** (condensed from `architecture.md` — the full file should
also be available to whoever runs this, e.g. pasted into the workflow's
continuity/brief input if there's room, since the brief alone is a
summary, not a replacement):

> Romantasy, Thornmere Reach (vertical cliffside lineage-houses). Isolde
> "Sol" Vane (fallen house, secretly training) and Kael Ashworth (rival
> house, neutral Reckoning auditor with legal power over House Vane's
> claim) — enemies-to-lovers, dual POV. Central mechanic: the Kindling
> (inherited flight-gift) burns years off the wielder; when forced to use
> it near someone, part of the cost transfers involuntarily to whoever is
> nearest — uncontrollable, never redirectable by choice. Sol can reduce
> HOW MUCH burns off with training; she never controls WHO absorbs it.
> Wards (contracted, consenting cost-absorbers) are the system's sanctioned
> version — House Vane couldn't afford one, the real reason Sol's mother
> failed her Reckoning. House Corrin (antagonist, financial motive)
> controls the ward trade. Kael's arc: ch.10 he learns the mechanic is
> worse than disclosed and doesn't report it (first compromise); ch.~20 he
> finds proof House Corrin engineered Sol's mother's failure, with his own
> father/mentor as the ruling auditor at the time, and hides it to protect
> Sol before he can verify it — a ward pays a real cost in the meantime.
> Six set pieces anchor the book (~ch.5-8 first forced-proximity crisis,
> ~13-15 night chase, ~20 incentive/discovery, ~26-28 public event goes
> wrong + first kiss, ~33-35 rupture, ~40-43 the Reckoning climax — Kael
> forced close by his role, not by Sol's choice). Every chapter ends on an
> open question, varying hook type. Book 1 resolves its own conflict
> (Reckoning, Corrin's scheme) and ends with Sol and Kael together (Happy
> For Now) — a larger world-level threat stays open for Book 2. Assign
> each chapter a concrete, internally consistent in-world date.

## After the beat map is generated
1. Verify it actually has exactly 45 entries and every entry has a
   non-empty `chapter_date` — `content_provider.generate_beat_map()`
   requires this field now, but confirm the live output, don't assume.
2. Do NOT start drafting chapters without checking the beat map against
   `architecture.md`'s six set pieces first — a human (or a fresh
   session) should confirm the beat map's actual chapter numbers roughly
   match the ~5-8, ~13-15, ~20, ~26-28, ~33-35, ~40-43 set-piece
   placement before chapters are drafted from it.
3. Chapter drafting: run the same workflow with `beat_map_only` UNticked
   and the same series/book/chapters/brief. It reuses the saved beat map
   automatically since chapter count matches, and `--checkpoint` (always
   on in the workflow) saves partial progress if the run is interrupted
   (GitHub Actions has a 6-hour limit) and resumes on re-run.
4. `proofreader.py` (new) should be run per chapter alongside
   `humanizer.py` once chapters exist — it is NOT yet wired into
   `voxel_cli.py`'s `cmd_novel` automatically. That wiring is also not
   yet done — flag as a possible next task, not assumed complete.

## Open decisions still deferred to Zia (unchanged from architecture.md)
- Cover design direction.
- `ai_disclosure_included` / `kdp_metadata_approved` gates.

## Scope note carried over from architecture.md
This book's outline now has real machinery (six set pieces, three
ledgers, a two-stage hidden-proof subplot) beyond what Amity Falls used.
Worth a deliberate go/no-go read after the first 10 chapters draft.
