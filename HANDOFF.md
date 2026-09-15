# Voxel — Handoff

Read this first if you're new to this repo (human or AI). It tells you
where things stand and how to not break what's already here.

## Read in this order

1. `README.md` — what Voxel does today, setup, known limitations.
2. `ARCHITECTURE.md` — the phased build plan.
3. This file — process rules and current status.

## Which repo is the working copy (important, read this before anything else)

As of 2026-09-13, `aliwaziri10/Voxel` is a fork of `Wazzaboyzz/Voxel` and
is the repo being actively worked in (Zia owns/admins this fork
outright). `Wazzaboyzz/Voxel` is the original/upstream repo, currently
in sync as of the same date. **Verify which repo you're being asked to
work in — don't assume — since both currently hold identical content and
it's easy to edit the wrong one.**

### The GitHub connector cannot write to `.github/workflows/` — permanent, not a bug

The connected GitHub App (used by AI assistants working on this repo)
returns a 403 on ANY write to a path under `.github/workflows/` —
confirmed on both `create_or_update_file` (single file) and `push_files`
(tree/multi-file), and confirmed the SAME on both `Wazzaboyzz/Voxel` and
`aliwaziri10/Voxel` regardless of collaborator/admin role. This is
**not** a repo-permission problem (admin role doesn't fix it) and is
**not** fixable from repo settings, org settings, or by re-forking.
GitHub Apps require a separate "Workflows" permission scope, distinct
from "Contents," declared in the app's own manifest — this app's
manifest doesn't request it, and that can only be changed by whoever
built the app (Anthropic), not from any settings page Zia has access to.

**What this means in practice:** any change to an existing
`.github/workflows/*.yml` file, or any new workflow file, has to be
pasted in manually by Zia via GitHub's web editor
(`https://github.com/<owner>/Voxel/edit/main/.github/workflows/<file>.yml`).
Everything else (all `.py` files, `story_bibles/`, `novels/`,
`CHANGELOG.md`, etc.) writes fine via the API — only the workflows path
is blocked. Don't re-attempt an automated workflow-file write and assume
it'll work this time; it won't, until the app manifest itself changes.

### Push-change logging (workaround for the above)

Because a `.github/workflows/push-logger.yml` (auto-runs on every push)
couldn't be created for the reason above, `push_logger.py` was added
instead — a script that appends one `CHANGELOG.md` entry (date, commit
SHA, author, message, changed files) for the current commit. It's wired
in as a manual step inside the two workflows that already existed and
already worked (`voxel-book.yml` and `voxel-novel.yml` both now call
`python push_logger.py` as a step, added by Zia pasting the change in
manually per the section above). It does NOT run on plain `git push` to
`main` outside those two workflows — there is currently no way to make
that fully automatic without the missing Workflows permission.

## Where things actually stand (Phase 9, 2026-09-13)

**Note on this file's own dating:** the Phase 8 section below was
originally written roughly two months before 2026-09-13; only the Phase
8b, and now Phase 9, additions genuinely happened on 2026-09-13. Verify
against git commit history if an exact date ever matters for something
in the Phase 8 section specifically.

- **Phases 1–3 are done.** `content_provider.py`, `image_provider.py`,
  `project_provider.py` are shared modules, tested, used by both
  `make_lesson.py` and `build_book.py`.
- **Phase 4 (first real book, end to end) is done and shipped**, off
  this repo's own pipeline (Luna and the Lost Star / Where the Frost
  Doesn't Reach) — see prior notes below, unchanged.
- **Phase 8 (one-command pipeline)** — `voxel_cli.py`, `humanizer.py`,
  `story_bible.py` — see below, unchanged from before.
- **Phase 8b — direct NVIDIA API support for text generation** — see
  below, unchanged from before.
- **Phase 9 (this session): whole-book beat map for novels, and NVIDIA
  batch image generation from a reference photo.**
  - **Beat map (`content_provider.generate_beat_map` +
    `story_bible.save_beat_map`/`load_beat_map`/`get_chapter_beat`).**
    Previously, `voxel_cli.py novel` gave every chapter only the
    top-level brief plus "continue naturally from the last chapter" —
    nothing tracked where the plot needed to go next, which is exactly
    how a 45-chapter novel loses the plot partway through. Now,
    `cmd_novel` generates a full chapter-by-chapter outline (one call,
    before any prose is written) and stores it under
    `story_bibles/<series>.json`'s new `book_beat_maps` key. Each
    chapter is then written from its own specific beat instead of a
    vague instruction. If a beat map already exists for that exact book
    + chapter count (e.g. a resumed run), it's reused rather than
    regenerated, so re-running doesn't silently produce a different
    outline than the one earlier chapters were already written against.
  - **NVIDIA batch image generation (`nvidia_image_provider.py`, new
    file; `voxel_cli.py images` command, new).** Takes ONE reference
    photo and a list of prompts, generates one output image per prompt
    with the reference subject kept consistent, via NVIDIA's
    FLUX.1-Kontext-dev model (chosen specifically because it's built for
    "keep this character, change the scene," unlike base FLUX.1-dev
    which is text-only). Uses the same `NVIDIA_API_KEY` already used for
    text. Example:
    `python voxel_cli.py images --reference luna.png --prompts "Luna at the beach" "Luna reading" --out-dir output_images/luna_batch`.
    **Not yet run end-to-end** — endpoint/payload shape is from NVIDIA's
    published docs (`ai.api.nvidia.com/v1/genai/{vendor}/{slug}`,
    `artifacts[0].base64` response), not from a live test call. First
    real use should be treated as a test: check output images by eye,
    and if it 404s or the response shape doesn't match, check
    https://build.nvidia.com/explore/discover for the current model slug
    and update `NVIDIA_FLUX_KONTEXT_MODEL`/`NVIDIA_FLUX_MODEL` env vars
    (see module docstring).
  - Neither of these two is wired into `voxel-book.yml`/`voxel-novel.yml`
    as a required step — beat map runs automatically inside `novel`
    (it's part of `cmd_novel` itself, not a separate workflow step); the
    `images` command is standalone/manual, not auto-invoked by either
    workflow.

### What was deliberately NOT built (know these before extending)

- No KDP upload automation.
- No story-concept generation — Zia supplies the concept/brief.
- `voxel_cli.py novel` still produces text only; `images` (Phase 9) is a
  separate manual command, not auto-called for novel covers yet — wiring
  that together (auto-generate a cover from the beat map's first-chapter
  description, say) is real future scope, not done here.
- The `humanizer.py` pattern list is still a starting set, not exhaustive.
- **Phase 9's beat map and `images` command have not been run
  end-to-end** — same caveat as Phase 8 below: code is believed correct
  (composes existing patterns already used elsewhere in the repo) but
  untested against a real API key. Treat the first real run as a test.
- No automated tests exist for `humanizer.py`, `story_bible.py`,
  `voxel_cli.py`, or the new `nvidia_image_provider.py`.

## Known doc/repo mismatches not yet fixed (flagged, not resolved)

- **`generate_images.py`** is a second, disconnected image pipeline
  (only used by `test-image-secret.yml`), now a THIRD image path
  alongside Gemini (`image_provider.py`) and NVIDIA
  (`nvidia_image_provider.py`, Phase 9) — none of the three share code.
  Worth consolidating in a future session.
- **`video_output.py`** is built but never wired into `voxel_cli.py`.
- **`build-book.yml` is redundant with `voxel-book.yml`.**

Fixed this session (2026-09-13, cleanup pass): `ARCHITECTURE.md`'s
"Current state"/phase list (was stale, said Phase 4 "NOT STARTED" —
reconciled with reality); README.md/`build_book.py`/`make_lesson.py`'s
stale "Pollinations.ai" image-source comments (actual provider is
Google Gemini — fixed to say so); `_workflows_scope_test.md` and
`_write_access_test.md` (leftover connectivity-check files — deleted).

## Rules for anyone (or anything) working on this repo

- **Read `ARCHITECTURE.md`'s "Current state" section before writing
  code.** If it's stale, fix the doc as part of your change.
- **Add or update a test when you change shared logic**
  (`content_provider.py`, `image_provider.py`, `project_provider.py`,
  `humanizer.py`, `story_bible.py`, and now `nvidia_image_provider.py`).
  Mock external calls.
- **Don't claim a change works without running the tests.**
- **Before attempting any write to this or any other repo, an AI
  assistant must confirm which GitHub account is currently connected**,
  then actually attempt the write and check the real result rather than
  assuming a past session's permission problem still applies — or
  doesn't. See the `.github/workflows/` section above: that specific
  block is real and permanent, but everything else writes fine.
- Zia is a non-coder working browser-only. Manual paste-and-commit steps
  should be given as: the full file path/URL, then the full file
  content to paste — never "find this line and change it."

## Original Phase 4 walk-through (superseded by voxel_cli.py, kept for reference)

1. Pick one real book concept.
2. Run `build_book.py` locally with that concept.
3. Open the output folder, check the PDFs and `project.json` by eye.
4. Run the interior + cover PDFs through Amazon's KDP Print Previewer.
5. Walk KDP's manual listing flow by hand; note repetitive/error-prone
   steps — that becomes future scope.
6. Come back and scope further automation based on what step 5 surfaced.

`voxel_cli.py book` now automates steps 1-3 into one command. Steps 4-5
are still manual and still the right place to learn what to automate next.

## Footer

Content generation pipeline — topic to finished deck/book. © 2026.

## Proofreading — Last Verified
- Run: 2026-09-15T06:51:48.896808Z
- Chapters scanned: 131
- Chapters with issues: 200
- Full report: PROOFREAD_REPORT.md
- Re-verify against live data before trusting this doc at face value.
