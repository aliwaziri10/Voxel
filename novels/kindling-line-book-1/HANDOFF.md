# Book 1 — HANDOFF (Kindling Line, "What the Gift Demands")

**Read this first**, then `architecture.md` in full, then `VOICE_GUIDE.md`.
Read `../EDITORIAL_CHARTER.md` before either. Standing rule: re-verify everything below against live GitHub before trusting it.

## 2026-10-02 STATUS: continuity passes 1 and 2 APPLIED to Book 1 and Book 2 (commits `b2c3ff2`, `1ea8800`). This supersedes every "open decision / still wrong / unfixed" note from 2026-09-28 that used to sit here.
Scripts (re-runnable, idempotent): `scripts/fix_book1.py` (pass 1, then chains `scripts/fix_pass2.py`). Workflow: Actions, "Fix Book 1", browser "Run workflow" button.
**Canon decided (Claude's call, delegated by Zia, 2026-10-01/02) — do not reopen without Zia:**
- **Valerius Ashworth is ALIVE through all of Book 1** (stripped of his seat in ch.44, 5 Sunspire, Year 3). Ch.3 plants a failing heart. He dies off-page in the year between the books. Book 2 is set one year later (Year 4, opens 9 Sunspire) where he is "eight months in the ground". No uncle Corven.
- **Sol's mother:** Reckoning flight 12 years before Book 1; burned forty years in that single flight; Sol was twelve; she died three winters later. Sol's father (Lord Vane) is alive but ruined. Sol's aunt (new, minor, named Aunt Rue) replaces the invented grandmother in ch.22 and the "Aunt Mara" in ch.29; Mara is the mother's name.
- **Reckoning is 29 Frostveil, Year 3.** Every in-text countdown was matched to its `chapter_date` header (30-day months: Emberfall, Frostveil, Sunspire). A live scan found no mismatch beyond the ch.22 "fourteen days" arrears notice, which is a separate deadline.
- No em-dashes; no "chapter N" mentions in narration.
**Book 2 was touched only by pass 2:** all 45 headers Year 3 to Year 4, and four mother lines (ch.1, 4, 9, 31). Nothing else in Book 2 changed.

**STILL OPEN (honest list, needs a human read):**
1. **Mother mechanism mismatch.** Book 1: she flew her Reckoning and burned alone, no ward. Book 2: she was a contract-bound ward-taker who "went under a plate" and was held to a binding contract (ch.4, 17, 22, 31, 41). Years and age now agree; the mechanism does not. Needs one deliberate rewrite choice by Zia.
2. **ch.22** was patched, not rewritten. It still reads as the most off-canon chapter; read it through.
3. **ch.35** "Four since the Kindling woke" and ch.39 "two point three years" were left as scale statements; read for sense.
4. **Book 2 `full_manuscript.md`** is stale (noted in Book 2 handoff).
5. Ch.3 Kael gives Sol his father's chain; the surrounding logic was patched (chain "cannot leave his name"). Read once.

## STATUS 2026-09-27: all 45 chapters CONFIRMED DRAFTED
Verified live: `chapters/chapter_01.md` through `chapter_45.md` all exist with full prose (Ashworth/Corrin/Vane, Kindling cost-transfer mechanic, leads Kael Ashworth and Sol/Isolde Vane, Reckoning Accord). Don't trust "no chapters yet" language in old handoff sections without a live listing check.

## 2026-09-27 continuity pass (done)
Missing `chapter_date` headers fixed in ch.10, 12, 20, 21 (14, 17, 29 Emberfall; 1 Frostveil). The earlier "Thorne house seal / Ward Deed / Anchor Seven" audit does not match any file in this book; do not run it here.

## STATUS 2026-09-25: beat map re-run PASSED review
Beat map (workflow run `be1dd31`, key `book_beat_maps.kindling-line` in `story_bibles/kindling-line.json`) passed all 8 checks: Kael pockets the proof; Ashworth offer before ch.20; ward dies from Kael's delay before ch.27; real rupture ch.33-35; no voluntary ward for Kael; one Reckoning across ch.40-43; countdown lands on ch.40; dates have real gaps.

## Next step
Zia reads the five open items above. Then (optional) re-run `python voxel_cli.py proofread --book "Kindling Line Book 1"` via the browser workflow.

## Process notes carried over
- `proofreader.py` is wired into `voxel_cli.py` (`date_consistency_check` inside `novel`; `grammar_scan` as `proofread`).
- `brief.txt` has 10 LOCKED RULES; `voxel-novel.yml` reads it via `brief_file`.
- Assistant writes to `.github/workflows/` return 403: Zia pastes workflow edits himself via the `blob` page then the pencil. Other repo files can be pushed directly.
- Deferred to Zia: cover design direction; `ai_disclosure_included` / `kdp_metadata_approved` gates.
- Scope note: the outline has machinery (six set pieces, three ledgers, two-stage hidden-proof subplot) beyond Amity Falls. The ledgers are not built in `story_bible.py`.
