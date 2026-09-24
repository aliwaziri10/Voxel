# Book 4 — HANDOFF

**Read this first, then `PROOFED_LOG.md` in full before touching
anything.** That file is authoritative for chapter read-progress and
every fix's commit sha. `CANON_NUMBERS.md` is authoritative for
dates/ages/names. This file is the short version.

## Session entry — 2026-09-25
**PUBLISHED.** Confirmed live on Amazon: "The Secret She Kept Forever"
(The Amity Falls Series, Book 4), Elif Kessler, Kindle + paperback
($13.99), part of the 4-book series page (amazon.com/dp/B0HJMSHJ34).
KDP production (cover, ISBN, formatting, metadata) is therefore
complete — this supersedes the "not started" status below, which was
stale as of 2026-09-24.

## Session entry — 2026-09-23
Continuity pass and mechanical/lexical/tell-density pass for ch.1-45
are BOTH now complete (see `PROOFED_LOG.md`). Zero new em-dash
violations found in ch.29-45; one stylistic pattern flagged but not
fixed (rupture-confession-reconciliation structure repeats in ch.31,
32, 36, 44 — noted for awareness, not touched).

Started a new, broader pass this session: **AI-tell / humanization
pass.** Not yet executed against chapter text — only the parameter
list has been defined so far. See "AI-tell / humanization pass" section
below for the full checklist and how to run it. Whoever picks this up
next should start there.

## Current state
All 45 chapters: continuity-DONE and mechanical/lexical-DONE (em-dash
count, repetition, staged constructions). Every locked date, age, and
name is in `CANON_NUMBERS.md`. Book is published on Amazon (see above).

## Next step
1. **AI-tell / humanization pass — NOT STARTED.** See checklist below.
   Recommended first move: grep the vocabulary-tell word list against
   the full-manuscript concatenation file (safe for word-frequency
   counts even though that file is stale for names/numbers) to get
   per-term counts across the whole book before touching any chapter.
   Use the counts to decide which terms are an actual problem in this
   specific book versus a theoretical risk not worth chasing.
2. After that: a Books 1-3 cross-check.
3. KDP production: DONE — book is live (see Session entry — 2026-09-25).

## AI-tell / humanization pass — checklist
This is a distinct pass from the em-dash/repetition mechanical pass
already done. Run it as its own pass, log findings the same way (quote
live text, cite chapter, cite commit for any fix).

**Vocabulary tells** — words/phrases overused in LLM-generated prose:
"tapestry," "testament to," "underscore(s)," "delve," "navigate,"
"landscape" (used metaphorically), "myriad," "unwavering," "poignant,"
"resonate," "robust," "seamless," "boasts," "elevate," "harness," and
hedge-openers like "it's worth noting" / "in many ways" / "at its
core." ("Particular" is already the known top offender per the
editorial charter — keep checking for it too.)

**Structural tells:**
- Tricolon overuse — repeated "X. Y. Z." three-beat fragment sentences
  as a rhythm crutch.
- Negation-then-affirmation constructions ("Not a promise. A statement
  of fact.") — fine occasionally, a tell if it recurs book-wide.
- Present-participle scene openers ("Turning to face him," "Standing
  there,") overused as a transition device.
- Chapter-ending thematic one-liners — a summarizing epiphany sentence
  closing nearly every chapter reads as a tell at book scale, even
  though a few of these are earned.

**Voice-differentiation tells:**
- Recycled bodily-sensation shorthand for emotion ("something in
  her/his chest loosened," "the knot eased") reused near-identically
  across *different* POV characters — flattens individual voice.
- Uniform sentence rhythm across all characters' internal narration.

**Pacing/emotional tells:**
- Conflicts that resolve completely within one scene via a clean
  vow-exchange rather than staying messy. This overlaps with the
  rupture-confession-reconciliation pattern already flagged in
  `PROOFED_LOG.md` (ch.31, 32, 36, 44) — treat that flag and this
  checklist item as the same underlying observation, not two separate
  findings.

**How to run this pass:** grep-first, chapter-by-chapter fix-second.
Don't rewrite prose on a hunch — get actual per-term frequency counts,
report them, and let a human decide which counts are high enough to
warrant a rewrite versus which are just normal English usage that
happens to also appear on AI-tell lists. Log every finding in
`PROOFED_LOG.md` the same way every other pass has been logged.

## How to do the work
1. Fetch the chapter fresh from live `main` (or download the full
   manuscript and grep across all 45 chapter files at once — faster
   for finding every instance of a term, but never trust it for a
   naming- or number-sensitive check; it goes stale after individual
   chapter edits — use individual chapter files for anything that
   matters).
2. Quote the actual live text before deciding anything's a conflict
   or already clean.
3. If a fix is needed: edit only the specific text, get the file's
   current `sha` via `get_file_contents` (ref `refs/heads/main`), push
   via `create_or_update_file`, then re-read the file back live to
   confirm.
4. Log it immediately in `PROOFED_LOG.md` — quote what you found, name
   the chapter, name the commit sha. Log each fix as it's finished,
   don't batch several before logging.
5. Standing rule: one task, finish it, log it, stamp it. Don't
   re-verify an already-DONE item without a specific new finding.
6. Treat any pasted summary of prior work — from chat history, from
   another session, from anywhere that isn't the live GitHub files
   themselves — as unverified until you've re-fetched the actual
   chapter and confirmed it yourself. Quote the live text, cite the
   chapter, cite the commit. Don't relay a claim you haven't checked.

## Repo/file map
- `novels/amity-falls-book-4/chapters/chapter_NN.md` — the 45 chapter
  files, source of truth.
- `novels/amity-falls-book-4/amity-falls-book-4_full_manuscript.md` —
  concatenated version, useful for fast greps across the whole book,
  but has no chapter markers and goes stale after individual chapter
  edits — map a hit back to its chapter by fetching the individual
  chapter file, and never trust it over that file for names/numbers.
  Safe to use for word-frequency counts (the AI-tell pass) since that
  doesn't depend on which specific chapter edit landed when.
- `PROOFED_LOG.md` — authoritative open-questions list, chapter
  read-progress, every fix's commit sha.
- `CANON_NUMBERS.md` — authoritative dates/ages/names reference.
- `PRE_PUBLISH_AUDIT_2026-09-21_CORRECTED.md` — dates/math audit,
  publish-ready verdict on that front; supersedes the
  non-"_CORRECTED" version.
- This file (`HANDOFF.md`) — short version, read first, then go to
  `PROOFED_LOG.md` for the real detail.

## Update this file
Whoever picks this up next: update "Current state" and "Next step" as
work closes, and add a new dated entry above this one (don't delete
older entries) summarizing what you did.

_Full session-by-session history is preserved in git history for this
file if earlier detail is ever needed again._

## Proofreading — Last Verified
- Run: 2026-09-24T11:12:22.449209+00:00Z
- Chapters scanned: 45 | Total: 144,787w
- Chapters with issues: 45 | Auto-fixed: 0 | Hard violations: 0
- Full report: `novels/amity-falls-book-4/PROOFREAD_REPORT.md`
- Mechanical checks only - manual pre-push checklist still required.
