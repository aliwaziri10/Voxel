# Claude Session Handoff — 2026-09-18

Read this before touching anything in this repo. It covers a proofreading/
tooling audit session and the fixes made. Written for the next AI profile
picking this up cold.

## Non-negotiable safety fact, read this first

**All three existing novels are PUBLISHED**, confirmed directly by Zia
on 2026-09-18:
- `where-the-frost-doesnt-reach`
- `amity-falls-book-2`
- `amity-falls-book-3`

`scripts/proofread_novel.py`'s `PUBLISHED_BLOCKLIST` now contains all
three, and `UNPUBLISHED_BOOKS` is empty. This means running
`proofread.yml` with `book: all-unpublished` currently does **nothing** —
that's correct, not a bug. It stays that way until a genuinely new,
unpublished book exists under `novels/`. Do not add a book folder to
`UNPUBLISHED_BOOKS` on your own inference — only on Zia's direct
confirmation that it is unpublished. The cost of guessing wrong here is
a script rewriting text in a book people have already bought.

## What was found (the actual state of the tooling)

There is no single proofreading tool — there are **five**, at very
different levels of wiring, and this was undocumented before this
session (not written down anywhere in `HANDOFF.md` or elsewhere):

| Tool | Wired to CI? | What it does | Can it edit chapter text? |
|---|---|---|---|
| `scripts/proofread_novel.py` | Yes — `.github/workflows/proofread.yml` | word count, AI-tell phrases, meta-leaks, overused words, dialogue tags, duplicate sentences (within + across chapters) | Yes — dash/hyphen auto-fix only, now **off by default** (`auto_fix` input defaults false) |
| `voxel_cli.py audit` (uses `humanizer.scan()`) | Yes — `.github/workflows/voxel-audit.yml` | word count, em-dash count, AI-tell score | No — read-only, writes a separate report file only |
| `scripts/manuscript_qa.py` | **No — manual only** | em dash, doubled words, AI-tell fingerprint phrases, structural uniformity, US/UK spelling consistency, invisible/zero-width chars, punctuation sanity, **real grammar/spelling via `language_tool_python`**, docx asterisk-leak scan, PDF page count | Only writes a report file (`qa_report.md`); reads a `--docx` if given |
| `scripts/word_repetition_fixer.py` | **No — manual only** | hedge-word scan (some/something, particular, "the kind of") | Yes — same dash/hyphen auto-fix, always on, no flag to disable |
| `scripts/continuity_extract.py`, `scripts/build_manuscript.py`, `scripts/build_cover.py` | **Not yet reviewed this session** | unknown — next profile should read these before assuming what they do | unknown |

The important logic here: a tool being "manual only" does not make it
safe by default. `word_repetition_fixer.py` has no book-published check
at all — if someone runs it by hand against a published book's chapter
folder, it will rewrite dashes with no blocklist stopping it. Any future
session that documents or wires these up needs to add the same
`PUBLISHED_BLOCKLIST` pattern from `proofread_novel.py` to each one
individually — the blocklist is not centralized anywhere, so fixing it
in one script does not protect the others.

## What was actually changed this session

1. `scripts/proofread_novel.py`: `ai_tells`, `meta_leaks`, and both
   duplicate-sentence checks were promoted from advisory-only to hard
   `_VIOLATION`s (they're objective errors, not editorial judgment calls
   — see the module docstring for the reasoning). `overused_words` and
   `dialogue_tags` stay advisory on purpose, because a repeated
   character name or theme word is often intentional and needs a human
   to decide, not a script.
2. `scripts/proofread_novel.py`: `PUBLISHED_BLOCKLIST` expanded from one
   book to all three; `UNPUBLISHED_BOOKS` emptied. This was a real gap —
   before this fix, books 2 and 3 were wrongly scannable and
   auto-fixable as "unpublished."
3. Deleted the stale root-level `PROOFREAD_REPORT.md`. It was from an
   older, different, undocumented tool (different report format, no
   per-book breakdown) and it had scanned `where-the-frost-doesnt-reach`
   — a published book — which is exactly what the current system exists
   to prevent. If a similar stray root-level report reappears, that's a
   sign something is generating reports outside the tracked scripts and
   needs the same scrutiny.
4. `.github/workflows/proofread.yml` (pasted in manually by Zia, since
   the connected GitHub App cannot write to `.github/workflows/` — see
   `HANDOFF.md`'s existing note on this, it's permanent, not a bug):
   - Added `FAIL_ON_ISSUES` logic via a final grep-for-`_VIOLATION` step,
     so the workflow actually shows red on a hard violation. Before this,
     the exit code was silently always 0 — the report was generated and
     committed but nothing ever failed, which is the same failure mode as
     not having the check at all: a check nobody has to look at doesn't
     function as a check.
   - Fixed `word_min`/`word_max` workflow-dispatch defaults from a
     hardcoded 2300/2500 back to 1900/2500, matching the floor Zia
     explicitly relaxed on 2026-09-16 — the workflow's own defaults had
     drifted out of sync with the script's documented, confirmed value.
   - Added an `auto_fix` boolean input, **defaulting to false**. Dash/
     hyphen auto-correction is the only thing in this whole system that
     rewrites chapter prose; Zia asked for it to require explicit opt-in
     per run rather than being silently on.

## What's still open (the "more logic" — reasoning for why each matters)

- **`voxel-audit.yml` has no `PUBLISHED_BLOCKLIST`.** It can't rewrite
  chapters (the underlying `cmd_audit` is read-only), so the actual risk
  is lower than it looks, but it can still commit an audit report into a
  published book's folder if someone runs it against one by mistake —
  free-typed `book`/`series` inputs, nothing stops a typo or a wrong
  guess. Low severity, real gap. Fix: add the same blocklist check
  `voxel_cli.py`'s `cmd_audit` does before it writes anything.
- **`word_repetition_fixer.py` has zero published-book protection** and
  it *does* rewrite text (dash mechanics), unconditionally, with no flag
  to turn it off. This is the highest-priority remaining gap of the five
  tools — it's the one manual tool that can actually alter a published
  book's prose if someone runs it against the wrong folder. Fix it the
  same way `proofread_novel.py` was fixed: add a blocklist check at the
  top of `main()` that refuses any path under a published book's folder.
- **`manuscript_qa.py` is unwired and does the most (real grammar via
  LanguageTool).** Before wiring this into anything automated, it needs
  the same blocklist logic — it currently has none, though today it only
  writes a report file, never source text, so the immediate risk is
  lower. Worth deciding deliberately whether Zia wants this run
  regularly rather than leaving it to bit-rot as dead code, same as the
  three disconnected image pipelines already flagged in `HANDOFF.md`.
- **Five separate proofreading tools with three different levels of
  wiring, no central registry.** This is the actual "not world-class"
  problem underneath all of today's specific fixes: nothing in this repo
  currently tells a new session all five exist, which is exactly how the
  stale root `PROOFREAD_REPORT.md` happened in the first place (an older
  tool nobody remembered, still emitting output). Recommend: this file
  itself becomes the pointer until someone consolidates the five into a
  single documented QA entry point in `HANDOFF.md`.
- **`continuity_extract.py`, `build_manuscript.py`, `build_cover.py`
  were not reviewed this session.** Don't assume what they do or whether
  they're safe against published books — read them first.

## A note on how this session went wrong once

Early in this session I described the proofread system as doing no
grammar/spelling/tone correction at all. That was true of
`proofread_novel.py` specifically but false as a claim about "the
system" — `manuscript_qa.py`, sitting unused in the same `scripts/`
folder, does real grammar checking via LanguageTool. The lesson for the
next session: when asked "does X do Y," check every tool that could
plausibly be X, not just the one already in front of you.
