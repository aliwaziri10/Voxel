# HANDOFF - Kindling Line Book 2 Polish Pass

Read `../EDITORIAL_CHARTER.md`, then this file, then `brief.txt` and `CONTINUITY_PLAN_ch10-20.md`. Update this file in the SAME commit as any chapter edit (`push_files`, both files, one call). STAMP every chapter you rewrite or proofread in the status table and the log, every time, no exceptions. Quality only, no budget constraint. Strict sequential order. Never strip em dashes on a structurally broken chapter; fix structure first.

**Condensed 2026-09-28** (was ~48 KB; full verbose ch.11-25 canon is in git history at commit `3ddce25c9ba9ab1f662810b20329325fbfbb13bb`). Keep it short: after each chapter add 2-4 lines to the topic blocks and one line to the log, not a per-chapter essay.

**Two books share this repo.** `novels/kindling-line-book-1/` has its OWN HANDOFF and is being fixed by another profile. Before assuming a commit touches this book, check the `files` list with get_commit. Only one profile works at a time, but stale copies of this file have cost wasted passes before: re-list `main` and re-fetch this file at the START of every turn.

## Canon lock (do not deviate)

- **Site:** Anchor Seven (Lower Reach ropewalk sublevel). The ch.13-15 infiltration happens ONLY here. Retired sites: Lower Ward Annex, Graywater Hollow, Greyledge, Embervein, "three miles north", any waystation.
- **Thorne seal, only correct wording:** three strands, unbroken, knotted; a drop, a flame, a feather at each terminus; house colors violet and copper; wax dark, near-black. No red wax, crown, vine, hawk, viper, ivy, tower, thorn, fox, motto. Malrik's own clasp is plain silver, no device.
- **Scripted line** ("I'm not asking you to tell me everything. I'm asking you to stop deciding what I don't need to know.") is USED ONCE, in ch.16. Never repeat it verbatim; a short callback at most.
- **Deed's legal meaning** was fully understood in ch.20. From ch.21 on it is known; do not re-explain it as news.
- **Thorne's line** ("A house that has already paid the cost has earned the right to control who pays it next") spoken by Malrik ch.1, echoed by the steward ch.15. Do not have a named lord repeat it verbatim again.
- **Formal co-lead / cession of authority is ch.39 ONLY.** Ch.17 gave a private promise only ("Together. Before."). Ch.28 did NOT say "Equals, starting now" and later chapters must not either.
- **Cost-transfer between Sol and Kael** is involuntary, non-redirectable, never a chosen buffer, never a felt bond used as a tool (brief rule 15). Not used at all in ch.24-32.
- **Dates:** Sunspire has 30 days. Ch.N = (N+8) Sunspire through ch.22 (30 Sunspire). From ch.23, ch.N = (N-22) Cinderveil (ch.27 = 5, ch.28 = 6, ch.29 = 7, ch.30 = 8, ch.31 = 9, ch.32 = 10, ch.40 = 18, ch.43 = 21, ch.45 = 23). No 31 Sunspire, no "Brightward".
- **Style bans:** no em/en dashes, no "particular", no "some/something/someone/somebody", no "kind of", no "the specific". No chapter may name a chapter number in prose. Word floor 1,800 (count real text with `wc -w` incl. header). Bells always need a time-of-day cue.
- **Names:** Kael Ashworth (Auditor; father Valerius is DEAD, never appears alive), Isolde "Sol" Vane ("my lady" to clerks), Lord Malrik Thorne, grandson Aldous (~25), Thorne's unnamed steward (woman past sixty), Keeper Cormac Vrell (archive), Renn (Council surveyor), wardens Joren (scar on hand) and Mara (20 years, NO surname), Ansa (old splicer, over the tar-shop), Tam (~20, her sister's son), Bram (junior clerk), Varel (missing clerk, now alive under Council protection). Chancellor is an old woman; the Council has TWELVE houses. Never use Marius, Hale, Cressida, Hest, Veyra, Veldt, Mirelle, Voss, Merrow, Elsbeth, Hestor.

## Status (verified against live files 2026-09-28)

| Ch | State |
|----|-------|
| 1-9 | Called clean earlier, but wrong seal wording still live in ch.1, 3, 5, 7. A full read in session 10 found deeper old-canon conflicts (Valerius alive, Nine Houses, wrong Ashworth seal, retired sites): see Findings. Ch.2, 4, 6, 8 need a full read too, not only a grep. |
| 10 | Clean (`d0723906`) |
| 11-14 | Rewritten + stamped: `f129fd09`, `9f7ea6de`, `1dda53d6`, `f18a859c` |
| 15-16 | `1d256b1b`, `1aae27fd` |
| 17 | `4266126a` |
| 18, 19, 20 | `9a3b65f7`, `14225a5e`, `050b0c73` |
| 21 | `d206fd1f`, proofread `6f2d43b5` |
| 22, 23 | `41b77585`; ch.23 + ch.22 date fix `ee2a9683` |
| 24, 25 | `9d977810`, `3ddce25c` |
| 26 | `5094d342` (Kael POV, 4 Cinderveil). 1,866 words, ASCII clean. |
| 27 | `1f979258` (Sol POV, 5 Cinderveil). 1,837 words, ASCII clean. |
| 28 | Rewritten `19b26601`, proofread + stamped `3ec6e9a9`. Kael POV, 6 Cinderveil, 1,872 words. |
| 29 | Rewritten `4e894d54`, proofread same commit. Sol POV, 7 Cinderveil, 2,340 words incl. header, ASCII clean, banned scan clean. |
| 30 | Rewritten (session 11), proofread `b0bf69cd` (session 12), no text edits needed. Kael POV, 8 Cinderveil, 1,822 words incl. header, ASCII clean. |
| 31 | Rewritten `a4531d7f` (session 12). Sol POV, 9 Cinderveil, the standard reading at the house. Old courtroom-censure draft fully replaced. NOT YET separately proofread on a fresh read. |
| **32** | **REWRITTEN THIS COMMIT (session 12).** Kael POV, 10 Cinderveil. Old draft (Valerius alive and present, Mara alert and working an audit session, a disconnected garden/audit-corrections plot, "Honesty without shared authority is still exclusion" spoken three chapters early, "I love you" misattributed to "the infirmary") fully replaced. New content: Mara visited, unchanged; Tam's signing confirmed via Ansa's slate (252, one new name); Sol names her unresolved discomfort from ch.31 again, briefly, without resolving it; Kael and Sol return to the boiling-house cellar and find the iron door standing open (previously shut) with a second brass tally peg left on the table, twin to the one Sol already carries; they send for Joren rather than go further alone. NOT YET PROOFREAD on a fresh read. |
| 33-45 | UNCHECKED. Treat all as broken until read. Session 10 SKIMMED only openings and endings (see Findings, now stale for ch.31-32); a full sequential read of each remaining chapter is still required before it is rewritten. |

## Running canon by topic

**Council, Deed, clocks**
- Petition needs 8 of 12 houses; 8 have signed. Council needs 9 to set the Deed aside. Deed's thirty days lapse 28 Cinderveil. Kael owes a written finding at the public sitting in the THIRD WEEK of Cinderveil (ch.40-43).
- Chain clock (ch.19): cycle TEN breaths, falling toward nine then eight by end of Cinderveil if unresolved. Malrik's order to shut the tap safely is lodged unopened with Renn. Resolve or honor at the climax.

**Sublevel and site facts (ch.12-15, updated ch.32)** - see git history at `3ddce25c` for full ch.12-15 detail. NEW (ch.32): the boiling-house cellar's iron door, shut since the clerks carried out the table's book on the 5th, now stands open. A second brass tally peg, twin to Sol's, left squared on the table inside, clearly placed rather than dropped. Kael wrapped it in a handkerchief, unhandled bare, and now carries two pegs together in his coat. Joren sent for; the chamber not yet explored past the table.

**Thorne people and archive (ch.16-20)** - unchanged, see git history at `3ddce25c`.

**Thorne's engagement table (ch.21-32)**
- Ch.31: standard read whole at the house, 9 Cinderveil. Hold lifted on all five. Tam chose to sign the new standard himself, over Sol's unspoken hope he would not; Kael declined to decide for him either way. Sol named her own overcorrection-shaped blind spot for the first time. This is unresolved rupture material for ch.33-35.
- Ch.32: Ansa's slate now 252 (Tam's name added, first new signer since the 3rd). Sol raises her ch.31 self-recognition again, briefly, still unresolved; the chapter does not let either of them close it.
- Withdrawal form: still unsigned by anyone.

**Kael's and Sol's growth pattern (protect this)**
- Ch.26 relapse, ch.27-32 steady repair (Kael). Ch.31-32: Sol's own blind spot (wanting to decide for Tam, silently) is now a live, unresolved thread parallel to Kael's arc. Do NOT let either of them resolve it symmetrically or neatly before ch.33-35. The rupture needs both threads live and uncomfortable when it lands.
- The total (Sol's "Every step held. It's the total I cannot sign.") stays unpaid. Not addressed in ch.31 or ch.32.

## Plan for ch.33 (author may override)

- Read the old ch.33 in full first; do not assume broken OR clean without reading (every chapter 31-32 was broken on full read, but check ch.33 itself; the session-10 skim flagged only "Thorne banner, its black thorn on grey wool" as a seal-wording problem, not necessarily full-plot drift).
- Ch.33-35 is the LOCKED rupture. Material now available for it: Kael's overcorrection history (ch.20-30), Sol's own blind spot named in ch.31-32 (a real parallel failure, not just his), the still-open second tally peg and iron door thread, Tam's choice, Renn and Mara both still unresolved. The rupture should draw on BOTH of their patterns now, not just his, since ch.31-32 gave Sol a real, ugly, unresolved piece of her own to reckon with.
- Do not resolve the iron-door/second-peg thread inside the rupture chapters; it is a separate plot thread, not rupture material.

## Open threads (do not resolve cheaply)

1. Who is behind the iron door in the boiling-house cellar; NOW: the door stands open and a second peg has been left, deliberately. Someone is signaling. Not yet explored past the table.
2. Copper Thorne link found on Renn's chain though the hatch seals were whole.
3. Aldous's "I did not" (ch.16, still open).
4. Who drew the standard originally; the two houses that asked Bram for their own Schedule line.
5. How the house learned of Tam's dawn question on Kael's own stair.
6. Mara's recovery (unchanged as of ch.32); Kael's left leg and stick.
7. Sol's unspoken FIRST, complicated by Tam's own choice. Do not resolve early.
8. Anchor Seven pass (ch.8) and the archive pass (ch.16) are DIFFERENT passes, same date.
9. Renn missing, entered on the record, commission sits on the 12th. TWO tally pegs now in Kael's coat, both promised to the commission only.
10. The second ward-line under the boiling house; the third count only Sol hears (31, 34, 31) stays unexplained.
11. The man with the lantern and flat case on Tar Lane, night of the 4th: almost certainly Renn, unconfirmed.
12. How the house knew Kael and Sol were due back at the fifth bell on the 6th-7th crossing.
13. What the house means to do with the five freed men, and whether Tam's signing becomes the ward-taker trial the ending needs, or must be complicated first.
14. Who the silent grey man at the ch.31 reading actually was. Never resolve into a named Keeper.

## Findings still live

- Name collision: missing clerk "Varel" vs House Varel (ch.7 "Lord Varel"). Check when ch.1-9 are circled back to.
- Ch.9 (after fix `4f2e1262`) says seven days since the Contract on 17 Sunspire; canon date math gives eight. Minor, fix when circling back.
- Seal wording still wrong in ch.1, 3, 5, 7. Ch.4, 6, 8 need a read, not only a grep.
- **Ch.1-9 old-canon conflicts (all unfixed):** Valerius alive and speaking; "Nine Houses"/"forty-one for" (canon: TWELVE); Ashworth seal given as both "crossed hammers" and "griffin rampant"; retired sites named (Kestrel's Hollow, Emberwatch). Treat ch.1-9 as unverified. Reconcile Valerius alive/dead with Book 1's own HANDOFF before touching ch.1-2.
- **Ch.33-45 SKIM only (session 10), NOT full read, showed old-canon drift, now confirmed the pattern holds for every chapter checked so far (31, 32 were both fully broken on full read despite passing a skim in some cases):** ch.33 ("Thorne banner, its black thorn on grey wool"); ch.34 (empty Keeper's seat foreshadowed too early); ch.35 ("Clerk Valerius", 13 Cinderveil "Thorne's decree advanced"); ch.36 ("co-equals" as ending, but cession is ch.39 ONLY); ch.37 ("Silver thorn on black field", "twelve ward-houses"); ch.39 ("Dallin Vorys"); ch.40 ("Thirty-seven" banners); ch.41 ("Hestia"); ch.43 ("House Thorne in black and burnt orange", 4,412 words, longest chapter); ch.44-45 end on the Keeper's seat, ch.45 needs the "I love you" fix (Kael first, forge on Tar Lane, at Renn's chalk). Treat EVERY remaining chapter as needing a full sequential read and likely full rewrite, not a light edit.
- Grep ch.33-45 for: Embervein, Veyra, Veldt, Mirelle, Hest, Councilor Thorne, "seventeen Sunspire", "thirteen", Voss, gondolas, Marius, Hale, Cressida, Elsbeth, Merrow, Hestor, fox, crimson, thorn-and-crown, "31 Sunspire", "Hall of", "Lady Varel", "Disciplinary Board".
- Keeper: quiet institutional hints only. Never name a person.
- Do not invent Accord article numbers or section numbers. Do not invent how long Kael has loved Sol or how long they have been together.

## Process notes

- Re-list `main` and re-fetch this file at the START of every turn; check each new commit's `files` (get_commit) before assuming it touches this book.
- `raw.githubusercontent.com` WORKS from the sandbox via `curl`. Fetch the raw chapter, run `wc -w`, banned-term grep, compare `git hash-object` against the contents-API SHA.
- Before each chapter: read charter, this file, `brief.txt`, the chapter before, and the OLD chapter in full. Assume the old draft is broken; replace, do not patch.
- Defect categories to scan every unchecked chapter for: wrong magic system, invented soulbond, wrong Thorne seal, front-loaded plot, non-Latin characters, under word floor, chapter-number meta-references, meta breaks, duplicated resolution of a locked beat.
- `kindling-line-book-2_full_manuscript.md` is OUT OF SYNC with `chapters/`; regenerate at the very end.
- Em-dash pass and full-book banned-word scan come after structure is fixed, not before.
- Repo `aliwaziri10/Voxel`, default branch `main`.

## Progress log

- 2026-09-28 (earlier sessions): ch.10-25 rewritten/proofread; canon lock established.
- 2026-09-28: ch.26-30 rewritten across several sessions; ch.30 proofread session 12.
- 2026-09-28 (session 12): rewrote ch.31 (`a4531d7f`, standard reading at the house). Rewrote ch.32 (`5ec42bf5`, Kael POV, iron door found open, second tally peg). Both replaced entirely broken drafts (courtroom censure motion; Valerius-alive garden scene). Next: proofread ch.31 and ch.32 on a fresh read, then read old ch.33 in full and rewrite the rupture opening.
