# Book 4 proofed log

Only what was read from live `main` is stamped. Never stamp from memory or a
handoff claim. Keep chapter entries to 2-4 lines; put repeated style notes in
Open question 14, not per chapter.

Legend: FIXED = edit read back from the live chapter. READ = sequential manual
read, no text change. OWED = real read not done. NOT PROOFED = mechanical pass
only.

## HIGH PRIORITY - NEEDS ZIA'S DECISION BEFORE ANY FURTHER WHITLOCK EDITS
Ch.14's central plot reveal (Wren becomes Warden by valley consensus) is
built on a note the text explicitly calls "Josiah Whitlock's precise script,
the same hand that had written the warning letter," and then says this same
person "tried to end the bargain," failed, and "hid the complete terms."
That directly conflicts with the already-RESOLVED canon below: Josiah
predates Ambrose's 1872-1901 tenure and only signed the 1847/1863 documents;
it is AMBROSE who taught Adelaide, attempted to end the bargain in 1889
(ch.3's "never change this" anchor), and hid the complete terms (Adelaide's
own account, ch.5). Ch.15's letter (separately verified this session)
correctly names Ambrose for this same story. Ch.14 has the wrong Whitlock in
its own key scene. NOT fixed - the note is load-bearing for the whole
chapter (Josiah is named four times in dialogue), so a rename needs Zia's
say-so on which way to resolve it, not a guess.

ALSO NOTE (found during ch.17-22 read, 2026-09-22): this file is internally
inconsistent on the same question. The paragraph above says the tried-and-
failed/hid-the-terms story is AMBROSE's. But the ch.9 commit message
(`0041d89`) says: "the tried-and-failed/hid-the-terms story now correctly
belongs to Josiah, matching the J. Whitlock 1847/1863 signatures." These are
opposite claims. Zia's decision on ch.14 needs to resolve BOTH this file's
self-contradiction and the chapter text - not just pick a chapter-14 fix in
isolation. Every new sighting of this story in ch.17+ is being logged as
flagged-not-fixed, same as ch.14, until this is settled. Ch.18 independently
names "Ambrose Whitlock" for this same tried-to-end-it story (Theo's line:
"the history that Ambrose Whitlock tried to end") - a second data point
(after ch.15's letter) supporting AMBROSE as the intended attribution, for
whenever Zia makes the call.

🔒 ch.17-22 claimed by Claude session, 2026-09-22 (IST). Ch.17-18 done this
pass (see Chapter status). Chapters 1-16 read/fixed as logged below (plus
ch.2 and additional ch.15 fixes since).

## Decided and applied
- Folio gap is 1887-1891 (last present 1886, first back 1892). Applied in
  ch.3, commit `207db70`. Check every later chapter that cites the gap years.
- Josiah vs Ambrose Whitlock naming (WHO SIGNED WHAT): Josiah signed the 1847
  marginal note and the 1863 hidden letter (both predate Ambrose's 1872-1901
  tenure). "A.W." in newer ink is Ambrose, who taught Adelaide. Fixed in
  ch.2 (`8c1aa1c`), ch.6 (`f9495fc`), ch.7 (`b98711c`), ch.9 (`0041d89`),
  ch.12 (`0553dba`), ch.13 (`e847ef7`), ch.14 partial (`d1c4763`: note author
  only), ch.15 (`ffe3562`). Ch.13 confirms this naming without a fix needed.
  This is separate from the WHO-TRIED-TO-END-IT-AND-HID-THE-TERMS question,
  which is still open - see HIGH PRIORITY above.
- Drake countdown "closed" verdict is RE-OPENED: ch.9 already has the printer
  confirmed ("final files by Friday"), ch.10 restarts planning from zero
  (eight weeks, council in three days for press funding), ch.14 has files due
  "noon tomorrow" for "Friday distribution" (i.e. imminent, 1-2 days), ch.16
  restarts it again after Drake's teaser forces a re-plan (two weeks, target
  date "the fifteenth", 14 days), ch.37 repeats the Friday print deadline.
  Ch.14's imminent deadline followed by ch.16's reset is plausibly a real
  plot beat (Drake's teaser blows up an almost-finished publication and
  forces a new plan) rather than a pure contradiction - but the full set of
  countdown numbers across all chapters still needs one pass to confirm they
  chain correctly in order. Re-check in the season/countdown pass. Ch.18 adds
  YET ANOTHER restart: an emergency council vote accelerates a stated
  "six-week schedule" to "ten days" (fixed an internal 10-vs-13 contradiction
  within the chapter itself, commit `4115858`), with named dates the 8th
  through 13th. This is at least the THIRD distinct countdown restart
  (ch.14's 1-2 days, ch.16's 14 days, ch.18's 10 days) - the season/countdown
  pass needs to establish whether these are sequential re-plans after
  Drake's teaser (plausible) or the same beat drifting across chapters.
- Anachronism pattern (FIXED in ch.8 and ch.12): early chapters treated the
  Drake trial, court testimony, "leverage collapsed" and "Dev proved the gap
  was deliberate" as past. Those are ch.36-45 events. Watch ch.17-35.

## Open questions for Zia (none touched; each needs a decision)
1. ELENA CASTELLANO. Ch.5 and ch.7: Wren's living MOTHER (baker, "Mama").
   Ch.11: Dev names "Elena Castellano" as Wren's dead GRANDMOTHER (1985
   search, lullaby) and Wren agrees. The grandmother is never named elsewhere.
   The ch.3 fix (1870s Elena -> Clara Castellano, commit `61225b8`; "her
   grandmother" -> "great-great-grandmother") was made on ch.11 alone and is
   in question. Options: rename the grandmother in ch.11; or two Castellano
   women.
2. WARDEN OF THE FIRST DEBT. Ch.3: Yusuf is the current Warden. Ch.9: Wren
   concludes she is the Warden by custody. Ch.11: Yusuf is the WEATHERS rep and
   Mara Voss the WARDENS rep. Ch.10: "the Warden elder" is a separate person.
   "Warden" is both a lineage and an office. Ch.14 adds a THIRD mechanism:
   Warden by valley consensus (see HIGH PRIORITY note - this reveal is itself
   compromised by the Josiah/Ambrose mixup, but the consensus MECHANISM idea
   is new and needs reconciling with ch.3/9/10/11's other Warden claims
   regardless of whose handwriting the note turns out to be in). Check ch.31
   and ch.37.
3. DRAKE'S 2005 MILLBROOK ATTEMPT. Ch.5: he coerced "a Whitlock descendant."
   Ch.11: he coerced the Finder Silas Kettering (served two years, out '09).
4. ADELAIDE. Ch.4: Wren's grandmother, a Finder ("For my granddaughter").
   Ch.5, 9, 12: Adelaide Whitlock, Ambrose's student and a Warden, undated
   1960s letter. Ch.4 is the outlier.
5. CH.5 CONFLICTS (text unchanged). Whitlock "alive in 2005, died 2009" vs
   ch.3's 1872-1901; Warden role "vacant" vs Yusuf; Drake "in custody" while
   his attorney files a motion (ch.4, ch.6-12 have him active); "four days"
   count wrong inside the chapter; "six times now" to Millbrook vs a first
   visit in ch.4; Harriet "raised her son ten years." Also two stray-space
   italics glitches, and the skipped-fix string "She was the Warden after
   him..." (2 matches; logged fix says "before").
6. LINEAGE ROSTER. Ch.11: six lineages (Wardens, Menders, Callers, Weathers,
   Finders, Wicks) with reps Mara, Aris Thorne, Priya, Yusuf, Dev, Odette;
   ch.37 says six; ch.10 says "five of seven." Dev is the Finders rep (ch.10,
   11) but "maintained" the Caller field at the ring (ch.8). Mara is "a Finder"
   in ch.5, a Voss/Mender line in ch.3, Wardens rep in ch.11.
7. CALENDAR. Ch.5 late summer; ch.8 reads a "year-old" notebook with Jan-Feb
   entries then Nov 3-12 entries that duplicate the book's present; ch.9
   "July"; ch.10 bare winter trees; ch.11 about Nov 6 ("fading since Nov 3,
   noticed three days ago"); ch.12 November, "recorded last spring"; ch.13
   "afternoon light was golden" (no season named); ch.14 "morning light
   slanted... sharp angle" (no season named); ch.16 spring, apple blossom,
   orchard blooming. Ch.4's cold-case review "next month" also unresolved.
   Ch.17 "no streetlights... sky thick with stars", ch.18 "afternoon light" -
   neither names a season. One calendar needed.
8. WREN'S MOTHER'S JOB: baker (ch.7), "clinic" (ch.8), "store by nine,
   Odette's back room" (ch.10).
9. HARRIET'S HOME: assisted living (ch.4), gardening (ch.5), roses at home
   (ch.8), nursing home (ch.9), care facility (ch.12, ch.16). Ch.4 Doris says
   she still visits asking about the gap. Ch.13 has Theo visiting a "care
   facility two counties over" reading her newspapers weekly - consistent
   with "care facility" wording, not "two hours" drive-time language.
10. KISS AND RUPTURE ARE EARLY. Ch.5 and ch.9 refer to the kiss interrupted by
    Yusuf's call ("three weeks ago"); ch.9 says "The rupture. It was here."
    Beat map: first kiss ch.21, rupture ch.30. Ch.13-14 have Theo and Wren
    still pre-relationship/circling (tender charged moments, held gazes,
    "chest ache" - but no kiss), consistent with the beat map's later
    placement, not a contradiction. Ch.17 NOW HAS an actual on-page kiss
    ("Not a question this time. Not a test." - implying the ch.5/9
    interrupted kiss was "the test" - then a full kiss, chapter-closing "she
    had found it" beat), i.e. the real first kiss lands in ch.17, not ch.21.
    The beat map's placement no longer matches the live text at all; either
    the beat map is stale or ch.21 needs to be a different relationship beat.
11. ARCHIVE BUILDING. Ch.9: tall windows, oak table, locked cabinet, spring
    under the floor. Ch.12: "converted cold-storage shed." Ch.16: "the
    repurposed library on Main Street", new sign not yet up. Ch.13-14 both
    call it "the municipal building" / "the archive" generically (no
    library/shed language) - so at minimum a THREE-way naming problem
    (municipal building vs library vs cold-storage shed) across ch.9, 12,
    13, 14, 16. Ch.18 adds "a converted barn behind the general store" - a
    FOURTH description. Check ch.3-4 too.
12. SMALL CONTINUITY. Two Silases (Kettering ch.11, Harker ch.37). Theo's
    search is "fifteen years" (ch.4, 11) or "nineteen" (ch.10, 12). Ch.15
    live text (re-read 2026-09-21 in full): Theo says "I'm twenty-six now"
    (sixteen + ten years), NOT 36 as previously logged here — that "36" claim
    does not match the live file and should not be carried forward. Twenty-six
    is a 1-year mismatch against born-1997/present-2024 (would be 27), not the
    9-10 year gap earlier logged. Ch.13 adds "eight months in the valley" -
    a new duration figure (presumably since he started working with Wren,
    not the whole search - not necessarily contradictory, log only).
    "Standing arrangement" means two things (ch.3 ledger notation; ch.4
    sealed 2005 record). The 1942 renewal gap (ch.10) is unexplained (ch.18
    mentions "the 1942 ledger" again, no new info). Ch.11 Wren's "first
    search... the first one" vs "paid small debts before." Ch.37 still has
    Drake "in a county holding cell" but the arrest is in ch.41. Ch.17
    CONFIRMS Theo's age cleanly: "I was seven when it happened" (Drake's 2005
    Millbrook attempt, "nineteen years" before the present) means Theo was
    born ~1998, age 26 in 2024/present - matches ch.15's corrected age with
    no gap. Good cross-check, no fix needed.
13. SPACED HYPHENS " - " as em-dash substitutes (invisible to the U+2014
    checks). Counts: ch.3 ~8, ch.4 ~14, ch.6 ~3, ch.7 ~9, ch.8 3, ch.9 0,
    ch.10 6, ch.11 11, ch.12 22, ch.16 ~2, ch.13 ~1, ch.14 0 seen, ch.18 ~2.
    Treat as house form, or sweep the book?
14. STYLE (line-edit, not mechanical; not fixed anywhere). Staccato fragment
    stacks; "Not X. Y" and "That's not X. That's Y." pivots; theme-restating
    scene endings; explaining-the-subtext speeches; echo dialogue (ch.6 x9);
    repetition density ("nineteen years" ch.4 x11, "thirty days" x13, "cost"
    ch.9, "timeline" ch.10, "ten days" ch.18 x9); heavy "said" tags (ch.8, 11,
    12).
15. DENISE / MARA / CALEB RELATIONSHIP, new find ch.16. Denise says at the
    council session: "I took two years from my grandson's husband" — but the
    same scene has Mara Voss and Caleb as the couple ("Mara's hand on Caleb's
    arm"), which reads like Caleb should be a granddaughter's husband, not a
    grandson's. NOT fixed — have not verified whose grandchild Mara or anyone
    else is in any other chapter. Ch.18 shows Mara and Caleb again as a
    couple (both vote "we accelerate" in sequence, no new relationship info).
    Needs a check across ch.1-12, 17+ (and Books 1-3) before touching this line.

## Chapter status
- ch.1: READ. No fix. Theo 26 confirmed.
- ch.2: FIXED (`8c1aa1c`): loupe-reading line Ambrose -> Josiah (7yrs/sister's
  face) to match Wren's own notebook entry two pages later. Harriet's decade
  1997-2007 confirmed.
- ch.3: FIXED (`207db70`): gap years, Elena label. Elena change in question (Q1).
- ch.4: READ. No fix. Flags: Q4, Q9, Q12, Q14. Ch.4's 1891 Eleanor Whitlock entry
  is the county Whitlock folio, not the valley renewal folios (no conflict).
- ch.5: READ, NOT CLEARED. No fix. See Q2-Q7, Q10, Q13.
- ch.6: FIXED (`f9495fc`): manuscript author Ambrose -> Josiah.
- ch.7: READ; FIXED later (`b98711c`): 4x Ambrose -> Josiah. Elena = mother (Q1).
- ch.8: FIXED (`46bd7e8`): removed three trial/leverage anachronisms. Flags: Q7, Q8.
- ch.9: READ. No new fix (`0041d89` live). Flags: Q2, Q7, Q9, Q10, countdown.
  Drake's lawyer asks for a meeting with a "proposal": check follow-up.
- ch.10: READ. No fix. Flags: Q2, Q6, Q7, Q8, Q12, countdown.
- ch.11: FIXED (`8d63946`): Odette Reynolds -> Reyes (4). Flags: Q1, Q3, Q6, Q7, Q12.
- ch.12: FIXED (`0553dba`): truncated last sentence; ledger finder attribution;
  hidden letter author Josiah; two anachronisms. Flags: Q7, Q9, Q11.
- ch.13: FIXED (`e847ef7`): Ambrose -> Josiah (2 spots) per ch.9. Otherwise
  clean - Odette's proposal-memory scene, no timeline breaks found. Flags:
  Q7, Q9, Q11, Q12, Q13.
- ch.14: FIXED partial (`d1c4763`: note author Ambrose->Josiah [flagged, see
  HIGH PRIORITY - this naming may need to reverse], "her grandfather's
  handwriting"->"Whitlock's", typo "correct"->"corrects"). The central
  reveal's Josiah/Ambrose mixup is NOT resolved - needs Zia's decision. Also
  flags: Q2 (new "Warden by consensus" mechanism), Q7 (no season named), Q11
  ("municipal building" again), countdown ("files due noon tomorrow, Friday
  distribution").
- ch.15: FIXED and VERIFIED by full live read (`ffe3562`, building on
  `f8551915`): "your father" (not "your mother"), husband's death "gave out
  in 2003", "two hours" (not "two hundred miles"), "find Arthur Whitlock",
  Theo's age 36 -> 26, grandmother "died when I was fourteen" (was "before I
  knew her"), hidden-letter author Josiah. This chapter's own Whitlock
  attribution is internally consistent now (does not have ch.14's problem).
- ch.16: READ (out of sequence, corrected). No fix applied. Flags: Q7, Q9,
  Q11 (a FOURTH Archive location description), Q13, new Q15 (Denise's
  "grandson's husband" line). Internally consistent on dates/figures it
  does use. Countdown restarts again here.
- ch.17: READ. No fix - chapter is clean and self-consistent. Confirms Theo's
  age math (Q12: "seven when it happened" [Drake's 2005 attempt, "nineteen
  years" ago] = born ~1998 = 26 now, matches ch.15). New renewal-year data
  (1987, 1992, both within the established 1972-2022 renewal window, no
  conflict). Flags: Q10 (first on-page kiss happens here, ahead of the beat
  map's ch.21 placement - see Q10 for detail), Q7 (no season named).
- ch.18: FIXED (`4115858`): internal countdown contradiction "Thirteen days
  from today" -> "Ten days from today" (chapter said "Ten days" once, then
  "Thirteen" once, then "ten days" seven more times through the rest of the
  chapter - thirteen was the clear outlier). Flags: HIGH PRIORITY (a second
  "Ambrose Whitlock tried to end it" sighting, supporting Ambrose), Q7 (no
  season), Q11 (fourth Archive description: "a converted barn"), Q13, Q15
  (Mara/Caleb reappear, no new info), countdown (third distinct restart -
  see "Decided and applied").
- ch.37: FIXED by `f8551915` (Weather/Silas Harker rewrite, tell phrases). Real
  read owed; Q12 holding cell still present per Q5/Q12 note above - recheck.
- All other chapters: NOT PROOFED (mechanical pass only: 0 hard violations,
  0 em dashes).

## Not done
- Sequential read of ch.19-45 (ch.17-18 done this pass; ch.19-22 remain
  claimed and in progress).
- Season/month, countdown, and Archive-building-name pass (now at least a
  FOUR-way naming problem: municipal building / repurposed library on Main
  St / cold-storage shed / converted barn - see Q11). Check against Books 1-3.
- Zia's decision on the ch.14 Josiah/Ambrose conflict (HIGH PRIORITY, top of
  file), INCLUDING this file's own internal contradiction on who tried-and-
  failed/hid-the-terms, before that chapter can be marked FIXED.
