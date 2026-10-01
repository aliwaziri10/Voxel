#!/usr/bin/env python3
"""
fix_book1.py - one-pass continuity fixes for Kindling Line Book 1.

Usage: python scripts/fix_book1.py [chapters_dir]
Default dir: novels/kindling-line-book-1/chapters

Decisions applied (Zia, 2026-10-01):
  - Valerius Ashworth is ALIVE (former High Auditor, Lord of House Ashworth).
  - Reckoning is 29 Frostveil; every in-text countdown matches its chapter_date header.
  - No "chapter N" references inside narration.
  - Sol's mother burned forty years in her final flight, twelve years ago.
  - Em-dashes removed.
Idempotent: safe to run twice. Prints a report; exit code 1 if a check fails.
"""
import re
import sys
import os

D = sys.argv[1] if len(sys.argv) > 1 else "novels/kindling-line-book-1/chapters"

# (chapter, old, new)   replaced everywhere in that chapter
E = [
    (1, "The Reckoning is in fifty-six days,", "The Reckoning is in fifty-eight days,"),
    (1, "She burned eighteen years. She died three winters later.", "She burned forty years. She died three winters later."),
    (2, "The Reckoning was in thirty-eight days.", "The Reckoning was in fifty-seven days."),
    (2, "He had thirty-eight days to the Reckoning.", "He had fifty-seven days to the Reckoning."),
    # ch3: Valerius alive
    (3, "He died three months after retiring. The official cause was heart failure. The autopsy was performed by a Corrin physician. The report was sealed.",
        "He retired with an empty ledger and a heart the Corrin physician called failing. The medical report was sealed."),
    (3, "The chain is registered to Valerius Ashworth. It passes to his heir. You.",
        "The chain is registered to Valerius Ashworth. It cannot leave his name without Corrin registry."),
    (3, "I am not my father's heir. I renounced the inheritance when I took the auditor's oath. The chain reverted to the Reckoning office.",
        "My father surrendered it to the Reckoning office when he retired."),
    (3, "Because my father died for a lie they wrote.", "Because my father signed a lie they wrote."),
    (4, "The Reckoning is six months away. Six months of protected", "The Reckoning is eight weeks away. Eight weeks of protected"),
    (4, "The Reckoning is six months out.", "The Reckoning is eight weeks out."),
    (4, "The Reckoning is in six months.", "The Reckoning is in eight weeks."),
    (6, "The Reckoning was three months away. The date had been fixed since the first chapter of the Accord. Eighty-seven days until Isolde Vane",
        "The Reckoning was seven weeks away. The date had been fixed since the signing of the Accord. Fifty-one days until Isolde Vane"),
    (6, "Eighty-seven days until the transfer marks", "Fifty-one days until the transfer marks"),
    (6, "died in the Reckoning three years past", "died three winters after her Reckoning, twelve years past,"),
    (7, "in seven weeks and twenty days.", "in seven weeks."),
    (9, "sixty-seven days from now", "forty-six days from now"),
    (9, "another stalled judgment. \u2014 V.*", "another stalled judgment. V.*"),
    (11, "thirty-two years in a single morning", "forty years in a single morning"),
    (13, "forty-three days away", "forty days away"),
    (14, "in chapter five, when the wind", ", when the wind"),
    (14, " Chapter five. She remembered", " She remembered"),
    (14, "The Reckoning. Six weeks away.", "The Reckoning. Thirty-nine days away."),
    (15, "The Reckoning is in eighteen weeks.", "The Reckoning is in five weeks."),
    (15, "The Reckoning was eighteen weeks away. Eighteen weeks to learn", "The Reckoning was five weeks away. Five weeks to learn"),
    (15, "eighteen weeks", "five weeks"),
    (15, "Eighteen weeks", "Five weeks"),
    (17, "forty-three days", "thirty-four days"),
    (17, "Forty-three days", "Thirty-four days"),
    (18, "The Reckoning comes in six weeks.", "The Reckoning comes in five weeks."),
    (19, "\"The Reckoning is in six weeks.\"", "\"The Reckoning is in five weeks.\""),
    # ch22: Valerius (father) replaces uncle Corven; grandmother replaces the living mother
    (22, "from the Corrin archive in chapter eleven,", "from the Corrin archive,"),
    (22, " The one from chapter eleven. The pricing weights.", " The pricing weights."),
    (22, "He had gone to the archive in chapter eleven looking for precedent.", "He had gone to the archive looking for precedent."),
    (22, "The proof had sat in his desk for twelve days. Twelve days since chapter twenty, since the archive, since the offer from his uncle",
        "The proof had sat in his desk for three days. Three days since the archive, since the offer from his father"),
    (22, "since chapter five, since the first forced proximity, since the night chase across the ledges in chapter thirteen when",
        "since the inspection ledge, since the first forced proximity, since the night chase across the ledges when"),
    (22, "The voice belonged to his uncle, Lord Corven Ashworth, head of the house since Kael's father died. The man who had made the offer in chapter twenty.",
        "The voice belonged to his father, Valerius Ashworth, the former High Auditor and now Lord of House Ashworth. The man who had made the offer."),
    (22, "\"Uncle.\"", "\"Father.\""),
    (22, "I've had it for twelve days. Since chapter twenty. Since before", "I've had it for three days. Since before"),
    (22, "Twelve days since", "Three days since"),
    (22, "Corven", "Valerius"),
    (22, "his uncle", "his father"),
    (22, "eighteen weeks", "four weeks"),
    (22, "Eighteen weeks", "Four weeks"),
    (22, "Lady Vane", "Grandmother Vane"),
    (22, "\"Mother.\"", "\"Grandmother.\""),
    (22, "\"Mother. If we", "\"Grandmother. If we"),
    (22, "her mother's garden", "her grandmother's garden"),
    (22, "where her mother had once", "where her grandmother had once"),
    (22, "Her mother", "Her grandmother"),
    (22, "told her mother", "told her grandmother"),
    (22, "facing her daughter", "facing her granddaughter"),
    (23, "burning twenty-three years in forty seconds", "burning forty years in a single flight"),
    (23, "three months before the date set in stone", "three weeks before the date set in stone"),
    (23, "Forty-seven days", "Twenty-five days"),
    (23, "He had known the calculation in chapter twenty.", "He had known the calculation at the archive."),
    (24, "Six weeks until the Reckoning.", "Three weeks until the Reckoning."),
    (24, "The Reckoning was in six weeks.", "The Reckoning was in three weeks."),
    (24, "son of the late High Auditor Valerius", "son of the former High Auditor Valerius"),
    (25, "The Reckoning is in six weeks. You're submitting", "The Reckoning is in three weeks. You're submitting"),
    (25, "Six weeks until the Reckoning. Forty-two days. One thousand eight hours.", "Three weeks until the Reckoning. Twenty-two days. Five hundred twenty-eight hours."),
    (25, "the original date \u2014 the date set in Chapter 1, the date that could not move \u2014 while", "the original date, the date that could not move, while"),
    (27, "The Reckoning was thirty days away. Thirty days to decide what kind of auditor he would be. Thirty days to decide what kind of man.",
         "The Reckoning was nineteen days away. Nineteen days to decide what kind of auditor he would be. Nineteen days to decide what kind of man."),
    (27, "The date is fixed in chapter one of the founding charter.", "The date is fixed in the founding charter."),
    (27, "\"Chapter one,\" Mireau laughed", "\"The founding charter,\" Mireau laughed"),
    (28, "The Reckoning is twenty-seven days away.", "The Reckoning is eighteen days away."),
    (29, "The Reckoning is in six weeks. I needed", "The Reckoning is in two weeks. I needed"),
    (30, "You have had six months. The Reckoning is less than three weeks away.", "You have had weeks. The Reckoning is two weeks away."),
    (30, "Three weeks until the Reckoning", "Two weeks until the Reckoning"),
    (30, "He had three weeks until the Reckoning.", "He had two weeks until the Reckoning."),
    (30, "\"Three weeks,\" she said. \"The Reckoning is in three weeks. You have three weeks to", "\"Two weeks,\" she said. \"The Reckoning is in two weeks. You have two weeks to"),
    (32, "The Reckoning is six weeks away. Six weeks.", "The Reckoning is twelve days away. Twelve days."),
    (32, "the Reckoning six weeks away", "the Reckoning twelve days away"),
    (34, "You have known for months.", "You have known for three weeks."),
    (34, "Since the hearing in the Hall of Ledgers. Twenty Frostveil last year.", "Since the Corrin archive. Twenty-nine Emberfall."),
    (34, "The offer from House Ashworth came three days later. My uncle's terms", "The offer from House Ashworth came that same day. My father's terms"),
    (34, "The offer from his uncle.", "The offer from his father."),
    (34, "You knew in chapter ten and you did not report it.", "You knew from the first transfer and you did not report it."),
    (35, "The Reckoning was eighteen days away. Eighteen days to decide", "The Reckoning was seven days away. Seven days to decide"),
    (36, "the date of the seventeenth. One day before the Reckoning.", "the date of the twenty-ninth of Emberfall. Thirty days before the Reckoning."),
    (39, "Three days until the Reckoning. Three days until twelve flares", "One day until the Reckoning. One day until twelve flares"),
    (44, "The Reckoning Accord was three days old.", "The Reckoning Accord was six days old."),
    (44, "on the ledge in chapter twenty-seven,", "on the ledge,"),
    (44, "The first one in chapter five, on the lower ledge.", "The first one on the lower ledge."),
]


def strip_dashes(t):
    t = t.replace(". \u2014 V.A.", ". V.A.")
    t = re.sub(r'\s*\u2014\s*"', '..."', t)            # interrupted speech
    t = re.sub(r'(\w)\u2014(\w)', r'\1, \2', t)        # unspaced
    t = re.sub(r'\s\u2014\s([^\u2014\n.!?]{1,90}?)\s\u2014\s', r', \1, ', t)   # paired asides

    def single(m):
        nxt = m.group(1)
        if nxt.isdigit():
            return ": " + nxt
        if nxt.islower():
            return ", " + nxt
        return ". " + nxt
    t = re.sub(r'\s\u2014\s(.)', single, t)
    t = t.replace("\u2014", ", ")
    t = t.replace(",,", ",").replace(", ,", ",").replace(" ,", ",").replace(".,", ".")
    return t


def main():
    report, bad = [], 0
    texts = {}
    for i in range(1, 46):
        p = os.path.join(D, "chapter_%02d.md" % i)
        with open(p, encoding="utf-8") as f:
            texts[i] = f.read()
    orig = dict(texts)
    for ch, old, new in E:
        if old in texts[ch]:
            texts[ch] = texts[ch].replace(old, new)
        elif new not in texts[ch]:
            report.append("MISSING ch%02d: %r" % (ch, old[:70]))
            bad += 1
    dash_before = sum(t.count("\u2014") for t in texts.values())
    for i in texts:
        texts[i] = strip_dashes(texts[i])
    changed = 0
    for i, t in texts.items():
        if t != orig[i]:
            with open(os.path.join(D, "chapter_%02d.md" % i), "w", encoding="utf-8") as f:
                f.write(t)
            changed += 1
    # ---- verification ----
    allt = "\n".join(texts.values())
    checks = {
        "em-dashes": allt.count("\u2014"),
        "chapter-N in narration": len(re.findall(r"\b[Cc]hapter (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty[- ]?\w*|\d+)\b", allt)),
        "Corven": allt.count("Corven"),
        "eighteen weeks": allt.lower().count("eighteen weeks"),
        "Frostfall": allt.count("Frostfall"),
        "late High Auditor": allt.count("late High Auditor"),
        "double punctuation": len(re.findall(r"(?<!\.)\.\.(?!\.)|,,|, ,|\.,", allt)),
    }
    months = ["Emberfall", "Frostveil", "Sunspire"]
    for i, t in texts.items():
        m = re.match(r"<!-- chapter_date: (\d+) (\w+)", t)
        if not m:
            checks["header missing ch%02d" % i] = 1
    for k, v in checks.items():
        if v:
            report.append("CHECK FAIL %s: %s" % (k, v))
            bad += 1
    print("chapters changed: %d | em-dashes removed: %d" % (changed, dash_before - checks["em-dashes"]))
    for r in report:
        print(r)
    print("RESULT:", "FAIL" if bad else "OK")
    sys.exit(1 if bad else 0)


main()
