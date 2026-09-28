# HANDOFF - Kindling Line Book 2 Polish Pass

Read `../EDITORIAL_CHARTER.md`, then this file, then `brief.txt` and `CONTINUITY_PLAN_ch10-20.md`. Update this file in the SAME commit as any chapter edit (`push_files`, both files, one call). STAMP every chapter you rewrite or proofread in the status table and the log, every time, no exceptions. Quality only, no budget constraint. Strict sequential order. Never strip em dashes on a structurally broken chapter; fix structure first.

**Condensed 2026-09-28** (was ~48 KB; full verbose ch.11-25 canon is in git history at commit `3ddce25c9ba9ab1f662810b20329325fbfbb13bb`). Keep it short: after each chapter add 2-4 lines to the topic blocks and one line to the log, not a per-chapter essay.

**Two books share this repo.** `novels/kindling-line-book-1/` has its OWN HANDOFF and is being fixed by another profile (Frostveil/Emberfall dates, Valerius alive/dead decision). Before assuming a commit touches this book, check the `files` list with get_commit. Only one profile works at a time, but stale copies of this file have cost wasted passes before: re-list `main` and re-fetch this file at the START of every turn.

## Canon lock (do not deviate)

- **Site:** Anchor Seven (Lower Reach ropewalk sublevel). The ch.13-15 infiltration happens ONLY here. Retired sites: Lower Ward Annex, Graywater Hollow, Greyledge, Embervein, "three miles north", any waystation.
- **Thorne seal, only correct wording:** three strands, unbroken, knotted; a drop, a flame, a feather at each terminus; house colors violet and copper; wax dark, near-black. No red wax, crown, vine, hawk, viper, ivy, tower, thorn, fox, motto. Malrik's own clasp is plain silver, no device.
- **Scripted line** ("I'm not asking you to tell me everything. I'm asking you to stop deciding what I don't need to know.") is USED ONCE, in ch.16. Never repeat it verbatim; a short callback at most.
- **Deed's legal meaning** was fully understood in ch.20. From ch.21 on it is known; do not re-explain it as news.
- **Thorne's line** ("A house that has already paid the cost has earned the right to control who pays it next") spoken by Malrik ch.1, echoed by the steward ch.15. Do not have a named lord repeat it verbatim again.
- **Formal co-lead / cession of authority is ch.39 ONLY.** Ch.17 gave a private promise only ("Together. Before."). Ch.28 did NOT say "Equals, starting now" and later chapters must not either.
- **Cost-transfer between Sol and Kael** is involuntary, non-redirectable, never a chosen buffer, never a felt bond used as a tool (brief rule 15). Not used at all in ch.24-31.
- **Dates:** Sunspire has 30 days. Ch.N = (N+8) Sunspire through ch.22 (30 Sunspire). From ch.23, ch.N = (N-22) Cinderveil (ch.27 = 5, ch.28 = 6, ch.29 = 7, ch.30 = 8, ch.31 = 9, ch.40 = 18, ch.43 = 21, ch.45 = 23). No 31 Sunspire, no "Brightward".
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
| 29 | Rewritten `4e894d54`, proofread `4e894d54` (same commit, no text edits needed). Sol POV, 7 Cinderveil, 2,340 words incl. header, ASCII clean, banned scan clean. |
| 30 | Rewritten (session 11), **PROOFREAD THIS COMMIT (session 12), no text edits needed.** Kael POV, 8 Cinderveil, 1,822 words incl. header, ASCII clean, banned scan clean, "not yet" used once. Cross-checked against ch.26-29's overcorrection-repair pattern: holds. |
| **31** | **REWRITTEN THIS COMMIT (session 12).** Sol POV, 9 Cinderveil, the standard reading at the house. Old draft (courtroom censure motion, "Lady Varel", "Disciplinary Board", "the vote would come in twelve days", Sol "photographing the Deed", an em dash) fully replaced. New content: four unnamed house-side chairs filled (steward, Aldous, a house clerk, one silent man in grey, never named); the standard read whole; Kael certifies nothing and says only what he read, into both books; Hold lifted on all five including Tam; Tam asks to sign the standard himself, unprompted, over Sol's unspoken hope he would hold out; Kael declines to decide for him either way; ends on Sol naming her own version of Kael's old pattern in herself. NOT YET PROOFREAD as a fresh read (written and reviewed in one pass, no separate proofread pass done yet). |
| 32-45 | UNCHECKED. Treat all as broken until read. Session 10 SKIMMED only openings and endings of 31-45 (see Findings, now partly stale for ch.31); a full sequential read of each remaining chapter is still required before it is rewritten. |

## Running canon by topic

**Council, Deed, clocks**
- Petition needs 8 of 12 houses; 8 have signed. Council needs 9 to set the Deed aside. Five signing houses must flip. Two signing houses asked Bram for copies of their own Schedule line (names not given). Four Schedule houses did not sign, Ashworth and Vane among them.
- Deed: pre-Accord instrument, sealed near-black wax, opened before the full Council 28 Sunspire ninth bell. 11 leaves + 6-leaf Schedule. Clause 7 (named contracts and all that follow pass to "the house administering reform"), clause 12 (that house's reading is final), clause 19 (takes effect on opening; unless 9 of 12 set it aside within THIRTY DAYS it is ratified). Thirty days lapse **28 Cinderveil**. Last line of the Schedule reaches contracts not yet written. Recital lists 33 Thorne dead, no Vane dead; the Vane block is added into Thorne's sum. Box kept in the clerks' strongroom; Renn holds a stamped fair copy.
- Kael refused to certify in chamber and owes a written finding at the public sitting in the THIRD WEEK of Cinderveil (that is where ch.40-43 land).
- Chain clock (ch.19): Renn's surveyor's chain (100 links, 10 pins, plumb, ~12 lb) sits on the pedestal-scale in the sublevel and balances Thorne's illicit tap on the Vault trunk line. Cycle is TEN breaths; falls to nine by mid-Cinderveil and to eight (surge, Lower Reach dark and flooded, 40-50 households) by end of Cinderveil if nothing is done. Malrik's order for shutting the tap safely is lodged UNOPENED with Renn (brass case, Thorne wax, Renn's strip). Honor or resolve at the climax.

**Sublevel and site facts (ch.12-15)** - unchanged since last version, see git history at `3ddce25c` for full detail if needed. Sealed hatch, dry spiral stair, vaulted chamber, tripwire lattice, iron Vault door, flooded gallery with an eleven-breath ward-line, Sol's cold-burned hands. Hooded Thorne watcher seen ch.11 and ch.11's dusk callback.

**Thorne people and archive (ch.16-20)** - unchanged, see git history at `3ddce25c` for full detail. Malrik, the steward, Aldous's "I did not" (OPEN), the archive visit, Sol's mother's contract, the private promise on the third landing ("Together. Before.").

**Thorne's engagement table (ch.21-31)**
- Annex withdrawn 28 Sunspire, reappeared as the awning table 29 Sunspire. Signer count held at 251 since the 3rd; FIVE held by the 7th (Tam among them). The flaw Kael and Sol use: the form promised consent "upon the standard as set" while no standard existed until now.
- **Ch.31: the standard was read whole at the house, 9 Cinderveil, seventh bell.** Four extra chairs on the house's side: the steward, Aldous, an unnamed house clerk, and one silent man in grey nobody named. Kael's exact answer, said aloud and entered in both books: "I have read it. I raise nothing against its wording. I certify nothing as to its fairness, or as to the manner of its adoption." The house lifted the Hold on all five regardless, calling the reading itself its answer. Kael separately entered, once, into both books: tonight's standard is not the one four hundred men signed. The five held men are freed. Tam, unprompted, tells Kael and Sol he wants to sign the new standard himself, citing his mother's ward-service and his own two readings of the terms; Kael refuses to decide for him either way ("That is not mine to decide. Or hers."; "Then it's yours to bring to the house. Not through us."). Sol, walking out, names her own version of Kael's old pattern: she wanted Tam held back, in her head, without ever saying so aloud, and did not stop him. This is new rupture material for ch.33-35, not a resolution.
- Withdrawal form: still unsigned by anyone, stack of ~200 printed early. Nobody has used it.

**Kael's and Sol's growth pattern (protect this)**
- Kael's failure mode is overcorrection, never concealment or lying. Ch.26 is the relapse; ch.27-30 show steady, unforced repair (asking before acting, telling first-hand, naming decisions in advance). **Ch.31 holds the line: Kael does not decide for Tam in either direction, matching his own repair rather than swinging to a new overcorrection.**
- Sol's own blind spot surfaces for the first time in ch.31: she recognizes that wanting to decide for Tam silently, even without acting on it, is the same shape as Kael's old pattern. This must not be resolved quickly. It is real material for the rupture, not a symmetrical "we're even now" beat.
- Sol's unspoken word FIRST (someone must sign the new standard first and prove it can be survived) is now COMPLICATED, not resolved: Tam may become that person, but by his own choice, not Sol's plan and not with her blessing. Keep this open and uncomfortable into ch.32+.
- The total: Sol's stance since ch.27 ("Every step held. It's the total I cannot sign.") stays unpaid. Not addressed directly in ch.31; do not let a later chapter resolve it before ch.33-35.

## Plan for ch.32 (author may override)

- Read the old ch.32 in full first before assuming it is broken (every chapter 31-45 has been broken so far on full read; do not assume ch.32 is the exception without checking).
- Material available to build from: the unresolved tension between Sol and Kael over Tam's choice; Mara's still-unresolved recovery; Renn still missing, entered as "not surveyed", commission sitting on the 12th; the third unexplained count Sol alone hears at the far ledge; the second ward-line under the boiling house; who is behind the iron door with the empty stool. Ch.32 does not need to resolve any of these, only advance one or two.
- Keep ch.33-35 rupture unresolved until then: no chapter before it may give Sol and Kael a settled, structural resolution of the overcorrection pattern OR of Sol's new self-recognition from ch.31.

## Open threads (do not resolve cheaply)

1. Who is behind the iron door in the boiling-house cellar (empty stool, opens for Thorne's clerks without a knock); whether it links to the sublevel. The forge stair runs to the same two-line water and "on below it" per Renn's chalk.
2. Copper Thorne link found on Renn's chain though the hatch seals were whole.
3. Aldous's "I did not" (ch.16, still open; his face at the ch.31 reading was not separately described, worth revisiting).
4. Who drew the standard originally; the two houses that asked Bram for their own Schedule line.
5. How the house learned of Tam's dawn question on Kael's own stair.
6. Mara's recovery (cold at the wrists, eyes open, unchanged as of ch.30); Kael's left leg and stick.
7. Sol's unspoken FIRST, now complicated by Tam's own choice (see above). Do not resolve early.
8. Anchor Seven pass (ch.8) and the archive pass (ch.16) are DIFFERENT passes, same date.
9. Renn missing, entered on the record, commission sits on the 12th. Sol holds his tally peg for the commission only. Keep him alive or dead for the author to decide.
10. The second ward-line under the boiling house (nine and eleven breaths) is not on Renn's survey. The third count only Sol hears (31, 34, 31) stays unexplained.
11. The man with the lantern and flat case on Tar Lane, night of the 4th: almost certainly Renn, unconfirmed.
12. How the house knew Kael and Sol were due back at the fifth bell on the 6th-7th crossing. Do not blame Bram, Joren or Ansa's boy.
13. What the house means to do with five men (now freed) after tonight, and whether Tam's own signing (if he goes through with it) becomes the very ward-taker trial the ending needs, or something the story must complicate first.
14. Who the silent grey man at the ch.31 reading actually was. Never resolve into a named Keeper (brief rule 11); keep it a quiet institutional hint if used again.

## Findings still live

- Name collision: missing clerk "Varel" vs House Varel (ch.7 "Lord Varel"). The ch.31 "Lady Varel" censure-motion reference is now GONE (chapter replaced), but ch.7's "Lord Varel" still needs checking against the missing-clerk name when ch.1-9 are circled back to.
- Ch.9 (after fix `4f2e1262`) says seven days since the Contract on 17 Sunspire; canon date math gives eight. Minor, fix when circling back.
- Seal wording still wrong in ch.1, 3, 5, 7. Ch.4, 6, 8 need a read, not only a grep.
- **Session 10 full read of ch.1-9 found old-canon conflicts beyond the seal (all unfixed):** Valerius Ashworth ALIVE and speaking (canon: dead, never appears alive); "the Nine Houses" and "forty-one for" (canon: TWELVE houses); Ashworth seal given as both "crossed hammers" and "griffin rampant" in different chapters; Kael already told by Valerius he starts "tomorrow" vs. ch.2's Council vote on 10 Sunspire; retired sites named (Kestrel's Hollow, Emberwatch). Treat ch.1-9 as unverified. Reconcile the Valerius alive/dead question with Book 1's own HANDOFF (which has it as an open decision, alive through Book 1 ch.40) before touching ch.1-2.
- **Session 10 SKIM (openings/endings only) of ch.32-45, NOT a full read, showed old-canon drift:** ch.33 ("Thorne banner, its black thorn on grey wool"); ch.34 (an empty Keeper's seat foreshadowed too early); ch.35 ("Clerk Valerius", 13 Cinderveil "Thorne's decree advanced"); ch.36 ("co-equals" as the ending, but cession is ch.39 ONLY); ch.37 ("Silver thorn on black field", "twelve ward-houses"); ch.39 ("formal notice three days past" on 17 Cinderveil; a name "Dallin Vorys"); ch.40 ("Thirty-seven" banners); ch.41 ("nine houses that still held seat", "Hestia"); ch.43 ("House Thorne in black and burnt orange", 4,412 words, longest chapter); ch.44-45 short, end on the Keeper's seat, ch.45 still needs the "I love you" fix (Kael first, forge on Tar Lane, at Renn's chalk, per ch.28). Em dashes appear in several endings. Each needs a full sequential read before it is rewritten.
- Grep ch.32-45 for: Embervein, Veyra, Veldt, Mirelle, Hest (also hits "chest"), Councilor Thorne, "seventeen Sunspire", "thirteen", Voss, Kestrel/Maraen jurist, gondolas, "Marius", "Hale", Cressida, Elsbeth, Merrow, Hestor, fox, crimson, thorn-and-crown, "31 Sunspire", "thirty-first", "Hall of", "Lady Varel", "Disciplinary Board", "twelve days".
- Ch.40-43: watch Thorne's line so no named lord repeats it verbatim.
- Keeper: quiet institutional hints only (the Deed's drafter, early-printed withdrawal leaves, the clerks knowing the boiling-house line's dark, now the unnamed grey man at ch.31's table). Never name a person.
- Do not invent Accord article numbers or section numbers. Do not invent how long Kael has loved Sol or how long they have been together.

## Process notes

- Re-list `main` and re-fetch this file at the START of every turn; check each new commit's `files` (get_commit) before assuming it touches this book.
- `raw.githubusercontent.com` WORKS from the sandbox via `curl`. Fetch the raw chapter, run `wc -w`, `grep -cP '[^\x00-\x7F]'`, the banned-term grep, and compare `git hash-object` against the SHA from the contents API. The unauthenticated `api.github.com` from the sandbox is rate-limited (use the GitHub tool for listings).
- Before each chapter: read charter, this file, `brief.txt`, the chapter before, and the OLD chapter in full. Assume the old draft is broken; replace, do not patch.
- Defect categories to scan every unchecked chapter for: wrong magic system, invented soulbond (brief rule 15), wrong Thorne seal, front-loaded plot, non-Latin/corrupted characters, under the word floor, chapter-number meta-references, meta breaks, duplicated resolution of a locked beat.
- Also scan for physical-object continuity, timeline claims in slates/notes/bells, and repeated stock phrases ("in the order it happened" is Kael's motif, used ch.26 and ch.30; do not overuse).
- `kindling-line-book-2_full_manuscript.md` is OUT OF SYNC with `chapters/`; regenerate at the very end.
- Em-dash pass and full-book banned-word scan come after structure is fixed, not before.
- Repo `aliwaziri10/Voxel`, default branch `main`.

## Progress log

- 2026-09-28 (earlier sessions): ch.10-25 rewritten/proofread; canon lock established.
- 2026-09-28 (session 7): rewrote ch.26 (`5094d342`).
- 2026-09-28 (session 8): rewrote ch.27 (`1f979258`).
- 2026-09-28 (another profile): rewrote ch.28 (`19b26601`).
- 2026-09-28 (session 9): proofread ch.28, stamped ch.27/28 (`3ec6e9a9`).
- 2026-09-28 (session 10): read ch.1-29 in full, skimmed ch.30-45; rewrote ch.29 (`4e894d54`); recorded ch.1-9 and ch.31-45 findings.
- 2026-09-28 (another profile, Book 1 only): four commits touched `kindling-line-book-1` only, nothing here.
- 2026-09-28 (session 11): proofread ch.29 (no edits needed); rewrote ch.30 (Kael POV, 8 Cinderveil, 1,822 words), not yet proofread at handoff.
- 2026-09-28 (session 12): re-listed main, found session 11's ch.30 rewrite. Proofread ch.30 (no text edits needed). Read old ch.31 in full, confirmed it matched the session-10 skim finding (courtroom censure motion, entirely disconnected from established plot) and fully rewrote it as the standard reading at the house. Next: read old ch.32 in full and rewrite or confirm clean.
