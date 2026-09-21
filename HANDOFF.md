# Voxel - Handoff

Read this first. Last rewritten 2026-09-21 (verified live against `main` at
commit `88cda82`). Read `novels/EDITORIAL_CHARTER.md` before touching any
chapter.

Rule zero: verify against live files before saying anything is missing or
done. Before saying a file "does not exist", check `main` and the branches
`book4-progress-saving` and `book4-pipeline-fixes`. A `raw.githubusercontent.com`
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
- `novels/amity-falls-book-4/PRE_PUBLISH_AUDIT_2026-09-21.md` (the list of
  timeline and canon contradictions this handoff works from)
- `novels/amity-falls-book-4/PROOFREAD_REPORT.md` (written by the workflow)
- `novels/amity-falls-book-4/amity-falls-book-4_full_manuscript.md` (compiled
  copy, rebuilt by the proofread script)
- `scripts/book4_fixes.json` (exact-text fixes; see "How fixes are applied")
- `scripts/proofread_novel.py` (the proofreader; workflow `proofread.yml`)
- `story_bibles/amity-falls.json` (bible; authoritative for Book 4 canon)
- There is no book-level `HANDOFF.md` for Book 4. This file is the handoff.

Repo-wide docs on `main`: `PLAYBOOK.md`, `GENRE_DECISION.md`,
`CLAUDE_HANDOFF_2026-09-18.md`, `novels/PIPELINE_SPEC.md`.

Other new title: `novels/kindling-line-book-1/` (romantasy series, started
2026-09-21; architecture and book config only). Do not mix it with Amity Falls.

## STATE AT HANDOFF (2026-09-21)

DONE and verified live:
- Batch 1 fixes (Harriet/Theo timeline, Drake's attempt year, Warden
  succession, Millbrook drive time, arrest order, Adelaide's surname): all 47
  entries of `scripts/book4_fixes.json` are present in the chapters (checked by
  exact text at bot commit `7bfb33d`). Pushed in `204afb3`.
- Em dashes: 0 in every chapter.
- Word counts: APPROVED by Zia (2026-09-21). Short and long Book 4 chapters
  stay as they are. Never flag them, never pad them, never list them as open
  work. The script no longer reports them (`89e5405`).
- Chapter 8 repeats a Drake letter on purpose; the script lets it pass.
- False alarm removed (`88cda82`): the workflow (`proofread.yml`, last step)
  fails the run if the report contains the literal text `_VIOLATION` anywhere.
  The old report header contained that text, so every run failed even with 0
  real violations. The header no longer contains it. Only real violation keys
  may. Tested with the workflow's exact grep: clean report passes, a planted
  AI-tell phrase still fails.

NOT DONE, do this first:
- The workflow has NOT been re-run since `88cda82`. The last bot commit
  (`2d54527`, 06:20 UTC) predates it. Ask Zia to run it once and confirm green.
  Zia's steps, exact labels:
  1. Open `https://github.com/aliwaziri10/Voxel/actions/workflows/proofread.yml`
  2. Press "Run workflow"; set "Which book to proofread" to `all-unpublished`;
     tick "Auto-fix dash/hyphen mechanics in chapter text"; leave the two
     word-count boxes alone.
  3. Expect the last step to print "No hard violations found."
  Then list commits on `main`, fetch the new bot commit's
  `novels/amity-falls-book-4/PROOFREAD_REPORT.md` by commit SHA and confirm
  `grep -c _VIOLATION` is 0.

Pre-publish audit verdict (`7350cac`): NOT ready to publish. Prose is clean;
timeline and canon are not. Batch 1 fixed part of the list.

## CANON LOCK (decisions made 2026-09-21; reversible via git)

From the bible and Books 1 to 3:
- Present day is autumn 2024. Drake's clock is about 30 days, so the book is
  one autumn (October into November).
- Harriet Marsh, born 1949 (75 now), lost 1997 to 2007 (ages 48 to 58).
  Drake's first attempt was 2005 (nineteen years ago), inside that decade.
- Theo born 1997. Harriet's husband Thomas died 2003, during the lost decade.
- Ring ritual (Book 3): 2023. Denise was freed by the split-the-weight ritual
  (Book 2), March 2022, ending 50 years of renewals (1972 to 2022).
- Millbrook is a two-hour drive from the valley.
- Adelaide's surname is Whitlock (Book 2). Denise Voss was 31 in 1981 (Book 2).
- Ambrose Whitlock died in 1945 (Book 3 chapter 5). His failed attempt to end
  the bargain is 1889 (Book 4 chapter 3).
- Yusuf is the current Warden only since Denise was freed; the role was vacant
  after the previous Warden died in 1987.
- Drake is arrested in chapter 41, not before.
- Published anchors (read-only): Book 2 has "Adelaide Whitlock" writing the
  letter; the bible says Ambrose taught Adelaide; Book 3 has Castellan as a
  young ring volunteer whose grandmother "lost her summer"; Dev is a Whitlock
  descendant.

## NEXT TASK: BATCH 2, THE WHITLOCK ERA

Problem: the book treats Ambrose Whitlock as all of these at once: an 1847 and
1863 ledger signer, an 1872 to 1901 Warden who tried to end the bargain in
1889, a man who tried in 1923, a man alive in the 1970s, and a man alive in
2003 to 2009. Published Book 3 says he died in 1945, and Book 3 cannot be
changed. So only the early-1900s Ambrose can stay Ambrose.

Recommended resolution (not yet applied; adopt it or change it, then record the
decision in the Canon lock above):
- Ambrose Whitlock: Warden of the first debt 1872 to 1901, attempt 1889,
  died 1945. Keep chapter 3's version as the anchor.
- 1847 and 1863 entries: signed by an earlier Whitlock, Ambrose's father
  (invent one first name, for example Josiah, and use it everywhere).
- The modern "A.W." in chapter 5 and chapter 37: a descendant, for example
  Arthur Whitlock, Ambrose's great-grandson, family keeper of the Whitlock
  papers, died 2009. He is NOT the Warden (Yusuf's line says the role was
  vacant after 1987).
- Adelaide: the bible says Ambrose taught her, so she is not his mother.

Exact places found (line numbers are for the chapter files at `7bfb33d`; they
shift only if a chapter is edited, so re-grep before writing entries):
- Chapter 2: 1847 ledger "recorded by Ambrose Whitlock" (about lines 113, 119),
  notebook line "1847 ledger. Ambrose Whitlock, seven years, sister's face" (187).
- Chapter 3: tenure "1872 to 1901", attempt 1889 (about lines 121 to 123).
  This is the anchor; do not change it.
- Chapter 4: "Terms of the First Debt, as witnessed by Ambrose Whitlock, Warden of
  the First Debt, Year 1847" (53); "1891: Eleanor Whitlock - Ambrose Whitlock's
  wife" (63); "Written by Ambrose Whitlock. Annotated by Adelaide." (87).
- Chapter 5: sealed box, journal signed "A.W." (135, 213, 217); Adelaide called
  "Ambrose Whitlock's mother ... the Warden before him" (223); line 31 "If the
  box was sealed in 2005, Whitlock was still alive. He died in 2009."; line 169
  "The last entry is dated 2005"; "He died four years later"; the journal
  describes Drake's attempt on Harriet, so its author must be living in 2005.
- Chapter 6 line 7: "Ambrose Whitlock's hand ... signed and dated 1847".
- Chapter 9: "A. Whitlock, 1847" (33), "A.W." (57), "A. Whitlock, 1863" (119).
- Chapter 15 lines 119 to 125: a letter "from Ambrose Whitlock ... before he
  died", and Harriet's husband in the 1970s saying "find Ambrose Whitlock".
- Chapter 19 line 11: a 1974 council record "from the private archives of
  Ambrose Whitlock".
- Chapter 37 line 39: "Ambrose Whitlock. The Warden of the first debt in 2003."
- Chapter 42 line 65: Whitlock's letter says "I tried to end the bargain in
  1923"; make it 1889 to match chapter 3.
- Chapters 12, 13, 39, 41, 43, 44, 45 mention "Whitlock's letter" without a
  date; check they still read correctly after the change.

## THEN

Batch 3, seasons and countdown: seasons wander (chapter 5 late summer, 8
January to February, 16 spring, 17 August, 28 April, 36 September to October);
Drake's clock reads 30 days (ch4), 4 days (ch9), 2 weeks (ch20), 12 days
(ch23), 9 days (ch28), "in three weeks" and "three days" (ch36), 6 and 10
days (ch37, 38); deadline "the solstice" (ch8) versus "summer solstice" (ch26).
Decide one timeline (one autumn, about 30 days) and fix each mention.

Batch 4, canon: chapter 39 says "ten volunteers split the weight of Denise's
debt" (ring and split-the-weight are two different rituals); Drake's claim in
chapter 30 (Thomas Marsh's debt) is never answered outright, though chapter 41
shows the extraction files; Harriet's family (granddaughter born 1998 who died
2001, "a daughter who never existed" ch31, "grandmother of one" ch34,
"my granddaughter's first steps" ch41); Drake's collapse (chapter 22
substitution versus chapter 45 falsified trust record; FBI and state police
versus Millbrook Sheriff); Castellan (chapter 2 family in the 1860s, chapter
22 clerk from 1981; Book 3 has Castellan as a young ring volunteer).

Spotted, not fixed: chapter 29 line 41 ("the boy she had raised" about Theo and
Harriet); chapter 38 line 131 (substation access "between 2018 and 2023";
Denise was freed in 2022); chapter 34 line 1 (a forty-minute drive from the
county seat; check it fits the two-hour rule).

Author decisions, not errors: no proposal scene in chapter 44 (the beat map
called for one); chapter 45 recaps the romance stages as a summary paragraph;
real places (Harrisburg, Delaware, Ohio, Wilmington) inside a fictional county.

Not done: the Charter's strict sequential manual read of all 45 chapters, and a
check of Book 4 against the full text of Books 1 to 3 beyond the anchors above.

## HOW FIXES ARE APPLIED (and how to test them)

`scripts/book4_fixes.json` is `{"chapter_NN.md": [[old, new], [old, new,
"all"]]}`. An entry applies only if `old` appears exactly once in that chapter
(or, with `"all"`, at least once). Entries already applied are skipped silently.
Add new entries to the existing file; never delete the applied ones.

Workflow for a batch:
1. Fetch every chapter by commit SHA into a scratch folder with bash
   (`curl https://raw.githubusercontent.com/aliwaziri10/Voxel/<sha>/novels/amity-falls-book-4/chapters/chapter_NN.md`).
2. Write the entries, then simulate the script's matching rules in Python:
   each `old` must match exactly once, and a second pass must change nothing.
3. Push the JSON with `create_or_update_file` (needs the file's current SHA;
   get it from the push result you last made, or re-list). Re-fetch by commit
   SHA and compare.
4. Zia runs `proofread.yml` (steps above). Then confirm every entry landed.
5. Update this file.

Dry run of the whole script without GitHub: copy the chapters into
`/tmp/repo/novels/amity-falls-book-4/chapters/`, put the script in
`/tmp/repo/scripts/`, run with `GITHUB_WORKSPACE=/tmp/repo BOOK=amity-falls-book-4
AUTO_FIX=0 FAIL_ON_ISSUES=1`, then run the workflow's own check
`grep -rl "_VIOLATION" novels/*/PROOFREAD_REPORT.md`.

## TOOL WARNINGS

- The GitHub connector's `get_file_contents` returns the whole file even with
  `fields`. Do not use it on big files; use bash `curl` by commit SHA.
- `create_or_update_file` replaces the whole file, so you must send the full
  content. For big files, edit a local copy with Python, test, then send it,
  then `cmp` the pushed copy against the tested one.
- The connector cannot write to `.github/workflows/`; Zia pastes workflow edits.
- The unauthenticated GitHub API rate-limits fast; prefer raw URLs by SHA.

## RULES FOR ANYONE WORKING HERE

- Zia is a non-coder working in a browser, often by voice. Give at most 3 or 4
  steps at a time. Paths, URLs, inputs and anything copyable go in their own
  code blocks with exact button labels. Do not describe finished work at
  length. Make technical decisions yourself; check things yourself before
  asking Zia to look anything up.
- Verify against live files and ALL branches before claiming anything is
  missing or done. Re-fetch a file's SHA right before editing; several
  sessions work at once.
- Published books are never edited, scanned with auto-fix, or padded.
- Never push a placeholder as file content. After any push, re-fetch and
  compare.
- Never say a fix is applied until you have read it back from the repo.
