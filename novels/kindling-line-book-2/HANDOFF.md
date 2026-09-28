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
  "Brightward." Header dates run one chapter per day: ch.N is (N+8) Sunspire
  up to ch.22 (30 Sunspire, the last day of the month). From ch.23 the header
  rolls into Cinderveil: ch.N is (N-22) Cinderveil (ch.23 = 1 Cinderveil,
  ch.24 = 2 Cinderveil, ch.40 = 18, ch.43 = 21, ch.45 = 23). There is NO
  "31 Sunspire" (see finding 29).
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
- **Ch.21:** REWRITTEN in `d206fd1f` (earlier session, HANDOFF not updated
  then), then PROOFREAD + STAMPED in `6f2d43b5`. Sol POV, 29 Sunspire. 1,859
  words by `wc -w` on the final draft including the header comment. Zero
  non-ASCII characters, no dashes, no banned terms, no scripted line, no
  old-canon names (grep for "Hest" hits only the word "chest"). Five fixes in
  the proofread pass: (1) "three days ago" became "four days ago" (Sol read
  the girl of fifteen in Thorne's ledger on 25 Sunspire, ch.17); (2) Sol's "it
  doesn't take the contracts we have" became "it doesn't stop at the contracts
  we have" (clause 7 as read in ch.20 DOES take the named contracts); (3)
  "the only clause in the instrument that reaches forward" became "the only
  place in the instrument that says how far 'follow' goes" (clause 7 and
  clause 19 both already reach forward); (4) Renn's chain figure now says "an
  ounce and a half in six days" and that he counts the link apart from the
  chain; (5) closing image changed from lamps "put out one by one" (reads as
  a blackout, and it is mid-morning) to the Lower Reach going about its
  morning "by the grace of a tap that was not lawful." Byte compare against
  the live file NOT run; re-fetch via the contents API next session.
- **Ch.22:** REWRITTEN + STAMPED. Kael POV, 30 Sunspire. 1,857 words by `wc -w`
  on the final draft including the header comment. Zero non-ASCII characters,
  no dashes, no banned terms, no wrong seal wording, no scripted line, no
  old-canon names. Old ch.22 (bot draft `7dc8ee6b`: invented Embervein Ward
  site, "Chancellor Veyra", a joint mandate "voted nine days ago", the Deed
  "decoded", Kael planning a solo run, the ch.16 pattern confrontation
  restaged, 14 hours to a midnight deadline) fully replaced, not patched. First
  draft was 1,617 words, UNDER the floor; two real sub-beats were added
  (Renn's note returning from the Chancellor's clerk; Sol editing Kael's
  request). Three canon fixes before push: Mara removed from the spire stair
  (not verified present; Sol serves the tea instead), Kael's "did not know it
  existed" corrected to "did not know a copy had left the house" (he knew the
  annex existed from ch.21), and "first of the month" made "first of
  Cinderveil." DATE FIX in `ee2a9683` (ch.23 session): "The healer had said
  the thirty-first" became "The healer had said tomorrow" (Sunspire has 30
  days; see finding 29). Nothing else in ch.22 changed.
- **Ch.23:** REWRITTEN + STAMPED in `ee2a9683` (chapter and ch.22 fix), HANDOFF
  in the follow-up commit that adds this line (process slip: two commits, not
  one). Sol POV, 1 CINDERVEIL. 1,941 words by `wc -w` on the final draft
  including the header comment. Zero non-ASCII characters (so no dashes), no
  "particular", no "some/something" at all, no wrong seal wording, no scripted
  line, no old-canon names (old ch.23 was the bot draft `d8145f7a` at 14,978
  bytes: invented Embervein Ward, a solo midnight audit restaged, the ch.16
  confrontation replayed, a ward-construct reciting Thorne's line, Kael's hands
  burned, cost-transfer used as a chosen shield, Sol picking a Thorne lock; all
  retired, chapter replaced not patched). First draft was 1,754 words, UNDER
  the floor; one real sub-beat added (Sol at the window: the count, the wage
  morning, "the paper has to be true, and it has to be first"). Byte compare
  against the live file NOT run; verify via the contents API next session.
- **Ch.24:** REWRITTEN + STAMPED (session 6). Kael POV, 2 CINDERVEIL (opens in
  retrospect on the 1 Cinderveil landing, then runs the night and the morning
  of the 2nd). 2,007 words by `wc -w` on the final draft including the header
  comment; first full draft landed above the floor, no expansion needed. Zero
  non-ASCII characters (so no dashes), no "particular", no "some/something/
  someone", none of the other tell words, no wrong seal wording, no scripted
  line, no old-canon names. Old ch.24 (bot draft, 9,436 bytes: Embervein site,
  a thorned-crown seal, Kael's solo descent, Mara's hands burned by a
  contractual flare, Sol rescuing them, a Deed "clause four, subsection seven",
  Thorne "seeding" sites into the petition; all retired, chapter replaced not
  patched). Chapter and HANDOFF pushed in ONE commit. Byte compare against the
  live file NOT run; verify via the contents API next session.
- **Ch.25-45:** UNCHECKED. Treat all as broken until verified.

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
  leaf with thumb and forefinger in two tries, still bandaged; 29th (ch.21)
  healer unwinds a finger's width of linen, fingertips shiny pink, welts
  closing from the heel, holds a heel of bread in both palms, turns leaves
  slowly, no pen; 30th (ch.22) lifts a page corner herself with thumb and
  forefinger, holds a cup in both palms, makes her FIRST FIST (three breaths, a
  day before the healer's date) and writes "I.V." with the pen in her whole
  fist in child-sized letters; 1 Cinderveil (ch.23) last linen off (see ch.23
  block). After this, show only what CHANGES: no more healer measurements each
  chapter.
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
  stair (Joren). Implies a second way into the sublevel, on no survey, known
  to Thorne. Weight about an ounce and a half; it does not move the cycle: "It
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

## Canon added by the ch.21 rewrite (ch.22 onward must honor)

- 29 Sunspire, morning, Sol POV. Reading room behind the Chancellor's dais: one
  window, one table. The junior clerk who cut the wax in ch.20 is named BRAM;
  he stands guard against the wall, addresses Sol as "my lady" and Kael as
  "Auditor". Eleven leaves lie under glass with brass rims; Renn's fair copy,
  stamped in the small hours with the clerks' leave, hour and date on every
  leaf. Kael's finding sheet is headed "Finding of the Auditor on the
  Instrument Opened 28 Sunspire" and is deliberately left EMPTY until both
  have read every leaf. He moved the pen out of Sol's reach without a word
  (she cannot hold one yet).
- Recital: THIRTY-THREE dead in a column by line and year, all THORNE's dead.
  The twenty-first is the girl of fifteen from Thorne's ledger (read 25
  Sunspire). NO VANE DEAD are named, yet the Vane block sits in the Schedule
  added into Thorne's sum: "Their dead pay for it. Ours are in the total." To
  go in the finding, after the Schedule is read.
- Renn's report (29 Sunspire): cycle TEN, steady at midnight and dawn; chain
  down an ounce and a half in six days, as his sum said; the copper link sits
  on the plate beside it and he counts the two apart; scale good to a
  quarter. He does not read law.
- THE LAST LINE OF THE SCHEDULE: "And all that shall follow them upon these
  lines, in whatever form the house administering reform shall set." Sol's
  reading: "follow" reaches contracts NOT YET WRITTEN. After ratification every
  contract written for the Reach is Thorne's before the ink is dry; Thorne's own
  reform standard is what would be written. Kael: "It's the reform itself that's
  the seizure." Kael read that leaf in chamber on the 28th and took it for the
  common close; Sol "took it for a plea"; Kael: "It was an instruction."
- Sol's unspoken word is FIRST: someone would have to be the first to sign a
  new standard and prove it could be survived. Deliberate seed for the ch.40-43
  trial (brief rule 10). Do NOT resolve early; she has not said it to Kael.
- Bram: two of the SIGNING houses sent to the clerks' office on the afternoon
  of 28 Sunspire for copies of the Schedule; both asked for their own line,
  neither asked for the clauses. Arithmetic on the page: nine to set aside, four
  houses of "us", five of the eight signers would have to turn; two have
  started reading. Names of those two houses NOT given; the author decides.
- THE ANNEX: Thorne's reform petition carried an annex, the contract standard
  to replace the old form. The petitioner WITHDREW it at NOON on 28 Sunspire,
  by Thorne runner under the house's seal, three hours after the box was
  opened, entered by the clerks as the petitioner's right before the vote. Sol:
  they needed the reform until nineteen started its clock, after that only the
  lines; "someone has to have drawn it" and it now exists on a desk off the
  record. Kael: "somewhere Thorne keeps things." OPEN THREAD (finding 22).
- Ch.21 ends: Kael and Sol decide TOGETHER to ask Thorne about the annex
  before noon ("Both of us." It "sounded like a plan"). Closing image: the
  Lower Reach going about its morning, its lamps still burning by the grace of
  a tap that was not lawful. Hook type: a decision to act plus a missing
  document (previous: ch.20 character crack). Vary in ch.22.
- Kael conceals nothing in ch.21; the scripted line is not used.

## Canon added by the ch.22 rewrite (ch.23 onward must honor)

- 30 Sunspire, first bell, Kael POV, at the trestle in their spire rooms. ANSA
  (old splicer, fifty years at rope, lives over the tar-shop) climbs the spire
  stair to bring them a paper. She calls Kael "Auditor" and "Kael Ashworth,"
  calls Sol "Sol" (no title). Sol serves her tea, both palms round the cup.
- THE ASK (29 Sunspire, noon): Kael and Sol climbed the shallow stair to
  Thorne's house together with a joint note in six plain lines asking what
  became of the annex and where the standard might be read. Two retainers
  bowed to Sol, not Kael. The unnamed STEWARD came down four steps, took the
  note WITHOUT reading it: the house has said what it wished recorded, the
  annex is withdrawn as the Council's rules allow, nothing further to file.
  ALDOUS stood at the head of the stair, hands hanging, and watched the note go
  into the steward's sleeve "as if it were his own"; said nothing (Sol noticed;
  Kael had left it out of his account and admitted it).
- WHERE THE ANNEX WENT: it was never off the record for long. A violet awning,
  two clerks and a brazier went up at the foot of the LOWER SPINE STAIR on the
  afternoon of 29 Sunspire while Kael and Sol were at Thorne's door. It offers
  PROVISIONAL ENGAGEMENT to any ward-trade worker with no line since the Accord
  sealed: a wage from the FIRST OF CINDERVEIL, paid by the house, the lamps
  kept. Ansa counted THIRTY-ONE signers before the lamps were lit (from her
  window); the queue was still standing when she shut her shutters. Her sister's
  boy TAM signed at the second bell of the afternoon. About FOUR HUNDRED
  ward-takers have no line on the Reach, more counting the eastern families.
- THE FORM: a single printed leaf (block type, hand-filled blanks) headed
  "Provisional Engagement of a Ward-taker under the Standard of the House
  Administering Reform." Wage; the lamps; TERM "until dissolution of the trade,
  or death of the bearer" (word for word Sol's mother's term, ch.17); a line
  "Dependents, name and age" (Tam wrote MOTHER. SISTER, 14.); a signer's mark; a
  witness; a place for the house; the knot in near-black wax at the foot, no
  larger than a coin; last line: "Consent of the holder, given freely, upon the
  standard as set."
- KAEL'S LEGAL READ: the Accord's article on transfer lets a contract change
  hands with the holder's consent OR the auditor's certification. Nobody is
  being taken; each signer consents, freely, in his own hand, over tea. "One
  signature at a time, and every signature lawful." Sol: the Deed "only has to
  be ratified over the top of them." Pace: at even half the first afternoon's
  pace Thorne holds the Reach's whole trade on its own paper before the public
  sitting; 28 days run from 30 Sunspire to 28 Cinderveil.
- Sol's receipt: she wrote "Received of Ansa, one form. 30 Sunspire, first
  bell. I.V." on the back with the pen in her whole fist; Kael signed beneath
  her. The leaf is now in their hands as evidence.
- KAEL TOLD SOL BEFORE ACTING (rule 2, no concealment): he had thought of
  going to the table alone at the fourth bell in a plain coat, reading the whole
  standard, being back before she finished with the healer ("I thought it would
  be clean"), and said: "I'm not going. I'm telling you because I thought it."
  Sol: "Thank you for the notice." The scripted line is NOT used.
- THE PLAN: they go together to the table at the FOURTH BELL on 30 Sunspire (the
  same morning; no time-of-day cue in the text beyond "first bell" and "the
  hours to the fourth bell"), in the auditor's coat, and Kael reads a request
  aloud in front of the queue. Written request (Sol cut "respectfully"): "The
  Auditor of the Accord requires a copy of the standard in full, under the
  Accord's article on transfer, and will read it at the table." Sol: "If they
  refuse, the queue sees them refuse." Kael expects refusal. THE TABLE SCENE IS
  NOT ON THE PAGE in ch.22; ch.23 must account for it. (DONE in ch.23.)
- Renn's sealed note about the copper link CAME BACK from the Chancellor's clerk
  at MIDNIGHT (29-30 Sunspire), wax whole, one line under it: "received, and the
  survey books of the Reach are being fetched." Not an answer; Kael: "a door
  beginning to move." THREAD STILL OPEN.
- HOOK (ch.22 ends): the table's clerk says to every signer, pen in hand: "The
  Auditor has read the standard and raised nothing." Kael never saw it before
  this morning and did not know a copy had left the house. Tam told Ansa it is
  why the first ones signed: "If Kael Ashworth had read it and raised nothing,
  it was safe." Kael's refusals (in chamber, in writing, before the Council) are
  silences, and "silence was the one coin House Thorne had always known how to
  spend." Hook type: a false attribution built from his own silence (previous:
  ch.21 decision plus missing document, ch.20 character crack). Vary in ch.23.

## Canon added by the ch.23 rewrite (ch.24 onward must honor)

- 1 CINDERVEIL, first bell onward, Sol POV, in the spire rooms (Kael at the
  trestle). NOT 31 Sunspire (there is none; finding 29).
- SOL'S HANDS: the healer (unnamed) takes the LAST LINEN off at first bell.
  Skin pink, new, shiny; welts flat and white, heel to fingertip; fingers spread
  to a count of five and no wider; she cannot yet close them round anything as
  thick as a rope, CAN close them round a pen. Orders: grease at night, gloves in
  the wet, nothing heavier than a cup for FOUR DAYS. From here show only what
  changes (rope and knife still off the table until about 5 Cinderveil).
- KAEL'S STATEMENT (third fair copy, written before the healer came; first
  copy "was worse"). Text as read aloud: he has been shown the FORM of
  provisional engagement and has NOT been shown the STANDARD it refers to; he
  has not read it; "I have raised nothing because I was given nothing to raise";
  he certifies no engagement under the Accord's article on transfer; "Let no
  signer take my silence for a reading." Last line, added at Sol's prompt after
  she said "I would have signed": "This statement is made against no one who has
  signed." Kael ASKED Sol to witness ("You don't have to"); she said yes and
  wrote "Isolde Vane" in full with the pen between thumb and three fingers, in
  a child's letters, last "e" off the line; Kael waited for her nod before he
  shook the sand himself.
- DISTRIBUTION (Sol's plan, "it needs to be heard"): ANSA reads it at the
  splicers' hall at the noon break; Warden MARA reads it on the ropewalk floor;
  a copy goes to the Chancellor's clerk under Ashworth wax so the record shows
  he said it on the FIRST day, not the tenth. Kael certifies nothing and
  conceals nothing; the scripted line is NOT used.
- THE TABLE SCENE (30 Sunspire, fourth bell of the MORNING, told in
  retrospect): the queue stood forty long and parted for them. Kael read his
  request to the awning cloth "like a man asking for a receipt he is owed." The
  younger of the two clerks (unnamed; ink on his cuff, pleasant voice, head on
  one side) bowed to Sol first and answered: the Auditor is welcome; here is the
  form, every signer gets a copy (the same leaf Ansa brought); "The standard is
  set upon ratification by the house administering reform, as the form says,
  and the house cannot lay before the Auditor what is not yet set"; the request
  is recorded in the table's book with the hour; he poured Kael a cup of tea.
  That was the refusal: lawful, courteous, useless. Sol: "I never thought of a
  house that would not bother to refuse."
- KAEL SPOKE TO THE QUEUE at the table when the next signer (a broad woman with
  a boy of six) took the pen and the clerk began "The Auditor has read the": "I
  have been shown the form. I have not been shown the standard. I certify
  nothing, and my silence is not a reading." The clerk, unblinking: "The Auditor
  is quite right. The house has never said he certified. The clerk will say
  instead that the Auditor has been asked." (True, and heard down the line as
  "has looked": Thorne lost a sentence and bought a better one.) NINE people
  left the queue; the rest stayed (wage starts today, rents due the same
  morning).
- COUNT: Ansa's runner boy brought a slate chalked at the lighting of the lamps
  on 30 Sunspire: SIXTY-NINE signers in two days (31 on the 29th, so 38 on the
  30th by implication), of about four hundred. First wages paid at the awning at
  DAWN on 1 Cinderveil; the line already runs past the end of the street.
- Sol's interior beat: "I would have signed. At his age, with a sister at home
  and that line on the leaf." Kael: "I know. I'm not writing this against them."
  Sol's unspoken word (FIRST, ch.21) "sat as it had for two days and did not
  move"; she has still not said it to Kael.
- Sol: "the paper has to be true, and it has to be first." Kael: "A wage in the
  hand is a better argument than anything I can put on paper."
- Renn sent word at dawn: the Chancellor's clerks have brought up THREE of the
  NINE survey books of the Reach; he will read them in order and tell them
  nothing until he has read all three. Copper link thread STILL OPEN.
- Kael ASKED before opening the door (looked at Sol, she nodded).
- HOOK (ch.23 ends): TAM (about twenty, splicer's apron with tar to the wrists,
  cap crushed in one fist, his leaf folded in the other, foot sealed in whole
  near-black wax; Ansa's jaw) climbs the spire stair: "I was the fourth to sign.
  I signed because the clerk said you'd read it." He holds his first wage in his
  apron ("the first coin I've had from a lawful hand since the Accord sealed")
  and asks "if a man can take his name back." Kael, from the article: it says
  how a contract changes hands and "not one word about how one was handed back."
  Hook type: a plea/question from a signer (previous: ch.22 false attribution,
  ch.21 decision plus missing document, ch.20 character crack). Vary in ch.24.

## Canon added by the ch.24 rewrite (ch.25 onward must honor)

- 2 CINDERVEIL, Kael POV. The chapter opens in retrospect on the 1 Cinderveil
  landing (same technique as ch.23's table scene), then runs the night and the
  morning of the 2nd.
- THE LANDING: Kael's answer to Tam was "I do not know." Sol sat Tam on the
  bench by the door and carried the tea to him in both palms. Kael felt a
  "clean" sentence rise ("Come down with me now... take your name back in front
  of the queue, and I will stand beside you") and did NOT say it; Sol: "You were
  about to say it." "I was about to help." "It was the same breath." Kael told
  Tam aloud that he had nearly said it and why he would not (he would be
  guessing at Tam's rent). Sol: "Thank you for the notice." Kael: "I would have
  been asking him to carry my cost." This is Kael's failure mode (deciding for
  another, in the guise of help) shown and stopped on the page; ch.26-28's solo
  act therefore needs real pressure.
- TAM (about twenty): the rent was paid at the door before he climbed; what is in
  his apron is what was left. He can read (his aunt saw to it). He only saw "until
  I'm dead" beside his sister's age (14) on the walk up. At DAWN on 1 Cinderveil
  he asked the clerk when the standard would be put out so a man could read it;
  the clerk said upon ratification and wrote him in the table's book with the
  hour. TWO others had asked before him; all three were entered in the book
  ("Everyone was very kind"). Kael's promise: he will read the article, the form
  and the schedule of dissolution again and send word by Tam's aunt; if the
  answer is no he will say no; what Tam does is his; he will not think less of
  him for keeping the wage. Tam: "The wage comes tomorrow either way." He has not
  said what he will do. OPEN: Tam's decision.
- KAEL AT THE ARTICLE: read it until the lamps and again at midnight (it is
  silent on handing back; "a door built to open one way"). At first bell 2
  Cinderveil he reads the form's last line as a sum (what was said, what was
  shown, what was owed). CANDIDATE MECHANISM, NOT DECIDED: the ones who signed
  before the fourth bell on 30 Sunspire signed on a FALSE sentence ("The Auditor
  has read the standard and raised nothing"); those after signed on a true
  sentence heard wrong ("has been asked"). Thirty-one before the lamps on the
  29th; the number before the fourth bell on the 30th is UNKNOWN (do not fix
  it). Kael: it is a door for a court, perhaps not even that; the clerk will call
  the sentence a courtesy of the table and no part of the form. Sol: "Forty
  mouths, then. Or fewer."
- KAEL TOLD SOL THE PLAN BEFORE ACTING and asked her to come (go to the awning
  and ask the clerk to say aloud what he told the fourth signer on the 29th):
  "I would rather ask it with you beside me than tell you afterward what I
  asked." Sol: "Together. Gloves first." Sol: "the first plan you have brought me
  with the hole already found." The scripted line is NOT used.
- SOL'S HANDS (2 Cinderveil): grey wool gloves lined with the healer's linen,
  fingers in to the second joint and no further; does up her own coat buttons
  (about a minute); lifts the corner of a stack of leaves with thumb and
  forefinger. Kael waits without helping. From ch.25 show only what CHANGES;
  knife and rope still barred until about 5 Cinderveil.
- ANSA'S REPORT (slate left on the stair before dawn): she read the statement at
  the splicers' hall at the noon break on 1 Cinderveil; forty splicers heard it; a
  woman at the back asked if it was a warning; Ansa: "It's a receipt"; the woman
  went out and signed anyway. COUNT: 143 names by the lighting of the lamps on 1
  Cinderveil (of about 400). The awning now has a second brazier.
- AT THE AWNING (2 Cinderveil, morning): the younger clerk (ink on cuff) rose,
  bowed to Sol first. He KNEW of Tam's question on Kael's own stair ("put
  yesterday morning on your own stair... The house is glad to have had an answer
  ready") and drew out a stand with a placard WITHDRAWAL and a stack of leaves
  under a brass weight. He would not say what was told the fourth signer: "The
  table's book records what the table says. It says the Auditor has been asked."
- THE FORM OF WITHDRAWAL (Thorne's counter; text as read): "Withdrawal of
  Provisional Engagement. I, the holder, having consented freely upon the
  standard as set, ask leave to withdraw my name. I make this request of my own
  will, advised by no officer of the Accord. Wages paid to the day of withdrawal
  are kept by the holder. No further engagement under the standard will be
  offered to the holder, or to any dependent named on the leaf." Kael's read: to
  take his name back a man must first write that he gave it FREELY (which
  forecloses the mechanism above), and must swear no officer of the Accord
  advised him (anyone who came up Kael's stair must leave that off the paper or
  lie beside it; Kael advised nobody; the form cares who was in the room). Sol
  read the last line: the dependent (Tam's sister, 14) is shut out. Clerk: "The
  house does not wish to see any holder held against his will. It also does not
  wish to be made a stair that any man can go up and down at his leisure. Both
  are true." Kael: "Both are true," hearing the house's whole method in it.
- HOOK (ch.24 ends): Sol counted about TWO HUNDRED withdrawal leaves under the
  weight; ink long dry, corners soft, the stack "had taken the shape of the days
  it had waited"; her fingertip came away clean. The exit was printed before
  anyone asked to leave; Kael does not know how many days before. Hook type: an
  anticipated counter that implies foreknowledge (previous: ch.23 plea, ch.22
  false attribution, ch.21 decision plus missing document). Vary in ch.25.
- NOT touched in ch.24 (all still OPEN): Renn's survey books and the copper
  link, Aldous, the annex desk / who drew the standard, the two houses that
  asked Bram for their own line, Sol's unspoken FIRST.

## Plan for ch.25 and after (updated 2026-09-28 after ch.24, author may override)

- **Ch.25 (3 Cinderveil, Sol POV per the alternation):** read old ch.25 first
  (bot draft, 15,177 bytes) and assume it is broken. It should carry Tam's
  decision and the cost of the withdrawal form without answering either
  cheaply: Tam may keep the wage, may go to the awning, may ask Sol rather than
  Kael. Sol's FIRST stays unspoken. Do not have anyone sign the form of
  withdrawal in ch.25 without a cost that lands on the page (the dependent
  clause is the cost). Do not restage the queue or the awning scene. Sol's hands:
  show only what changes. Vary the hook (previous four: plea, anticipated
  counter, false attribution, decision plus missing document).
- Candidate mechanism (AUTHOR DECIDES, finding 30): a consent procured by a
  false statement about the auditor's reading, and given upon a standard not yet
  set, is arguably not "given freely" under the form's own last line. Ch.24 has
  now shaped it (false sentence before the fourth bell on 30 Sunspire, true
  sentence heard wrong after) and shown Thorne's counter (the withdrawal form
  makes the leaver write "freely"). Keep it a question Kael and Sol chase.
- Keep Sol's FIRST unspoken. Keep Aldous, the annex desk, the copper link and
  Renn's three survey books open. Do not resolve any of them cheaply.
- Petition arithmetic (unchanged): Thorne holds EIGHT signatures, needs eight to
  pass; the Council needs NINE to set the Deed aside within thirty days, so five
  signing houses must flip. Two signing houses asked Bram for their own line.
  The climax (ch.40-43) must earn the flip with exposure at the public sitting;
  the exposure must answer "every signature was lawful."
- Ch.26-28 is Kael's solo mistake that backfires (brief rule 7). The growth beats
  since ch.16 (asking before helping, telling Sol before acting, and now
  naming the impulse to decide for Tam in ch.24) make a plain solo act hard to
  justify. Before ch.26, decide what pressure makes him act alone; check what
  old ch.25-26 set up; do not have him conceal anything.
- **Ch.26 onward:** read each before touching; assume broken.

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
   lord. (Old ch.23 also had a ward-construct say it; that draft is gone.)
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
13. Grandson is ALDOUS (ch.18, ch.20, ch.22), about 25. Old ch.27 line 9 calls
    Thorne's heir "a woman named Cressida with her father's pale eyes":
    reconcile when ch.27 is checked; she must not displace Aldous as the
    grandson at Malrik's elbow.
14. Ch.1 line 29 describes Malrik's clasp as "a thorn wrapped in chain": fix
    with finding 11 (canon: plain silver clasp, no device; ch.18 and ch.20 use
    "plain").
15. OPEN THREAD from ch.19, carried through ch.20, ch.21, ch.22, ch.23 and ch.24
    (untouched in ch.24): copper Thorne link on the Council chain, second way
    into the sublevel, on no survey. The Chancellor's clerk is fetching the
    survey books (ch.22); Renn has three of nine (ch.23). Resolve (Thorne smith
    route, old drain, ropewalk cellar) or deliberately close before the climax.
16. CLOCK from ch.19: chain cycle nine by mid-Cinderveil, eight (surge) by the
    end of Cinderveil. Headers run to 23 Cinderveil (ch.45), so this is live
    in ch.37-45. Honor it or resolve by shutting the tap in order at the
    climax (ch.40-43). Renn holds the lodged shutting order (unopened).
17. Varel's ch.14 line "I thought you were early" rules out any scene where
    the steward warned him of visitors. Do not add that.
18. Bell system is ambiguous in earlier chapters (registrar opens at seventh
    bell in the MORNING in ch.11; supper at seventh bell in the EVENING in
    ch.17-18; tenth bell is night). Always disambiguate a bell with a
    time-of-day cue. (Ch.21 uses "a bell marked the second hour" with no cue;
    the morning is anchored by the healer at dawn and the window. Ch.22 uses
    "the fourth bell" for the same morning and "the second bell of the
    afternoon" for Tam; the first is inferred from "first bell" and "the hours
    to the fourth bell". Ch.23 says "the fourth bell of the morning" outright.
    Ch.24 says "first bell on the second of Cinderveil" and "the fourth bell on
    the thirtieth" (morning, per ch.23).)
19. NEW (ch.20): Old ch.21+ may still say the Deed is dated seventeen Sunspire,
    that Thorne has a Councilor Thorne, or that the Deed's seal is a crimson
    thorn-bush. Grep for "seventeen Sunspire", "Councilor", "Mirelle", "Hest",
    "Veyra", "thirteen". (Case-insensitive "Hest" also hits "chest"; check
    context.) Old ch.22 also leaked "Chancellor Veyra" and "Embervein";
    grep later chapters for "Embervein" too. (Old ch.24 also had Embervein.)
20. NEW (ch.20): The Deed is now the pre-Accord instrument "sealed under the old
    trade" and the drafter had read the Accord's dissolution schedule before the
    Accord sat. That is a quiet hint of foreknowledge (Keeper's institutional
    seat, ch.45). Do not name a person; keep it institutional (brief rule 11).
    Ch.24's stack of withdrawal leaves printed days early adds a second hint of
    the house (or an office behind it) knowing how signers would behave.
21. NEW (ch.20): Ch.16's Chancellor is an old woman ("her voice thin with age");
    keep pronouns consistent. The Council has TWELVE houses.
22. NEW (ch.21): THE ANNEX. Ch.21 establishes that Thorne's petition carried an
    annex (the contract standard) withdrawn at noon on 28 Sunspire. Not yet
    checked against ch.5-8 and ch.12, where Thorne's reform proposal and the
    eighth signature are described; if those chapters describe the proposal
    differently (no annex, or a different form), reconcile when reached. Ch.22
    now answers where it went (the provisional engagement table), but the two
    houses that asked Bram for their own line and the identity of whoever drew
    the standard remain OPEN; author decides.
23. NEW (ch.21): Sol is addressed "my lady" by Bram and Renn. Not verified
    against ch.1-19 usage. Confirm when circling back that Sol is styled "my
    lady" and Kael "Auditor" consistently. (Ch.22: Ansa uses no title for Sol.
    Ch.23: Tam uses no title for Sol and does not address her. Ch.24: Tam uses
    no title for either; the clerk bows to Sol first and says "Auditor" to Kael.)
24. NEW (ch.21): Sol's hands may not need every chapter to restate the healer's
    measurements; once the fist is possible show only what changes. Ch.22 showed
    the first fist; ch.23 showed the last linen off; ch.24 showed gloves, her own
    coat buttons and a thumb-and-forefinger lift. DONE; from ch.25 show only
    changes (knife and rope still barred until about 5 Cinderveil).
25. NEW (ch.22): Ansa's history with Sol is unstated. Ch.22 has her call Sol
    "Sol" and treat both as people she tells things to (ch.11). Do NOT add a
    scene where Ansa knew Sol's mother unless ch.1-19 already say so; if
    checking early chapters, grep "Ansa" first.
26. NEW (ch.22): The provisional engagement is a consent mechanism (finding
    27). The Deed's clause 7 takes named contracts by seizure and "all that
    follow" as future contracts; the table gives Thorne future contracts by
    CONSENT. Any later chapter that calls the engagement forced, coerced or
    fraudulent needs a mechanism; the untruths so far are the clerk's "The
    Auditor has read the standard and raised nothing" (ch.22) and the
    replacement "has been asked" (ch.23), which is true but is heard as "has
    looked". See finding 30.
27. NEW (ch.22): Kael's counter-power is that the Accord's transfer article
    needs the holder's consent OR the AUDITOR'S CERTIFICATION. He has refused
    to certify. Keep him from certifying anything at the table or in ch.23;
    his refusal is what the false attribution counterfeits. (Ch.23 and ch.24
    honored this; keep honoring it.)
28. RESOLVED (ch.23): the table scene at the fourth bell on 30 Sunspire is now
    on the page (in retrospect); the count is 69 in two days of about 400.
29. NEW (ch.23): **SUNSPIRE HAS 30 DAYS.** An earlier version of this file said
    ch.23 is "31 Sunspire" and ch.22 said the healer's date was "the
    thirty-first"; there is no 31 Sunspire, and ch.23 is 1 CINDERVEIL (which is
    also the day the provisional wage starts). Ch.22 fixed in `ee2a9683`. Grep
    the whole book (ch.1-45, and HANDOFF/CONTINUITY_PLAN/architecture) for
    "31 Sunspire", "thirty-first", and any header that does not follow the
    rule above (ch.N = N-22 Cinderveil from ch.23). Old ch.23 header already
    read "1 Cinderveil", so the old drafts may be right where the plan was wrong.
30. NEW (ch.23): "THE STANDARD AS SET." The table clerk says the standard "is set
    upon ratification by the house administering reform, and the house cannot
    lay before the Auditor what is not yet set." Combined with the form's last
    line ("Consent of the holder, given freely, upon the standard as set"),
    signers consent to terms no one has put in front of them (Kael: "A holder
    consents freely upon terms that no one has put in front of him"). Candidate
    mechanism for the ch.40-43 exposure. AUTHOR DECIDES; do not let a later
    chapter show the standard in full or name who drew it without that decision.
    Reconcile with finding 22 (the annex "exists on a desk off the record"): read
    the annex as a draft, "the standard" as what the house sets after
    ratification.
31. NEW (ch.23): Thorne adapts fast. After Kael's public disclaimer the clerk
    switched to "The Auditor has been asked" without a flicker. Do not have the
    house fold, apologize or be caught in a lie in a later chapter without a
    cost to Kael and Sol; the house's method is the true sentence heard as a
    false one. Ch.24 repeats it ("Both are true").
32. RESOLVED (ch.24, opening): TAM (about twenty, Ansa's sister's son, signer
    number four on 29 Sunspire, sister of 14 named on his form) asked whether a
    man can take his name back; Kael answered "I do not know" and told him the
    truth about what he nearly said. Tam's own DECISION is still open (see
    finding 33). The Accord's transfer article says how a contract changes
    hands and nothing on handing it back; do not invent article numbers.
33. NEW (ch.24): THE FORM OF WITHDRAWAL (text in the ch.24 canon block) is
    Thorne's counter. Three costs: the leaver must write that consent was given
    freely; must swear no officer of the Accord advised him; forfeits any future
    engagement for himself and every named dependent. AUTHOR DECIDES whether Tam
    signs it, ignores it, or is the first to be caught by it. Do not have the
    form struck down by an invented article. Do not have anyone sign it without
    the dependent clause landing on the page.
34. NEW (ch.24): HOW DID THE HOUSE KNOW? The clerk knew within a day of a
    question asked on Kael's own spire stair with only Kael, Sol and Tam present
    (Ansa's window overlooks the awning, not the spire stair). Candidates: the
    hooded watcher (ch.16 rope bridge), a leak through Tam's own circle, someone
    in the Ashworth household. AUTHOR DECIDES; do not make Tam or Ansa the leak
    cheaply; do not resolve before ch.30. Kael noticed it and said nothing
    aloud in ch.24 (his face did not move); ch.25 may have Sol notice it.
35. NEW (ch.24): THE STACK. About 200 withdrawal leaves under a brass weight,
    ink long dry, corners soft (printed days before Tam asked). Implies Thorne
    planned the exit before the entrance drew a single leaver. Do not name a
    printer or set a printing date; the number of days is Kael's open question.
36. NEW (ch.24): THE TABLE'S BOOK. The clerk records every request to see the
    standard with the hour (Kael's on 30 Sunspire; Tam and two others at dawn on
    1 Cinderveil). Possible exposure evidence at the public sitting (signers
    asked to read the terms and were refused). AUTHOR DECIDES; Kael cannot
    demand the book, only the Chancellor's clerks can.

## Known landmarks to watch for once chapters reach them

- Ch.18: the formal "Co-leadership" idea is dead; private promise only
  (formal cession is ch.39).
- Ch.20: DONE. Deed fully understood; trimmed from 4,190 to about 1,860.
- Ch.21: DONE (proofread pass). Last line of the Schedule read as reaching
  future contracts; annex withdrawn.
- Ch.22: DONE. Annex found circulating as provisional engagement; consent
  mechanism; false "auditor has read it and raised nothing".
- Ch.23: DONE. Table scene told; Kael's public disclaimer and written
  statement; clerk's "has been asked"; Tam's question ends the chapter.
- Ch.24: DONE. Tam answered honestly ("I do not know"); Kael's impulse to
  decide for him named and stopped; consent mechanism shaped; Thorne's form of
  withdrawal and the pre-printed stack end the chapter.
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
- Do not estimate word counts from byte size: a session estimated ch.21 at
  about 1,740 from bytes and the real count was well above the floor (1,859).
  Count the actual text.
- Defect categories to scan any unchecked chapter for: wrong magic system,
  invented soulbond (brief rule 15), wrong Thorne seal, front-loaded plot,
  corrupted or non-Latin characters, under word floor, chapter-number
  meta-references, meta breaks ("the brief", "this book").
- Repo owner is `aliwaziri10/Voxel`. Default branch is `main`.
- Sandbox for bash has no network, so raw-URL word counts are not available
  there; word counts are taken on the drafted text before push and the push is
  confirmed via commit stats or a contents-API re-fetch.
- Push chapter AND HANDOFF in ONE `push_files` call (three slips so far where
  they landed in separate commits: ch.20, ch.23).

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
- 2026-09-28 (session 4): ch.21 had been rewritten in `d206fd1f` by an earlier
  session with no HANDOFF entry. This session verified account
  (`aliwaziri10`), read charter, HANDOFF, brief, ch.21 and ch.20, confirmed
  ch.22 is still the untouched bot draft, then proofread ch.21: five fixes
  (see status), 1,859 words, chapter and HANDOFF pushed in ONE commit
  `6f2d43b5`. Ch.21 canon logged; findings 22-24 added.
- 2026-09-28 (session 4, cont.): old ch.22 read in full and replaced (see
  status: Embervein, Chancellor Veyra, joint mandate and the restaged
  confrontation all retired). Ch.22 rewritten to 1,857 words, chapter and
  HANDOFF in ONE commit. Ch.22 canon logged; findings 25-28 added.
- 2026-09-28 (session 5): account verified (`aliwaziri10`), charter, HANDOFF,
  brief, ch.22 and old ch.23 read in that order. Old ch.23 replaced with a
  Sol-POV rewrite (1 Cinderveil, 1,941 words incl. header; first draft 1,754,
  one sub-beat added). Caught that Sunspire has 30 days, so the plan's "31
  Sunspire" and ch.22's "the thirty-first" were wrong; ch.22 fixed. Chapters
  pushed in `ee2a9683`, this HANDOFF in the next commit (two commits, a
  process slip). Ch.23 canon logged; findings 28 resolved, 29-32 added. Next:
  ch.24 (2 Cinderveil; read old ch.24 in full first; it opens on Tam's
  question).
- 2026-09-28 (session 6): account verified (`aliwaziri10`), charter, HANDOFF,
  brief, ch.23 and old ch.24 read in that order. Old ch.24 (Embervein, Mara's
  burned hands, solo descent, thorned-crown seal) replaced with a Kael-POV
  rewrite (2 Cinderveil, 2,007 words incl. header; scans clean before push).
  Chapter and HANDOFF pushed in ONE commit. Ch.24 canon logged; finding 32
  resolved, findings 33-36 added; ch.25 plan written. Next: ch.25 (3
  Cinderveil, Sol POV; read old ch.25 in full first; carry Tam's decision and
  the withdrawal form's cost). Verify ch.24 via the contents API first.
