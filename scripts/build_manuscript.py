#!/usr/bin/env python3
"""
build_manuscript.py — Assemble final KDP-ready .docx from chapter markdown.

Usage:
    python build_manuscript.py --chapters chapters/ --out manuscript.docx \
        --title "Where the Frost Doesn't Reach" --series "The Amity Falls Series" \
        --book-number 1 --author "Elif Kessler" --trim 6x9 --year 2026

What it does that the old manual process didn't:
  - Sets the docx page size to the exact KDP trim from the start (so the page
    count KDP calculates matches reality later).
  - Converts markdown *italics* / _italics_ into REAL run-level italic
    formatting (w:i / w:iCs) instead of leaving literal asterisks in the text —
    this is the bug that previously required manual XML surgery after the fact.
  - Adds standard front matter (title page, copyright page).
  - Runs validate.py-equivalent paragraph-count sanity check at the end.

Requires: python-docx (pip install python-docx --break-system-packages)
"""
import argparse
import glob
import os
import re
import sys
from datetime import datetime

TRIM_SIZES_IN = {
    "5x8": (5, 8), "5.25x8": (5.25, 8), "5.5x8.5": (5.5, 8.5),
    "6x9": (6, 9), "6.14x9.21": (6.14, 9.21), "7x10": (7, 10), "8.5x11": (8.5, 11),
}

EMPHASIS_RE = re.compile(r"(\*{1,2}|_{1,2})(?!\s)(.+?)(?<!\s)\1")


def read_chapters(chapters_dir):
    files = sorted(glob.glob(os.path.join(chapters_dir, "chapter_*.md")))
    if not files:
        files = sorted(glob.glob(os.path.join(chapters_dir, "*.md")))
    return files


def add_markdown_emphasis_paragraph(paragraph, line):
    """Split a line on markdown emphasis markers and add runs with real
    italic formatting instead of leaving literal asterisks/underscores."""
    pos = 0
    for m in EMPHASIS_RE.finditer(line):
        if m.start() > pos:
            paragraph.add_run(line[pos:m.start()])
        run = paragraph.add_run(m.group(2))
        run.italic = True
        pos = m.end()
    if pos < len(line):
        paragraph.add_run(line[pos:])
    if not line.strip():
        paragraph.add_run("")


def build(args):
    try:
        from docx import Document
        from docx.shared import Inches, Pt
        from docx.enum.text import WD_ALIGN_PARAGRAPH
    except ImportError:
        print("python-docx not installed. Run: pip install python-docx --break-system-packages", file=sys.stderr)
        sys.exit(1)

    w_in, h_in = TRIM_SIZES_IN.get(args.trim, (6, 9))
    doc = Document()
    section = doc.sections[0]
    section.page_width = Inches(w_in)
    section.page_height = Inches(h_in)
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

    # -- Title page --
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(args.title)
    run.bold = True
    run.font.size = Pt(28)
    doc.add_paragraph()
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(f"{args.series}, Book {args.book_number}")
    r2.italic = True
    r2.font.size = Pt(14)
    doc.add_paragraph()
    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p3.add_run(args.author).font.size = Pt(14)
    doc.add_page_break()

    # -- Copyright page --
    year = args.year or datetime.now().year
    cp_lines = [
        f"© {year} {args.author}",
        "All rights reserved.",
        "",
        "This is a work of fiction. Names, characters, businesses, places, events, "
        "locales, and incidents are either the products of the author's imagination "
        "or used in a fictitious manner. Any resemblance to actual persons, living "
        "or dead, or actual events is purely coincidental.",
        "",
        "No part of this book may be reproduced, or stored in a retrieval system, "
        "or transmitted in any form or by any means, without the prior written "
        "permission of the author, except as provided by United States of America "
        "copyright law.",
    ]
    for line in cp_lines:
        cp = doc.add_paragraph()
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cp.add_run(line).font.size = Pt(10)
    doc.add_page_break()

    # -- Chapters --
    files = read_chapters(args.chapters)
    if not files:
        print(f"No chapter files found under {args.chapters}", file=sys.stderr)
        sys.exit(1)

    for idx, path in enumerate(files):
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        # First heading line becomes the chapter title
        lines = raw.split("\n")
        title_line = None
        body_start = 0
        for i, l in enumerate(lines):
            stripped = l.strip().lstrip("#").strip()
            if stripped:
                title_line = re.sub(r"^\*+|\*+$", "", stripped)
                body_start = i + 1
                break
        heading = doc.add_paragraph()
        heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
        hrun = heading.add_run((title_line or f"Chapter {idx + 1}").upper())
        hrun.bold = True
        hrun.font.size = Pt(16)
        doc.add_paragraph()

        for line in lines[body_start:]:
            if not line.strip():
                continue
            para = doc.add_paragraph()
            add_markdown_emphasis_paragraph(para, line.strip())
        if idx < len(files) - 1:
            doc.add_page_break()

    doc.save(args.out)

    # -- Sanity check --
    from docx import Document as D2
    check = D2(args.out)
    non_empty_paras = sum(1 for p in check.paragraphs if p.text.strip())
    print(f"Built {args.out}: {len(files)} chapters, {non_empty_paras} non-empty paragraphs, trim {w_in}x{h_in}in.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--series", required=True)
    ap.add_argument("--book-number", required=True)
    ap.add_argument("--author", default="Elif Kessler")
    ap.add_argument("--trim", default="6x9", choices=list(TRIM_SIZES_IN.keys()))
    ap.add_argument("--year", type=int, default=None)
    args = ap.parse_args()
    build(args)


if __name__ == "__main__":
    main()
