# HANDOFF - Kindling Line (series-level, Book 3 not yet started)

Written 2026-10-03 at the end of a session. Pushed to the repo at Zia's request; identical to the text Zia pasted into the next profile. Nothing else in the repo was changed for Book 3.

## READ FIRST - ZIA'S STANDING RULES
1. Anything Zia must copy, paste or run (links, paths, commands, text) goes full length, full link or path, in its own code block with a copy button. Never shortened.
2. NEVER ASSUME. Research and verify against the live repo or source first, then answer. Label anything unverified as unverified.
3. No book title may use the What/Where/When/Why/How template. Zia dislikes it; Amity Falls Book 4 was deliberately retitled away from it. Titles must be specific and distinct.
4. The Kindling Line is a ROMANCE (Romantasy). Romance is the A-plot. Do NOT let it become a political or legal saga.
5. Zia dictates by voice, so proper nouns may arrive garbled. Verify before trusting.

REPO: aliwaziri10/Voxel (NOT Wazzaboyzz/Voxel). Default branch: main (verified). Read novels/EDITORIAL_CHARTER.md FIRST, then the book's HANDOFF.md. Both Kindling HANDOFF files already carry rule 1 and rule 2 at the top (commits d95d979 and 34a482c). Rules 3 and 4 are NOT yet in them.

## STATE OF BOOKS 1 AND 2 (verified this session)
- Both 45 chapters, proofreading complete, nothing published online. Zia's plan: write all three books first, then publish 1, 2, 3 in order.
- Workflow "Finalize Kindling" ran successfully after a bug fix (build_manuscript.py, commit 9c2e43f: the old check flagged its own finished "* * *" scene break). Commit ff0924b landed (grey spelling + rebuilt full_manuscript.md files). Built kdp_out/kindling-line-book-1.docx (3943 paragraphs) and book-2.docx (2602 paragraphs), 6x9. Zia reports both under 220 KB, which is plausible and far below KDP's 650 MB limit.
- Run page: https://github.com/aliwaziri10/Voxel/actions/workflows/finalize-kindling.yml
- UNVERIFIED: whether Zia applied the edit that uploads the two docx as two separate artifacts; whether the docx files look right in Word; whether the artifact upload step succeeded.
- Titles come from each book's book_config.json "title" field; docx is built from it. Retitling = edit that field, re-run Finalize. Not checked: front matter or blurb drafts carrying old titles.
- Do not commit to the repo while Finalize is running: its final push can be rejected.
- Per Book 1 HANDOFF, assistant writes to .github/workflows return 403 (not re-tested); Zia pastes workflow edits himself. GitHub tool replaces whole files only.
- Repo code search (search_code) is UNRELIABLE: it returned incomplete_results and missed "Deep Vault", which exists in Book 1 ch.45. Do not trust a zero result from it.

## KEY FINDING - SEAM BETWEEN BOOK 1 AND BOOK 2 (verified in Book 1 ch.45 and Book 2 HANDOFF)
Book 1 ch.45 ends on the "Contract of Perpetual Surety", the "Deep Vault", the "Keeper of the Burning Ledger" (said to be the Kindling itself), "Magister Vane", and a hostile hawk diving at the Ashworth aerie. Book 2's HANDOFF BANS all of those terms, and Book 2 ch.44-45 (the only Book 2 chapters read this session) never mention them. Book 1 therefore promises a conspiracy Book 2 never delivers. RECOMMENDATION (needs Zia's approval before any edit): rewrite Book 1 ch.45's final section so the closing hook is romance-forward and consistent with Book 2. STILL TO CHECK: whether other Book 1 chapters mention Vault/Keeper/Contract/Magister (read chapters or full_manuscript; do not rely on search_code). Book 1 ends 7 Sunspire Year 3; Book 2 is Year 4.

## GENRE FINDINGS
- Both briefs say Romantasy. The plans themselves were political: Book 1 makes Kael an auditor with legal power over Sol's claim, Reckoning as a trial; Book 2's brief makes the antagonist House Thorne's legal takeover (Ward Deed of Succession), climax a public Council ceremony, and Kael/Sol's conflict is who signs warrants. So drift came from the plan, not only from the generator. Book 2 ch.45 ends on a political question (Chancellor asks who held the ledger pen forty years ago).
- Market research (secondary sources, partly blogs): romantasy is growing (Bloomberg est. $610M in 2024 vs $454M 2023; Circana: fastest-growing print category 2024) but shows saturation/"fatigue" signals and concentration among top authors. Readers hold romantasy to romance rules for plot beats; the ending must be an earned HEA that resolves the central conflict; early series books may end HFN, the final book delivers HEA. Test: if you remove the romance and still have a story, it is not a romance.
- Zia's decision: genre was a deliberate move to romance; Book 3 must honor it.

## BOOK 3 - CLAUDE'S DECISION AT ZIA'S INSTRUCTION ("decide on the third book")
Zia has NOT explicitly confirmed it; she rejected only the title. Working shape:
- Series arc as three versions of one failure: Book 1 he hid the truth; Book 2 he decided for her; Book 3 SHE decides for HIM. Driving question: how long do they get together, and who decides what that time is worth.
- 1 Opening quarter: leftover Book 2 threads (Anchor Seven tap, Renn missing, Mara hurt and not waking, the forged line / Aldous's tutor, the second line under the boiling house) closed quickly via known people. No votes, no hearings.
- 2 Midpoint: public commitment to a shared life. Explicitly NOT a ward-binding (forbidden between them by Book 1 rules).
- 3 Dark moment: Sol sees the cost on Kael and leaves, deciding alone to protect him.
- 4 Climax: a rescue flight only Sol can make. They decide it together, out loud ("every time", Book 2 rule). Kael chooses to stand near knowing what lands on him. Transfer stays involuntary; her training makes the cost smaller (training changes HOW MUCH, never WHO).
- 5 Ending: permanent HEA, short epilogue years later, growing old together.
- Politics capped and background only.

## LOCKED CANON TO RESPECT (from HANDOFFs and Book 1 brief; verify against chapters)
Cost transfer is always involuntary; no ward-binding or chosen buffer between Sol and Kael; wards belong only to the paid, contracted ward trade; Sol burned 3 years at Book 1's Reckoning and Kael absorbed 3 (Book 1 ch.45); Kael has silver at his temples; Book 2 ends 30 Cinderveil Year 4 (ch.45): tap closed on a count of eleven, a pulse from the east under the boiling house, petition signed with two names (Sol co-lead, "two names or none"), Sol and Kael together, intimate scene in ch.44. Word floor 2,300-2,700 per chapter. No em dashes. Avoid "particular" and "some/something ___" hedges. Spell grey.

## NEXT STEPS FOR BOOK 3, IN ORDER (per novels/BEAT_MAP_PROTOCOL.md)
1. Get Zia's confirmation of the Book 3 shape above and of the Book 1 ch.45 rewrite.
2. Step 0: audit names against EVERY Voxel novel (Amity Falls 1-4, Where the Frost Doesn't Reach, Kindling 1-2).
3. Write the canon lock with a CLOSED CAST LIST (any name not on it must fail a check), calendar computed once (month list not yet verified), locked one-time lines.
4. Write the beat map (15-20 lines per chapter, previous chapter's real text fed into the next, generate 5 chapters at a time, verify between batches).
5. Create the rest of novels/kindling-line-book-3/ (brief.txt, book_config.json, VOICE_GUIDE.md, architecture.md); this HANDOFF.md already exists there.
6. Add a measurable GENRE GUARD to the canon lock: every chapter names a romance beat first; chapters must fail without the romance; council/legal scenes capped; no new factions or magic rules. UNVERIFIED whether scripts/proofreader.py can enforce a cast whitelist; if not, write a small script.

## UNVERIFIED THIS SESSION
- Sol's remaining-years count ("nine years at old burn rate, twenty-two at new") comes from Book 1 HANDOFF; Book 1 ch.44 not re-read.
- Calendar month order and lengths.
- Mara and Renn details (only from HANDOFF canon lines).
- Book 2 chapters 1-43 and Book 1 chapters 1-44 were not read this session.
- Whether Book 1's book_config.json author is Ivy Cassel (Book 1 architecture and Book 2 config both say Ivy Cassel).

## TITLES
- Book 1: Zia chose BORROWED YEARS (not yet applied; current config title is "What the Gift Demands").
- Book 2: Zia rejected "What the Ledger Keeps", "Hold Me to It", "Eleven Breaths". New options (not collision-checked on Amazon): Count With Me; Two Names or None; Say It Aloud; Ink and Ash.
- Book 3: Zia rejected "What the Years Hold" and "All the Years Between". New options: Years Enough; Silver at His Temples; Stand Near Me; Slow to Burn.
- Series name stays "The Kindling Line". Series recognition should come from KDP series metadata and matching covers, not title shape.
- Zia has not yet picked Book 2 or Book 3 titles.
