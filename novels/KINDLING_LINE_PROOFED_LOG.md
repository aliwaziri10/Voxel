# KINDLING LINE PROOFED LOG

Protocol: `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md` (read it first). Append only. One stamp line per chapter, written right after that chapter is finished. A stamp is void if the chapter's blob SHA has changed since.

## LOCKS (add a line while working, remove it when done)
(none)

## COVERAGE (update after every stamp)
- Book 1: chapters stamped 3 of 45 (ch01, ch11, ch26). All 45 had a mechanical scan on 2026-10-07 (see SCAN NOTES); the other 42 are NOT yet read in full, so they are not stamped. Next unstamped in order: ch02.
- Book 2: chapters stamped 0 of 45. Next unstamped: ch01. Start only after Book 1 is fully stamped or FLAGGED.
- Book 3: chapters stamped 0 of 45. Next unstamped: ch01. Start only after Book 2 is fully stamped or FLAGGED.

## FLAGS WAITING FOR ZIA
Carried from READER_FIX_LIST.md group A, not yet decided:
1. Book 1: the ward's death told several ways (digest ch.24 to 30, 32, 38) and three different verdicts at the end (ch.41 to 43).
2. Book 1: Sol's mother (name, ward, Valerius Ashworth's part in her Reckoning) and Kael's status vary across chapters.
3. Book 2 ch.44 to 45: Auda Ashworth, Kael's grandmother, appears with no earlier mention.
4. Book 1 ch.44 has Kael's father stripped and exiled; Book 2 has him buried nine months before ch.33. (B1 ch01 has him alive, aged seventy, recused from the audit on health grounds.)
New from the 2026-10-07 scan (Book 1, not fixed, low priority, Zia may ignore):
5. Book 1 ch.09 ends "The Reckoning in sixty-seven" days on 13 Emberfall; ch.11 says forty-three days on 16 Emberfall (Emberfall 16 to Frostveil 29). The two cannot both be right. Counts like this are READER_FIX_LIST group C, so left alone unless Zia wants it fixed. Update 2026-10-07: B1 ch01 (58 days from 1 Emberfall) agrees with ch11, so ch09 is the odd one out; from 13 Emberfall the count would be 46.
6. Book 1 chapter endings: about ten chapters close on the same formula, "The open question was..." or "The question settled in his/her ribs..." (ch.04, 07, 10, 13, 20, 23, 32, 40 and similar). Not rewritten. If Zia wants it varied, vary only the last line of each.
New from the ch01 read (2026-10-07), Zia decides:
7. Book 1 dating label. Every chapter header and in-text date says "Year 3 of the Reckoning Accord", but ch01 says House Ashworth has held the auditor's seat "for four generations, since the Accord was signed", and ch11 says the ledger fragment covers "Accord years five to fourteen" with the master ledger unseen for sixty years. Read literally, "Year 3 of the Accord" cannot sit with those lines. Option A: leave all as is (readers will most likely take Year 3 as the cycle year; ch04 shows Sol's mother's notes "Year 1, Year 2, Year 3, the Reckoning took" which fits a three-year cycle). Option B: change "since the Accord was signed" in ch01 and the "Accord years" wording in ch11. Recommendation: A, change nothing.

## SCAN NOTES (mechanical, whole book, 2026-10-07)
Book 1, all 45 chapters fetched live and scanned for: em and en dashes (0 found), banned and AI words, doubled punctuation (0), glued `---` (0), leaked planning text such as "Ch.N" (0), duplicated paragraphs inside a chapter and across chapters, one chapter header each, clean endings, stray markup.
- Found and fixed: ch.26 was the whole chapter pasted twice (about 3,600 words, 48 duplicated paragraphs, header glued to the last line of the first copy). Kept one copy (1,797 words). Commit 09e03c582e82b59aab68eacd8ca19c9aeb88752b.
- Found and fixed: ch.11 had a stray last line repeating the dialogue as a summary. Removed. Commit 5c7953aa8cd81ff6a0a0beacfa52297367425c10.
- Not a defect, left alone: "Frostveil" is a real month in Book 1 and Book 2 headers and text (banned only in Book 3). "harness" in ch.01, 04, 09, 29, 40, 45 is the flying harness. "tapestry" in ch.01 is a literal wall hanging. `***` and `---` in ch.04, 11, 19, 21, 22, 25, 28, 30, 35 are scene breaks. `[REDACTED]` in ch.06 is a ledger entry.
- Watch while reading: "particular" appears once each in ch.11, 16, 22, 28, 32, 41 (banned word); "the kind of" in ch.08, 09, 28, 29, 36; hedge words (something, someone, somewhere) 14 to 24 times in ch.11, 26, 29, 30, 36, 39. Read in context before changing.
- Chapter lengths run 1,150 (ch.45) to 4,683 (ch.29). Length is not a defect.
- Cross-book grep 2026-10-07: "Mississippi" appeared only in B1 ch01 (now fixed); no other real-world counting words found in Books 1 to 3.

## LOCKED FACTS (fill in while reading Book 1, then 2, then 3; cite chapter for every fact)
- B1 ch01 (1 Emberfall, Year 3): Reckoning announced by criers, the Thirty-Seventh Reckoning, audit begins 29 Frostveil = 58 days. House Vane liquid reserves 47,000 crowns vs debts 52,000 (gap 5,000). A ward costs 30,000 plus a 15,000 Corrin brokerage fee = 45,000 (B1 ch04 also gives 45,000 as the Third Tier ward rate). Isolde Vane is 24, dark hair, storm-cloud eyes; her mother burned forty years in forty minutes at her Reckoning and lived three more winters; Vane has been out of good standing twelve years. Isolde's threshold drill costs about three weeks per second held (ten seconds = about thirty weeks). Unbuffered audit minimum eighteen years; average lifespan in the Reach seventy-three. Kael Ashworth is the presiding auditor: dark short hair, grey-green eyes, charcoal coat with silver thread; he saw Isolde's mother fly when he was a boy; his father is seventy and recused on health grounds; Ashworth has held the auditor seat four generations. Corrin has filed a lien on the Vane house (executes if Vane is found insolvent).
- B1 ch11: Reckoning is 43 days from 16 Emberfall (Year 3) to 29 Frostveil; Sol's mother's Reckoning was twelve years ago; the ledger fragment covers Accord years five to fourteen; master ledger is in the Corrin strongroom, unseen by any auditor for sixty years.
- B1 ch26 (8 Frostveil, Year 3): a ward dies at the Ember Festival on the Obsidian Terrace; Kael's first kiss with Sol happens in the colonnade afterwards; the inquest follows.

## STAMPS
B1-ch11 | STAMPED-FIXED | 2026-10-07 | Claude (chat session) | blob 95fb8618ca85099e3491eb52b65edc4c39d8b849 | fixes: 5c7953aa8cd81ff6a0a0beacfa52297367425c10 | checks: P1-P10 | notes: read in full; removed stray repeated last line; "particular" x1 left (context fine); ch.11 says 43 days, see flag 5
B1-ch26 | STAMPED-FIXED | 2026-10-07 | Claude (chat session) | blob eb582eb56085abb8e6e8a9424bf86fa89d367375 | fixes: 09e03c582e82b59aab68eacd8ca19c9aeb88752b | checks: P1-P10 | notes: read in full after de-duplication; whole chapter had been pasted twice; hedge words x24 not changed
B1-ch01 | STAMPED-FIXED | 2026-10-07 | Claude (chat session) | blob f055e76eca9e704e120bd8b8c69c4b36e06f63e7 | fixes: b7622acfe54ca99db902444dedf963c6ac042752 | checks: P1-P10 | notes: read in full; three fixes: "One Mississippi" count replaced with "One stone" (real-world word in a secondary world, only occurrence in Books 1 to 3); brokerage "fifteen percent" changed to "fifteen thousand" so 30,000 + fee = the stated 45,000; lamp "returned to its peg" changed to taken from its ledge (it was set on a ledge). Pushed text diffed against intended text, identical. Left alone: tricolon closers and short-sentence rhythm (voice), hedge "something shifted" x1 (next line gives the image), "seven and a half months" vs thirty weeks (roughly). See flags 4, 5, 7.
