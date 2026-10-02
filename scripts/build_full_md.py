#!/usr/bin/env python3
"""
build_full_md.py - rebuild a book's <book_id>_full_manuscript.md from its
chapter files. Never hand-edit that file; run this instead.

Usage:
    python3 scripts/build_full_md.py novels/kindling-line-book-2

Reads book_config.json for the title, book_id and chapters_dir. Strips the
HTML chapter_date comments and heads each chapter "## Chapter N".
"""
import glob
import json
import os
import re
import sys

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    book_dir = sys.argv[1]
    with open(os.path.join(book_dir, "book_config.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    chapters_dir = os.path.join(book_dir, cfg.get("chapters_dir", "chapters"))
    files = sorted(glob.glob(os.path.join(chapters_dir, "chapter_*.md")))
    if not files:
        sys.exit(f"No chapter files in {chapters_dir}")
    parts = [f"# {cfg['title']}\n"]
    for i, path in enumerate(files, 1):
        with open(path, encoding="utf-8") as f:
            body = COMMENT_RE.sub("", f.read()).strip()
        parts.append(f"## Chapter {i}\n\n{body}\n")
    out = os.path.join(book_dir, f"{cfg['book_id']}_full_manuscript.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print(f"Wrote {out}: {len(files)} chapters.")


if __name__ == "__main__":
    main()
