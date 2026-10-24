# Warm Enough: HANDOFF (Larkmere, second novel)

Read `novels/EDITORIAL_CHARTER.md` first, then `novels/HUMAN_WRITING.md`, then `novels/BEAT_MAP_PROTOCOL.md`, then this file. Series rules: `novels/larkmere-series/SERIES_BIBLE.md`.
Repo: `aliwaziri10/Voxel` (public). Zia is non-technical, works by voice and copy/paste. Push each file right after creating it. Verify pushes live.

STATUS (cleaned 2026-10-24): planning DONE, writing automated. Closed-world canon (`canon/CANON_LOCK.md`), heat ladder (`canon/HEAT_LADDER.md`) and all 40 chapter briefs (`briefs/ch01.md` to `ch40.md`) exist. The writer is `scripts/write_warm_enough.py`; the workflow is `.github/workflows/write-warm-enough.yml` (run by hand from the Actions tab; the daily schedule is pending Zia pasting the new workflow file). The writer is pinned (Zia, 2026-10-24) to `nvidia/nemotron-3-ultra-550b-a55b:free` through OpenRouter only. Chapters are written by the workflow in strict order, one commit per chapter, into `chapters/chapter_NN.md`. As of 2026-10-24 NO chapters exist yet; check the `chapters/` folder, never trust this line.
SUPERSEDED: the earlier instruction to write by hand and not to use the automated workflow (Zia chose automation on 2026-10-24). The hand method in `novels/proof-of-home/HANDOFF.md` is no longer the way this book is written.
Where this file and `canon/CANON_LOCK.md` or a brief disagree, the canon lock and the brief win. They carry the conflict fixes made on 2026-10-22 (tin first seen in chapter 5 and opened in 30; family secret learned by the reader in 15 and by Hester in 21; Longnight defined in brief 13).

## File map
- `canon/CANON_LOCK.md`: closed world. Cast, places, objects (exact wording), magic rules, locked lines with their chapter, time rules, style bans, hidden-fact schedule.
- `canon/HEAT_LADDER.md`: levels 0 to 10g and one body target per chapter.
- `briefs/chNN.md`: one brief per chapter (plot, who is present, magic, objects, locked lines, what to withhold, interior beat, stakes, callback, ending image).
- `WRITER_COMMAND.md`: the writer's hard rules. `VOICE_GUIDE.md`: voice. `book_config.json`, `PROOFREAD_TRACKER.md`: book state and per-chapter tracker.
- `canon/STATUS.md`: build status. `AUDIT_REPORT.md`: written by the writer once all 40 chapters exist (mechanical checks only).

## Decision (made by Claude for Zia on 2026-10-22, Zia may overrule)
Book 2 is a winter book: a grumpy, guarded knitter and a sunny newcomer schoolmaster who cannot get warm. Different from Book 1 in season, craft, who is the newcomer, and wound (giving versus receiving, not leaving versus staying). Market tags it serves: cozy fantasy, small town, slow burn, forced proximity (snowed in), grumpy/sunshine, found family, second-chance-ex-returns tension, winter/seasonal, HEA, closed door.
Working title: Warm Enough. Alternates: The Open Door; A Winter's Worth of Warm. Pen name: Elif Kessler. Series line: Larkmere, Book Two. Check Amazon title and series-name search before locking metadata.
Logline: In Larkmere every newcomer is knit a winter sweater, and it only warms if the knitter means it. Hester Tansley would rather freeze than mean it. Ansel Brandt would rather freeze than ask.

## Why 40 chapters (revision 2, 2026-10-22, after Zia asked why not 50 or 60)
Version 1 had 32 chapters only because Book 1 had 32. That was inherited, not a market decision. Market check: romance sits around 70,000 to 100,000 words; fantasy 80,000 to 120,000 with most around 100,000 to 115,000. A cozy fantasy romance belongs at the top of the romance range and the bottom of the fantasy range: about 100,000 words. 40 chapters at 2,300 to 2,700 words is about 92,000 to 108,000 words, squarely right. 50 to 60 chapters (125,000 to 160,000 words) overshoots what romance readers expect, makes the print book thicker and dearer, and raises the sag risk in a book whose first kiss is already late. The real gain is not length but more turns: version 2 adds a returning rival, two twists, a community set piece and a hook rule. Kindle Unlimited pays by pages read, so a longer book earns more per finished read, but only if readers finish it.
Changes from version 1: (1) 32 to 40 chapters, first kiss at chapter 33 (82.5 percent), release in chapter 40. (2) Added Piers Ellory, the cartographer who left nine winters ago, who returns on the winter post: a kind, charming, wrongly-timed rival, never a villain. (3) Twist one: Ansel's tin holds a scrap of grey wool that twelve-year-old Hester gave him on the quay the one winter he lived in Larkmere as a boy. It is the only thing he has never given away. (4) Twist two: the first Winter Knitter's page in Gran's pattern book says the toll is paid back only when the knitter is knit for. Nobody has ever knit for Hester. Ansel knits her the scarf. (5) Community set piece: the Great Knit-In at the Kettle Room during the cold snap (found family). (6) Hook rule: every chapter ends on a turn, a question or a held image, never a summary. (7) The old Longnight, hut and Breaking set pieces stay.

## Standing rules carried over from the old canon section
- Never name or involve any Book 1 character. Shared world only (see the series bible).
- The cast was audited against every other Voxel book on 2026-10-22; Pell, Bram, Hale, Oakes were rejected as already used.
- Style: all rules in HUMAN_WRITING.md and the charter. American spelling except "grey". No em dashes. No dates, weekdays, years or digits for ages.

## Shape
40 chapters, 2,300 to 2,700 words. Odd chapters Ansel, even chapters Hester, close third, past tense. First kiss chapter 33. After it the wanting only grows. Full release chapter 40 (closed door). Pre-kiss maximum is level 8. Obstacles are always feeling, weather, magic or a person who loves them, never procedure. Tilda and Gran only meddle at the edges. Every chapter ends on a turn or a held image.
Act one, cold: chapters 1 to 8. Act two, the thread: 9 to 16. Act three, the return: 17 to 32. Act four, the Breaking: 33 to 40.

## Open decisions for Zia
- Confirm the title (Warm Enough) and 40 chapters.
- Cameo policy: default is shared places only, no Book 1 people.
- KDP: primary Romance, second Science Fiction & Fantasy, confirm in the dashboard. Fill the AI disclosure gate in `book_config.json`.
- Chapter 40 holds a closed-door love scene of about 600 to 900 words (decided by Claude 2026-10-22, Zia may overrule).

## NEXT STEP
Let the workflow write chapters 1 to 40 in strict order. When chapters 1 to 3 exist, read them first for voice and canon; if they are wrong, disable the workflow. When all 40 exist, read `AUDIT_REPORT.md`, then do the human continuity, voice and canon read (manual gates in `book_config.json`), then proofread and the remaining KDP gates.
