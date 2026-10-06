# KINDLING LINE PROOFED LOG

Protocol: `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md` (read it first). Append only. One stamp line per chapter, written right after that chapter is finished. A stamp is void if the chapter's blob SHA has changed since.

## LOCKS (add a line while working, remove it when done)
(none)

## COVERAGE (update after every stamp)
- Book 1: chapters stamped 2 of 45 (ch11, ch26). All 45 had a mechanical scan on 2026-10-07 (see SCAN NOTES); the other 43 are NOT yet read in full, so they are not stamped. Next unstamped in order: ch01.
- Book 2: chapters stamped 0 of 45. Next unstamped: ch01. Start only after Book 1 is fully stamped or FLAGGED.
- Book 3: chapters stamped 0 of 45. Next unstamped: ch01. Start only after Book 2 is fully stamped or FLAGGED.

## FLAGS WAITING FOR ZIA
Carried from READER_FIX_LIST.md group A, not yet decided:
1. Book 1: the ward's death told several ways (digest ch.24 to 30, 32, 38) and three different verdicts at the end (ch.41 to 43).
2. Book 1: Sol's mother (name, ward, Valerius Ashworth's part in her Reckoning) and Kael's status vary across chapters.
3. Book 2 ch.44 to 45: Auda Ashworth, Kael's grandmother, appears with no earlier mention.
4. Book 1 ch.44 has Kael's father stripped and exiled; Book 2 has him buried nine months before ch.33.
New from the 2026-10-07 scan (Book 1, not fixed, low priority, Zia may ignore):
5. Book 1 ch.09 ends "The Reckoning in sixty-seven" days on 13 Emberfall; ch.11 says forty-three days on 16 Emberfall (Emberfall 16 to Frostveil 29). The two cannot both be right. Counts like this are READER_FIX_LIST group C, so left alone unless Zia wants it fixed.
6. Book 1 chapter endings: about ten chapters close on the same formula, "The open question was..." or "The question settled in his/her ribs..." (ch.04, 07, 10, 13, 20, 23, 32, 40 and similar). Not rewritten. If Zia wants it varied, vary only the last line of each.

## SCAN NOTES (mechanical, whole book, 2026-10-07)
Book 1, all 45 chapters fetched live and scanned for: em and en dashes (0 found), banned and AI words, doubled punctuation (0), glued `---` (0), leaked planning text such as "Ch.N" (0), duplicated paragraphs inside a chapter and across chapters, one chapter header each, clean endings, stray markup.
- Found and fixed: ch.26 was the whole chapter pasted twice (about 3,600 words, 48 duplicated paragraphs, header glued to the last line of the first copy). Kept one copy (1,797 words). Commit 09e03c582e82b59aab68eacd8ca19c9aeb88752b.
- Found and fixed: ch.11 had a stray last line repeating the dialogue as a summary. Removed. Commit 5c7953aa8cd81ff6a0a0beacfa52297367425c10.
- Not a defect, left alone: "Frostveil" is a real month in Book 1 and Book 2 headers and text (banned only in Book 3). "harness" in ch.01, 04, 09, 29, 40, 45 is the flying harness. "tapestry" in ch.01 is a literal wall hanging. `***` and `---` in ch.04, 11, 19, 21, 22, 25, 28, 30, 35 are scene breaks. `[REDACTED]` in ch.06 is a ledger entry.
- Watch while reading: "particular" appears once each in ch.11, 16, 22, 28, 32, 41 (banned word); "the kind of" in ch.08, 09, 28, 29, 36; hedge words (something, someone, somewhere) 14 to 24 times in ch.11, 26, 29, 30, 36, 39. Read in context before changing.
- Chapter lengths run 1,150 (ch.45) to 4,683 (ch.29). Length is not a defect.

## LOCKED FACTS (fill in while reading Book 1, then 2, then 3; cite chapter for every fact)
- B1 ch.11: Reckoning is 43 days from 16 Emberfall (Year 3) to 29 Frostveil; Sol's mother's Reckoning was twelve years ago; the ledger fragment covers Accord years five to fourteen; master ledger is in the Corrin strongroom, unseen by any auditor for sixty years.
- B1 ch.26 (8 Frostveil, Year 3): a ward dies at the Ember Festival on the Obsidian Terrace; Kael's first kiss with Sol happens in the colonnade afterwards; the inquest follows.

## STAMPS
B1-ch11 | STAMPED-FIXED | 2026-10-07 | Claude (chat session) | blob 95fb8618ca85099e3491eb52b65edc4c39d8b849 | fixes: 5c7953aa8cd81ff6a0a0beacfa52297367425c10 | checks: P1-P10 | notes: read in full; removed stray repeated last line; "particular" x1 left (context fine); ch.11 says 43 days, see flag 5
B1-ch26 | STAMPED-FIXED | 2026-10-07 | Claude (chat session) | blob eb582eb56085abb8e6e8a9424bf86fa89d367375 | fixes: 09e03c582e82b59aab68eacd8ca19c9aeb88752b | checks: P1-P10 | notes: read in full after de-duplication; whole chapter had been pasted twice; hedge words x24 not changed
