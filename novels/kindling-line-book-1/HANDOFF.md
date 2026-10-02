## 2026-10-02 STATUS: continuity passes 1 and 2 APPLIED to Book 1 and Book 2 (commits `b2c3ff2`, `1ea8800`). This supersedes every "open decision / still wrong / unfixed" note from 2026-09-28 that used to sit here.
Scripts (re-runnable, idempotent): `scripts/fix_book1.py` (pass 1, then chains `scripts/fix_pass2.py`). Workflow: Actions, "Fix Book 1", browser "Run workflow" button.
**Canon decided (Claude's call, delegated by Zia, 2026-10-01/02) — do not reopen without Zia:**
- **Valerius Ashworth is ALIVE through all of Book 1** (stripped of his seat in ch.44, 5 Sunspire, Year 3). Ch.3 plants a failing heart. He dies off-page in the year between the books. Book 2 is set one year later (Year 4, opens 9 Sunspire) where he is "eight months in the ground". No uncle Corven.
- **Sol's mother:** Reckoning flight 12 years before Book 1; burned forty years in that single flight; Sol was twelve; she died three winters later. Sol's father (Lord Vane) is alive but ruined. Sol's aunt (new, minor, named Aunt Rue) replaces the invented grandmother in ch.22 and the "Aunt Mara" in ch.29; Mara is the mother's name.
- **Reckoning is 29 Frostveil, Year 3.** Every in-text countdown was matched to its `chapter_date` header (30-day months: Emberfall, Frostveil, Sunspire). A live scan found no mismatch beyond the ch.22 "fourteen days" arrears notice, which is a separate deadline.
- No em-dashes; no "chapter N" mentions in narration.
**Book 2 was touched only by pass 2:** all 45 headers Year 3 to Year 4, and four mother lines (ch.1, 4, 9, 31). Nothing else in Book 2 changed.

## 2026-10-02 (later) — mother-mechanism conflict: SCOPED, NOT YET FIXED, NEXT SESSION'S FIRST JOB

Zia confirmed Book 1 and Book 2 are being proofread **together** as one project; the mechanism conflict between them must actually be fixed, not just logged. Decision stands: **Book 2's mechanism is canon** (bound ward-taker under a plate). Book 1 needs to be rewritten to match.

**Real scope, checked live against every chapter this session** — this is NOT a one-line fix. The "she flew alone and burned, no ward" mechanism is load-bearing dialogue/plot logic in at least these Book 1 chapters:
- ch.1 (lines ~51, 145, 151, 173): Sol's own origin-story monologue and Kael's memory of her mother's flight.
- ch.2 (97, 99): Sol's accusation speech to Kael — "my mother burned forty years because she had no ward and no choice... That is the system you verify."
- ch.4 (43, 65, 93): ledger notations ("3.2 years burned," etc.), Sol's "Mother didn't have a ward" line, the steward's exposition on ward-vs-no-ward cost.
- ch.6 (63): background exposition, "no ward could be afforded."
- ch.7 (97, 157): a burned-records detail and a physical memory on a ledge.
- ch.8 (31, 49): Sol's own trained breathing technique, explicitly taught by the unwarded mother.
- ch.17 (63, 147, 207, 285): the clearest statement of the no-ward mechanic as an immutable rule ("No ward contract could shield against it unless... House Vane had never been able to afford a ward"), tied into the subplot that the ward-contract market was rigged against House Vane.
- ch.29 (17, 245, 311): Aunt Rue's grief, journal references.
- ch.41 (31, 45, 47, 51): the climax. Sol's public accusation against Valerius Ashworth is BUILT on "she had no ward... burned alone for eight years" as the legal/moral crux of the whole courtroom scene, and names her aunt "Mara Vane" (collides with Book 2's unconscious warden character Mara — separate open issue, note below).

**Why this needs a dedicated session, not a tail-end patch:** switching the mechanism to "bound ward-taker under a plate" changes WHY the mother died (a binding contract gone wrong, not an absence of one), which changes the moral shape of Sol's grievance against House Corrin and against Valerius Ashworth in ch.41's climax. This is a structural rewrite across 9 chapters' worth of dialogue and plot logic, not a search-and-replace. Attempting it with limited context produces a half-rewritten, internally inconsistent book — worse than leaving it alone a while longer.

**Also surfaced, separate from the mechanism issue:** Book 1's ch.41 names Sol's aunt "Mara Vane." Book 2 has an unrelated character also named Mara (an Ashworth warden, unconscious ch.24-45). Not the same person, but the name collision across the two books in the same series will read as an error to anyone who's read both. Flag for Zia: rename one of them.

**Next session, in order:** (1) confirm with Zia this scope and the Mara name collision before starting, (2) rewrite the ch.41 climax speech first since it's the load-bearing one, (3) work backward through ch.1/2/4/6/7/8/17/29 adjusting the earlier mentions to match the new ch.41 version, (4) re-run the 7 checks on every touched chapter, (5) update this file and Book 2's handoff together since the decision affects both.

**STILL OPEN (honest list, needs a human read):**
1. ~~Mother mechanism mismatch.~~ SCOPED above, canon direction decided, rewrite not yet done.
2. **ch.22** was patched, not rewritten. It still reads as the most off-canon chapter; read it through.
3. **ch.35** "Four since the Kindling woke" and ch.39 "two point three years" were left as scale statements; read for sense.
4. **Book 2 `full_manuscript.md`** is stale (noted in Book 2 handoff).
5. Ch.3 Kael gives Sol his father's chain; the surrounding logic was patched (chain "cannot leave his name"). Read once.
6. **NEW:** the Mara/Mara name collision between the books, above.

## STATUS 2026-09-27: all 45 chapters CONFIRMED DRAFTED
Verified live: `chapters/chapter_01.md` through `chapter_45.md` all exist with full prose (Ashworth/Corrin/Vane, Kindling cost-transfer mechanic, leads Kael Ashworth and Sol/Isolde Vane, Reckoning Accord). Don't trust "no chapters yet" language in old handoff sections without a live listing check.

## 2026-09-27 continuity pass (done)
Missing `chapter_date` headers fixed in ch.10, 12, 20, 21 (14, 17, 29 Emberfall; 1 Frostveil). The earlier "Thorne house seal / Ward Deed / Anchor Seven" audit does not match any file in this book; do not run it here.

## STATUS 2026-09-25: beat map re-run PASSED review
Beat map (workflow run `be1dd31`, key `book_beat_maps.kindling-line` in `story_bibles/kindling-line.json`) passed all 8 checks: Kael pockets the proof; Ashworth offer before ch.20; ward dies from Kael's delay before ch.27; real rupture ch.33-35; no voluntary ward for Kael; one Reckoning across ch.40-43; countdown lands on ch.40; dates have real gaps.

## Next step
Zia reads the six open items above, confirms scope for the mechanism rewrite, then a fresh session executes it. Then (optional) re-run `python voxel_cli.py proofread --book "Kindling Line Book 1"` via the browser workflow.

## Process notes carried over
- `proofreader.py` is wired into `voxel_cli.py` (`date_consistency_check` inside `novel`; `grammar_scan` as `proofread`).
- `brief.txt` has 10 LOCKED RULES; `voxel-novel.yml` reads it via `brief_file`.
- Assistant writes to `.github/workflows/` return 403: Zia pastes workflow edits himself via the `blob` page then the pencil. Other repo files can be pushed directly.
- Deferred to Zia: cover design direction; `ai_disclosure_included` / `kdp_metadata_approved` gates.
- Scope note: the outline has machinery (six set pieces, three ledgers, two-stage hidden-proof subplot) beyond Amity Falls. The ledgers are not built in `story_bible.py`.
