#!/usr/bin/env python3
"""
kdp_metadata.py — Generates a KDP upload metadata package (Markdown)
from a book's book_config.json.

This script does NOT invent title, keywords, categories, description,
or price. Those are business/creative decisions. If a field is missing
from the config's "kdp" section, it is listed as an OPEN ITEM in the
output rather than filled in with a guess -- pipeline.py checks for
the literal string "OPEN ITEM" in this script's output and refuses to
advance the book past the kdp_metadata stage until every item is filled
in and the script is re-run clean.

Usage:
    python kdp_metadata.py --config path/to/book_config.json --out path/to/KDP_METADATA.md
"""
import argparse
import json
import sys
from datetime import datetime, timezone


REQUIRED_KDP_FIELDS = {
    "subtitle": "Subtitle (or null/empty string if intentionally none)",
    "series_reading_order_note": "One line on where this sits in the series",
    "description": "Back-cover / KDP product description copy",
    "keywords": "List of up to 7 KDP search keywords",
    "categories": "List of 2-3 KDP browse categories",
    "price_usd": "List price in USD",
    "kdp_select_enrolled": "true/false -- KDP Select enrollment decision",
}


def build_report(config):
    book_id = config["book_id"]
    title = config["title"]
    series = config["series"]
    book_number = config["book_number"]
    author = config["author"]
    publisher = config["publisher"]
    kdp = config.get("kdp", {})

    lines = []
    lines.append(f"# KDP Metadata Package — {title}")
    lines.append("")
    lines.append(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    lines.append(f"Book: {series}, Book {book_number}")
    lines.append(f"Author (pen name): {author}")
    lines.append(f"Publisher: {publisher}")
    lines.append(f"book_id: {book_id}")
    lines.append("")
    lines.append("## Fields")
    lines.append("")

    open_items = []
    for field, description in REQUIRED_KDP_FIELDS.items():
        value = kdp.get(field)
        if value in (None, "", [], {}):
            lines.append(f"- **{field}**: OPEN ITEM — {description}")
            open_items.append(field)
        else:
            if isinstance(value, list):
                lines.append(f"- **{field}**: {', '.join(str(v) for v in value)}")
            else:
                lines.append(f"- **{field}**: {value}")

    lines.append("")
    if open_items:
        lines.append(f"## Status: {len(open_items)} OPEN ITEM(S) — not ready for upload")
        lines.append("")
        lines.append("Fill these into the `kdp` section of this book's "
                      "`book_config.json`, then re-run this script. "
                      "pipeline.py will not advance past this stage until "
                      "the report is clean.")
    else:
        lines.append("## Status: complete — all fields present")
        lines.append("")
        lines.append("This does not mean the copy is *good*, only that "
                      "every required field has been filled in by hand. "
                      "Publisher-role review still applies before upload.")

    return "\n".join(lines) + "\n", open_items


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with open(args.config, encoding="utf-8") as f:
        config = json.load(f)

    report, open_items = build_report(config)

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(report)

    print(report)
    if open_items:
        print(f"OPEN ITEM count: {len(open_items)}", file=sys.stdout)
        sys.exit(0)  # not a hard failure -- pipeline.py checks the text
    print("Metadata package clean.")


if __name__ == "__main__":
    main()
