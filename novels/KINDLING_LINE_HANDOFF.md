# **KINDLING LINE — MASTER HANDOFF (2026-10-13, end of session)**

**READ THIS FIRST. THEN READ `novels/KINDLING_LINE_PROOFED_LOG.md` (the real source of truth). THEN `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md`. DO NOT TRUST ANY SUMMARY, INCLUDING THIS ONE, WITHOUT RE-CHECKING LIVE FILES FIRST.**

**Run `get_me` before anything else. It must say `aliwaziri10`.**

**Re-fetch the log, the chapters folder (`fields: name, sha, size`), and the commit list before every single write. Multiple sessions edit this repo concurrently — a blob that was void an hour ago may already be fixed, and a chapter that looks clean may have been silently broken since.**

---

## **OVERALL PROJECT STATUS: ~90% COMPLETE**

**There are THREE books in the Kindling Line series, all in `aliwaziri10/Voxel`:**

| Book | Path | Chapters Stamped | Status |
|---|---|---|---|
| **Book 1** | `novels/kindling-line-book-1/` | **45 / 45** | **PROOFREAD COMPLETE.** Several book-wide continuity flags left open on purpose (see below) — these are Zia's calls, not defects to silently fix. |
| **Book 2** | `novels/kindling-line-book-2/` | **45 / 45** | **PROOFREAD COMPLETE.** A final "humanizer" style pass has **NOT** started — waiting on Zia's go-ahead. |
| **Book 3** | `novels/kindling-line-book-3/` | **45 / 45** | **PROOFREAD COMPLETE as of THIS session (2026-10-13).** The VOID list (ch01, 02, 03, 05, 06, 34, 35) was fully cleared and re-stamped this session. See full detail below. |

**The missing ~10%:**
1. **Book 2's humanizer pass** — not started, needs Zia's word before beginning.
2. **A handful of named, deliberately-open continuity flags in Book 1** (Valerius told many ways, the ward's death told several ways, years-left numbers, cost-per-flare inconsistencies, first-transfer-event told differently, several name echoes) — **these are flagged for Zia's decision, not bugs to fix unilaterally.**
3. **Small named items in Book 3** (see "OPEN BEHIND THE STAMPS" below) — mostly "should we pad X chapter" or "which date is right" questions for Zia.
4. **CANON_LOCK.md still lists the smith as "Corwin"** when Books 2 and 3 both use **"Edmar"** — a reference-doc fix, not a chapter fix, still outstanding.
5. **One one-word fix in Book 2 ch41** ("another man's handwriting" → "another hand's") flagged as the editor's job after ch27 — still not done.

**Nothing is currently FLAGGED-and-broken. Everything stamped is either CLEAN or FIXED and verified against live text.**

---

## **BOOK 3 — WHAT HAPPENED THIS SESSION (2026-10-13)**

**A pasted report from another session claimed the VOID chapters needed specific fixes, including a theory that "the plate should hum before the close and go quiet after." This was checked against live text and was WRONG — it contradicted the book's own locked canon.**

**THE CORRECT, CONFIRMED CANON: the plate NEVER hums. Anywhere. In any chapter. Full stop.** (Confirmed directly: ch33 says "It did not hum"; ch45's last line is "The iron was only iron.") "The rope hums/hummed" describing physical tension through a hemp line is a **different, allowed image** and is NOT this leak — do not confuse the two.

**What was actually found and fixed, verified against live text chapter by chapter:**

- **ch01, ch02, ch03, ch33** — **re-checked, found CLEAN, NO CHANGE NEEDED.** The specific AI-tell phrases a pasted report claimed were there either weren't present in the live text or were already fine in context. **Do not re-open these without a new, specific, cited finding.**
- **ch34** — the hum leak had been **reintroduced** since an earlier fix (four instances: "plate hummed," "hum rose through his legs," etc.). **Removed again.** Dialogue line now reads: *"The cords stay coiled. The plate is awake. Nobody pulls."*
- **ch35** — two more "the plate hummed" instances found and removed (now "the plate woke" / "the plate was awake").
- **ch05** — two genuine AI-tell phrases fixed: **"the cellar held its breath"** and **"the word hung between them"** — both varied to break the stock-transition pattern.
- **ch06** — one genuine hum instance fixed: **"The metal hummed"** → **"The metal held its rhythm against her palm."**

**All of this is logged with exact blob SHAs and commit hashes in `KINDLING_LINE_PROOFED_LOG.md`'s B3 STAMPS section — that log entry is the authoritative record, not this summary.**

**NEW STANDING RULE (added to the log this session, Rule 7): a relayed or pasted report from another session is a LEAD TO VERIFY, not a fact to act on. Always re-fetch the live chapter and confirm the exact claim before editing anything.** This session's near-miss (almost "fixing" the hum canon backwards based on a wrong pasted note) is the example written into the rule.

---

## **WHAT TO DO NEXT, IN ORDER**

1. **If picking up Book 3:** nothing is void. Move to the "OPEN BEHIND THE STAMPS" items below, or wait for Zia.
2. **If picking up Book 2:** ask Zia whether to start the humanizer pass. Do not start it unprompted.
3. **If picking up Book 1:** the open continuity flags are listed in the log under "Book 1 flags left on purpose" — **these are intentionally NOT fixed.** Do not touch them without Zia's explicit instruction.
4. **Either way:** fix the CANON_LOCK.md smith-name mismatch (Corwin → Edmar) and the Book 2 ch41 one-word fix whenever convenient — both are small, uncontroversial, standing to-dos.

---

## **OPEN BEHIND THE STAMPS (Book 3) — DO NOT FIX WITHOUT ZIA**

- **ch04:** Yelva says "four days ago" for Mara's injury, but the wrists are already cold on Day 2 ("Wrists on the fourth"), while canon puts the injury on 4 Cinderveil and Day 0 on 30 Cinderveil. **Zia to say which count is right.**
- **ch31:** opening romance scene is ~300 words; CANON_LOCK asks for a quarter of the chapter. **Left as is, no padding done. Zia to say whether to expand.**
- **ch02, ch03, ch07, ch09, ch10:** still below their pre-cleanup sizes after pasted duplicates were removed. **Zia to say whether to add more scene content.**
- **Flags 16 and 17** (Sol's mother's status across books; the name "Mara" clashing across characters) — **still open, Zia's call.**

---

## **ZIA'S STANDING RULES (apply to all three books, every session)**

- **Fix facts and AI tells only.** No cosmetic tweaks, no unrequested style passes.
- **NEVER reduce a chapter's file size. NEVER pad without being asked.**
- **No em dashes, anywhere, in any book.**
- **Banned in Book 3 prose specifically:** some, something, someone, somewhere, somebody, somehow, kind of, particular, the specific, Frostveil.
- **American spelling; "grey" stays "grey" everywhere (deliberate exception).**
- **One chapter at a time. Stamp it immediately, one line in the log, as soon as it's done — do not batch unlogged work.**
- **Work only inside the three Kindling Line books unless told otherwise. Do not ask permission to continue — just continue.**
- **Zia is non-technical and works by voice dictation.** Anything he needs to copy/paste goes in its own code block. GitHub edit links go first in any message that references a file.

---

**END OF HANDOFF. THIS FILE AND THE LOG ARE THE ONLY THINGS TO TRUST — NOT A PASTED SUMMARY, NOT MEMORY, NOT A PRIOR SESSION'S CLAIM. VERIFY AGAINST LIVE TEXT, EVERY TIME.**
