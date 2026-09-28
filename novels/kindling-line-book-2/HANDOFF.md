# HANDOFF - Kindling Line Book 2 Polish Pass

Read `../EDITORIAL_CHARTER.md`, then this file, then `brief.txt` and `CONTINUITY_PLAN_ch10-20.md`. Update this file in the SAME commit as any chapter edit (`push_files`, both files, one call). Quality only, no budget constraint. Strict sequential order. Never strip em dashes on a structurally broken chapter; fix structure first.

**This file was condensed on 2026-09-28** (was ~48 KB). The full verbose per-chapter canon for ch.11-25 is in git history at commit `3ddce25c9ba9ab1f662810b20329325fbfbb13bb`. Everything a later chapter must honor is kept below, grouped by topic instead of by chapter. Keep it short: after each chapter add 2-4 lines to the topic blocks and one line to the log, do not write a new per-chapter essay.

## Canon lock (do not deviate)

- **Site:** Anchor Seven (Lower Reach ropewalk sublevel). The ch.13-15 infiltration happens ONLY here. Retired sites: Lower Ward Annex, Graywater Hollow, Greyledge, Embervein, "three miles north", any waystation.
- **Thorne seal, only correct wording:** three strands, unbroken, knotted; a drop, a flame, a feather at each terminus; house colors violet and copper; wax dark, near-black. No red wax, crown, vine, hawk, viper, ivy, tower, thorn, fox, motto. Malrik's own clasp is plain silver, no device.
- **Scripted line** ("I'm not asking you to tell me everything. I'm asking you to stop deciding what I don't need to know.") is USED ONCE, in ch.16. Never repeat it verbatim; a short callback at most.
- **Deed's legal meaning** was fully understood in ch.20. From ch.21 on it is known; do not re-explain it as news.
- **Thorne's line** ("A house that has already paid the cost has earned the right to control who pays it next") spoken by Malrik ch.1, echoed by the steward ch.15. Do not have a named lord repeat it verbatim again.
- **Formal co-lead / cession of authority is ch.39 ONLY.** Ch.17 gave a private promise only ("Together. Before."). Ch.28 must not say "Equals, starting now" as a settled resolution.
- **Cost-transfer between Sol and Kael** is involuntary, non-redirectable, never a chosen buffer, never a felt bond used as a tool (brief rule 15). Not used at all in ch.24-26.
- **Dates:** Sunspire has 30 days. Ch.N = (N+8) Sunspire through ch.22 (30 Sunspire). From ch.23, ch.N = (N-22) Cinderveil (ch.26 = 4, ch.40 = 18, ch.43 = 21, ch.45 = 23). No 31 Sunspire, no "Brightward".
- **Style bans:** no em/en dashes, no "particular", no "some/something/someone/somebody", no "kind of", no "the specific". No chapter may name a chapter number in prose. Word floor 1,800 (count real text with `wc -w` incl. header). Bells always need a time-of-day cue.
- **Names:** Kael Ashworth (Auditor; father Valerius is DEAD, never appears alive), Isolde "Sol" Vane ("my lady" to clerks), Lord Malrik Thorne, grandson Aldous (~25), Thorne's unnamed steward (woman past sixty), Keeper Cormac Vrell (archive), Renn (Council surveyor), wardens Joren (scar on hand) and Mara (20 years, NO surname), Ansa (old splicer, over the tar-shop), Tam (~20, her sister's son), Bram (junior clerk), Varel (missing clerk, now alive under Council protection). Chancellor is an old woman; the Council has TWELVE houses. Never use Marius, Hale, Cressida, Hest, Veyra, Mirelle, Voss.

## Status (verified against live files 2026-09-28)

| Ch | State |
|----|-------|
| 1-9 | Called clean earlier, but wrong seal wording still live in ch.1 (l.29 "thorn wrapped in chain"), ch.3 (l.45, 57, 121), ch.7 (l.5, 49, 57, 65). Read ch.2, 4-6, 8-9 too, not only by grep. Fix when circling back. |
| 10 | Clean (`d0723906`) |
| 11-14 | Rewritten + stamped: `f129fd09`, `9f7ea6de`, `1dda53d6`, `f18a859c` |
| 15-16 | Rewritten + stamped `1d256b1b`, `1aae27fd` |
| 17 | `4266126a` ("two days ago" fix) |
| 18, 19, 20 | `9a3b65f7`, `14225a5e`, `050b0c73` |
| 21 | `d206fd1f`, proofread `6f2d43b5` |
| 22, 23 | `41b77585`; ch.23 + ch.22 date fix `ee2a9683` |
| 24, 25 | `9d977810`, `3ddce25c` |
| **26** | **REWRITTEN + STAMPED this commit.** Kael POV, 4 Cinderveil, 1,866 words by `wc -w` incl. header (first draft 1,868; three canon fixes, no expansion needed). Zero non-ASCII, banned-term scan clean, no old-canon names, no scripted line. Old ch.26 (bot draft: Valerius alive in Council, "Marius" Thorne speaker, Warden Hale, crimson Thorne seal and fox, Sol petitioning co-lead "effective immediately", first "I love you", cost-transfer as felt heartbeat, messenger with a full cascade) fully replaced. Byte compare against live file NOT run; verify via the contents API next session. |
| 27-45 | UNCHECKED. Treat all as broken until read. Sampled earlier: 28 (has the repeated scripted line and "Equals, starting now"), 35 (good rupture, wrong seal), 39 (good repair + first intimate scene, wrong seal), 45 (good Keeper ending, "thorn-and-tower" seal, mis-remembers the first "I love you" as a rebar tear in a site collapse). |

## Running canon by topic

**Council, Deed, clocks**
- Petition needs 8 of 12 houses; 8 have signed. Council needs 9 to set the Deed aside. Five signing houses must flip. Two signing houses asked Bram for copies of their own Schedule line (names not given). Four Schedule houses did not sign, Ashworth and Vane among them.
- Deed: pre-Accord instrument, sealed near-black wax, opened before the full Council 28 Sunspire ninth bell. 11 leaves + 6-leaf Schedule. Clause 7 (named contracts and all that follow pass to "the house administering reform"), clause 12 (that house's reading is final), clause 19 (takes effect on opening; unless 9 of 12 set it aside within THIRTY DAYS it is ratified). Thirty days lapse **28 Cinderveil**. Last line of the Schedule reaches contracts not yet written. Recital lists 33 Thorne dead, no Vane dead; the Vane block is added into Thorne's sum. Box kept in the clerks' strongroom; Renn holds a stamped fair copy.
- Kael refused to certify in chamber and owes a written finding at the public sitting in the THIRD WEEK of Cinderveil (that is where ch.40-43 land).
- Chain clock (ch.19): Renn's surveyor's chain (100 links, 10 pins, plumb, ~12 lb) sits on the pedestal-scale in the sublevel and balances Thorne's illicit tap on the Vault trunk line. Cycle is TEN breaths; falls to nine by mid-Cinderveil and to eight (surge, Lower Reach dark and flooded, 40-50 households) by end of Cinderveil if nothing is done. Malrik's order for shutting the tap safely is lodged UNOPENED with Renn (brass case, Thorne wax, Renn's strip). Honor or resolve at the climax.
- Hearing 24 Sunspire: no vote while the Deed lay unopened. Malrik WANTS it opened and has for years; keep that menace. Malrik's offer to Kael (state "good faith") was answered publicly by Sol's plan: Kael reports what he verified, certifies no good faith or stewardship.

**Sublevel and site facts (ch.12-15)**
- Sealed hatch at far end of the ropewalk gallery; dry spiral stair; vaulted chamber (blue ward-lamp, table, Varel's ledger); tripwire lattice; iron door with seven-ring Vault lock plate topped with copper-and-violet knot; short stair to a long flooded gallery with a buried ward-line, charge cycle about eleven breaths (safe on the drop, dangerous on the swell); arch, alcove, pedestal-scale.
- Ledger: charge drawn through an illicit tap for THREE years (older hand) plus six weeks of Varel's entries. Varel: thin, ~40, ink on knuckles, watched the meter under Thorne's three violet retainers, does not know what the charge is for.
- Council sublevel guard; Ashworth wardens keep the ropewalk floor. Order to wardens (ch.11): they do not enter unless either Kael or Sol signals; then they come fast and armed; nothing goes upstairs without both names.
- Ch.15 cost: Sol's palms and fingers cold-burned by a swell up a wet rope; both hands.
- Hooded Thorne watcher (copper cloak clasp with the knot) seen ch.11 and again on the rope bridge at dusk 24 Sunspire. Fresh knife-scratched "Seven" on the rope-bridge post.

**Thorne people and archive (ch.16-20)**
- Malrik: white hair, deep grey dress, plain silver clasp, stands unaided, smaller than Kael remembered. Steward: small, upright, grey, copper clasp with the knot; institutional, never a named lord. Aldous went white at the Lower Spine leaf of the Schedule and shaped "I did not" before the steward's fingers settled on his sleeve (OPEN).
- Archive (25 Sunspire): six retainers on the stair. Vrell wrote Sol into the gate ledger himself ("Isolde Vane, bearer, second"). Sol read three volumes of Thorne's ward-service ledgers (dead marked in oak-gall and rust ink). Sol's mother's contract (Vane spine, green leather): ward-taker, term "until dissolution of the trade or death of the bearer", dependents schedule "Isolde, daughter, age 8", countersigned by a Thorne steward. Character only, no plot hook.
- Supper (26 Sunspire): Sol fed without cutlery (cup, torn bread, cut cheese, pear). Kael ASKED before helping. Kael said "Not at this table, and not alone."
- Private promise (25 Sunspire, third landing): "From here. No more passes I haven't seen. No more days I hear about after." / "Together. Before." Sol's terms: any future pass shown to her before use.

**Thorne's engagement table (ch.21-25)**
- Annex (contract standard) withdrawn from the petition at noon 28 Sunspire, then reappeared as a violet awning, two clerks and a brazier at the foot of the LOWER SPINE STAIR (29 Sunspire). "Provisional Engagement of a Ward-taker under the Standard of the House Administering Reform": wage from 1 Cinderveil, lamps kept, term "until dissolution of the trade, or death of the bearer", dependents line, last line "Consent of the holder, given freely, upon the standard as set." About 400 ward-takers on the Reach.
- Signer counts (Ansa's slate): 31 (29th), 69 in two days, 143 (1st), 214 (2nd), **251 by the lamps of the 3rd (only 37 that day)**.
- Kael certifies nothing; the Accord's transfer article needs holder consent OR auditor certification. The clerk first said "The Auditor has read the standard and raised nothing", then after Kael's public disclaimer "has been asked" (true, heard as "has looked"). Thorne method: the true sentence heard as a false one. Do not run this a fourth time unchanged.
- Withdrawal form: leaver writes consent was given freely, swears no officer of the Accord advised him, forfeits future engagement for self and named dependents. A stack of about 200 was printed days early (implies foreknowledge). Nobody has signed it.
- **Hold (3 Cinderveil):** Tam and two unnamed men served "Notice of Hold" (no wage from the 3rd, "the house will advise"), the exact three who asked to read the terms at dawn on 1 Cinderveil. The table's book records every request to read the standard with the hour; Kael's own request (30 Sunspire, fourth bell of the morning) heads it. Tam keeps his name ("Tell the Auditor thank you for the no"). Sol's receipt on the back of Tam's Notice: "Received of Tam, one Notice of Hold... I.V."; **Kael signed beneath it at Ansa's on the evening of the 3rd: "Seen, and copied. K. Ashworth."** Tam: "Your name under hers. I asked for it, and you've done it. The bread I'll manage."
- How the house knew of Tam's question on Kael's own stair is UNRESOLVED (do not make Tam or Ansa the leak cheaply).

**Kael's and Sol's growth pattern (protect this)**
- Kael's failure mode is overcorrection, never concealment or lying. He tells Sol after, every time. Ch.20-25 show growth: asking before helping, telling before acting, naming the "clean" sentence and not saying it (ch.24), Sol refusing to decide for Tam (ch.25). His written statement of 1 Cinderveil and Sol's witness ("Isolde Vane" in a child's hand) stand.
- Sol's unspoken word is FIRST: someone must sign the new standard first and prove it can be survived (seed for the ch.40-43 ward-taker trial). She has NOT said it to Kael. Do not resolve early.
- Sol's hands: last linen off 1 Cinderveil; grey wool gloves lined with linen, fingers in to the second joint; does her own coat buttons; child-sized handwriting on a thick splicer's pen; Ansa says rope back by the 5th; knife barred until then. From ch.27 show only what changes.

**Ch.26 events (ch.27 onward must honor)**
- Morning of 4 Cinderveil: Renn's note (book FOUR of nine, year before the Accord sealed): the boiling house behind the old ropewalk shows a cellar and smiths' stair struck through in a second ink; no level named; he will read the fifth and sixth by evening; "Do not go looking." Ansa's slate: clerks carried the book and a bundle down the boiling-house yard at lamp-lighting and came back empty; a carter is hired for the noon bell. Kael handed Sol Renn's strip unasked.
- Second bell of the morning, senior clerk (bald grey, ink to the wrist): the table's book is a paper of the petitioner until ratification; the petitioner filed a notice at first bell to cart the book and papers to the house at the top of the Reach at the NOON bell; the office enters an objection, read at the sitting of the third week; a motion needs a sponsoring house and a second; the office has not been shown the book.
- Sol's healer sent for her (glove fitting, kept till noon). Sol's plan: "Noon, then. In the yard, together, with Mara and Joren at the gate." Kael did NOT say yes; he noticed and went anyway. He left a note against the teapot ("Gone to look at the boiling-house cellar. Mara at the yard gate. Back before noon, and I will tell you all of it. K."): honest, no concealment, but a receipt for a decision already taken.
- Kael told Mara (ropewalk floor): hold the gate, do not come down unless I call.
- Boiling house: black, roofless, leaning chimney, tarred ground. Cellar door new oak on old stone, oiled hasp hanging open, palm-sized three-ring lock plate with the copper-and-violet knot. Twelve cart-wide dry steps; a room "the length of a chapel" under two fingers of black water; a buried ward-line whose cycle Kael could not read (nine, eleven, nine breaths); ward-lamp over an iron door with an enamelled knot; a violet thread on a rusted bracket and fresh lamp oil; a stylus scratching behind the door.
- Kael stepped onto the swell: left leg dead below the hip, ears ringing. He called "Mara!" once. Mara ran down, was taken at the heels by the next swell, fell forward, is UNRESPONSIVE (blue lips, thin slow breath, eyes open seeing nothing, hands cold as iron). Kael dragged her onto the stair with his good arm. No cost-transfer used. Ch.26 ends: the stylus stopped, then a knuckle rapped twice on the INSIDE of the iron door, patiently. Hook type: an unseen presence (previous: ch.25 implied threat, ch.24 anticipated counter, ch.23 plea).
- Sol has NOT been told yet. Kael's left leg and Mara's condition are the cost. Do not cure either cheaply.

## Plan for ch.27-28 (author may override)

- **Ch.27 (5 Cinderveil, Sol POV):** read old ch.27 first and assume it is broken (it calls Thorne's heir "Cressida"). Sol learns of the descent from the note or from Joren or Kael himself and hears everything from Kael (he tells all, no excuses). Mara's condition on the page (healer, unresolved). What does Sol do with her anger without deciding for him? Do NOT restage the old ch.25 infirmary scene and do NOT have Sol say the scripted line. Noon in the yard: the cart. Keep the reveal of who knocked open.
- **Ch.28 (Kael POV):** the first "I love you" (delivered or interrupted by fallout), not a first kiss. Strip the old "Equals, starting now. No unilateral decisions" line and the repeated scripted line; the promise here is personal and fragile, leaving room for the ch.33-35 rupture and the ch.39 formal cession.
- Later landmarks: ch.31 Sol/Kael before the Council (Lady Varel name issue); ch.33-35 rupture must stay unresolved; ch.38-39 repair then first on-page intimate scene; ch.40 check for chapter-number references; ch.41 cost-transfer stays involuntary; ch.45 Keeper reveal institutional, fix seal, fix the misremembered first "I love you".
- Petition arithmetic and the ch.40-43 exposure must answer "every signature was lawful" (candidate: consent given freely upon a standard not yet set, procured by a false statement about the auditor's reading; the table's book as hold list). AUTHOR DECIDES.

## Open threads (do not resolve cheaply)

1. Who is behind the iron door in the boiling-house cellar; whether it links to the sublevel (the copper link and the "second way in").
2. Copper Thorne link found on Renn's chain (101 links) though the hatch seals were whole; Chancellor's clerk fetching the survey books; Renn has read four of nine.
3. Aldous's "I did not".
4. Who drew the standard (annex "on a desk off the record"); the two houses that asked Bram for their own line.
5. How the house learned of Tam's question; who the two other held men are.
6. Mara's recovery; Kael's left leg.
7. Sol's unspoken FIRST.
8. Anchor Seven pass from ch.8 (decommissioned vs contested) and ch.16's archive pass are DIFFERENT passes, same date; do not confuse them.

## Findings still live

- Name collision: missing clerk "Varel" (ch.10-15) vs House Varel (ch.7 "Lord Varel", ch.31 "Lady Varel" leading the censure motion against Sol). Decide: rename the clerk or make him a minor disaffected relation.
- Ch.31 says Sol "photographed the Deed" and hid it in a site "the Accord forgot existed": contradicts the chain of custody (sealed, Renn-stamped, opened only before the Council, text read aloud). Rework any "secret Deed" reveal.
- Ch.9 says "nine days" since the Contract on 17 Sunspire (should be eight). Minor.
- Grep ch.27-45 for: Embervein, Veyra, Mirelle, Hest (also hits "chest"), Councilor Thorne, "seventeen Sunspire", "thirteen", Voss, Kestrel/Maraen jurist, gondolas, "Marius", "Hale", Cressida, fox, crimson, thorn-and-crown, "31 Sunspire", "thirty-first".
- Ch.31 and ch.40-43: watch Thorne's line so no named lord repeats it verbatim.
- Sol's honorific "my lady" (Bram, Renn, the senior clerk) and Kael "Auditor": confirm when circling back through ch.1-19; Ansa calls Sol "Sol" or "girl"; do NOT invent Ansa knowing Sol's mother unless ch.1-19 already say so (grep "Ansa").
- Keeper: the Deed's drafter had read the Accord's dissolution schedule before the Accord sat, and Thorne printed withdrawal leaves days early. Both are quiet hints of an institutional office. Never name a person (brief rule 11).
- Ch.33 rupture must not be pre-empted: no chapter before it may give Sol and Kael a settled, structural resolution.
- Do not invent Accord article numbers or section numbers.

## Process notes

- Verify before trusting: re-fetch via the GitHub contents API (raw.githubusercontent may serve stale copies right after a push). Sandbox has no network, so word counts are taken on the drafted text before push.
- Count actual text with `wc -w` (byte estimates were wrong before).
- Before each chapter: read charter, this file, `brief.txt`, the chapter before, and the OLD chapter in full. Assume the old draft is broken; replace, do not patch.
- Defect categories to scan every unchecked chapter for: wrong magic system, invented soulbond (brief rule 15), wrong Thorne seal, front-loaded plot, non-Latin/corrupted characters, under the word floor, chapter-number meta-references ("chapter 8" once appeared in narration), meta breaks ("the brief", "this book"), duplicated resolution of a locked beat.
- `kindling-line-book-2_full_manuscript.md` is OUT OF SYNC with `chapters/`; regenerate at the very end.
- Em-dash pass and full-book banned-word scan come after structure is fixed, not before.
- Repo `aliwaziri10/Voxel`, default branch `main`.

## Progress log

- 2026-09-28 (earlier sessions): ch.10-25 rewritten/proofread as in the status table; canon lock established; continuity plan `CONTINUITY_PLAN_ch10-20.md` executed through ch.25.
- 2026-09-28 (session 7): account verified (`aliwaziri10`); confirmed head was `3ddce25c` and that only one profile works at a time; read charter, HANDOFF, brief, ch.14 (spot check: no chapter-number meta line, correct seal) and old ch.26 in full. Old ch.26 replaced with a Kael-POV rewrite (solo descent, Mara hurt, Kael's leg). HANDOFF condensed from ~48 KB. Chapter + HANDOFF in ONE commit. Next: ch.27 (5 Cinderveil, Sol POV; read old ch.27 in full first).
