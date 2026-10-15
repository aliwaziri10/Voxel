#!/usr/bin/env python3
"""Read-only AI-tell scanner for a Voxel novel.

Usage: python tools/scan_tells.py novels/kindling-line-book-2

Reads <book>/chapters/chapter_*.md, never edits them, and writes
<book>/TELL_REPORT.md: per-chapter counts plus exact line numbers and
snippets, so the sequential manual pass (EDITORIAL_CHARTER.md) knows
where to look. Context decides every fix; nothing is auto-rewritten.
"""
import re
import sys
from pathlib import Path

PATTERNS = {
    "Not X. Y. pivot": r"\bNot [^.!?\n]{2,40}\. [A-Z]",
    "not X, but Y pivot": r"\bnot (?:just |merely |only )?[^.!?\n]{1,40}, but\b",
    "long moment": r"\blong moment\b",
    "let out / released a breath": r"\b(?:let out|released|exhaled) (?:a|the) breath\b",
    "a beat": r"\ba beat\b",
    "hung in/between": r"\bhung (?:in|between)\b",
    "stock abstractions": r"\b(?:tapestry|testament|symphony|palpable|unspoken|interplay)\b",
    "ozone/copper/petrichor": r"\b(?:ozone|copper|petrichor)\b",
    "something + vague hedge": r"\bsomething (?:like|in (?:her|his|their) (?:chest|throat|face)|shifted|changed|cracked|settled|tightened)\b",
    "the kind of": r"\bthe kind of\b",
    "particular": r"\bparticular\b",
    "neither of them said/had": r"\bneither of them (?:said|had)\b",
    "at the foot/top/head of": r"\bat the (?:foot|top|head) of the\b",
    "em dash": "\u2014",
}


def scan(book: Path) -> str:
    chapters = sorted((book / "chapters").glob("chapter_*.md"))
    if not chapters:
        sys.exit(f"No chapters found in {book / 'chapters'}")
    compiled = {k: re.compile(v) for k, v in PATTERNS.items()}
    totals = {k: 0 for k in PATTERNS}
    rows, details = [], []
    for ch in chapters:
        text = ch.read_text(encoding="utf-8")
        counts = {k: 0 for k in PATTERNS}
        hits = []
        for no, line in enumerate(text.splitlines(), 1):
            for k, rx in compiled.items():
                for m in rx.finditer(line):
                    counts[k] += 1
                    totals[k] += 1
                    s = max(0, m.start() - 40)
                    hits.append(f"- L{no} [{k}] ...{line[s:m.end() + 40].strip()}...")
        n = sum(counts.values())
        rows.append((ch.stem, len(text.split()), n))
        if hits:
            details.append(f"### {ch.stem} ({n} hits)\n" + "\n".join(hits))
    out = [f"# Tell report: {book.name}", "",
           "Read-only scan. Fix in sequential order, reading context for each hit.", "",
           "## Totals", ""]
    out += [f"- {k}: {v}" for k, v in totals.items() if v]
    out += ["", "## Per chapter", "", "| Chapter | Words | Hits |", "|---|---|---|"]
    out += [f"| {a} | {b} | {c} |" for a, b, c in rows]
    out += ["", "## Locations", ""] + details
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    book_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "novels/kindling-line-book-2")
    (book_dir / "TELL_REPORT.md").write_text(scan(book_dir), encoding="utf-8")
    print(f"Wrote {book_dir / 'TELL_REPORT.md'}")
