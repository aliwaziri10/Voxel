# HANDOFF - Kindling Line Book 1

## ZIA'S STANDING RULES (read first, every session)
1. **Style.** Anything Zia must copy, paste or run (workflow or YML links, file paths, commands, text) is given full length, with the full link or path, in its own code block so it has a copy button. Never shortened, never partial.
2. **Never assume.** Research and verify against the live repo or source first, then answer. If something is not verified, say so plainly. Never present a guess as fact.

**Status (2026-10-03):** continuity passes 1 to 4 are APPLIED to Book 1. Pass 4 landed in commit `37fc3f4` (ch.2, 4, 6, 17, 37, 38, 39, 40, 41, 43, 44, 45; ch.42 untouched). Follow-up fixes by hand: ch.41 "two days ago" x2 (`6190358`), ch.2 "waited twelve years" (`414f4f7`), and the ch.40 to 43 reframe (`60fd62d`, below). Book 2 got only the Year 4 headers and four mother lines (pass 2). Re-runs are safe; pass 1 printing MISSING on a re-run is expected noise.

**Scripts:** `scripts/fix_book1.py` runs pass 1, then `fix_pass2.py`, then `fix_pass3_mother_ward.py` (which runs `fix_pass4` first). Workflow: Actions, "Fix Book 1", browser "Run workflow". Only pass 2 and pass 3 decide the exit code. A failed run commits nothing, so a stale rule in pass 2 or 3 blocks everything. Assistant writes to `.github/workflows/` return 403; Zia pastes workflow edits himself. The GitHub tool replaces whole files only, so a script saves tokens only when it carries many edits.

**Canon (locked by Zia, do not reopen):**
- Valerius Ashworth is alive through Book 1 and is "former Lord Auditor, senior advisor to the Accord". He wrote a dissent, was overruled, and Corrin stamped the denial with his own seal (Corrin paid fifteen thousand crowns for it). He is stripped of his seat in ch.44 (5 Sunspire, Year 3) and dies off-page between the books. Book 2 is Year 4: "eight months in the ground".
- Sol's mother: Reckoning twelve years before Book 1. She went under a plate with a ward Corrin sold her that was never truly bound. She burned forty years in one flight, died at 42, looked eighty. Sol was twelve. The mother died three winters later. Book 2 matches.
- Sol's aunt is Rue. The dead ward is Mira, who died on the ledge and left a sister. The Vane seat is on the western face. Ch.45 uses flight-harnesses, not wings.
- The Reckoning is 29 Frostveil, Year 3 (30-day months). Ch.44 explains Sol's count: nine years at the old burn rate, twenty-two at the new one.
- Ch.40 to 43 are four stages, not four verdicts (Zia, 2026-10-03, done in `60fd62d`): ch.40 Reckoning, interim ruling only (Corrin frozen, debt suspended pending the Council's inquiry, Vane in good standing until the Council rules); ch.41 the Council's formal ruling; ch.42 the charter and oversight board (the ward trade continues under it); ch.43 aftermath (the OLD trade is dismantled). Do not merge or re-verdict them. The body says "Council", never "Conclave".

**STILL OPEN:**
1. Spelling: Book 1 mixes gray and grey. Ch.40 and 41 now use grey. Ch.42 and others still have gray, graying. Fix with a script replace (gray to grey, graying to greying), not by hand.
2. Left alone by Zia's decision: the header-vs-prose pacing (ch.34 rupture about nine days before the Reckoning in headers, "six weeks" in prose). Do not change it.
3. Minor, still to check: ch.4 "eight weeks" beside "fifty-four days"; Sol is 24 in ch.17 (check other chapters).
4. Name overlap: Book 1 has Auditor Mara Vex (ch.40) and Book 2 has an Ashworth warden named Mara. Decide whether to rename one.
5. Ch.22 was patched, not rewritten; read it through. Ch.3 chain logic was patched; read once. Ch.35 "Four since the Kindling woke" was left as a scale statement.
6. Book 2 `full_manuscript.md` is stale. Regenerate it from the chapter files; do not hand-edit.

**Process notes:** `proofreader.py` is wired into `voxel_cli.py`. `brief.txt` holds 10 LOCKED RULES. Deferred to Zia: cover direction, `ai_disclosure_included` and `kdp_metadata_approved` gates.
