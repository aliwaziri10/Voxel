# Warm Enough: who is editing right now

Read this before you touch any chapter. Two Claude sessions already wrote chapter 16 at the same time and only a failed push exposed it.

- Active editor: Claude chat session, started 2026-10-28.
- Job: whole-book revision, in this order. (1) repeat-move scan across all 40 chapters, (2) continuity check, (3) line-edit chapters 3 to 40 in order, voice first.
- Decision rule (from Zia, 2026-10-28): Claude has full authority and must critically evaluate every step. Zia's standing orders: never cut a chapter for length, no money suggestions, say plainly when he is wrong.
- Before you edit any chapter: check `stamps/` and the latest commits. If a commit is less than a few hours old and not yours, stop and read it first.
- Chapter 02 is already line-edited and stamped (`stamps/ch02.md`).
- When you finish a step, add a line here with the date and what changed. Do not delete other lines.

## Log
- 2026-10-28: claim file created. Nothing else edited yet beyond chapter 02.
- 2026-11-03: Claude chat (second session of the day) started the strict sequential human read from ch01. ch01 read and stamped (stamps/ch01.md), no text change. Spelling fixes pushed in ch13, ch20, ch22, ch23, ch35 (commits 0c1209c, cf006e5, 17934a1, 18374b0, afd1efa).
- 2026-11-03: ch03 to ch06 read and stamped (stamps/ch03.md to ch06.md). One fix: ch04 jacket cuff (commit b743c9b). Next unread chapter: ch07.
- 2026-11-03: ch07 to ch10 read and stamped, no text change. Open item logged in HANDOFF.md (layer order of Ansel's clothes). Next unread chapter: ch11.
- 2026-11-03: ch11 to ch14 read and stamped. One fix: ch14 one word (pupil to boy, schoolroom comparison in Hester's chapter). Next unread chapter: ch15.
- 2026-11-05: Claude chat ran the repo checker on all 40 chapters. The 2026-11-03 ch14 edit (pupil to boy) had made a HARD failure ("as a boy" matches the boyhood rule). Fixed in ch14, one word, "as a man" (commit 66ecce8). ch31 "somebody" removed (commit 3a0eeab). No chapter was read or stamped. Next unread chapter is still ch15. Run `python scripts/write_warm_enough.py --check novels/warm-enough/chapters/chapter_NN.md --chapter N` on every chapter you edit BEFORE you push it. Details: `HANDOFF_2026-11-05.md`.
- 2026-11-07: ch15 to ch18 read and stamped. Three small fixes: ch16 "lesson" to "thing she knew" and a nine-winters continuity scope, ch17 sealed letters. Next unread chapter: ch19. Note: ch18 is 2,820 words (over target, left).
- 2026-11-07: ch19 and ch20 read and stamped, no text change (ch19 3,331 words left uncut). Next unread chapter: ch21.
- 2026-11-07: ch21 and ch22 read and stamped. One small fix: ch22 chipped blue teapot added (brief object). Next unread chapter: ch23.
- 2026-11-07: ch23 and ch24 read and stamped. Two small fixes: ch23 "thread" to "whisper", ch24 "Spindle House" to "Knit-In". Next unread chapter: ch25 (check Dunstan's name there).
- 2026-11-07: ch25 to ch28 read and stamped (Zia approved the batch). Two small fixes: ch26 "lesson" to "rule", ch28 "the blue" to "the grey-green". Next unread chapter: ch29.
- 2026-11-07: ch29 to ch32 read and stamped (Zia asked for fixes and for them to be written in HANDOFF). Fixes: ch29 "thread" to "edge" and "A letter" to "Two letters"; ch31 two knitting figures in Ansel's chapter; ch32 unclear scuttle sentence. Next unread chapter: ch33.
- 2026-11-07: ch33 and ch34 read and stamped. One fix: ch33 "lost the thread of a sum" to "lost his place in a sum". Logged: ch33 school scene has Tilda although the brief says nobody else (kept). Next unread chapter: ch35 (check Piers and the locked-line reference).
