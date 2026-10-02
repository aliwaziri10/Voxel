#!/usr/bin/env python3
"""
fix_grey.py - one spelling: grey, not gray (British style, as the Kindling
Line books use).

Usage:
    python3 scripts/fix_grey.py DIR [DIR ...]           # dry run, prints counts
    python3 scripts/fix_grey.py --apply DIR [DIR ...]   # writes the changes

Replaces whole words only: gray, graying, grayed, grayish, grayer, grayest,
grays (and the capitalized forms). Safe to re-run: a second run finds nothing.
"""
import glob
import os
import re
import sys

GRAY_RE = re.compile(r"\b([Gg])ray(ing|ed|ish|er|est|s)?\b")


def swap(m):
    return m.group(1) + "rey" + (m.group(2) or "")


def main():
    args = sys.argv[1:]
    apply = False
    if args and args[0] == "--apply":
        apply = True
        args = args[1:]
    if not args:
        print(__doc__)
        sys.exit(2)

    total = 0
    for d in args:
        for path in sorted(glob.glob(os.path.join(d, "*.md"))):
            with open(path, encoding="utf-8") as f:
                text = f.read()
            new, n = GRAY_RE.subn(swap, text)
            if n:
                total += n
                print(f"{path}: {n}")
                if apply:
                    with open(path, "w", encoding="utf-8", newline="") as f:
                        f.write(new)
    print(f"{'Replaced' if apply else 'Would replace'} {total} occurrence(s).")


if __name__ == "__main__":
    main()
