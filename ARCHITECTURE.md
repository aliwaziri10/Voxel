# Voxel — Architecture

This is the phased build plan referenced by `HANDOFF.md`. It has been
missing from the repo until 2026-08-22, which caused ambiguity about
scope for Phase 2+ — this file exists to close that gap and prevent it
recurring.

**If you're a new session/profile picking this up: read this file top to
bottom before writing any code. The "Phases" list below is the single
source of truth for what's done vs not — HANDOFF.md has more day-to-day
detail on each phase, but if the two ever disagree, fix HANDOFF.md to
match this file, not the other way around, and note the fix.**

## Ground rule

**Work one phase at a time, in order.** A phase is done when the
duplication/gap it targets is actually gone from the repo, not when a
new file merely exists alongside the old one. Do not start a phase
before the prior one is done. Do not build ahead into later phases
"while you're in there" — **this rule was already overridden once**
(Phase 8 was built ahead of the Phase 7 gate, explicitly at Zia's
direction — see HANDOFF.md). That override stands; it doesn't retroactively
permit skipping ahead again without the same kind of explicit direction.

A large "AI creative production studio" vision (orchestrator, provider
registry across text/image/design/audio/video, Canva integration, live
multi-project dashboard, canonical multi-format rendering, multi-product
architecture) was proposed from a different working session on
2026-08-22 and explicitly rejected as premature. That vision is not
banned forever - it's just not in scope until Phase 7, and Phase 7 is
not scheduled until there is real usage (real books actually produced
and sold) to design against — see "What's actually still missing" below;
that's still true even though Phases 4-9 below have since been built.
Building orchestration/provider-abstraction machinery before a single
book has been generated end-to-end through this pipeline is still
designing blind.

## Phases

### Phase 1 — Shared content generation (DONE)
`content_provider.py` is the one shared place that calls
Nemotron/OpenRouter/NVIDIA direct. `make_lesson.py` (`generate_outline`),
`build_book.py` (`generate_manuscript`), and `voxel_cli.py`
(`generate_novel_chapter`, `generate_beat_map`) all import from it. No
local copies of that logic remain in any caller.
Tested by `test_content_provider.py`.

### Phase 2 — Canonical `project.json` per run (DONE)
Every `build_book.py` run writes a `project.json` manifest into its
output folder. Implemented in `project_provider.py`. Tested by
`test_project_provider.py`.

### Phase 3 — Shared image generation (DONE)
`image_provider.py` wraps Google Gemini image generation (this comment
was previously wrong here and in other files — it does NOT wrap
Pollinations.ai; that's a stale mismatch, see HANDOFF.md's "Known
doc/repo mismatches" section) and is shared by `make_lesson.py` and
`build_book.py`. Tested by `test_image_provider.py`.

### Phase 4 — First real book, end to end (DONE, off-pipeline)
Two real products exist, but neither actually ran through this repo's
own `build_book.py`/`voxel_cli.py` pipeline: "Luna and the Lost Star"
was built manually in Canva; "Where the Frost Doesn't Reach" (45
chapters) was written by hand/direct-API-push. So the *usage data* this
phase was meant to generate (what breaks in KDP's real flow, what's
repetitive) was never actually captured through this pipeline. See
"What's actually still missing" below — this is the real gap, not a doc
mismatch.

### Phase 5 — KDP metadata + upload prep (NOT STARTED)
Title, subtitle, description, keywords, categories, regional pricing.
Still not started — Phase 4's off-pipeline shortcut means the lessons
this phase was meant to depend on were never captured either.

### Phase 6 — Automation of the proven manual steps (NOT STARTED)
Depends on Phase 4/5 actually happening through the pipeline first.

### Phase 8 — One-command pipeline (DONE, built ahead of the Phase 7 gate)
`voxel_cli.py`, `humanizer.py`, `story_bible.py` — see HANDOFF.md for
full detail. Explicitly overrides the "no building ahead" rule above, at
Zia's direction. Phase 5/6's original scope (KDP metadata/upload
automation) is still NOT done — Phase 8 automated manuscript+image+PDF
generation, not the KDP listing side.

### Phase 8b — Direct NVIDIA API (text) (DONE)
`content_provider.py` prefers `NVIDIA_API_KEY` over `OPENROUTER_API_KEY`
when both are set. See HANDOFF.md.

### Phase 9 — Novel beat map + NVIDIA batch images (DONE)
`content_provider.generate_beat_map()` + `story_bible.py`'s beat-map
storage (whole-book chapter outline generated up front, so a novel
doesn't lose the plot over many chapters); `nvidia_image_provider.py` +
`voxel_cli.py images` (one reference photo → N consistent images via
NVIDIA FLUX.1-Kontext-dev). See HANDOFF.md for full detail. Not yet run
end-to-end against a real API key — see "What's actually still missing."

### Phase 7 — Re-scope, not before (NOT SCHEDULED)
Dashboard, Canva, video, multi-product-type architecture. Still not
reached — Phases 4/5/6's original purpose (real usage data from an
actual pipeline run) still doesn't exist yet, even though Phase 8/9 were
built ahead of this gate for other reasons. Don't treat Phase 8/9 being
done as Phase 7 having been earned — they're different kinds of "ahead."

## What's actually still missing (read this before picking a task)

Despite Phases 1, 2, 3, 4(partial), 8, 8b, and 9 all showing DONE above,
**nothing has ever been run end-to-end through this repo's own pipeline
with a real API key.** Every "DONE" phase above is DONE in the sense of
"the code exists and is believed correct" — not "verified working."
Concretely, nobody has yet:
- Run `voxel_cli.py book ...` and gotten a real finished picture book out.
- Run `voxel_cli.py novel ...` and gotten real chapters out (with the
  Phase 9 beat map actually feeding them).
- Run `voxel_cli.py images ...` and gotten a real NVIDIA-generated image
  out (the endpoint/payload shape is from docs, not a live test).
- Taken any pipeline output through KDP's actual upload flow.

**This is the single most useful next task for whoever picks this up
next:** run one real, small novel or picture book through the full
`voxel_cli.py` pipeline, start to finish, and record what actually
happens in HANDOFF.md — that's the real Phase 4/5 data this whole plan
has been waiting on since 2026-08-22.

## Current state (keep this in sync with reality)

- Shared modules: `content_provider.py`, `image_provider.py`,
  `project_provider.py`, `nvidia_image_provider.py` (Phase 9) — used
  across `make_lesson.py`, `build_book.py`, `voxel_cli.py`.
- One-command entry point: `voxel_cli.py` (`book`, `novel`, `images`).
- Continuity: `story_bible.py` (characters/style/plot facts/beat maps).
- AI-tell mitigation: `humanizer.py`.
- CI: `.github/workflows/test.yml` runs `python -m pytest -v` on every
  push/PR to `main`.
- **No automated tests exist yet for `humanizer.py`, `story_bible.py`,
  `voxel_cli.py`, or `nvidia_image_provider.py`** — only the original
  Phase 1-3 modules have test coverage.
- **No book/novel has been produced end-to-end through this pipeline
  yet.** This is still the actual next step, not further infrastructure
  — true today the same way it was true when this line first appeared.
