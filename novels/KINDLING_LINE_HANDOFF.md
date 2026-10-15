# **KINDLING LINE — MASTER HANDOFF (2026-10-13, end of session)**

**ZIA'S LOCK ORDER (2026-10-13, overrides everything below): Book 1 is published. Book 2 and Book 3 are stamped and locked. DO NOT EDIT ANY CHAPTER of any book unless Zia gives a new explicit order in the current conversation. The 2,300-word floor work and every "ask Zia whether to pad or fix" item below is ON HOLD. Several sessions edited chapters after the lock was due (B3 ch02, 03, 04, 44, 45 edited and re-stamped 2026-10-13); B3 ch01 and ch37 and B1 ch22 live blobs did not match their stamps when checked. Verify, report to Zia, do not fix.**

**READ THIS FIRST. THEN READ `novels/KINDLING_LINE_PROOFED_LOG.md` (the real source of truth). THEN `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md`. DO NOT TRUST ANY SUMMARY, INCLUDING THIS ONE, WITHOUT RE-CHECKING LIVE FILES FIRST.**

**Run `get_me` before anything else. It must say `aliwaziri10`.**

**Re-fetch the log, the chapters folder (`fields: name, sha, size`), and the commit list before every single write. Multiple sessions edit this repo concurrently — a blob that was void an hour ago may already be fixed, and a chapter that looks clean may have been silently broken since.**

---

## **OVERALL PROJECT STATUS: ~90% COMPLETE**

**There are THREE books in the Kindling Line series, all in `aliwaziri10/Voxel`:**

| Book | Path | Chapters Stamped | Status |
|---|---|---|---|
| **Book 1** | `novels/kindling-line-book-1/` | **45 / 45** | **PUBLISHED.** Several book-wide continuity flags left open on purpose (see below) — Zia's calls, not defects to silently fix. |
| **Book 2** | `novels/kindling-line-book-2/` | **45 / 45** | **PROOFREAD COMPLETE, LOCKED.** A final "humanizer" style pass has **NOT** started — waiting on Zia's go-ahead. |
| **Book 3** | `novels/kindling-line-book-3/` | **45 / 45** | **PROOFREAD COMPLETE, LOCKED.** The VOID list (ch01, 02, 03, 05, 06, 34, 35) was cleared and re-stamped 2026-10-13. See the log. |

**The missing ~10%:**
1. **Book 2's humanizer pass** — not started, needs Zia's word before beginning.
2. **A handful of named, deliberately-open continuity flags in Book 1** (Valerius told many ways, the ward's death told several ways, years-left numbers, cost-per-flare inconsistencies, first-transfer-event told differently, several name echoes) — **flagged for Zia's decision, not bugs to fix unilaterally.**
3. **Small named items in Book 3** (see "OPEN BEHIND THE STAMPS" below) — questions for Zia.
4. **CANON_LOCK.md still lists the smith as "Corwin"** when Books 2 and 3 both use **"Edmar"** — a reference-doc fix, not a chapter fix.
5. **One one-word fix in Book 2 ch41** ("another man's handwriting" → "another hand's") flagged as the editor's job after ch27 — not done, and now on hold with the lock.

---

## **BOOK 3 — WHAT HAPPENED THIS SESSION (2026-10-13)**

**A pasted report from another session claimed the VOID chapters needed specific fixes, including a theory that "the plate should hum before the close and go quiet after." This was checked against live text and was WRONG — it contradicted the book's own locked canon.**

**THE CORRECT, CONFIRMED CANON: the plate NEVER hums. Anywhere. In any chapter.** (ch33 says "It did not hum"; ch45's last line is "The iron was only iron.") "The rope hums/hummed" describing tension through a hemp line is a **different, allowed image**.

- **ch01, ch03, ch33** — re-checked, found CLEAN (then ch02 and ch03 were edited for the word floor by sessions that day; see the log).
- **ch34, ch35** — plate-hum leaks removed. **ch05, ch06** — stock-tell phrases and one hum instance fixed.
- All of it is logged with blob SHAs and commit hashes in the B3 STAMPS section of the log, which is the authoritative record.

**STANDING RULE 7 (in the log): a relayed or pasted report from another session is a LEAD TO VERIFY, not a fact to act on. Re-fetch the live chapter and confirm the exact claim before editing anything.**

---

## **WHAT TO DO NEXT**

1. Nothing in the chapters. The books are locked.
2. If Zia asks: Book 2 humanizer pass; Book 1 and Book 3 open flags; CANON_LOCK smith name.
3. If asked to check stamps: recompute each chapter's git blob SHA from the live file and compare to the stamp rows (B1 and B2 in `novels/KINDLING_LINE_STAMPS_B1_B2.md`, B3 in the log). Report mismatches to Zia; do not fix them.

---

## **OPEN BEHIND THE STAMPS (Book 3) — ON HOLD, DO NOT FIX WITHOUT ZIA**

- **ch04:** Yelva says "four days ago" for Mara's injury, but the wrists are already cold on Day 2, while canon puts the injury on 4 Cinderveil and Day 0 on 30 Cinderveil. Zia to say which count is right.
- **ch31:** opening romance scene is about 300 words; CANON_LOCK asks for a quarter of the chapter. Left as is.
- **ch07, ch09, ch10, ch41:** below their pre-cleanup sizes after pasted duplicates were removed.
- **Flags 16 and 17** (Sol's mother's status across books; the name "Mara" clashing across characters) — Zia's call.

---

## **ZIA'S STANDING RULES (apply to all three books, every session)**

- **Fix facts and AI tells only.** No cosmetic tweaks, no unrequested style passes. (Suspended while the books are locked.)
- **NEVER reduce a chapter's file size. NEVER pad without being asked.**
- **No em dashes, anywhere, in any book.**
- **Banned in Book 3 prose specifically:** some, something, someone, somewhere, somebody, somehow, kind of, particular, the specific, Frostveil.
- **American spelling; "grey" stays "grey" everywhere (deliberate exception).**
- **One chapter at a time. Stamp it immediately, one line in the log.**
- **Work only inside the three Kindling Line books unless told otherwise.**
- **Zia is non-technical and works by voice dictation.** Anything he needs to copy/paste goes in its own code block.

---

**END OF HANDOFF. THIS FILE AND THE LOG ARE THE ONLY THINGS TO TRUST — NOT A PASTED SUMMARY, NOT MEMORY, NOT A PRIOR SESSION'S CLAIM. VERIFY AGAINST LIVE TEXT, EVERY TIME.**
