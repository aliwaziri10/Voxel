# HANDOFF - Kindling Line Book 3

Updated 2026-10-04. FREEZE: no new rules, sections or checks.

## HOW SESSIONS WORK
- Claude has no memory between sessions. The repo is the memory. Sessions run ONE AT A TIME, never in parallel. Do not guard against a second writer.
- If the repo changed since you last looked, it was a workflow commit (Finalize Kindling pushes commits and changes SHAs) or an earlier session. Fetch the current file and SHA before every edit; the GitHub tool replaces whole files only.
- Do NOT re-read Book 1 or Book 2 chapters to answer a fact. Use the digests: novels/kindling-line-book-1/digest/INDEX.md and novels/kindling-line-book-2/digest/INDEX.md (both complete, ch.1-45). Read a chapter only to confirm one fact.
- Write files straight to GitHub with the tool; a file made in the sandbox first has to be sent twice.
- Before ending a session: push the work and update the STATUS line below.

## READ IN THIS ORDER
1. novels/EDITORIAL_CHARTER.md
2. novels/BEAT_MAP_PROTOCOL.md
3. novels/kindling-line-book-3/CANON_LOCK.md (v3.1: authoritative for days, counts, plates, cast, calendar)
4. The batch files in novels/kindling-line-book-3/: BEAT_MAP.md (ch.1-15), BEAT_MAP_BATCH4.md (16-20), BEAT_MAP_BATCH5.md (21-25), BEAT_MAP_BATCH6.md (26-30), BEAT_MAP_BATCH7.md (31-35), then BATCH8 (36-40) and BATCH9 (41-45) if they exist. Where the old spine in BEAT_MAP.md for ch.16-45 disagrees, the batch files and CANON_LOCK win.

## STATUS
Nothing drafted: no Book 3 chapter text exists. Beat-map entries in full: ch.1-35. NEXT: write BEAT_MAP_BATCH8.md (ch.36-40) and BEAT_MAP_BATCH9.md (ch.41-45), built exactly like BATCH7; the old spine for ch.36-45 in BEAT_MAP.md has old counts (Kael 32, Sol 15, thirty-two each) and must be replaced using CANON_LOCK v3.1 (ending: thirty-three each). Then generate a batch only after the previous one is verified against its real text, five chapters per batch, real text of the previous chapter fed forward.
ROMANCE CHECK (Zia asked, 2026-10-04): batches 1-3 and 4-6 were written before the rule that the romance beat is a FULL SCENE (talk and touch, at least a quarter of the chapter; CANON_LOCK section 1). Before generating any chapter from them, check its romance beat is big enough and enlarge it if not. Batch 7 has three chapters apart (ch.32-34): ch.31 and ch.35 must give them real scenes together. Batches 8-9 must give heat and tenderness room: ch.37 (night before the descent) and ch.44 (aftermath) are the intimate chapters, cut away at the door, not explicit beyond Book 2's level.

## DECIDED (Claude under Zia's full delegation; Zia may reverse any)
- Sol (Isolde Vane) starts at 18 years left; Kael about 34. The stored sum is 17. Ending: Kael stands back because Sol asks aloud; she is at the plate, so the whole stored sum goes to her. Thirty-three each. (Burn ledger: CANON_LOCK section 4.)
- 45 chapters, odd Sol, even Kael. Three short political scenes only: ch.2, 12, 30.
- No month names in Book 3 except Cinderveil; chapter headers say "Day N". The Chancellor is Ingrith Tenn (off the page).
- The steward is the carrying hand; her reveal is ch.27 only (CANON_LOCK section 8). One-word fix to B2 ch.41 ("another man's handwriting" to "another hand's") only after ch.27 is generated and verified, by the editor, never the writer.

## ZIA'S STANDING RULES
1. Zia is a man, 51, not technical. ONE step at a time, plain language, click by click. Anything he must copy goes in its own code block, full length, full link or path.
2. NEVER ASSUME. Verify against the live repo; label unverified items. Be proactive: do the straightforward work, do not ask permission.
3. Be critical; flag problems, do not bury them. Also: do not overdo it, keep it simple.
4. Romance (Romantasy) is the A-plot. Politics is pressure only.
5. Zia dictates by voice, so verify any proper noun before trusting it.
6. When Zia asks for a reply for another profile, write the reply itself in a code block.
7. Titles: variety. Of the seven novels (four published, three Kindling) the new ones should not all open What/Where/When/Why/How.

REPO: aliwaziri10/Voxel (NOT Wazzaboyzz/Voxel), branch main.

## BOOKS 1 AND 2
- Both 45 chapters, proofread, not published. Plan: write all three, then publish 1, 2, 3 in order.
- Finalize Kindling must be re-run after commits 1fa8e02 (B2 ch.3) and 42bba69 (B1 carried hand "leans to the right"). Zia runs it here: https://github.com/aliwaziri10/Voxel/actions/workflows/finalize-kindling.yml
- Do not commit while Finalize is running. Assistant writes to .github/workflows return 403; Zia pastes workflow edits.
- Book 1 ch.45 was rewritten (commit c56f3f4): a Records clerk sends a loose ledger leaf from Corrin's seized books; every row's total is a year or two above its lines, the difference in a second, darker hand under "carried".

## NEXT STEPS
1. Write batches 8 and 9 (ch.36-45).
2. Romance check of batches 1-6 (see STATUS), then check batches 1-3 against the Book 1 digest.
3. Name audit across all Voxel novels for Ulla, Yelva and any new name (Book 1 has Auditor Mara Vex, ch.40; Book 2 has warden Mara).
4. Create brief.txt, book_config.json, VOICE_GUIDE.md, architecture.md for Book 3.
5. Verify batch 1, generate it, verify, then batch 2, and so on.

## TITLES (Zia's call; not needed to write the book)
- Book 1: Zia chose BORROWED YEARS (not yet applied; book_config.json still says "What the Gift Demands").
- Book 2: rejected "What the Ledger Keeps", "Hold Me to It", "Eleven Breaths". Options: Count With Me; Two Names or None; Say It Aloud; Ink and Ash.
- Book 3: rejected "What the Years Hold", "All the Years Between". Options: Years Enough; Silver at His Temples; Stand Near Me; Slow to Burn.
- Series name stays "The Kindling Line".
