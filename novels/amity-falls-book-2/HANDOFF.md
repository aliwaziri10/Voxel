## CONTINUITY / VOICE / CANON REVIEW — PROCEDURE (READ FIRST)

Mechanical proofreading (word count, dashes, banned phrases) is handled by `scripts/proofread_novel.py` / `PROOFREAD_REPORT.md` and is separate from this. This section covers continuity, plot logic, voice consistency, and canon accuracy — the things the mechanical script cannot check.

Rules, in order, for any profile picking this up:

1. **Work in small batches (1-5 chapters), not the whole book at once.**
1a. **STRICT SEQUENTIAL ORDER — mandatory, per Zia.** Review chapters in exact numeric order: check the log below for the highest-numbered chapter with a completed stamp, then start at the next number up. Do not skip ahead to a chapter the mechanical report flags as worse.
2. **Read the chapter(s), beat_map.md, and the "Established canon" section below before judging anything.** Don't rely on a prior session's summary.
3. **Stamp each chapter individually the moment you finish it**, in the log below, before moving to the next one. Don't wait until a batch or the whole pass is "done" to write anything down.
4. **Identify yourself in the stamp** (date + rough session description is enough).
5. **A chapter with no stamp = not reviewed for continuity/voice/canon.** No whole-book "COMPLETE" claim overrides that.
6. **If you find a fixable issue (contradiction, factual slip, wrong name/number, banned tell word), fix it in the chapter file itself, not just note it in the log.** The log records what you found AND what you did about it.
7. **Do not pad word count past the 2,100 hard floor.** If a chapter is already at or above 2,100 words, leave it alone. A chapter within ~70 words of the floor (e.g. 2,031-2,099) also does not need padding — flag it "close to floor" and move on. Only genuinely short chapters (well under 2,000) need real content added.
8. Log format: `ch.NN — [ok / issues below] — reviewed by [label] — YYYY-MM-DD`, followed by findings and the fix applied (or "no issues found").
9. **Update this file after every 2-3 chapters, not just at session end.** Push each small batch to GitHub as it finishes.

---

> ⚠️ **DO NOT TRUST THIS FILE FOR STATUS.** This is a reference/notes file only. Always check the live repo (`chapters/`, real word counts, `beat_map.md`) before trusting any claim here, including anything marked "COMPLETE." **The automated proofreading workflow (`.github/workflows/proofread.yml`) is PAUSED (push + schedule triggers commented out) to stop it racing against manual edits during live sessions. It can still be run manually via workflow_dispatch. Re-enabling requires "workflow" OAuth scope on the GitHub connector, which it may not have — ask Zia to do it via the Actions tab, or re-authorize the connector with that scope first.**

# WHAT THE VALLEY STILL OWES — HANDOFF NOTES

**BOOK 2 COMPLETE as of 2026-09-15.** All 41 chapters written, pushed, and verified live at `novels/amity-falls-book-2/chapters/chapter_01.md` through `chapter_41.md`, all at or near the 2,100-word floor (verify live, don't trust this line). **A chapter-by-chapter continuity/voice/canon review is underway in strict sequential order — chapters 1-28 are reviewed and fixed as of 2026-09-16 (see log below). Continue at chapter 29.**

**Series:** The Amity Falls Series, Book 2
**Working title:** "What the Valley Still Owes" — TENTATIVE, not yet confirmed by Zia. Alternatives: "The Names It Forgets", "Every Ending But the Last."

## What this project is

Direct sequel to "Where the Frost Doesn't Reach" (Book 1, `novels/where-the-frost-doesnt-reach/`, published). Picks up from Book 1's final-page hook: at the wedding, Wren gives Mara a century-old letter from a woman named **Adelaide**, who made the *original* bargain — trading a town's safety for a person's memory — believing it would end with her own life. It didn't.

**Full resolved story:** Adelaide's younger sister Denise had been renewing the bargain every six to eight years since the 1970s, aging almost none at all while quietly taking small, precious memories from the valley. Mara, Caleb, and Wren uncovered the pattern (ch.1-19), brought in Priya, Dev, and Yusuf, and confirmed Denise through direct confrontation (ch.29), where she revealed she'd personally taken Caleb's own missing two years. Rather than simply exposing or punishing her, the group and Denise together attempted an untested "split the weight" redirection ritual at the old well (ch.35-38), successfully redistributing fifty years of carried grief across six willing people and freeing Denise to finally age naturally, gently, alive and at peace. Caleb's two years were fully returned to him (ch.37, ch.40). The valley processed the truth publicly (ch.39), and the book closes six weeks later (ch.41) on ordinary healing, alongside a deliberately unresolved thread reserved for Book 3: Adelaide's letter named Ambrose Whitlock as the one who taught her the bargain, meaning Denise's fifty-year cycle was only one branch of something older.

## Read before writing anything (for a future revision pass or Book 3)

1. `novels/where-the-frost-doesnt-reach/chapters/chapter_45.md` — the Book 1 ending this directly continues from.
2. `novels/where-the-frost-doesnt-reach/architecture.md` — established worldbuilding.
3. `novels/where-the-frost-doesnt-reach/HANDOFF.md` — Book 1's standing rules.
4. `beat_map.md` in this same folder — full chapter-by-chapter summary and the Book 3 setup note.
5. `chapters/chapter_41.md` — the exact wording of Adelaide's letter on Whitlock, essential for any Book 3 planning.

## Established canon (final, for reference)

- Kell "renewed" a version of the bargain himself and collapsed publicly at the harvest festival (Book 1, ch.43) — a separate person from Denise, connected only by Denise once letting him see too much of her own practice eight years ago.
- Wren is **20** (ch.2, "Twenty years old now") — confirmed high-risk recurring error; two separate drift instances found and fixed (ch.12: "a nineteen-year-old"; ch.18: "I'm nineteen" x2). Double-check her age in every remaining chapter it comes up.
- Ch.12: Wren's first full unsupervised read (pocket watch), against her own safety guidance — fragmentary vision (a woman's hands, faceless), nosebleed, near-collapse. Ch.26 escalates this directly: a second solo read on the same watch, against explicit instruction, produces a 3-second vision of young Denise mid-ritual and a severe physical cost (near-collapse, heavy bleeding) after the connection actively resists being watched and shuts itself down. Ch.36 escalates further during the redirection ritual, nearly costing her the most before the group forces an even redistribution.
- Mara and Caleb are married, wedding **six weeks** before ch.1's opening (confirmed anchor figure; ch.1 and ch.4 both had "four weeks" drift errors, fixed — check any later specific week-count against this anchor). Caleb's missing two years were Denise's 8-years-ago renewal (ch.29), returned in fragments during the ritual (ch.37) and in full over the following weeks (ch.40), including the cause of his original grief: his father's death.
- Thomas (Mara's father figure in Book 1) died before the wedding, not a source in Book 2.
- Ch.8: Dev (serving community-service hours, reported by his own sister Priya per ch.19) drops the "pie lady never aging" seed line. Ch.9: Priya follows up privately, learns the fuller Walt Pruitt warning, reconciles with Dev; he agrees to introduce her to Walt as family, not a formal interview. Ch.24: Dev discovers Priya's memory theft and insists on formally joining the group. Ch.28: Dev formally requests to be present at the confrontation itself, over Priya's protective hesitation, framing it as debt repayment for his past sentence — granted. Ch.36-38: Dev/Priya sibling relationship steady and close, with an undeveloped hint of something more (open for Book 3).
- Yusuf, permanent council chair. Ch.10-11: his personal stake is that Denise sat with his dying mother through her final weeks — he stalls, then grants quiet informal authorization after personally sitting with Denise and finding nothing conclusive (an honest half-measure, not a clean yes). Ch.25: after Priya's memory theft, he escalates to a full formal inquiry via emergency chair authority rather than a council vote. Ch.28: sets the final plan — all six go together to confront Denise within three days. Took part in the full climax.
- Bargain mechanics (confirmed ch.3, ch.23-24, ch.30-31, ch.35-38): a continuous pull that collects early from its carrier if delayed; taken memories are transferred into the carrier rather than destroyed; Denise can remove a single targeted memory from a specific person leaving a clean gap (not fog/confusion) without touching adjacent memories; redirection requires physical contact at the site (the well), a spoken release, and active willed effort from each participant to claim an even share, since the default failure mode is collapse onto the weakest person present. Ch.26 adds a new, consistent wrinkle: the bargain's residue in an object (the pocket watch) can actively sense and resist being read once watched too closely, not just passively hold an impression — worth remembering for any Book 3 use of similar objects.
- Denise's real birth year: 1938 (Odette, ch.21). Visible arthritis in her left hand (ch.12, Priya's observation) — useful if a later chapter needs to date a hands-only glimpse of her. Alive, aging naturally, living alone with a quiet rotation of valley check-ins as of ch.41, visited twice by Caleb.
- **Ambrose Whitlock** — named in Adelaide's letter as the one who taught her the bargain, predating even her. Ch.11 plants the Whitlock name decades early (a childhood peach-stealing story). Odette's ch.21 family stories suggest the practice predates the town itself, one teacher per generation. DELIBERATELY UNRESOLVED — the reserved Book 3 hook (ch.41).

## Standing rules (for reference / future books)

- Target 2,000-2,500 words per chapter, 2,100 floor. Do not pad a chapter already at/above 2,100, or within ~70 words of it — flag "close to floor" and move on. Only genuinely short chapters (well under 2,000) get real content added, via interiority/sensory/dialogue expansion only — no new plot events, characters, or information beyond what beat_map.md already assigns that chapter.
- **No em dashes anywhere in chapter prose.**
- Matched voice throughout: Mara dry/controlled/engineering-metaphor, Caleb steady/plainspoken/dry humor, Wren blunt/raw/fast-talking.
- **Banned/tracked tell phrases:** "particular" (now at zero across all 41 chapters — highest historical offender), "the specific ___", "the kind of ___" (still being actively removed chapter-by-chapter during the continuity review; distinguish real, meaningful uses of the phrase from vague filler before auto-replacing — several legitimate uses have been correctly left in place; also watch for the close variant "own kind of ___" as a repeated filler construction, e.g. "its own kind of obligation" — found and fixed in ch.28). **Newer, higher-priority find: the "some/something ___" vague-emotion hedge** ("some old instinct," "something like relief") — flagged as worse than "particular" ever was in a 2-chapter diagnostic sample (ch.1, ch.41), not yet fixed as a dedicated pass, only opportunistically logged/fixed so far during the sequential review. Ch.26 and ch.28 both run notably dense on this hedge — worth weighing toward the top of the priority list for a future dedicated pass. Start checking for it in Book 3 drafting now.
- **Always re-scan the full chapter for ALL banned terms after ANY edit**, not just the one you were fixing — a rewrite can reintroduce the same banned phrase nearby, or introduce a different one. This has happened multiple times (ch.8, ch.13, ch.14) and was only caught by a deliberate post-edit re-scan.
- All filenames lowercase (`chapter_NN.md`). Zia is a non-technical, voice-dictation user — always give file paths and full GitHub URLs in copy blocks.
- Each chapter pushed individually via the API and read back to verify before moving to the next.
- Repo owner is `aliwaziri10`, not `Wazzaboyzz` (an unrelated public repo that caused confusion once).
- **Multiple profiles/sessions may work this project concurrently.** Always re-fetch a chapter's live word count and content immediately before touching it — don't trust this file's, beat_map.md's, or a prior session's summary. Treat any "COMPLETE" claim as a hypothesis to verify, not a fact (this file has been wrong before: a "BOOK 2 COMPLETE" claim once omitted four chapters that were still genuinely broken).
- Only Book 2 is in scope right now (per Zia). Book 3 review/fixes are paused regardless of what Book 3's own PROOFREAD_REPORT.md shows — do not touch Book 3 chapters until Zia says to resume.

## Word count & style-tic status (summary, verified 2026-09-15/16)

Every chapter was audited against live files and brought to or near the 2,100 floor; zero em dashes and zero "particular" confirmed across all 41 chapters as of the word-count pass. The ongoing continuity review has since found isolated regressions and fixed them as encountered (e.g. ch.8 dipped back to 2,038 and was refixed) — treat any word-count claim as needing live re-verification, not as settled. "The kind of" is being cleaned up gradually chapter-by-chapter during the review, not in one dedicated pass. The "some/something ___" hedge (see Standing rules above) is a confirmed real pattern, worse in emotional/climax chapters (working hypothesis from a small sample, not yet verified book-wide) — not yet addressed as a dedicated pass; a future session should either commit to a full line-edit pass on the flagged checkpoint chapters (13, 24, 26, 28, 32, 39, 41, likely 45) or sample a few more procedural chapters first to firm up the hypothesis.

## Next steps (for Zia to decide)

- **Continue the sequential continuity/voice/canon review starting at ch.29.**
- Decide whether to commission a full line-edit pass targeting the "some/something ___" hedge on the flagged checkpoint chapters (13, 24, 26, 28, 32, 39, 41, likely 45).
- Cover, formatting, and publishing logistics — not yet discussed for Book 2.
- Book 3 planning around the Whitlock thread — PAUSED per Zia. (Book 3 drafting itself continues separately at `novels/amity-falls-book-3/`, currently ch.24 of ~45, inherits all standing rules above including the new hedge-word finding; do not confuse its progress tracker with this one.)

## Continuity / Voice / Canon Review Log

*(Strict numeric order — see rule 1a above. One entry per chapter, written the moment it's reviewed. Fixable issues are fixed in the chapter file itself, not just logged.)*

| Ch | Status | Key finding(s) & fix | Word count |
|---|---|---|---|
| 1 | Fixed | Wedding timeline: two "four weeks ago" instances contradicted the chapter's own "six weeks" opening — corrected to six weeks (this is now the anchor figure for the whole book). 2 "some/something" hedges logged, not fixed. | not padded |
| 2 | Fixed | Removed 1 "the kind of." Added a short exchange distinguishing this situation from Kell's (strengthens canon, no new facts). | 2,111→2,299 |
| 3 | Fixed | Removed 1 "the kind of." | 2,250, no padding |
| 4 | Fixed | Cross-chapter timeline bug: two more "four weeks ago" instances (caught only because of strict sequential order) — corrected to six weeks. | 2,122, no padding |
| 5 | OK | No issues. | 2,310 |
| 6 | Fixed | Removed 2 "the kind of." One hedge logged, not fixed. | 2,581 |
| 7 | OK | No issues. Sets up ch.8 cleanly. | 2,488 |
| 8 | Fixed | Word count regressed to 2,038, expanded to ~2,100+. 3x "the kind of" found; 2 fixed immediately, 3rd mis-corrected on first attempt, fixed properly on re-scan. | ~2,100+ |
| 9 | Fixed | Removed 2 "the kind of." | 2,088, close to floor, left alone |
| 10 | Fixed | Removed 4 "the kind of." Yusuf's mother/Denise-caregiving stake established (now in canon above). | 2,271 |
| 11 | Fixed | Removed 2 "the kind of." Whitlock-orchard foreshadowing noted (now in canon above). | 2,031, close to floor, left alone |
| 12 | Fixed | Wren called "a nineteen-year-old" — corrected to twenty (canon: she's 20). | 2,159 |
| 13 | Fixed | Word count 1,995, genuinely under floor — expanded to 2,195 (interiority only). Self-caught: added text briefly reintroduced "particular," fixed before push. | 2,195 |
| 14 | Fixed | 3x "the kind of" found across two passes (1 missed on first re-scan, caught on a second deliberate re-scan). | comfortably above floor |
| 15 | OK | No issues. Well/cellar numbers (4/2/1) match ch.14. | well above floor |
| 16 | OK | No issues. One hedge + one mild physical-contact ending logged, not fixed. | well above floor |
| 17 | OK | No issues. Caleb's "never near a well" line correctly preserves the pre-ch.29 mystery, not a contradiction. | well above floor |
| 18 | Fixed | Wren says "I'm nineteen" x2 — corrected to twenty (same bug class as ch.12, now flagged as high-risk recurring). Removed 1 "the kind of." | comfortably above floor |
| 19 | OK | No issues. New canon: Priya was the one who reported Dev, leading to his sentence (fits ch.8-9 arc). 3 hedges logged, not fixed. | comfortably above floor |
| 20 | Fixed | Removed 1 "the kind of." Whitlock named via Adelaide's letter — matches established canon exactly. | 2,206 |
| 21 | OK | No issues. Denise's 1938 birth year and Odette's "split the weight" rumor both consistent with canon. | 2,049, close to floor, left alone |
| 22 | Fixed | Word count 2,022, under floor — expanded to 2,223 (short closing exchange, no new facts). Removed 2 "the kind of." | 2,223 |
| 23 | Fixed | Removed 1 "the kind of." Multiple hedges logged, not fixed. | 2,296 |
| 24 | Fixed | Removed 2 "the kind of." Establishes Dev's formal entry + the surgical single-memory-removal mechanic (now in canon above). | 2,234 |
| 25 | Fixed | Removed 3 of 5 "the kind of" matches; 2 left in place as genuine, non-filler uses. Yusuf's formal-inquiry escalation confirmed consistent with his ch.10-11 arc. Independently re-verified clean on a second direct read, 2026-09-16 (no changes needed on re-check). | 2,166 |
| 26 | Fixed — reviewed by Claude (chat session, Voxel pipeline check), 2026-09-16 | Removed 1 "the kind of" ("some kind of ledger" → "a ledger"); left "that kind of surgical cruelty" as a legitimate backward-referencing use. No em dashes, no "particular"/"the specific". Wren's age consistent. Dense "some/something" hedge count logged, not fixed (now flagged as a priority chapter for a future hedge pass — see Standing rules). New canon: the watch's residue actively resists a read once watched too closely (added to canon above). Consistent with ch.12/ch.36 Finder-strain escalation. | 2,184 |
| 27 | OK — reviewed by Claude (chat session, Voxel pipeline check), 2026-09-16 | No issues. Word count 2,122, above floor. No em dashes, no "particular"/"the specific", no Wren-age or wedding-timeline conflicts. Both "kind of" instances ("its own kind of cruelty", "the kind of choice Wren made") judged genuine, meaningful uses, left in place. Consistent with ch.26's aftermath and Caleb's established steady/plainspoken voice under strain. | 2,122 |
| 28 | Fixed — reviewed by Claude (chat session, Voxel pipeline check), 2026-09-16 | Removed 2 filler "own kind of ___" instances (obligation, bracing) that repeated the same construction identically; left 3 legitimate uses referencing specific antecedents ("kind of drawing", "kind of teeth", "kind of preparation"). No em dashes, no "particular"/"the specific", no Wren-age or wedding-timeline conflicts. New canon: Dev's formal request to join the confrontation, granted (added above); Yusuf sets the final three-day plan for all six to go together (added above). | 2,265 |

## Proofreading — Last Verified
- Run: 2026-09-16T02:24:49.340957+00:00Z
- Chapters scanned: 41 | Total: 87,838w
- Chapters with issues: 41 | Auto-fixed: 0 | Hard violations: 17
- Full report: `novels/amity-falls-book-2/PROOFREAD_REPORT.md`
- Mechanical checks only — manual pre-push checklist still required.

## Book 3 status note

A separate novel, `novels/amity-falls-book-3/` ("What the Blood Remembers"), is in active drafting, currently at ch.24 of a planned ~45. Depends on this book's canon and inherits these standing rules, including the "some/something ___" hedge finding. See that folder's own HANDOFF.md and beat_map.md — do not confuse its progress tracker with this one. **Only Book 2 is in scope right now (per Zia) — do not touch Book 3 chapters until told to resume, even though Book 3's own PROOFREAD_REPORT.md shows outstanding issues (word floor violations and a literal meta-leak, "the last book," in ch.25).**
