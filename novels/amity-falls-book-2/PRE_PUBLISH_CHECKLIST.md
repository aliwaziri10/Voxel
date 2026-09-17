# PRE-PUBLISH CHECKLIST — Book 2, "What the Valley Still Owes"

**Read this file first if Zia asks whether Book 2 is ready to publish.** HANDOFF.md in this folder has the chapter-by-chapter status table; this file is the punch list sitting on top of it, same structure as Book 1's checklist.

## Already done — do not redo

- All 41 chapter files confirmed to exist, correctly numbered, non-empty.
- Mechanical proofreading (word count, em dashes, banned phrases) complete via `scripts/proofread_novel.py` — 0 hard violations as of 2026-09-16.
- Full sequential continuity/voice/canon review complete, all 41 chapters, individually stamped in HANDOFF.md's Round 1 log. Real bugs found and fixed: wedding timeline drift ("four weeks" vs. six weeks, ch.1/ch.4), Wren's age drift (ch.12, ch.18), a phantom object-ownership line (ch.29), an unconfirmed-fact slip about Walt Pruitt's fate (ch.30).
- Word floor locked final at 2,100w. No further padding — confirmed by Zia this is deliberate, not incomplete.
- Style-tic diagnostic pass (2026-09-15/16): theme-summary closing paragraph and hand-on-shoulder/embrace ending in ch.41 identified and rewritten to a concrete image and a hand-hold instead. Independently re-checked 2026-09-17 (fresh read, no prior notes referenced) — confirmed the fix reads natural, not over-corrected.
- Fleeting spot-check re-read, 2026-09-17 (ch.20, ch.41 sampled cold): no new issues found.

## TASK 1 — "Some/something ___" hedge sweep — IN PROGRESS, ch.1-3 of 41 done

Tool: `scripts/word_repetition_fixer.py`. Standard: fix only a bare "some/something ___" standing in for an unnamed feeling with no concrete referent ("some old instinct," "something steadier"). Leave "something closer to X than Y," anything qualified by a specific adjective or defining clause, and referential uses ("someone we love," "hold something of his").

Confirmed done: ch.1, ch.2, ch.3.
Confirmed NOT done: ch.4 through ch.41 (38 chapters). Per HANDOFF.md's Round 1 log, dense concentrations were flagged (not fixed) in ch.13, 16, 19, 23, 24, 26, 28, 29, 32, 37, 38, 39, 40, 41 specifically — start there if working non-sequentially, though the charter's standing rule is strict sequential order.

**This is cosmetic polish, not a publish-blocker.** Genuinely optional before going live.

## TASK 2 — Character-name collision audit — NOT STARTED

Book 1's audit caught two real collisions (Constance Aldridge/Oakes, Priti/Priya) that would have confused readers. This has never been run for Book 2's own new names (Yusuf, Dev, Elias Thorne, Odette, Ambrose Whitlock) against each other, against Book 1's cast, or against real public figures. Recommend running before publish, same method as Book 1's Task 1/3.

## TASK 3 — Real-person name check — NOT STARTED

Same as above — never explicitly run for Book 2's cast.

## TASK 4 — KDP publishing-format requirements — PARTIALLY STARTED

1. Front matter — see `front_matter.md` in this folder (drafted 2026-09-17, needs Zia's confirmation on author name/pen name and dedication text).
2. Back-cover blurb — see `back_cover_blurb.md` in this folder (drafted 2026-09-17, needs Zia's approval).
3. Table of contents — not yet built.
4. Chapter-break formatting spot-check for KDP's converter — not yet done. Book 1 found a real base64-encoding corruption bug in two chapters; worth a quick raw-file spot-check on a few Book 2 chapters before upload, even though nothing like it has been reported here.
5. Trim size / manuscript formatting settings — not yet decided.
6. Metadata: title "What the Valley Still Owes" is still marked TENTATIVE in HANDOFF.md — **needs Zia's final confirmation before publish**, along with series numbering ("Book 2" vs. a different series label) and author/pen name (Book 1 used "Elif Kessler" — confirm this carries forward).
7. Cover — image generation prompt already drafted earlier in this project (matching Book 1's photoreal romance-cover style, well visible in the background as a callback). Not yet generated or finalized as an actual file.

## Priority order recommended for next session

1. Confirm title, series label, and author name with Zia — blocks the front matter and cover text.
2. Task 2/3 (name collision + real-person checks) — quick, catches embarrassing errors before anything else.
3. Task 1 (hedge sweep) — optional polish, can run in parallel with anything else, never blocking.
4. Task 4 remainder (ToC, format spot-check, trim size) — last, once text is declared final.

## Update this file

Mark each task DONE with a one-line result summary as it's completed — don't delete the task, log the outcome.
