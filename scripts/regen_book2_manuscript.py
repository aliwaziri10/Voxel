#!/usr/bin/env python3
"""Rebuild the Book 2 full manuscript from the 45 chapter files.

Reads  novels/kindling-line-book-2/chapters/chapter_01.md ... chapter_45.md
Writes novels/kindling-line-book-2/kindling-line-book-2_full_manuscript.md

Format: "# <title>" then "## Chapter N" for each chapter, with the
<!-- chapter_date ... --> header line removed. Safe to re-run any time.
"""
import json
import re
import sys
from pathlib import Path

BOOK = Path("novels/kindling-line-book-2")
CHAPTERS = BOOK / "chapters"
OUT = BOOK / "kindling-line-book-2_full_manuscript.md"
TOTAL = 45


def main():
    title = json.loads((BOOK / "book_config.json").read_text(encoding="utf-8"))["title"]
    parts = ["# " + title + "\n"]
    words = 0
    for n in range(1, TOTAL + 1):
        path = CHAPTERS / ("chapter_%02d.md" % n)
        if not path.exists():
            sys.exit("MISSING: %s" % path)
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"\A\s*<!--.*?-->\s*", "", text, count=1, flags=re.S).strip()
        if not text:
            sys.exit("EMPTY: %s" % path)
        words += len(text.split())
        parts.append("## Chapter %d\n\n%s\n" % (n, text))
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print("Wrote %s: %d chapters, %d words" % (OUT, TOTAL, words))


if __name__ == "__main__":
    main()
