#!/usr/bin/env python3
"""
write_keel_and_comb.py - strict, chapter-by-chapter writer and auditor for Keel and Comb
(Larkmere, Book Three, Elif Kessler).

This is a thin wrapper around scripts/write_warm_enough.py (which stays untouched, Warm Enough is
frozen). It imports that module and swaps in this book's own cast, places, locked lines, banned names,
brief format and canon view, then runs the same engine: strict order, hard and soft checks, repair loop,
brief check, free writer model only, a commit per chapter.

Usage (same as the Warm Enough writer):
  python scripts/write_keel_and_comb.py --auto --checkpoint
  python scripts/write_keel_and_comb.py --start 1 --end 1 --dry-run
  python scripts/write_keel_and_comb.py --check novels/larkmere-book-3/chapters/chapter_01.md --chapter 1
  python scripts/write_keel_and_comb.py --audit

Book files: novels/larkmere-book-3/ (canon/CANON_LOCK.md, canon/HEAT_LADDER.md, VOICE_GUIDE.md,
WRITER_COMMAND.md, briefs/ch01..ch40.md). Chapters land in novels/larkmere-book-3/chapters/.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import write_warm_enough as w  # noqa: E402

ROOT = w.ROOT
BOOK = ROOT / "novels" / "larkmere-book-3"
TOTAL = 40

# ---------- this book's tables ----------

w.BOOK = BOOK
w.TOTAL = TOTAL

w.ALLOWED = set("""
Bryony Bry Fairlie Ewan Marrick Tobiah Ottoline Abel Trent Larkmere Water Rise Honey House
Net Sheds Far Shore Heron Lantern Street
""".split())

w.BANNED_NAMES = ("Wren Pell Bram Hale Oakes Corrin Voss Marius Mara Renn "
                  "Jack Nell Sarah Odalys Fenna Gideon Teague Mercer Quill Pike "
                  "Hester Ansel Tilda Mina Piers Dunstan Ostler Winifred").split()

# first and last chapter in which a named character may appear at all
w.CHAR_RANGES = {
    "Abel": (9, 40), "Trent": (9, 40),
}

# marker (lower case, straight apostrophes) -> chapters where it must appear and may appear
w.LOCKED = {
    "they're only deciding": {1},
    "fairlie keel, marrick comb": {3, 40},
    "i light it every dusk": {28},
    "i would have said go": {34},
    "i'm not asking you to stay": {36},
    "is there room": {40},
    "there is room": {40},
}


# ---------- briefs ----------

def load_brief(n):
    p = BOOK / "briefs" / ("ch%02d.md" % n)
    if not p.exists():
        raise SystemExit("STOP: brief for chapter %d is missing." % n)
    text = w.read(p)
    head = text.split("\n", 1)[0]
    m = re.match(r"# Brief (\d+) \| (Bryony|Ewan) \| ([^|]+) \|", head)
    if not m or int(m.group(1)) != n:
        raise SystemExit("STOP: brief %d heading is not readable: %r" % (n, head))
    pov, season = m.group(2), m.group(3).strip()
    if (pov == "Bryony") != (n % 2 == 1):
        raise SystemExit("STOP: chapter %d heading says %s but odd chapters are Bryony and even are Ewan." % (n, pov))
    return text, pov, season


# ---------- per-chapter canon view ----------

def canon_for_chapter(canon, n, brief):
    """The canon this chapter needs: rules, cast, voice anchors, places, objects, magic, this chapter's locked
    lines, time and style. Left out: the hidden-fact schedule and the author's notes (they would spoil later
    chapters), characters who may not appear yet, and objects that do not exist yet."""
    head, secs = w.split_canon(canon)
    not_yet = [nm for nm, (lo, hi) in w.CHAR_RANGES.items() if not (lo <= n <= hi)]
    out = [head]
    for k in (1, 2, 3, 4):
        if k not in secs:
            continue
        lines = []
        for ln in secs[k].split("\n"):
            if k == 2 and ln.startswith("- ABEL") and "Abel" in not_yet:
                continue
            lines.append(ln)
        out.append("\n".join(lines))
    if 5 in secs:
        lines = []
        for ln in secs[5].split("\n"):
            if ln.startswith("- "):
                if n < 2 and "THE LEAVING JAR" in ln:
                    continue
                if n < 11 and "THE KEEL NOTE" in ln:
                    continue
                if n < 14 and "BOOT-BOX" in ln:
                    continue
            lines.append(ln)
        out.append("\n".join(lines))
    if 6 in secs:
        out.append(secs[6])
    if 7 in secs:
        keep = [x for x in secs[7].split("\n")[1:] if x.startswith("- ") and re.search(r"chapters? [^.]*\b%d\b" % n, x)]
        out.append("## 7. Locked lines for THIS chapter\n" + ("\n".join(keep) if keep else "(No locked line belongs to this chapter. Write none.)"))
    for k in (8, 9):
        if k in secs:
            out.append(secs[k])
    return w.scrub_names("\n\n".join(out), not_yet)


# ---------- the 'never' block ----------

def chapter_limits(n, brief=None):
    no_names = [nm for nm, (lo, hi) in w.CHAR_RANGES.items() if not (lo <= n <= hi)]
    no_lines = [m for m, chs in w.LOCKED.items() if n not in chs]
    out = ["=== NEVER IN THIS CHAPTER (the checker rejects the whole chapter for any of these) ==="]
    if no_names:
        out.append("Do not write these names at all, not even in a thought, a rumor or a memory: " + ", ".join(sorted(no_names)) + ".")
    out.append("Only the people on this brief's PRESENT line may be named. Everyone else is an unnamed quay person or neighbor, one short line at most.")
    if no_lines:
        out.append("Do not write any of these lines, even changed slightly: " + "; ".join('"%s"' % m for m in sorted(no_lines)) + ".")
    if n % 2 == 1:
        out.append("This is Bryony's chapter. Her comparisons come only from boats, wood, grain, joinery, tools, water and lake weather. "
                   "Never compare anything to bees, hives, comb or honey in her narration. She can taste honey and call it honey.")
    else:
        out.append("This is Ewan's chapter. His comparisons come only from bees, comb, honey, hives, flowers, smoke, weather and seasons. "
                   "Never compare anything to boats, planks, keels, joints or carpentry in his narration.")
    out.append("No invented backstory, no invented job, place or relative. Do not name any month or weekday (no January to December, no Monday to Sunday). "
               "Do not use an em dash or en dash anywhere: use a comma, a full stop or a new sentence. "
               "Never write the words beat, chapter, canon or protagonist, even in an ordinary sense (use thump, pulse, section, and so on).")
    out.append("Write only what the brief's PLOT says happens, in its SETTING, with the objects its OBJECTS line names. "
               "Add no extra scenes, no extra places and no extra objects. Never write a note, a marker or a line about the halves of the chapter.")
    out.append("The chapter ENDS on the image named in the brief's ENDS ON line and stops there: nothing happens after it. "
               "Everyone speaks only to the person the brief says they speak to, and knows only what the brief's WITHHOLD line allows. "
               "Never repeat a sentence from earlier in the same chapter.")
    forb = w.brief_forbidden(brief)
    if forb:
        out.append("The brief's SETTING says these are absent, so do not write these words at all: " + ", ".join(forb) + ".")
    if n < 2:
        out.append("Do not mention any jar kept on a shelf, and do not mention a lantern.")
    if n != 33:
        out.append("The Leaving Jar is not opened or tasted in this chapter.")
    if n < 11:
        out.append("Do not mention pencil writing inside the keel.")
    if n < 14:
        out.append("Do not mention a boot-box or unopened letters from Bryony to Tobiah.")
    if n < 28:
        out.append("They do not kiss in this chapter. Memories of the year they were together stay at the level of one small body detail.")
    return "\n".join(out)


# ---------- checks ----------

_orig_check = w.check


def check(body, n, brief=None):
    hard, soft = _orig_check(body, n, brief)
    # the Warm Enough engine also carries a tin and a boyhood rule; neither exists in this book
    hard = [h for h in hard if not ("a tin is mentioned" in h or "the tin is opened" in h or "boyhood" in h)]
    pm = re.search(r"(?m)^PRESENT:(.*)$", brief or "")
    present = pm.group(1) if pm else ""
    if brief:
        for nm in ("Tobiah", "Ottoline", "Abel"):
            if re.search(r"\b%s\b" % nm, body) and nm not in present:
                soft.append("%s is named but is not in this chapter's PRESENT line" % nm)
    if n < 28 and re.search(r"\bkiss(ed|es|ing)?\b", body, re.I):
        soft.append("a kiss is mentioned before chapter 28 (check it is only a one-detail memory, not a scene)")
    return hard, soft


w.load_brief = load_brief
w.canon_for_chapter = canon_for_chapter
w.chapter_limits = chapter_limits
w.check = check

# ---------- cosmetic: keep Warm Enough's name out of this book's files and logs ----------

_orig_write_text = Path.write_text


def _write_text(self, data, *a, **k):
    if isinstance(data, str) and str(self).startswith(str(BOOK)):
        data = data.replace("<!-- warm-enough ", "<!-- keel-and-comb ").replace("Warm Enough", "Keel and Comb")
    return _orig_write_text(self, data, *a, **k)


Path.write_text = _write_text

_orig_checkpoint = w.checkpoint


def checkpoint(path, message):
    return _orig_checkpoint(path, message.replace("Warm Enough", "Keel and Comb"))


w.checkpoint = checkpoint

_orig_summary = w.summary


def summary(text):
    return _orig_summary(text.replace("Warm Enough", "Keel and Comb"))


w.summary = summary


if __name__ == "__main__":
    sys.exit(w.main())
