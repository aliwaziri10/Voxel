#!/usr/bin/env python3
"""
fix_pass2.py - second continuity pass, Kindling Line Book 1 and Book 2.

Canon (decided 2026-10-01):
  - Book 2 happens one year after Book 1 (Book 2 headers read Year 4).
  - Valerius Ashworth is alive through Book 1, then dies of his failing heart
    in the year between the books. Book 2's "eight months in the ground" stands.
  - Sol's mother: Reckoning flight twelve years before Book 1, burned forty
    years, Sol was twelve, died three winters later. Book 2 matches.
  - Every in-text countdown in Book 1 matches its chapter_date header.
Idempotent. Usage: python scripts/fix_pass2.py <book1_chapters_dir>
Book 2 chapters are read from the sibling kindling-line-book-2/chapters.
"""
import os
import re
import sys

B1 = [  # (chapter, old, new, regex?)
    # ch01: countdown to 58 (header 1 Emberfall), mother's burn
    (1, "Eight weeks. Fifty-six days.", "Eight weeks and two days. Fifty-eight days.", False),
    (1, "fifty-six days", "fifty-eight days", False),
    (1, "Fifty-six days", "Fifty-eight days", False),
    (1, "56 days", "58 days", False),
    (1, "the burn had taken eighteen years in forty minutes. Eighteen years.", "the burn had taken forty years in forty minutes. Forty years.", False),
    # ch02
    (2, "That title had died with Sol's father six years past.", "That title belonged to Sol's father, and the gout kept him in his rooms.", False),
    (2, "Your mother's Reckoning was seven years past.", "Your mother's Reckoning was twelve years past.", False),
    (2, "She died three months later.", "She died three winters later.", False),
    # ch03
    (3, "She had been sixteen, standing in the gallery with her father's hand", "She had been twelve, standing in the gallery with her father's hand", False),
    (3, "It saved him once. It did not save him the last time.", "It saved him once. It did not save him enough.", False),
    # ch04: 54 days from header 5 Emberfall
    (4, "eight weeks away", "fifty-four days away", False),
    (4, "eight weeks out", "fifty-four days out", False),
    (4, "in eight weeks", "in fifty-four days", False),
    # ch04 mother line is now owned by fix_pass3_mother_ward.py (the old rule here went stale)
    # ch06
    (6, "seven weeks away", "seven weeks and two days away", False),
    # ch07, ch08 (weeks since first audit visit / burns)
    (7, "first audit visit three weeks past", "first audit visit nine days past", False),
    (8, "two Kindling burns in three weeks", "two Kindling burns in under two weeks", False),
    # ch11 (header 16 Emberfall = 43 days)
    (11, "The Reckoning is in six weeks.", "The Reckoning is in forty-three days.", False),
    # ch13: 40 days ok; mother
    (13, "My mother lost thirty years in her final flight. She was forty-two. She looked seventy.", "My mother lost forty years in her final flight. She was forty-two. She looked eighty.", False),
    # ch15 (header 22 Emberfall = 37 days)
    (15, "The Reckoning is in five weeks.", "The Reckoning is in thirty-seven days.", False),
    (15, "rail at the five weeks", "rail at the thirty-seven days", False),
    (15, "The Reckoning was five weeks away.", "The Reckoning was thirty-seven days away.", False),
    # ch17
    (17, "She had been seven when the Reckoning took her mother. Seven and standing", "She had been twelve when the Reckoning took her mother. Twelve and standing", False),
    # ch18 (header 26 Emberfall = 33 days)
    (18, "The Reckoning comes in five weeks.", "The Reckoning comes in thirty-three days.", False),
    # ch19 (header 28 Emberfall = 31 days)
    (19, "The Reckoning is in five weeks.", "The Reckoning is in thirty-one days.", False),
    (19, "The Reckoning happens in five weeks.", "The Reckoning happens in thirty-one days.", False),
    (19, "the Reckoning was five weeks away.", "the Reckoning was thirty-one days away.", False),
    # ch22 (header 2 Frostveil = 27 days; archive was 29 Emberfall = 3 days ago)
    (22, "Grandmother Vane", "Aunt Rue", False),
    (22, "her grandmother's", "her aunt's", False),
    (22, "Her grandmother's", "Her aunt's", False),
    (22, "her grandmother", "her aunt", False),
    (22, "Her grandmother", "Her aunt", False),
    (22, "\"Grandmother.\"", "\"Aunt Rue.\"", False),
    (22, "\"Grandmother. If we default", "\"Aunt Rue. If we default", False),
    (22, "granddaughter", "niece", False),
    (22, "four weeks", "twenty-seven days", False),
    (22, "Four weeks", "Twenty-seven days", False),
    (22, "Five-year term.", "Twenty-year term.", False),
    (22, "He spent the rest of his life paying Tomas's family. He died in debt to them.", "He has spent every year since paying Tomas's family. He is still in debt to them.", False),
    (22, "his tragic early death", "his ruin", False),
    (22, "You've had it for twelve days.", "You've had it for three days.", False),
    (22, "She's not a piece on the board, Uncle.", "She's not a piece on the board, Father.", False),
    (22, "\"Twelve days,\" she repeated.", "\"Three days,\" she repeated.", False),
    (22, "I've been a coward for twelve days. For three years, if you count from the archive. For twenty, if you count from my father's signature on your mother's failure.", "I've been a coward for three days. For twelve years, if you count from my father's signature on your mother's failure.", False),
    (22, "Three days since you knew.\"", "Three days since you knew.\"", False),
    (22, "\"Thirteen,\" he corrected. \"Tomorrow makes thirteen.\"", "\"Four,\" he corrected. \"Tomorrow makes four.\"", False),
    (22, "\"Thirteen days of silence.", "\"Four days of silence.", False),
    (22, "Report to your uncle.", "Report to your father.", False),
    # ch23 (header 4 Frostveil = 25 days)
    (23, "three weeks before the date set in stone", "nearly four weeks before the date set in stone", False),
    # ch24 (header 5 Frostveil = 24 days)
    (24, "The Reckoning was in three weeks.", "The Reckoning was in twenty-four days.", False),
    (24, "Three weeks until the Reckoning.", "Twenty-four days until the Reckoning.", False),
    # ch25 (header 7 Frostveil = 22 days)
    (25, "The Reckoning is in three weeks.", "The Reckoning is in twenty-two days.", False),
    (25, "Three weeks until the Reckoning.", "Twenty-two days until the Reckoning.", False),
    # ch26 (header 8 Frostveil: Kael has held the proof since 29 Emberfall = 9 days)
    (26, "for six weeks while the ward trade", "for nine days while the ward trade", False),
    # ch27: mother
    (27, "the cost took twenty-three years in a single afternoon. Sol had been fourteen.", "the cost took forty years in a single afternoon. Sol had been twelve.", False),
    # ch29 (header 13 Frostveil = 16 days)
    (29, "The Reckoning is in two weeks.", "The Reckoning is in sixteen days.", False),
    (29, "Aunt Mara had spent six years watching the Kindling eat Sol's mother alive", "Aunt Rue had spent three years watching the Kindling eat Sol's mother alive", False),
    # ch30 (header 14 Frostveil = 15 days)
    (30, "The Reckoning is two weeks away.", "The Reckoning is fifteen days away.", False),
    (30, "Two weeks until the Reckoning.", "Fifteen days until the Reckoning.", False),
    (30, "Three weeks to find a file", "Fifteen days to find a file", False),
    (30, "He had two weeks until the Reckoning.", "He had fifteen days until the Reckoning.", False),
    (30, "The Reckoning is in two weeks.", "The Reckoning is in fifteen days.", False),
    # ch33 (header 19 Frostveil; proof since 29 Emberfall = 20 days)
    (33, "knew the truth for six weeks and reported nothing", "knew the truth for twenty days and reported nothing", False),
    # ch35: mother twelve years, Valerius alive, two months not two years
    (35, "Seven years since her mother's Reckoning.", "Twelve years since her mother's Reckoning.", False),
    (35, "Two since Kael Ashworth had walked", "Under three months since Kael Ashworth had walked", False),
    (35, "The date was fifteen years past", "The date was twelve years past", False),
    (35, "Seven years since her mother. Four since her own waking. Two since him.", "Twelve years since her mother. Four since her own waking. Under three months since him.", False),
    (35, "Ten years since his first audit. Three since his father's death. Forty-three", "Ten years since his first audit. Forty-three", False),
    (35, "The seven years and four years and two years he had watched", "The twelve years and four years and three months he had watched", False),
    (35, "and the ten years and three years he had counted on his own", "and the ten years he had counted on his own", False),
    # ch40
    (40, "seventeen years ago and taken Sol's mother", "twelve years ago and taken Sol's mother", False),
    # ch43 (header 4 Sunspire; first marks 1 to 4 Emberfall = nine weeks)
    (43, "cliffside inspection eight weeks past", "cliffside inspection nine weeks past", False),
]

B2_HEADERS = (r"(<!-- chapter_date: [^>]*?)Year 3( of the Reckoning Accord -->)", r"\1Year 4\2")
# Book 2 is one year after Book 1, and the mother's Reckoning was twelve years
# before Book 1, so Book 2 says "thirteen years" (12 + 1) in ch01 and ch04.
B2 = [
    (1, "It had not had one in three years, since the last ward-taker of the Lower Spine line had gone under a plate", "It had not had one in thirteen years, since the last ward-taker of the Lower Spine line had gone under a plate", False),
    (4, "In this chamber, three years ago, Sol's mother had sat at that plate", "In this chamber, thirteen years ago, Sol's mother had sat at that plate", False),
    (9, "I spent months in the archive tower three years ago, over my mother's papers.", "I spent months in the archive tower ten years ago, over my mother's papers.", False),
    (31, "My mother was six years a bearer under the old trade", "My mother was four years a bearer under the old trade", False),
]


def run_book(d, rules, tag, report, headers=None):
    changed = 0
    for ch in sorted({r[0] for r in rules}):
        p = os.path.join(d, "chapter_%02d.md" % ch)
        with open(p, encoding="utf-8") as f:
            t = f.read()
        o = t
        for c, old, new, rx in rules:
            if c != ch:
                continue
            if old in t:
                t = t.replace(old, new)
            elif new not in t:
                report.append("MISSING %s ch%02d: %r" % (tag, ch, old[:70]))
        if t != o:
            with open(p, "w", encoding="utf-8") as f:
                f.write(t)
            changed += 1
    if headers:
        for i in range(1, 46):
            p = os.path.join(d, "chapter_%02d.md" % i)
            with open(p, encoding="utf-8") as f:
                t = f.read()
            n = re.sub(headers[0], headers[1], t, count=1)
            if n != t:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(n)
                changed += 1
    return changed


def main():
    d1 = sys.argv[1] if len(sys.argv) > 1 else "novels/kindling-line-book-1/chapters"
    d2 = os.path.join(os.path.dirname(os.path.dirname(d1.rstrip("/"))), "kindling-line-book-2", "chapters")
    report = []
    c1 = run_book(d1, B1, "B1", report)
    c2 = run_book(d2, B2, "B2", report, B2_HEADERS)
    print("fix_pass2: book1 chapters changed %d | book2 chapters changed %d" % (c1, c2))
    bad = 0
    for r in report:
        print(r)
        bad += 1
    # checks
    t1 = "\n".join(open(os.path.join(d1, "chapter_%02d.md" % i), encoding="utf-8").read() for i in range(1, 46))
    t2 = "\n".join(open(os.path.join(d2, "chapter_%02d.md" % i), encoding="utf-8").read() for i in range(1, 46))
    checks = {
        "B1 Grandmother": t1.count("Grandmother"),
        "B1 Aunt Mara": t1.count("Aunt Mara"),
        "B1 fifty-six days": t1.lower().count("fifty-six days"),
        "B1 em-dashes": t1.count("\u2014"),
        "B2 em-dashes": t2.count("\u2014"),
        "B2 Year 3 headers": len(re.findall(r"chapter_date: [^>]*Year 3", t2)),
        "B2 Year 4 headers": 45 - len(re.findall(r"chapter_date: [^>]*Year 4", t2)),
    }
    for k, v in checks.items():
        if v:
            print("CHECK FAIL %s: %s" % (k, v))
            bad += 1
    print("PASS2 RESULT:", "FAIL" if bad else "OK")
    return bad


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
