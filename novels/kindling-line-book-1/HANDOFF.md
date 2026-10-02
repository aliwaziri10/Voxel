# HANDOFF - Kindling Line Book 1

**Status (2026-10-03):** continuity passes 1 to 4 are APPLIED to Book 1. Pass 4 landed in commit `37fc3f4` (ch.2, 4, 6, 17, 37, 38, 39, 40, 41, 43, 44, 45; ch.42 untouched). Book 2 got only the Year 4 headers and four mother lines (pass 2). Re-runs are safe; pass 1 printing MISSING on a re-run is expected noise.

**Scripts:** `scripts/fix_book1.py` runs pass 1, then `fix_pass2.py`, then `fix_pass3_mother_ward.py` (which runs `fix_pass4` first). Workflow: Actions, "Fix Book 1", browser "Run workflow". Only pass 2 and pass 3 decide the exit code. A failed run commits nothing, so a stale rule in pass 2 or 3 blocks everything. Assistant writes to `.github/workflows/` return 403; Zia pastes workflow edits himself.

**Canon (locked by Zia, do not reopen):**
- Valerius Ashworth is alive through Book 1 and is "former Lord Auditor, senior advisor to the Accord". He wrote a dissent, was overruled, and Corrin stamped the denial with his own seal (Corrin paid fifteen thousand crowns for it). He is stripped of his seat in ch.44 (5 Sunspire, Year 3) and dies off-page between the books. Book 2 is Year 4: "eight months in the ground".
- Sol's mother: Reckoning twelve years before Book 1. She went under a plate with a ward Corrin sold her that was never truly bound. She burned forty years in one flight, died at 42, looked eighty. Sol was twelve. The mother died three winters later. Book 2 matches.
- Sol's aunt is Rue. The dead ward is Mira, who died on the ledge and left a sister. The Vane seat is on the western face. Ch.45 uses flight-harnesses, not wings.
- The Reckoning is 29 Frostveil, Year 3 (30-day months). Ch.44 explains Sol's count: nine years at the old burn rate, twenty-two at the new one.

**STILL OPEN:**
1. **Zia:** ch.40, 41, 42 and 43 each deliver a Reckoning verdict. Merging them is a scene rewrite, left alone.
2. **Check against live text and headers (found by reading the pass 4 patch, not yet verified):** ch.41 says "four days" since the ledger was presented, but headers suggest two (29 Frostveil to 1 Sunspire). Ch.39 says "six weeks" of drills, but headers put the rupture only about a week before 28 Frostveil. Ch.2 still has "I have waited seven years" near the new "twelve years". Ch.4 has "eight weeks" beside "fifty-four days". Ch.40 still has "cracked wing-bone". Sol is now 24 in ch.17; check other chapters for her age.
3. Ch.22 was patched, not rewritten; read it through. Ch.35 "Four since the Kindling woke" was left as a scale statement. Ch.3 chain logic was patched; read once.
4. Possible name collision: Book 2 has an Ashworth warden named Mara. Check Book 1's mother's name against it.
5. Book 2 `full_manuscript.md` is stale. Regenerate it from the chapter files; do not hand-edit.

**Process notes:** `proofreader.py` is wired into `voxel_cli.py`. `brief.txt` holds 10 LOCKED RULES. Deferred to Zia: cover direction, `ai_disclosure_included` and `kdp_metadata_approved` gates.
