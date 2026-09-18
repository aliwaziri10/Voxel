#!/usr/bin/env python3
"""
story_bible.py - character/continuity bible for Voxel series and picture
books, stored as one JSON file per series/book under story_bibles/.

Idea borrowed from bookframes' "style bible + character reference before
final export" step. No code copied - original implementation.

A bible answers three questions before any new content is generated:
  1. Who/what must look or sound the same as last time? (characters, style)
  2. What has already happened? (plot facts, so a sequel doesn't contradict)
  3. What's the visual reference (image path/description) to keep art
     consistent across pages/books?

Phase 9 addendum: added per-book beat map storage (save_beat_map / 
load_beat_map / get_chapter_beat). A beat map is the whole-book chapter
outline from content_provider.generate_beat_map(), generated once before
any chapter prose is written and stored under book_beat_maps so a novel
doesn't lose the plot over many chapters, and so a resumed/re-run session
reuses the same outline instead of generating a different one.

2026-09-19: content_provider.generate_beat_map() changed from one flat
"beat" string per chapter to a "sub_beats" list of 2-4 typed entries
(plot/relationship-micro/interior/stakes/callback - see
novels/EDITORIAL_CHARTER.md's sub-beat planning method). get_chapter_beat()
now renders that list into a readable multi-part brief for
generate_novel_chapter() instead of assuming a single string, with a
fallback for any old-format bible entry saved before this change.
"""

import json
import os

BIBLE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "story_bibles")


def _path(series_slug):
    os.makedirs(BIBLE_DIR, exist_ok=True)
    return os.path.join(BIBLE_DIR, f"{series_slug}.json")


def load(series_slug):
    p = _path(series_slug)
    if not os.path.exists(p):
        return {
            "series_slug": series_slug,
            "characters": {},
            "visual_style": "",
            "plot_facts": [],
            "books": [],
            "book_beat_maps": {},
        }
    with open(p, "r") as f:
        bible = json.load(f)
    bible.setdefault("book_beat_maps", {})
    return bible


def save(series_slug, bible):
    with open(_path(series_slug), "w") as f:
        json.dump(bible, f, indent=2)


def register_book(series_slug, title, summary, new_plot_facts=None):
    bible = load(series_slug)
    bible["books"].append({"title": title, "summary": summary})
    if new_plot_facts:
        bible["plot_facts"].extend(new_plot_facts)
    save(series_slug, bible)
    return bible


def continuity_prompt_block(series_slug):
    """
    Renders the bible into a text block to prepend to any generation prompt
    (manuscript or image) so a sequel/new page/chapter stays consistent
    with what came before. Returns "" if no bible exists yet (first book
    in the series) so the prompt is unaffected.
    """
    bible = load(series_slug)
    if not bible["books"] and not bible["characters"]:
        return ""

    lines = ["CONTINUITY — must stay consistent with:"]
    if bible["visual_style"]:
        lines.append(f"Visual style: {bible['visual_style']}")
    for name, desc in bible["characters"].items():
        lines.append(f"Character '{name}': {desc}")
    if bible["plot_facts"]:
        lines.append("Established plot facts:")
        for fact in bible["plot_facts"]:
            lines.append(f"  - {fact}")
    if bible["books"]:
        lines.append("Prior books in this series:")
        for b in bible["books"]:
            lines.append(f"  - {b['title']}: {b['summary']}")
    return "\n".join(lines)


def set_characters(series_slug, characters_dict):
    bible = load(series_slug)
    bible["characters"].update(characters_dict)
    save(series_slug, bible)
    return bible


def set_visual_style(series_slug, style_text):
    bible = load(series_slug)
    bible["visual_style"] = style_text
    save(series_slug, bible)
    return bible


def save_beat_map(series_slug, book, beats):
    """
    Stores the whole-book chapter outline (see content_provider.
    generate_beat_map) under book_beat_maps[book], keyed by book title.
    Each entry is {"chapter": int, "sub_beats": [{"type": str, "detail": str}, ...]}
    as of 2026-09-19 (previously a flat {"chapter": int, "beat": str}).
    """
    bible = load(series_slug)
    bible["book_beat_maps"][book] = beats
    save(series_slug, bible)
    return bible


def load_beat_map(series_slug, book):
    """Returns the stored beat list for this book, or None if none exists
    yet (so callers know whether to generate one)."""
    bible = load(series_slug)
    return bible["book_beat_maps"].get(book)


def get_chapter_beat(series_slug, book, chapter_number):
    """
    Returns a rendered brief string for one chapter number, or None if no
    beat map exists or that chapter number isn't in it. Callers should
    fall back to the book-level brief when this returns None.

    2026-09-19: renders the current "sub_beats" list format (2-4 typed
    entries per chapter - see content_provider.generate_beat_map) into a
    readable multi-line brief, one line per sub-beat with its type
    labelled, so generate_novel_chapter() gets concrete direction for
    each real piece of content instead of one vague sentence. Falls back
    to the old flat "beat" string format for any bible entry saved before
    this change, so an in-progress/resumed book with an old-format map
    doesn't break.
    """
    beats = load_beat_map(series_slug, book)
    if not beats:
        return None
    for entry in beats:
        if entry.get("chapter") != chapter_number:
            continue

        sub_beats = entry.get("sub_beats")
        if sub_beats:
            lines = [f"- ({sb.get('type', 'beat')}) {sb.get('detail', '')}" for sb in sub_beats]
            return "\n".join(lines)

        # Old-format fallback (flat "beat" string, pre-2026-09-19 bibles).
        if entry.get("beat"):
            return entry["beat"]

        return None
    return None
