# HANDOFF - Kindling Line Book 2 Polish Pass

Read `../EDITORIAL_CHARTER.md` first, then this file, then `brief.txt` and
`CONTINUITY_PLAN_ch10-20.md`. Update this file in the SAME commit as any
chapter edit. Quality only, no budget constraint. Never strip em-dashes on a
structurally broken chapter; fix structure first. Strict sequential order.

## Canon lock for ch.10-20 - do not deviate

- **Site:** Anchor Seven (Lower Reach ropewalk sublevel). Ch.13-15
  infiltration happens ONLY here. No other site (not Lower Ward Annex, not
  "three miles north," not Graywater Hollow, not Greyledge, not a waystation).
- **Thorne seal, the only correct wording:** three strands, unbroken,
  knotted; a drop, a flame, a feather at each terminus; house colors violet
  and copper; wax dark, near-black. No red wax, no crown, no vine, no hawk,
  no viper, no ivy, no towers, no motto.
- **Scripted line** ("I'm not asking you to tell me everything. I'm asking
  you to stop deciding what I don't need to know.") belongs ONLY to ch.16-18.
  It is now USED, once, in ch.16. Ch.17 and ch.18 must NOT repeat it.
- **Ward Deed's full legal meaning** (clause 7/12/19 chain) is understood
  ONLY in ch.20. Ch.13-19: discovered, not understood, not opened. DONE in
  ch.20 (see canon block below); ch.21 onward may refer to it as known.
- No chapter may reference its own or another chapter's number in prose.
- Months in this book are Sunspire (30 days) then Cinderveil. There is no
  "Brightward." Header dates run one chapter per day: ch.N is (N+8) Sunspire.
- No em dashes, no "particular", no "some/something ___" hedges.

## Status (verified against live files 2026-09-28)

- **Ch.1-9:** earlier sessions called them clean, BUT a seal scan this session
  found wrong seal wording still live (see finding 11). Fix when circling back.
- **Ch.10:** clean. Raw `<!-- chapter_date -->` header restored, `d0723906`.
- **Ch.11:** REWRITTEN + STAMPED, `f129fd09`. 2,130 words.
- **Ch.12:** REWRITTEN + STAMPED, `9f7ea6de`. 1,834 words.
- **Ch.13:** REWRITTEN + STAMPED, `1dda53d6`. 1,865 words.
- **Ch.14:** REWRITTEN + STAMPED, `f18a859c`. 1,852 words.
- **Ch.15:** REWRITTEN + STAMPED, `1d256b1b`, corrected in `1aae27fd`
  (warden signal matches ch.11, sheaves counted at the hatch, steward's line
  framed as Malrik's). 2,298 words verified live.
- **Ch.16:** REWRITTEN + STAMPED, `1aae27fd`. 2,018 words verified live.
- **Ch.17:** REWRITTEN + STAMPED, then corrected in `4266126a` ("yesterday"
  became "two days ago", since Kael's archive visit was 23 Sunspire; Sol's
  healing-hands beat added). 1,841 words verified live.
- **Ch.18:** REWRITTEN + STAMPED, `9a3b65f7`. 1,950 words verified live
  (byte-identical to draft, no dashes, no banned terms).
- **Ch.19:** REWRITTEN + STAMPED, `14225a5e`. 1,905 words verified live.
- **Ch.20:** REWRITTEN + STAMPED, `050b0c73`. Kael POV, 28 Sunspire. 1,867
  words by `wc -w` on the draft including the header comment (about 1,856
  body). Draft scanned before push: zero non-ASCII characters (so no em or en
  dashes), no banned terms, no wrong seal wording. Push confirmed by commit
  stats (one file, +43/-247). Byte-level re-fetch compare NOT run (sandbox has
  no network); next session should re-fetch via the contents API to confirm.
  Old ch.20 (crimson thorn-bush seal, invented Council cast, replayed coat
  pass, 4,190 words) fully replaced, not patched.
- **Ch.21-45:** UNCHECKED. Treat all as broken until verified.

## Canon added by the ch.11-14 rewrites (ch.15 onward must honor)

- Council granted the petition: both names (Ashworth and Vane), entry to
  Anchor Seven's sublevel from first bell 21 Sunspire through 23 Sunspire.
  Renn (surveyor, Council survey commission) is UNDERGROUND with them and
  stamps copies of evidence with his commission, hour and date.
- Thorne moved its reform hearing from 21 to 24 Sunspire, citing Kael's
  "forthcoming report" (none exists). An eighth house signed (ch.12), so the
  24th hearing includes the VOTE (eight of twelve).
- Two Ashworth wardens (Joren, scar on hand; Mara, 20 years' service) hold the
  ropewalk floor and answer jointly to Kael and Sol. ACTUAL ch.11 order:
  they do not enter the sublevel unless either of them signals; if either
  signals they come fast and armed; nothing they see goes upstairs without
  both names.
- Hooded Thorne watcher shows itself in daylight, copper cloak clasp with the
  Thorne knot; fresh knife-scratched "Seven" on the rope-bridge anchor post.
- Ansa (old splicer, lives over the tar-shop) will tell Kael and Sol, not
  "the copper-collared lot," if Varel returns.
- Site (ch.12-14): sealed hatch at far end of ropewalk gallery; spiral stair
  dry to the second landing (pumped for years); vaulted chamber with blue
  ward-lamp, table, blanket, Varel's ledger; three passages, they took LEFT;
  tripwire lattice with piggyback trigger and ward-sleep dart trap; iron door
  with seven-ring Vault lock plate topped with polished copper-and-violet
  Thorne knot enamel; short stair down to a long flooded GALLERY with a buried
  ward-line whose charge cycles about every eleven breaths (safe on the drop,
  dangerous on the swell); low arch, alcove, pedestal.
- Ledger shows charge drawn from the Vault's main trunk line through an
  illicit tap, metered for THREE years (older hand) plus six weeks of Varel's
  entries. If the meter stops balancing, the trunk line surges back up the tap
  and hits the Lower Reach (Ansa's tar-shop, splicing halls, tenements, 40-50
  households): lights out above, flooding below.
- Varel is ALIVE (ch.14): thin, about forty, ink on his knuckles, terrified;
  ward-trade clerk under the old system, minor clerk under the Accord;
  Thorne's three retainers in violet made him watch the meter ("they gave me
  a blanket"); Thorne came every night at the tenth bell except the night of
  21 Sunspire. He wrote the note and the hidden ledger entries. He does NOT
  know what the charge is for.
- The Deed is FOUND (ch.14) in a lead-lined oak box bound in iron on the
  pedestal, lid wax (Thorne knot, near-black) UNBROKEN; only the vellum
  wrapper title "Ward Deed of Succession", a date, a signature line and the
  seal are visible through a sprung iron band. Nobody has read it.

## Canon added by the ch.15 rewrite

- Timeline: standoff begins at the tenth bell of 22 Sunspire; the climb out
  ends at first bell, so the header reads 23 Sunspire.
- Thorne's steward (unnamed, woman past sixty, small, upright, grey hair,
  copper clasp with the Thorne knot, three retainers in violet with
  copper-tipped staves). Institutional, never a named lord. She echoes Lord
  Malrik Thorne's line from ch.1 ("A house that has already paid the cost has
  earned the right to control who pays it next"), framed as "an accounting,"
  not pride. Brief rule 1 is satisfied by Malrik himself in ch.1; the steward's
  use is a house refrain. Exit line: hearing on the 24th will decide "which of
  us the Reach can afford."
- The pedestal is a SCALE. The box weighs 12 lb (Varel: an iron ingot of 12
  lb was set on it twice when Thorne changed the lid wax). Lifting the box
  shortened the swell cycle from 11 breaths to 8 and the tap began to surge.
- Stabilized with Renn's surveyor's chain (100 links, 10 pins, a plumb, about
  12 lb), hauled across on the rope and laid on the pedestal. Cycle now TEN
  breaths, not eleven. The chain is still on the plate. Thorne's illicit tap
  keeps running, balanced by the Council's own chain. Carry this irony.
- COST: Sol's palms and fingers (both hands) are cold-burned by a swell that
  ran up the wet rope: white, then red, long welts heel to fingertips, bound
  in strips of Kael's shirt, then healer's linen and grey salve. She cannot
  grip a knife, pen or rope for days. Every chapter must show her hands
  healing. Kael asked before helping; "I hate that it was you."
- Either voice brings the wardens (ch.11 order). In ch.15 Kael and Sol chose
  to call together, "Joren!" "Mara!"
- Renn's stamped copies: two sheaves went up on 22 Sunspire (noon, dusk),
  each counted and signed for by Warden Mara at the hatch.
- Renn laid a strip of Council wax across the lid seam beside Thorne's
  unbroken wax, pressed his commission seal, cut "Twenty-three Sunspire.
  First bell. Unbroken." Varel walked out with them.

## Canon added by the ch.16 rewrite

- HEARING, 24 Sunspire, ninth bell, Council chamber. Kael states there is NO
  report, only a short finding: the illicit tap, three years, the two-hand
  ledger, Renn's stamped copies, Varel under Council protection, the Thorne
  knot lock plate. Malrik Thorne (white hair, deep grey, silver clasp, on his
  grandson's arm) answers: Thorne kept the Lower Reach lit, "does not
  apologize for lamps," does not fear the box, and asks the Council to OPEN
  it. Sol (hands bandaged) testifies the plate is balanced by the Council's
  own chain. The Chancellor (a woman, voice thin with age) rules: no vote
  while an instrument sealed in the claimant's wax lies unopened in Council
  custody. VOTE HELD. The Deed will be opened before the full Council at ninth
  bell on 28 SUNSPIRE (ch.20's date), seals examined by Council clerks.
  Sublevel under Council guard, chain stays, Ashworth wardens keep the
  ropewalk floor.
- Kael's read: Malrik WANTS the box opened and has for years. Do not lose
  this menace. (Consistent with the Deed being Thorne's own legal instrument.)
- The coat pass: "Entry pass. The Precedent Archive of House Thorne, lower
  gallery, western face. Twenty-three Sunspire. Bearer, Kael Ashworth,
  Auditor." Kael told Sol he would file Renn's sheaves at the clerk's desk
  while she sat with the healer; he did, for an hour, then went to the archive
  alone. The scripted line is spoken; Kael admits without denial or excuse.
  Reasons: the steward's speech, and Sol's burned hands.
- What Kael found: Thorne's own ward-service ledgers, three generations, by
  name and year, the dead marked in ink. The grievance is real. He read
  NOTHING about the Deed. He did NOT take down the Vane shelf (growth beat).
- Sol's terms (private, no Accord filing): back to the archive together at
  first bell 25 Sunspire; she reads what she chooses; any future pass is
  shown to her BEFORE use.
- Ch.16 ends: hooded watcher with copper clasp on the rope bridge between the
  spires at dusk, looking at their window, then walking away.

## Canon added by the ch.17 rewrite (ch.18 onward must honor)

- 25 Sunspire, first bell. The archive stair on the western face now has SIX
  Thorne retainers in violet (there were two when Kael came). Keeper Cormac
  Vrell: narrow, pale, dark hair drawn back, grey scholar's robes with violet
  piping; courteous, never hostile, "keeps the records, does not draft the
  petitions." He wrote Sol's name in the gate ledger himself ("Isolde Vane,
  bearer, second") because she cannot hold a pen.
- Vrell delivered Lord Malrik's message: read ALL the ledgers before the
  Council opens the box; Malrik would rather be opposed by a reader than
  admired by one who has not. Sol's reply: she will read every page and
  oppose him anyway; both are true and should be recorded. Vrell: "It is
  recorded."
- Thorne ward-service ledgers: three volumes. Details on the page: a warden
  of the Lower Spine dead at 31, two brothers seven years apart, a girl of 15
  contracted to the eastern line ("did not come home"), red-brown ink dots
  beside each death. Sol read volumes 1-3 over two hours.
- SOL'S MOTHER'S CONTRACT (Vane spine, cracked green leather, fourth tier):
  ward-taker, House Vane, term "until dissolution of the trade or death of
  the bearer." A Dependents schedule in the mother's own quick forward-leaning
  hand: "Isolde, daughter, age 8." Counter-signature by a Thorne steward:
  "Received for the works of the Lower Spine, House Thorne," with the knot in
  near-black wax. Sol's mother and Thorne's wards were on the SAME line of the
  same system. Kael turned the pages on her word (she cannot). Vrell says this
  is why the pass was extended; Malrik thinks the trade made the houses
  "neighbors." A copy of the page and the next, under the archive's seal, is
  to reach Sol by noon. NO plot hook here; it is character only.
- Thorne has petitioned the Council for a custodial role over its own
  precedents; Vrell: "The house is watching everyone. It learned the habit
  from being watched."
- PRIVATE PROMISE at the third landing: "From here. No more passes I haven't
  seen. No more days I hear about after." Kael: "Together. Before." Not
  formal, not recorded. Formal cession is ch.39.
- Ch.17 ends: an Accord runner delivers a violet card. Lord Malrik requests
  Kael and Isolde Vane at supper tomorrow (26 Sunspire), seventh bell, in the
  house at the top of the Reach, "He asks that neither come alone." The first
  card (ch.10) was addressed to Kael alone and refused. Thorne knew their
  promise within minutes.

## Canon added by the ch.18 rewrite (ch.19 onward must honor)

- 26 Sunspire, seventh bell (evening), Kael POV. Thorne's house at the top of
  the Reach has no gate: a wide shallow stair with a violet-shaded lamp every
  fourth step, two retainers at the head who bow to Sol first. Dark panelling,
  copper lamp brackets, bare walls, NO portraits. Dining room: round table for
  four, one wall of window over the drop.
- Malrik at home: deep grey, PLAIN silver clasp (no device), stands unaided,
  smaller than Kael remembered. Grandson is ALDOUS, about 25, tall, unsure of
  himself (pulled out Sol's chair, looked stricken). The unnamed steward (small,
  upright, copper clasp) stands behind Malrik's chair and laid the folded slip.
- Sol's supper: no cutlery; two-handled cup of broth, torn bread, cut cheese,
  pear halved and cored. Malrik: the kitchen learned it in the last year of the
  trade feeding forty people who could not hold a spoon. Kael ASKED before
  helping ("On the bread, or as it is?" "Only that.").
- The red-brown dots in the ledgers are oak gall and rust ink; Malrik touches
  every name himself at each turn of season, four days' work now, Aldous goes
  down with him. Vrell's two pages were "not put on account"; Sol thanked him
  once, unfiled.
- THE OFFER: Kael, as sitting auditor, to state before the Council opens the
  box: "House Thorne kept the Lower Reach lit for three years, at its own cost,
  in good faith and in the public interest, and stands ready to make the trunk
  line safe." Malrik: the tap must be shut "in order"; his smiths took three
  years to learn it; the order is set down in one hand and ONE PERSON holds
  the page. He admits the clerk was "kept... warm", "I would lock it again".
  If Kael refuses he will say it himself and let the Council choose between a
  distrusted house and forty households in the dark ("I have counted the
  votes"). "Good faith" may be struck: "Keep the lamps. Keep the last clause."
  Malrik would sooner be opposed by both than tolerated by either.
- CLOCK: Thorne files its statement with the Chancellor's clerk at the seventh
  bell on 27 Sunspire (either Thorne offers the order WITH the auditor's word,
  or AGAINST his silence). Kael's answer due by sixth bell, before the day's
  first session.
- Kael said, "Not at this table, and not alone." On the stair he told Sol
  unprompted that he wanted to say yes and would have done it alone and told
  her after.

## Canon added by the ch.19 rewrite (ch.20 onward must honor)

- Night of 26-27 Sunspire, Sol POV. Kael began "I'll go and look at the chain,
  and then I'll..." and stopped and ASKED her to come; she said yes.
- Renn's log: cycle by breaths (from the second landing; Sol feels it: TEN,
  steady), links counted by glass from the near edge of the gallery on the
  drop at every change of guard (100 links, 10 pins, plumb). CLOCK: the chain
  loses about 1-2 oz a week; the plate forgives a few ounces; cycle falls to
  nine by mid-Cinderveil and to eight (the surge) by the end of Cinderveil if
  nothing is done. Weeks, not days. "He's right about the chain. He's wrong
  about the hour."
- Sol's hands (5 days after injury): pinched a brass tally peg between thumb
  and forefinger for a count of four; painful. Healing timeline so far: 25th
  fingers curl in the wrappings; 26th curls to second knuckle, lifts a cup
  between both palms; 27th holds a peg for four; 28th (ch.20) turns a vellum
  leaf with thumb and forefinger in two tries, still bandaged. Fist about the
  end of the week (30-31 Sunspire) per the healer.
- THE REPLY (Sol's idea: report, don't vouch; make Thorne's offer public so it
  cannot be withdrawn as leverage). Text: the auditor will state what he has
  verified (three years lit by a tap on the Vault's trunk line; House Thorne
  kept the meter); will state the house has OFFERED the order for shutting the
  tap safely; will NOT certify good faith or stewardship; Isolde Vane joins;
  the order to be lodged under seal with the Council surveyor (Renn) before the
  box is opened, not held against anyone's answer. Witnessed by Warden Mara
  ("hands unfit to sign"). Ashworth wax, runner, an hour before sixth bell.
- HOOK / OPEN THREAD: two hours after the last count a bright copper link with
  the three-strand knot was on the Council chain (101 links) though the hatch
  seals (Council wax and Ashworth wax) were whole and nobody came down the
  stair (Joren). Implies a second way into the sublevel, on no survey, known to
  Thorne. Weight about an ounce and a half; it does not move the cycle: "It
  only says that it could."
- Kael said aloud he was afraid ("we've just told him no in a way he can't
  argue with"); Sol: "Now we're counting the same thing."

## Canon added by the ch.20 rewrite (ch.21 onward must honor)

- 28 Sunspire, ninth bell (morning), Council chamber, Kael POV. Sol beside him,
  hands still bandaged.
- Malrik ACCEPTED the public reply. Thorne's filing of the evening of 27
  Sunspire (read by the senior clerk, a bald grey man with ink to the wrist):
  received the auditor's reply; the offer of the order for shutting the tap
  stands and is not withdrawn; the order, in the hand of the house's MASTER
  SMITH, was lodged at eighth bell on 28 Sunspire with Renn under seal (brass
  case no longer than a forearm, Thorne wax on both ends, Renn's strip across
  the seam), Malrik brought it up the Reach on foot; Renn may read it alone but
  only when the Council says; UNOPENED. "The house did not ask to be called a
  steward. It asked to be read." Kael and Sol: he gave up the one page that
  was his leverage because "he has found a better thing to hold."
- Copper link: still on the plate (nobody will lift it and change the weight).
  Kael and Sol decided TOGETHER to send it to the Chancellor in a sealed note,
  not into open chamber. Renn's sealed note has been with the Chancellor's clerk
  since noon 27 Sunspire. Renn and Joren walked the sublevel twice more: no door,
  no drain, nothing off the survey. THREAD STILL OPEN (finding 15).
- Seal examination by the Council's clerks: Renn's strip whole (cut words
  "Twenty-three Sunspire. First bell. Unbroken."), Thorne wax whole with TWO
  LATER LAYERS laid over the first, not through it (old-trade custom for an
  instrument kept in damp). Both seals found whole. Box: lead-lined oak, bound
  in iron, one band sprung, kept under guard in the clerks' strongroom, brought
  in by two clerks. Inside on dry felt: vellum wrapper "Ward Deed of
  Succession" tied with violet-and-copper cord; ELEVEN leaves of the instrument
  and SIX leaves of a Schedule; foot seal near-black, the knot.
- Recital: three generations of wards, the names of the dead, the cost borne.
  Operative clauses as read aloud: CLAUSE 7 (all contracts named in the
  Schedule and all that follow them upon any line pass on ratification into
  the custody of "the house administering reform," to be kept, assigned or
  dissolved at its discretion); CLAUSE 12 (in any question touching the
  instrument or its contracts, that house's reading is final and no body sits
  in review); CLAUSE 19 (takes effect upon opening by the Council's clerks in
  sight of the full Council, its own seal whole; if within THIRTY DAYS of that
  opening the Council has not set it aside by the voices of NINE of twelve
  houses, it is held ratified and "the house whose seal closes it" administers).
- Accord law used (no section numbers were given; do not invent any): the
  Accord's article on transfer lets a contract change hands only with the
  holder's consent or the sitting auditor's certification; the last article of
  the Accord's dissolution schedule keeps alive any instrument of succession
  sealed under the old trade on the condition that it is opened before the
  Council entire with its own seal whole. So the Deed is a PRE-Accord
  instrument and was drafted to that letter ("Somebody had read it before the
  Accord ever sat"). The Deed's own date is NOT stated in ch.20.
- Kael realized and TOLD SOL IMMEDIATELY at the table, low: "It's a seizure.
  Seven takes the contracts, twelve takes the last word, and nineteen makes
  them live." Interior beat: guarding the box as evidence was precisely what
  clause nineteen required. He blames his own care.
- Sol's contribution: nine to set aside vs eight to pass the petition ("built
  to be easier to keep than to stop"); read the Schedule heads with him: eleven
  houses by line; under the Lower Spine, Thorne and Vane stand side by side (as
  in her mother's contract) and one hand ruled a line and added them into one
  sum; FOUR houses on the Schedule did not sign the petition, Ashworth and Vane
  among them ("Nobody asked either of us."). Kael had the record show it as
  ISOLDE VANE'S observation. Callback: "The corner?" "The corner."
- Kael REFUSED to certify in the chamber; leave granted to read every leaf
  with Sol under a clerk's eye and give a written finding at the PUBLIC SITTING
  IN THE THIRD WEEK OF CINDERVEIL, when the petition vote is taken.
- CLOCKS (both live): the Deed's thirty days run from ninth bell on 28 Sunspire
  and lapse 28 CINDERVEIL ("The Council does not stop a clock it did not set");
  the chain falls to nine by mid-Cinderveil and to eight (surge) by the end.
  Both run out in the same week.
- Malrik: "The house is content to be read"; thanked Kael for his diligence
  ("The box could hardly have been in better hands."); Kael: "It has been in
  the Council's hands, my lord." Malrik: "Yes. That was the hope." Menace kept.
- ALDOUS did not stand with his grandfather, went white at the Lower Spine leaf,
  his lips shaped "I did not" before the steward's fingers settled on his sleeve.
  OPEN THREAD: what did Aldous not do or not know? Do not resolve cheaply.
- Ch.20 ends on that image. Hook type: character crack inside Thorne (previous:
  ch.19 discovery, ch.18 clock, ch.17 card). Vary in ch.21.

## Plan for ch.21 and after (updated 2026-09-28 after ch.20, author may override)

- **Ch.21 (29 Sunspire):** read old ch.21 first and assume it is broken. It must
  follow from ch.20: the private read of all seventeen leaves with Sol under a
  clerk's eye, the written finding not due until the third week of Cinderveil.
  Old ch.21 may use Councilor names (Mirelle, Hest, Thorne, scribe Veyra) and
  "thirteen houses"; canon is TWELVE houses, the Chancellor is an old woman, the
  senior clerk is unnamed. Grep for the wrong seal and cross-series names.
- Do NOT repeat the scripted line. Do NOT have Kael conceal anything. Do not
  restage the coat-pass moment.
- Keep Sol's hands healing (fist about 30-31 Sunspire).
- Resolve, or keep deliberately open, the copper link and Aldous threads.
- Petition arithmetic: Thorne holds EIGHT signatures, needs eight to pass and
  the Council needs NINE to set the Deed aside within thirty days, so five
  signing houses would have to flip. The climax (ch.40-43) must earn that with
  exposure at the public sitting; author to decide the mechanism.
- **Ch.22 onward:** read each before touching; assume broken.

## Findings for the author or later sessions (not yet resolved)

1. **Pass conflict.** In ch.10 Kael says "Thorne's pass called it
   decommissioned" (the ch.8 pass for Anchor Seven, dated 23 Sunspire).
   The ch.16 coat pass is a DIFFERENT pass, to the Precedent Archive, also
   dated 23 Sunspire. Acceptable (different sites, same date); later chapters
   must not confuse the two.
2. **Name collision.** The missing clerk is "Varel" (ch.10, 12, 13, 14, 15)
   but House Varel is a Thorne ally (ch.7 "Lord Varel", ch.31 "Lady Varel",
   who leads the censure motion against Sol). Decide: rename the clerk
   everywhere or make him a disaffected minor relation of House Varel.
3. Ch.9 says "nine days" since the Contract on 17 Sunspire (should be eight
   if it went public 9 Sunspire). Minor; not touched.
4. RESOLVED: Thorne's line is spoken by Lord Malrik in ch.1 and echoed by the
   steward in ch.15. Old ch.17 had Vrell say it twice; dropped. Ch.20 does NOT
   use it. Watch ch.31 and ch.40-43 so it is not repeated verbatim by a named
   lord.
5. Ch.13 introduces "the Vault's line was cut off from every private house
   the day the Accord sealed" and a three-year illicit tap. Check later
   chapters do not contradict it.
6. Ch.11 says Sol memorized the Thorne knot in the archives three years ago
   while researching her mother's case (brief rule 3 recognition, earned).
   Ch.17 now shows her mother's contract in Thorne's archive; check nothing
   later says Sol never saw her mother's paperwork.
7. Ch.31 says Sol "photographed the Deed" and "copied its clauses" and that
   it was hidden in a site "the Accord forgot existed": check against the
   chain of custody (sealed, Renn-stamped, opened only before the Council on
   the 28th). After ch.20 the Deed's text is on the Council record, read aloud
   in open session, so any "secret Deed" reveal in ch.21-45 must be reworked.
8. Cross-series name leak. Old ch.15 called the warden "Mara Voss" (Amity
   Falls Book 1 heroine). Warden Mara has NO surname. Grep later chapters
   for "Voss" and other Amity Falls names.
9. Old ch.15 had Valerius Ashworth dead eight months and an unsent letter to
   a jurist Maraen of House Kestrel. Retired. Check ch.18-45 for leftovers.
10. Old ch.17-18 used Thorne colors "charcoal and burnt orange" and
    "climbing ivy". Canon is violet and copper. Lord Malrik personally wears
    deep grey with a silver clasp (ch.1, 3); fine as his own dress, but the
    clasp must not be described as a crown or thorn-and-chain house seal.
11. **WRONG SEAL WORDING STILL LIVE IN EARLY CHAPTERS** (found by grep, not
    yet fixed): ch.1 line 29 ("a thorn wrapped in chain" clasp); ch.3 lines
    45, 57, 121 ("thorned crown wrapped in chain"); ch.7 lines 5, 49, 57, 65
    ("thorned crown at its center"). Fix to the canon seal when circling back.
    Also check ch.2, ch.4-6, ch.8-9 by reading, not only by grep. Ch.6/8
    griffin and Ashworth wax are House Ashworth's own seals and are fine.
12. Timeline check ahead: header dates run to 23 Cinderveil (ch.45). The 28
    Sunspire opening (ch.20) is now consistent with ch.19 (27 Sunspire).
    Ch.40 is 18 Cinderveil, ch.43 is 21 Cinderveil: the public sitting in the
    third week of Cinderveil must land there (ch.40-43), before the 28
    Cinderveil lapse.
13. Grandson is ALDOUS (ch.18, ch.20), about 25. Old ch.27 line 9 calls Thorne's
    heir "a woman named Cressida with her father's pale eyes": reconcile when
    ch.27 is checked; she must not displace Aldous as the grandson at
    Malrik's elbow.
14. Ch.1 line 29 describes Malrik's clasp as "a thorn wrapped in chain": fix
    with finding 11 (canon: plain silver clasp, no device; ch.18 and ch.20 use
    "plain").
15. OPEN THREAD from ch.19, carried through ch.20: copper Thorne link on the
    Council chain, second way into the sublevel, on no survey. Resolve (Thorne
    smith route, old drain, ropewalk cellar) or deliberately close before the
    climax.
16. CLOCK from ch.19: chain cycle nine by mid-Cinderveil, eight (surge) by the
    end of Cinderveil. Headers run to 23 Cinderveil (ch.45), so this is live
    in ch.37-45. Honor it or resolve by shutting the tap in order at the
    climax (ch.40-43). Renn holds the lodged shutting order (unopened).
17. Varel's ch.14 line "I thought you were early" rules out any scene where
    the steward warned him of visitors. Do not add that.
18. Bell system is ambiguous in earlier chapters (registrar opens at seventh
    bell in the MORNING in ch.11; supper at seventh bell in the EVENING in
    ch.17-18; tenth bell is night). Always disambiguate a bell with a
    time-of-day cue.
19. NEW (ch.20): Old ch.21+ may still say the Deed is dated seventeen Sunspire,
    that Thorne has a Councilor Thorne, or that the Deed's seal is a crimson
    thorn-bush. Grep for "seventeen Sunspire", "Councilor", "Mirelle", "Hest",
    "Veyra", "thirteen".
20. NEW (ch.20): The Deed is now the pre-Accord instrument "sealed under the old
    trade" and the drafter had read the Accord's dissolution schedule before the
    Accord sat. That is a quiet hint of foreknowledge (Keeper's institutional
    seat, ch.45). Do not name a person; keep it institutional (brief rule 11).
21. NEW (ch.20): Ch.16's Chancellor is an old woman ("her voice thin with age");
    keep pronouns consistent. The Council has TWELVE houses.

## Known landmarks to watch for once chapters reach them

- Ch.18: the formal "Co-leadership" idea is dead; private promise only
  (formal cession is ch.39).
- Ch.20: DONE. Deed fully understood; trimmed from 4,190 to about 1,860.
- Ch.26-28: Kael's solo mistake backfires; first "I love you." Ch.28: strip
  settled "Equals, starting now" line and the repeated scripted line.
- Ch.31: Sol/Kael before the Council; note the Varel house name issue.
- Ch.33-35: rupture, must stay unresolved.
- Ch.38: first on-page intimate scene.
- Ch.40: check for chapter-number references.
- Ch.41: cost-transfer mechanic involuntary and non-redirectable (no chapter
  uses the Sol/Kael cost transfer as a chosen buffer).
- Ch.45: Keeper reveal institutional, never a named person; fix seal.

## Other notes

- `kindling-line-book-2_full_manuscript.md` is OUT OF SYNC with `chapters/`.
  Regenerate at the very end.
- Word floor: 1,800 words. Verify by reading, not by old logs.
- Defect categories to scan any unchecked chapter for: wrong magic system,
  invented soulbond (brief rule 15), wrong Thorne seal, front-loaded plot,
  corrupted or non-Latin characters, under word floor, chapter-number
  meta-references, meta breaks ("the brief", "this book").
- Repo owner is `aliwaziri10/Voxel`. Default branch is `main`.
- Sandbox for bash has no network, so raw-URL word counts are not available
  there; word counts are taken on the drafted text before push and the push is
  confirmed via commit stats or a contents-API re-fetch.

## Progress log (one short line per session/chapter)

- 2026-09-28: ch.10 rewritten clean, commit `09a74af8`.
- 2026-09-28: ch.11 first rewrite violated canon lock (wrong seal, site,
  restaged confrontation).
- 2026-09-28 (proofread session): ch.10 header fix `d0723906`; ch.11
  `f129fd09`; ch.12 `9f7ea6de`; ch.13 `1dda53d6`; ch.14 `f18a859c`.
- 2026-09-28 (proofread session 2): ch.15 `1d256b1b`, corrected and ch.16
  rewritten in `1aae27fd` (both verified live: 2,298 and 2,018 words, no
  dashes, no banned terms). Seal grep of ch.1-15 logged (finding 11).
- 2026-09-28 (proofread session 2, cont.): ch.17 rewritten. Next: verify
  push and word count, then ch.18 (supper at Malrik's; read ch.19 first).
- 2026-09-28 (proofread session 2, cont.): ch.17 verified live at 1,746 words,
  UNDER the 1,800 floor and with a date slip; fixed in `4266126a` (1,841).
  Ch.18 rewritten `9a3b65f7` (1,950), ch.19 rewritten `14225a5e` (1,905), both
  verified byte-identical to draft at the pinned commit. Next: ch.20 (read the
  full old ch.20 first, then rewrite from canon above).
- 2026-09-28 (proofread session 3): charter, HANDOFF, brief, plan, ch.16, ch.19
  and old ch.20 read in order. Ch.20 rewritten `050b0c73` (1,867 by wc incl.
  header). A timeline slip caught before push (Renn's sealed note originally
  dated "first bell yesterday", but the copper link was found after sixth bell
  on 27 Sunspire; now "noon yesterday"). That commit's message says "+ HANDOFF
  update" but it carried only the chapter; this HANDOFF commit is the actual
  update (process slip: HANDOFF and chapter were not in the same commit).
  Next: ch.21 (read old ch.21 in full first, then rewrite from canon).
