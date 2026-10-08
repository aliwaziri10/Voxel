# KINDLING LINE BOOK 1 PROOFREAD: SESSION HANDOFF (2026-10-08)

Read this first, then the log. If this file and the log disagree, the log wins. Do not use chat memory for status; the GitHub log is the source of truth.

## Read order
1. `novels/EDITORIAL_CHARTER.md`
2. `novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md` (the ten parameters P1 to P10, steps, stamp format)
3. `novels/KINDLING_LINE_PROOFED_LOG.md` (COVERAGE, DECISIONS D1 to D20, OPEN FLAGS, LOCKED FACTS, STAMPS)
4. This file

## Status at end of this session
- Book 1: ch01 to ch39 stamped (39 of 45). Last fix commit: `90345efca38c8b93c85513a8aac3b63017e55fb5` (ch35 to ch39). Log commit: `e2f39442d938476bdab9dbd52b180044c36a7a4f`.
- Next: ch40, ch41, ch42, ch43, ch44, ch45 (6 chapters). Then Book 1 is done, unless Zia wants the open flags decided.
- Book 2 and Book 3: not started. Start Book 2 only after Book 1 is stamped or flagged.
- Before working, list `novels/kindling-line-book-1/chapters` with `fields: name, sha, size` and compare each blob to the STAMPS lines. A stamp is void if the blob changed.

## How Zia wants the work done
- Read chapters in blocks of five. Edit each, push the block with `push_files` as one commit, then stamp.
- Fix only what a normal reader would feel (continuity, broken sentences, wrong names or numbers, stock phrases, hedges). Ignore counts, ages, days and bell hours unless they break the scene. Do not over-proofread.
- During repetitive work give brief updates only: chapter number, what was fixed, stamp confirmation. No repeated explanation of the process.
- No em dashes and no "AI tell" patterns in anything you write. Text meant to be copied goes in an inline code block in chat.
- Full liberty on Book 1: decide, apply, log. Do not stop to ask approval.

## Method used (chat session, no sandbox, network off)
- Read each chapter live with `get_file_contents` (ref `refs/heads/main`).
- Send the full corrected text with `push_files`. Compute each edit's byte change by hand and compare with the pushed size in the folder listing. Sizes matched to the byte; a one-byte surplus on a chapter is a trailing newline the original lacked.
- This is weaker than a byte diff or a local blob hash. Say so when stamping. If a sandbox with network is available, use `scripts/kindling_scan.py` and the raw commit URL diff described in the log.
- Stamp format: `B1-chNN | FIXED or CLEAN | blob | fix commit(s)`. One log write per block of five is accepted by Zia; the protocol itself says one per chapter.
- The log must be resent in full on every write. Read it fresh (get its sha) before writing.

## Decisions added this session
- D20: Kael surrenders his badge and his name is struck in ch36, but Councilor Veyne keeps him on the bench as auditor of record until the Reckoning concludes, then he is a private citizen. ch37 to ch40 rely on this.
- D8 applied to ch38 (ward Mara died on the Obsidian Terrace at the Festival; the dark crescent on Vane's ledge is Sol's own first-flare scorch). D15 applied to ch38 (Reckoning Hall, not a plaza or Hall of Contracts).

## Already known for the remaining chapters (not yet fixed)
- ch40 (read once, not edited): "six weeks since the rupture" is wrong (the rupture was about 22 Frostveil, the Reckoning is 29 Frostveil); Kael is "Auditor Ashworth" in a charcoal robe and is relieved of duty at the end (fits D20); "first night in the wind tunnels" and "three months" for the first transfer disagree with D17 (first transfer is ch05, 7 Emberfall, chimney); Sol "nineteen years feeding it" and her years left must be checked against D13; "Auditor Mara Vex" is a name clash (flag 8); "Year Zero" is a new dating label (flag 14 style, probably leave); Sol drops vellum pages instead of using ch38's crystal (flag 7).
- ch41 to ch43: three different verdicts on the ward's death; ch43 uses "Mira", change to Mara (D8, flag 2). Check the death location, crowd and manner against D8.
- ch44: Valerius exiled (flag 1); Sol "nineteen now" matches D13, compare other numbers to it.
- ch45: Auda Ashworth, Kael's grandmother, appears with no earlier mention (flag 15).
- Run the "particular", "the kind of" and hedge-word checks on each chapter (see SCAN NOTES in the log).

## Open flags that need Zia (all in the log, nothing blocks stamping)
Valerius's title and role (flag 1), Sol and Kael years-left split (flag 3), cost-per-use alignment (flag 4), first-transfer versions (flag 5), the many descriptions of Kael's evidence (flag 6), dropped threads including the ch38 crystal plan (flag 7), name clashes (flag 8), merging ch33 and ch34 (flag 9).

## After Book 1
- Update COVERAGE in the log, note the final commit, and tell Zia Book 1 is stamped.
- Book 2 and Book 3 follow the same protocol. Book 3 bans the month name "Frostveil" (see the log's SCAN NOTES).
- Zia's earlier instruction for Book 2: after ch45, one final humanizer and proofreading pass over ch1 to 45; if all passes, declare it KDP publishing ready. Do not act on this until Book 2 is reached.
