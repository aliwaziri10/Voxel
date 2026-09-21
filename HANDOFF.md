# Voxel - Handoff

Read this first. Last rewritten 2026-09-21 (this session), verified live
against `main` at commit `4cbfbe5` / `b8b61f6`. Read `novels/
EDITORIAL_CHARTER.md` before touching any chapter.

Rule zero: verify against live files before saying anything is missing or
done. Before saying a file "does not exist", check `main` and the branches
`book4-progress-saving` and `book4-pipeline-fixes` (both now superseded by
`main` for Book 4 - see "Branch status" below). A `raw.githubusercontent.com`
read right after a push can be stale; read by commit SHA instead
(`.../Voxel/<commit-sha>/path`).

## WHERE EVERYTHING LIVES

Repo: `aliwaziri10/Voxel` (connector account is `aliwaziri10`). Upstream
`Wazzaboyzz/Voxel` is stale, do not use it.

Published books (frozen, on `main`, never edited or scanned):
- `novels/where-the-frost-doesnt-reach/chapters/` (Book 1, 45 chapters)
- `novels/amity-falls-book-2/chapters/` (Book 2)
- `novels/amity-falls-book-3/chapters/` (Book 3)

Book 4 "The Secret She Kept Forever" is on `main`:
- `novels/amity-falls-book-4/chapters/chapter_01.md` to `chapter_45.md`
  (all 45 exist; the book is complete; about 145,450 words)
- `novels/amity-falls-book-4/architecture.md` (story bible, ending confirmed)
- `novels/amity-falls-book-4/PRE_PUBLISH_AUDIT_2026-09-21.md` (the original
  list of timeline/canon contradictions this handoff works from)
- `novels/amity-falls-book-4/PROOFREAD_REPORT.md` (written by the workflow)
- `novels/amity-falls-book-4/amity-falls-book-4_full_manuscript.md` (compiled
  copy, rebuilt by the proofread script)
- `scripts/book4_fixes.json` (exact-text fixes; see "How fixes are applied")
- `scripts/proofread_novel.py` (the proofreader; workflow `proofread.yml`)
- `story_bibles/amity-falls.json` (bible; authoritative for Book 4 canon)
- `content_provider.py`, `story_bible.py`, `voxel_cli.py` (pipeline code -
  see "Branch status", these are now current on `main`)
- There is no book-level `HANDOFF.md` for Book 4. This file is the handoff.

Repo-wide docs on `main`: `PLAYBOOK.md`, `GENRE_DECISION.md`,
`CLAUDE_HANDOFF_2026-09-18.md`, `novels/PIPELINE_SPEC.md`.

Other new title: `novels/kindling-line-book-1/` (romantasy series, started
2026-09-21; architecture and book config only). Do not mix it with Amity Falls.

## BRANCH STATUS (this session's main change)

`main` is now the single working branch for Book 4. This session copied over
from `book4-progress-saving`:
- The reviewed 45-chapter bible (was previously an empty, leak-ridden stub on
  `main` - see "Root cause" below).
- Chapter 1 (verified clean).
- `content_provider.py`, `story_bible.py`, `voxel_cli.py` with the multi-key
  OpenRouter rotation, broken-chapter guard, meta-leak guard, and
  `--checkpoint` flag (all verified against the live code, not just the
  commit messages).

Root cause found and fixed: `main`'s `story_bibles/amity-falls.json` used to
have `"book_beat_maps": {}` (empty) and leak-ridden character bios ("Book 1
protagonist", "no persuasion arc needed", etc.). A `voxel_cli.py novel` run
against an empty beat map always plans a FRESH one from scratch - this is
almost certainly why an earlier run produced a 60-chapter book instead of the
reviewed 45-chapter one, and why early chapters (chapter 5 especially) leaked
bible phrasing straight into prose. Fixed by overwriting main's bible with the
corrected version. Any future run, on any branch, should target `main`.

`book4-progress-saving` and `book4-pipeline-fixes` are now stale relative to
`main` for Book 4 and can be deleted once you've confirmed nothing else on
them is needed (check for any other in-progress work first).

## STATE AT HANDOFF (2026-09-21, end of session)

DONE and verified live:
- Batch 1 fixes (Harriet/Theo timeline, Drake's attempt year, Warden
  succession, Millbrook drive time, arrest order, Adelaide's surname): all
  entries present in the chapters as of bot commit `c9291a2`.
- Em dashes: 0 in every chapter. Word counts: approved by Zia, never flagged.
- The `_VIOLATION` grep false-alarm is fixed; a clean run passes.
- **Batch 2 (Whitlock era), 6 of the 8 listed chapters fixed and pushed to
  `scripts/book4_fixes.json`, NOT YET APPLIED to chapter text** - Zia needs to
  run `proofread.yml` once more (see "Next 3 steps" below) to actually apply
  them:
  - Chapter 4: 1847 folio authorship, Ambrose -> Josiah (his father; an
    invented earlier Whitlock, since 1847 predates Ambrose's 1872 tenure).
  - Chapter 5: three places where Adelaide/Ambrose's teacher-student
    direction was backwards (the bible says Ambrose taught Adelaide, not the
    reverse) - all three corrected to match; also dropped Adelaide being
    called "Ambrose Whitlock's mother" (biologically impossible if he taught
    her), now "Ambrose Whitlock's student".
  - Chapter 6: same 1847 -> Josiah reattribution as chapter 4.
  - Chapter 9: both "A. Whitlock, 1847" and "A. Whitlock, 1863" -> Josiah.
  - Chapter 15: the 1970s "find Ambrose Whitlock" (Harriet's husband, in
    conversation decades before Theo was born) reassigned to Arthur (the
    modern descendant HANDOFF's original resolution proposed), since Ambrose
    was long dead by then.
  - Chapter 19: checked, no fix needed - the "archives of Ambrose Whitlock"
    line is Drake's own in-story FABRICATION (confirmed forged by Priya in
    the same chapter), so it doesn't need to be historically accurate.

NOT DONE - two real problems found this session, bigger than a text swap,
that need a decision before they're touched:

1. **Chapter 37's Warden-vacancy contradiction.** Chapter 37 has Theo say
   "Ambrose Whitlock. The Warden of the first debt in 2003," and treats
   Harker's brother as "the Warden that year" (2003). But the canon lock
   says the Warden role was VACANT from 1987 until Yusuf took over after
   Denise was freed (2022) - so nobody held that title in 2003. This isn't
   just Ambrose's name being wrong (he died 1945 regardless); the whole
   Harker's-brother-was-Warden-in-2003 beat contradicts the vacancy. Needs
   one of: (a) rewrite this mini-subplot so Harker's brother held some other
   role/blame, or (b) revise the vacancy dates in the canon lock. Not
   patched - a wrong guess here would need to be undone across whatever
   depends on it.

2. **Chapter 15's husband-death-date contradiction (new, not in the original
   Batch 2 list).** Harriet's husband, in this chapter, dies "six months
   later" right after a conversation held "when I was pregnant with your
   mother" - i.e., decades before Theo's mother grew up, roughly the 1970s.
   But the canon lock says Harriet's husband Thomas died in 2003, DURING her
   lost decade - which is the emotional core of Theo's grief (his
   grandfather died in the very years she can't remember). These can't both
   be true. Not patched - resolving it means rewriting either this passage's
   timing or reconsidering the locked death date, and it touches Theo's
   whole arc, not just a fact.

## NEXT 3 STEPS, IN ORDER

1. Run `proofread.yml` to apply the 6 queued Batch 2 fixes above (they are in
   `scripts/book4_fixes.json` right now but NOT yet in the chapter text).
   Same steps as before:
   `https://github.com/aliwaziri10/Voxel/actions/workflows/proofread.yml` ->
   "Run workflow" -> "Which book to proofread" = `all-unpublished` -> tick
   "Auto-fix dash/hyphen mechanics" -> leave word-count boxes alone -> Run.
   Confirm the last step still prints "No hard violations found."
2. Decide chapter 37's Warden-vacancy contradiction (see above) and chapter
   15's husband-death-date contradiction (see above). Both need a call on
   what the story actually says before anyone writes a fix.
3. Then continue to Batch 3 (seasons/countdown) and Batch 4 (canon), both
   fully described below, unchanged from before this session's Batch 2 work.

## CANON LOCK (decisions made 2026-09-21; reversible via git)

From the bible and Books 1 to 3:
- Present day is autumn 2024. Drake's clock is about 30 days, so the book is
  one autumn (October into November).
- Harriet Marsh, born 1949 (75 now), lost 1997 to 2007 (ages 48 to 58).
  Drake's first attempt was 2005 (nineteen years ago), inside that decade.
- Theo born 1997. Harriet's husband Thomas died 2003, during the lost decade
  (SEE OPEN ISSUE 2 ABOVE - chapter 15 currently contradicts this).
- Ring ritual (Book 3): 2023. Denise was freed by the split-the-weight ritual
  (Book 2), March 2022, ending 50 years of renewals (1972 to 2022).
- Millbrook is a two-hour drive from the valley.
- Adelaide's surname is Whitlock (Book 2). Denise Voss was 31 in 1981 (Book 2).
- Ambrose Whitlock died in 1945 (Book 3 chapter 5). His failed attempt to end
  the bargain is 1889 (Book 4 chapter 3). Warden of the first debt, 1872 to
  1901 (chapter 3's anchor - never change this).
- Josiah Whitlock (invented this session, Ambrose's father): signed the 1847
  and 1863 ledger/manuscript entries, predating Ambrose's tenure.
- Arthur Whitlock (invented this session, per the original resolution plan):
  the modern descendant referenced in the 1970s and in chapter 5's sealed
  box; family keeper of the Whitlock papers; NOT the Warden.
- Adelaide Whitlock: Ambrose's STUDENT, and Warden AFTER him (not his mother,
  not his teacher - fixed this session, was backwards in chapter 5).
- Yusuf is the current Warden only since Denise was freed; the role was vacant
  after the previous Warden died in 1987 (SEE OPEN ISSUE 1 ABOVE - chapter 37
  currently contradicts this for the year 2003).
- Drake is arrested in chapter 41, not before.
- Published anchors (read-only): Book 2 has "Adelaide Whitlock" writing the
  letter; the bible says Ambrose taught Adelaide; Book 3 has Castellan as a
  young ring volunteer whose grandmother "lost her summer"; Dev is a Whitlock
  descendant.

## BATCH 3, seasons and countdown (not started)

Seasons wander (chapter 5 late summer, 8 January to February, 16 spring, 17
August, 28 April, 36 September to October); Drake's clock reads 30 days
(ch4), 4 days (ch9), 2 weeks (ch20), 12 days (ch23), 9 days (ch28), "in three
weeks" and "three days" (ch36), 6 and 10 days (ch37, 38); deadline "the
solstice" (ch8) versus "summer solstice" (ch26). Decide one timeline (one
autumn, about 30 days) and fix each mention.

## BATCH 4, canon (not started)

Chapter 39 says "ten volunteers split the weight of Denise's debt" (ring and
split-the-weight are two different rituals); Drake's claim in chapter 30
(Thomas Marsh's debt) is never answered outright, though chapter 41 shows the
extraction files; Harriet's family (granddaughter born 1998 who died 2001, "a
daughter who never existed" ch31, "grandmother of one" ch34, "my
granddaughter's first steps" ch41); Drake's collapse (chapter 22 substitution
versus chapter 45 falsified trust record; FBI and state police versus
Millbrook Sheriff); Castellan (chapter 2 family in the 1860s, chapter 22
clerk from 1981; Book 3 has Castellan as a young ring volunteer).

Spotted, not fixed: chapter 29 line 41 ("the boy she had raised" about Theo
and Harriet); chapter 38 line 131 (substation access "between 2018 and
2023"; Denise was freed in 2022); chapter 34 line 1 (a forty-minute drive
from the county seat; check it fits the two-hour rule).

Author decisions, not errors: no proposal scene in chapter 44 (the beat map
called for one); chapter 45 recaps the romance stages as a summary paragraph;
real places (Harrisburg, Delaware, Ohio, Wilmington) inside a fictional
county.

Not done: the Charter's strict sequential manual read of all 45 chapters, and
a check of Book 4 against the full text of Books 1 to 3 beyond the anchors
above.

## HOW FIXES ARE APPLIED (and how to test them)

`scripts/book4_fixes.json` is `{"chapter_NN.md": [[old, new], [old, new,
"all"]]}`. An entry applies only if `old` appears exactly once in that chapter
(or, with `"all"`, at least once). Entries already applied are skipped silently.
Add new entries to the existing file; never delete the applied ones.

Workflow for a batch:
1. Fetch the chapter's live text (this session used the GitHub connector's
   `get_file_contents` against `refs/heads/main` directly - simpler than the
   curl-by-SHA method below when the connector is available and the file
   isn't huge).
2. Find the EXACT text to match (copy-paste from the fetched content, don't
   retype from memory - whitespace and punctuation must match exactly).
3. Push the JSON with `create_or_update_file` (needs the file's current SHA -
   fetch it fresh right before each push, since several sessions may be
   working at once).
4. Zia runs `proofread.yml` (steps above). Then confirm every entry landed by
   re-fetching the actual chapter text, not just trusting the commit log.
5. Update this file.

Dry run of the whole script without GitHub: copy the chapters into
`/tmp/repo/novels/amity-falls-book-4/chapters/`, put the script in
`/tmp/repo/scripts/`, run with `GITHUB_WORKSPACE=/tmp/repo BOOK=amity-falls-book-4
AUTO_FIX=0 FAIL_ON_ISSUES=1`, then run the workflow's own check
`grep -rl "_VIOLATION" novels/*/PROOFREAD_REPORT.md`.

## TOOL WARNINGS

- The GitHub connector's `get_file_contents` returns the whole file even with
  `fields`. For very large files this session used it directly against
  `main` without trouble; use bash `curl` by commit SHA as a fallback if it
  becomes slow or unreliable.
- `create_or_update_file` replaces the whole file, so you must send the full
  content. For big files (like `book4_fixes.json`), fetch current content
  first, add your entries, then push the complete merged file.
- The connector cannot write to `.github/workflows/`; Zia pastes workflow edits.
- The unauthenticated GitHub API rate-limits fast; prefer raw URLs by SHA, or
  the connector against a specific branch ref.
- SHA mismatches: if a push is rejected as stale, re-fetch the file from the
  branch you're actually pushing to (not a different branch you happened to
  read earlier) before retrying.

## RULES FOR ANYONE WORKING HERE

- Zia is a non-coder working in a browser, often by voice. Give at most 3 or 4
  steps at a time. Paths, URLs, inputs and anything copyable go in their own
  code blocks with exact button labels. Do not describe finished work at
  length. Make technical decisions yourself; check things yourself before
  asking Zia to look anything up.
- Verify against live files and ALL branches before claiming anything is
  missing or done. Re-fetch a file's SHA right before editing; several
  sessions work at once. Don't trust a HANDOFF claim (including this one)
  over what the live file actually says - this session found HANDOFF claims
  that were stale by minutes, and found real contradictions HANDOFF hadn't
  listed. Check the actual chapter text before accepting either kind of claim.
- Published books are never edited, scanned with auto-fix, or padded.
- Never push a placeholder as file content. After any push, re-fetch and
  compare.
- Never say a fix is applied until you have read it back from the repo.
- Multiple OpenRouter accounts/keys can be used via `OPENROUTER_API_KEY_2`,
  `_3`, etc. (already wired into `content_provider.py`). A one-time $10
  OpenRouter credit unlocks 1000 free-model requests/day permanently on a
  single account, which is simpler to operate than key rotation if daily
  throughput is the goal.
