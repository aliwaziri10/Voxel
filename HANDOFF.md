# Voxel - Handoff

Read this first. Last rewritten 2026-09-21 (second session of the day),
verified live against `main`. Read `novels/EDITORIAL_CHARTER.md` before
touching any chapter.

Rule zero: verify against live files before saying anything is missing or
done. A `raw.githubusercontent.com` read right after a push can be stale; read
by commit SHA instead (`.../Voxel/<commit-sha>/path`). `main` is the only
working branch for Book 4; `book4-progress-saving` and `book4-pipeline-fixes`
are stale and can be deleted once nothing else on them is needed.

## WHERE EVERYTHING LIVES

Repo: `aliwaziri10/Voxel` (connector account confirmed this session:
`aliwaziri10`). Upstream `Wazzaboyzz/Voxel` is stale, do not use it.

Published books (frozen, on `main`, never edited or scanned):
- `novels/where-the-frost-doesnt-reach/chapters/` (Book 1, 45 chapters)
- `novels/amity-falls-book-2/chapters/` (Book 2)
- `novels/amity-falls-book-3/chapters/` (Book 3)

Book 4 "The Secret She Kept Forever" is on `main`:
- `novels/amity-falls-book-4/chapters/chapter_01.md` to `chapter_45.md`
  (complete; about 145,455 words per the latest proofread report)
- `novels/amity-falls-book-4/architecture.md` (story bible, ending confirmed)
- `novels/amity-falls-book-4/PRE_PUBLISH_AUDIT_2026-09-21.md` (ORIGINAL audit,
  partly wrong: many claims did not match the live text)
- `novels/amity-falls-book-4/PRE_PUBLISH_AUDIT_2026-09-21_CORRECTED.md`
  (corrected audit, checked against live files; trust this over the original,
  but it also says the calendar/season read is still not done)
- `novels/amity-falls-book-4/PROOFREAD_REPORT.md` (written by the workflow)
- `novels/amity-falls-book-4/amity-falls-book-4_full_manuscript.md` (compiled
  copy, rebuilt by the proofread script)
- `scripts/book4_fixes.json` (exact-text fixes; see "How fixes are applied")
- `scripts/proofread_novel.py` (the proofreader; workflow `proofread.yml`)
- `story_bibles/amity-falls.json` (bible; authoritative for Book 4 canon)
- `content_provider.py`, `story_bible.py`, `voxel_cli.py` (pipeline code)
- There is no book-level `HANDOFF.md` for Book 4. This file is the handoff.

Repo-wide docs on `main`: `PLAYBOOK.md`, `GENRE_DECISION.md`,
`CLAUDE_HANDOFF_2026-09-18.md`, `novels/PIPELINE_SPEC.md`.

Other new title: `novels/kindling-line-book-1/` (romantasy series). Do not
mix it with Amity Falls.

## STATE AT HANDOFF (2026-09-21, end of second session)

VERIFIED LIVE this session (read directly from `main`):
- Chapter 37 shows the applied fix: Drake "was still free, two towns over"
  (was "in a county holding cell"; he is arrested in chapter 41).
- Chapter 15 shows "find Arthur Whitlock" (earlier Batch 2 fix applied).
- The proofread run at 15:42 UTC ended with 0 hard violations. Its only
  "not applied" entry: chapter 5, "She was the Warden before him. She tried
  to end the bargain." appears TWICE, so the fix was skipped (see Next steps).
- Seen in an earlier grep this session (not re-read since): chapter 4 has
  "Josiah", chapter 6 has "Josiah", chapter 9 has "J. Whitlock, 1847".

DECISIONS MADE THIS SESSION (Zia said: decide and move on):
1. Chapter 15, husband's death. KEEP the canon lock (Thomas Marsh died 2003,
   inside Harriet's lost decade). The "died six months later" line is
   rewritten: he never brought it up again, and Theo tells Harriet his heart
   gave out in 2003. Also "pregnant with your mother" becomes "your father"
   (Theo's father is Harriet's son, per chapter 5), and "two hundred miles"
   from the bargain's source becomes "two hours" (matches the two-hour rule).
2. Chapter 37, Warden in 2003. KEEP the canon lock (Warden role vacant until
   Yusuf, after Denise was freed in 2022). The Harker subplot is rewritten:
   Old Man Harker's brother was the WEATHER (Weathers lineage) who held the
   wind debt in 2003, not the Warden. The brother is named Silas Harker
   (invented this session). Ambrose Whitlock's name is removed from that
   passage (he died in 1945).

QUEUED in `scripts/book4_fixes.json` but NOT YET APPLIED to chapter text
(pushed this session; Zia must run `proofread.yml`):
- chapter_15.md: 3 new entries (your father; husband's death line; two hours)
- chapter_37.md: 6 new entries (Weather/Silas Harker rewrite)
After the run, re-fetch chapters 15 and 37 and confirm each entry landed
(entries whose old text is not found exactly once are skipped silently).

## NEXT 3 STEPS, IN ORDER

1. Run `proofread.yml`: open
   `https://github.com/aliwaziri10/Voxel/actions/workflows/proofread.yml` ->
   "Run workflow" -> "Which book to proofread" = `all-unpublished` -> tick
   "Auto-fix dash/hyphen mechanics" -> leave word-count boxes alone -> Run.
   Confirm the last step prints "No hard violations found." and check the
   report's "Fixes not applied" section.
2. Fix the chapter 5 duplicate: fetch chapter 5, find both copies of "She
   was the Warden before him. She tried to end the bargain.", add enough
   surrounding text to make the entry unique for the copy that describes
   Adelaide relative to Ambrose (Adelaide is Warden AFTER him), then add it to
   `scripts/book4_fixes.json`.
3. Batch 3 (seasons and countdown), see below. Then Batch 4 (canon).

## CANON LOCK (decisions made 2026-09-21; reversible via git)

- Present day is autumn 2024. Drake's clock is about 30 days, so the book is
  one autumn (October into November).
- Harriet Marsh, born 1949 (75 now), lost 1997 to 2007 (ages 48 to 58).
  Drake's first attempt was 2005 (nineteen years ago), inside that decade.
- Theo born 1997. Harriet's husband Thomas died 2003, during the lost decade.
  Harriet's son is Theo's father (born about 1972).
- Ring ritual (Book 3): 2023. Denise was freed by the split-the-weight ritual
  (Book 2), March 2022, ending 50 years of renewals (1972 to 2022).
- Millbrook is a two-hour drive from the valley.
- Adelaide's surname is Whitlock (Book 2). Denise Voss was 31 in 1981.
- Ambrose Whitlock died in 1945 (Book 3 chapter 5). His failed attempt to end
  the bargain is 1889 (Book 4 chapter 3). Warden of the first debt, 1872 to
  1901 (chapter 3's anchor - never change this).
- Josiah Whitlock (invented, Ambrose's father): signed the 1847 and 1863
  ledger/manuscript entries, predating Ambrose's tenure.
- Arthur Whitlock (invented): the modern descendant Harriet's husband said to
  find; family keeper of the Whitlock papers; NOT the Warden.
- Adelaide Whitlock: Ambrose's STUDENT, and Warden AFTER him.
- Warden role: vacant after the previous Warden died in 1987 until Yusuf,
  appointed after Denise was freed (2022). Nobody was Warden in 2003.
- Silas Harker (invented this session): Old Man Harker's brother, the Weather
  who held the wind debt in 2003 (chapter 37). Not a Warden.
- Drake is arrested in chapter 41, not before.
- Published anchors (read-only): Book 2 has "Adelaide Whitlock" writing the
  letter; the bible says Ambrose taught Adelaide; Book 3 has Castellan as a
  young ring volunteer whose grandmother "lost her summer"; Dev is a Whitlock
  descendant.

## BATCH 3, seasons and countdown (not started)

The CORRECTED audit confirms one real problem: Drake's countdown is
inconsistent. Live text shows: 14 days (ch2), 30 days (ch4), 4 and 3 days
(ch5), 6-week vs 10 days (ch18, Yusuf's vote), 12 days (ch23), 9 days (ch28),
"two weeks" (ch30), 10 days then 9 days (ch31), "three weeks" and "three days"
(ch36), 10 and 6 days (ch37), first hearing 3 weeks out (ch38). Deadline
"the solstice" (ch8) vs "summer solstice" (ch26). Also chapter 8 mentions
November and chapter 37 has ripening apples, so the seasons are unresolved.
Decide one timeline (one autumn, about 30 days) and fix each mention.
Read each scene before writing its fix.

## BATCH 4, canon (not started)

Chapter 39 says "ten volunteers split the weight of Denise's debt" (ring and
split-the-weight are two different rituals); Drake's claim in chapter 30
(Thomas Marsh's debt) is never answered outright; Harriet's family
(granddaughter born 1998 who died 2001, "a daughter who never existed" ch31,
"grandmother of one" ch34, "my granddaughter's first steps" ch41); Drake's
collapse (chapter 22 substitution versus chapter 45 falsified trust record;
FBI and state police versus Millbrook Sheriff); Castellan (chapter 2 family
in the 1860s, chapter 22 clerk from 1981; Book 3 has Castellan as a young ring
volunteer).

Spotted, not fixed: chapter 15 has Theo say he is 36 and began searching at
26, but canon has him born 1997 (27 in 2024); chapter 29 line 41 ("the boy she
had raised" about Theo and Harriet); chapter 38 line 131 (substation access
"between 2018 and 2023"; Denise was freed in 2022); chapter 34 line 1 (a
forty-minute drive from the county seat; check it fits the two-hour rule).

Author decisions, not errors: no proposal scene in chapter 44; chapter 45
recaps the romance stages as a summary paragraph; real places (Harrisburg,
Delaware, Ohio, Wilmington) inside a fictional county.

Not done: the Charter's strict sequential manual read of all 45 chapters, and
a check of Book 4 against the full text of Books 1 to 3.

## HOW FIXES ARE APPLIED (and how to test them)

`scripts/book4_fixes.json` is `{"chapter_NN.md": [[old, new], [old, new,
"all"]]}`. An entry applies only if `old` appears exactly once in that chapter
(or, with `"all"`, at least once). Entries already applied are skipped silently.
Add new entries to the existing file; never delete the applied ones.

Workflow for a batch:
1. Fetch the chapter's live text with the GitHub connector's
   `get_file_contents` against `refs/heads/main`.
2. Copy the EXACT text to match from the fetched content; whitespace and
   punctuation must match.
3. Push the JSON with `create_or_update_file` (fetch the file's current SHA
   right before pushing; several sessions may be working at once) or
   `push_files` together with other files.
4. Zia runs `proofread.yml`. Then confirm every entry landed by re-fetching
   the actual chapter text, not just trusting the commit log.
5. Update this file.

## TOOL WARNINGS

- `get_file_contents` returns the whole file even with `fields`.
- `create_or_update_file` replaces the whole file, so send the full content.
- The connector cannot write to `.github/workflows/`; Zia pastes workflow edits.
- The unauthenticated GitHub API rate-limits fast; prefer the connector.
- SHA mismatches: re-fetch the file from the branch you are pushing to.

## RULES FOR ANYONE WORKING HERE

- Zia is a non-coder working in a browser, often by voice. Give at most 3 or 4
  steps at a time. Paths, URLs, inputs and anything copyable go in their own
  code blocks with exact button labels. Do not describe finished work at
  length. Make technical decisions yourself; check things yourself before
  asking Zia to look anything up. Do not invent facts: say what was verified.
- Verify against live files before claiming anything is missing or done.
  Re-fetch a file's SHA right before editing. Do not trust a HANDOFF claim
  (including this one) over what the live file says.
- Published books are never edited, scanned with auto-fix, or padded.
- Never push a placeholder as file content. After any push, re-fetch and
  compare.
- Never say a fix is applied until you have read it back from the repo.
- Multiple OpenRouter accounts/keys can be used via `OPENROUTER_API_KEY_2`,
  `_3`, etc. (wired into `content_provider.py`).
