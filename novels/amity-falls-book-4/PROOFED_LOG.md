# Book 4 proofed log

Only what was read from live `main` is stamped. Never stamp from memory or a
handoff claim. Condensed 2026-09-22 — detail trimmed, no findings dropped.

Legend: FIXED = edit read back live. READ = manual read, no change needed.
NOT PROOFED = mechanical pass only, no manual read yet.

**LAST CHAPTER STAMPED: ch.26.** Ch.1-26 read/fixed. Ch.27-45 not yet read
this pass. Ch.14, ch.17, ch.21 have DECIDED but NOT YET APPLIED fixes (see
"Decisions applied this session" below) — do this before ch.27+ if the read
reaches them, so nothing downstream gets built on the old versions.

## Decisions applied this session (2026-09-22, made without further
## checking with Zia — he delegated this call)
1. **Josiah vs Ambrose: Josiah tried and failed to end the bargain and hid
   the terms.** His signed 1847/1863 letters are the primary-source
   evidence; Ambrose is the later Warden who taught Adelaide (1872-1901).
   LOCKED. Ch.2,3,6,7,9,12,13,15 already match this. **Ch.14's central
   reveal still calls the letter-writer "Ambrose Whitlock" and needs the
   same fix — NOT YET DONE.**
2. **Chapter order: not renumbering files.** "The fifteenth" is the one
   publication deadline. Ch.26's "summer solstice" line was the odd one
   out — FIXED to "the fifteenth" (`4175ca7`). The ch.18-23 countdown-
   number mismatches are NOT resolved by this — that's a separate,
   unresolved ordering problem, still open.
3. **Drake's arrest: ch.41's early-morning home arrest is canon.** Ch.21's
   motel pickup and ch.25's "voluntary surrender/custody" both needed to
   stop being actual arrests. **Ch.25 is FIXED** (`f9e01f5`): Drake's
   lawyer makes contact, nothing is filed, no custody, "custody hearing"
   line in ch.26 also fixed to match (`4175ca7`). **Ch.21's motel-pickup
   arrest scene is NOT YET FIXED** — still needs downgrading to a failed/
   averted attempt when the read reaches it, so it doesn't contradict ch.41.
4. **First kiss: ch.21's version stays, ch.17's needs to be cut or
   rewritten into a different beat** (a near-miss, an aborted moment, or
   removed entirely) so ch.26's "not like the first one, hurried and
   interrupted in the records room" has only one referent. **NOT YET
   APPLIED** — ch.17 still has its own complete kiss scene live.
5. **Drake's em-dash note: kept, as the one deliberate exception to house
   style**, since the plot point depends on it. FIXED in ch.25 (`f9e01f5`,
   both instances now use a real —).
6. **Ch.26 pacing (kiss + first night, same chapter): left where it is.**
   Consistent now that Decision 4 points to ch.21 as the real first kiss;
   no change needed here once ch.17 is fixed.

Related, lower-stakes, not decided: **Ambrose Kell** vs **Ambrose Whitlock**
naming collision (ch.19) — a different person sharing a first name with the
now-settled Ambrose Whitlock. Consider renaming Kell if it reads confusing
once the whole book is checked.

## Fixed and locked (do not re-touch without new evidence)
- Folio gap: 1887-1891. (ch.3, `207db70`)
- Josiah/Ambrose signatures: fixed ch.2, 6, 7, 9, 12, 13, 14(partial - see
  Decision 1, the *reveal* line in ch.14 is still wrong), 15.
- Anachronisms (trial/leverage as past when it's ch.36-45 material): fixed
  ch.8, ch.12. Ch.24-26 clean.
- ch.11: Odette Reynolds → Reyes. ch.22: Harriet is Theo's grandmother.
  ch.23 & ch.25: Harriet's age fixed to seventy-five (locked: born 1949,
  present 2024) — two independent slips, same fix; worth a full-book grep
  once the read finishes.
- ch.12: truncated sentence, ledger-finder attribution, 2 anachronisms.
- ch.15: full rewrite verified.
- ch.18: internal day-count contradiction fixed.
- ch.24: READ, clean, confirms the ch.45 large-debt fix made earlier.
- ch.25: Harriet's age, Drake's custody status, em dash — all FIXED
  (`f9e01f5`). Confirmed applying Decisions 3 and 5.
- ch.26: READ. "Summer solstice" and "custody hearing" lines FIXED
  (`4175ca7`) applying Decisions 2 and 3. Otherwise no text changed.

## Open questions (unchanged from prior stamp except where noted)
- Q1 Elena Castellano: still open; ch.24 adds a THIRD age for when the
  grandmother died (sixteen, vs ch.15's fixed "fourteen").
- Q2 Warden of the first debt: unresolved.
- Q3 Drake's 2005 Millbrook target: unresolved.
- Q4 Adelaide: unresolved.
- Q5 Ch.5 unreliable: unresolved.
- Q6 Lineage roster: unresolved.
- Q7 Calendar: still cycling through all four seasons across chapters with
  no fixed calendar; needs the full ch.1-45 read to resolve.
- Q8 Wren's mother's job: unresolved.
- Q9 Harriet's home terminology: unresolved.
- Q10 Kiss/rupture beat map: PARTIALLY RESOLVED by Decision 4 above — kiss
  keeps ch.21, drops ch.17. Rupture placement still unresolved.
- Q11 Archive building: still 5-6 competing descriptions, unresolved.
- Q12 Two "Silas" characters: unresolved.
- Q13 Spaced hyphens as em-dash substitutes: still an open house-style
  question generally; the one case where it broke a plot point (ch.25) is
  now fixed via Decision 5.
- Q14 Line-edit style: not urgent.
- Q15 Denise's "grandson's husband" line: unresolved.
- Q16 Ambrose Kell vs Ambrose Whitlock: unresolved, see above.
- Q17 "The house on the ridge": unresolved.
- Q18 M. Harrow / Harlan & Associates thread: self-contained so far.
- Q19 Search-cost mechanic: confirmed consistent, no action needed.
- Q20 Shell company names ("Holloway & Finch" ch.24 vs "Meridian
  Consulting" ch.25): presented as two different shells, not necessarily a
  conflict; re-check once ch.26+ is read for a possible third name.

## Not done
- Apply Decision 1 to ch.14 (Josiah, not Ambrose, in the letter reveal).
- Apply Decision 4 to ch.17 (cut/rewrite the duplicate first kiss).
- Sequential read of ch.27-45 (17 chapters remaining).
- Full season/countdown/Archive-naming reconciliation pass.
- Cross-check against Books 1-3 (Q1, Q15).
