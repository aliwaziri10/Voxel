#!/usr/bin/env python3
"""
build_docx_from_config.py - build a book's KDP .docx straight from its
book_config.json, without going through the pipeline stage gates.

Usage:
    python3 scripts/build_docx_from_config.py novels/kindling-line-book-2 out.docx
"""
import json
import os
import subprocess
import sys


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    book_dir, out = sys.argv[1], sys.argv[2]
    with open(os.path.join(book_dir, "book_config.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    here = os.path.dirname(os.path.abspath(__file__))
    cmd = [
        sys.executable, os.path.join(here, "build_manuscript.py"),
        "--chapters", os.path.join(book_dir, cfg.get("chapters_dir", "chapters")),
        "--out", out,
        "--title", cfg["title"],
        "--series", cfg["series"],
        "--book-number", str(cfg["book_number"]),
        "--author", cfg["author"],
        "--trim", cfg.get("trim", "6x9"),
    ]
    sys.exit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
