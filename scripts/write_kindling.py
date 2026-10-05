#!/usr/bin/env python3
"""
write_kindling.py - strict, chapter-by-chapter writer for Kindling Line Book 3.

Why this exists: voxel_cli.py novel plans its own beat map and never reads the
Book 3 canon lock, beat maps, romance scenes or the real text of the previous
chapter. That is the drift recipe BEAT_MAP_PROTOCOL.md describes. This script
feeds the model exactly the repo files the plan is made of, one chapter at a
time, in strict order, then checks the result mechanically before saving.

Per chapter the model receives: WRITER_COMMAND.md (system), CANON_LOCK.md, the
batch rules and state, that chapter's romance scene and plot entry, the real
text of the previous chapter (Book 2 ch.45 for chapter 1) and a short voice
sample. Nothing else.

Checks. HARD failures are never saved: a name not on the cast, banned terms or
names, editor tags, month names, years, bells as hours, chapter or book
references, a cut-off or far too short chapter. SOFT findings (style words,
dashes, word range) are retried, and if only soft findings remain after the last
try the chapter is saved and listed in the report for the editor.
Strict order: chapter N is only written if chapter N-1 exists. Existing chapters
are kept unless --force. The workflow commits each chapter as it is written.

Model: OPENAI_API_KEY + OPENAI_MODEL if both are set, otherwise the repo's own
content_provider (NVIDIA / OpenRouter keys, same as voxel-novel.yml).

Usage:
  python scripts/write_kindling.py --start 1 --end 5
  python scripts/write_kindling.py --start 1 --end 1 --dry-run
  python scripts/write_kindling.py --check novels/kindling-line-book-2/chapters/chapter_45.md
"""
import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BOOK = "novels/kindling-line-book-3"
B2_CHAPTERS = ROOT / "novels" / "kindling-line-book-2" / "chapters"
B1_CHAPTERS = ROOT / "novels" / "kindling-line-book-1" / "chapters"

MIN_HARD_WORDS = 1800
MIN_WORDS, MAX_WORDS = 2300, 2700
SINGLE_CALL = False  # set by --single

# Closed cast (CANON_LOCK section 6 and THREAD_LEDGER) plus world words that are
# legitimately capitalised. Anything else capitalised and not an everyday word is
# treated as an invented name.
ALLOWED = set("""
Sol Isolde Vane Vanes Kael Ashworth Ashworths Malrik Thorne Thornes Aldous Ansa Tam
Corren Joren Mara Renn Ulla Odo Marl Tessa Rook Bram Yelva Corwin Ingrith Tenn Ferra
Auda Valerius Varel Wenna Tobin Farrow Dessa Cinderveil Lady Lord Chancellor Council
Kindling Reckoning Deed Instrument Dissolution Reach Lower Spine Anchor Seven Records
Corrin Accord Auditor Tar Lane Ropewalk Standard Hold Schedule Day Lanes
""".split())

BANNED_NAMES = """Marius Hale Cressida Hest Veyra Veldt Mirelle Voss Merrow Elsbeth Hestor
Varrick Helseth Dallin Vorys Xanthe Emberfall Frostveil Sunspire""".split()

BANNED_TERMS = [
    "Contract of Perpetual Surety", "Deep Vault", "Keeper of the Burning Ledger",
    "Accord Hall", "Great Hall", "Grand Auditor", "Nine Houses", "inquiry board",
    "Tripartite Seal", "Founding Council", "Consultant", "the Compact", "the annex",
]

STYLE_PATTERNS = [
    r"\bparticular\b", r"\bsome\b", r"\bsomething\b", r"\bsomeone\b", r"\bsomewhere\b",
    r"\bsomebody\b", r"\bsomehow\b", r"\bkind of\b", r"\bthe specific\b", r"\bgray\b",
    r"\btestament to\b", r"\btapestry\b", r"\bunwavering\b", r"\bwoven\b", r"\bseamless",
]

ORDINALS = "first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth"


def words(text):
    return len(text.split())


def read(p):
    return Path(p).read_text(encoding="utf-8")


# ---------- parsing the plan files ----------

def parse_beat_file(text):
    """-> (header_block, {chapter: entry_text}, writer_notes)"""
    header, entries, notes = [], {}, []
    cur, buf, note_mode = None, [], False
    for ln in text.split("\n"):
        m = re.match(r"^## CH\.(\d+)\b", ln)
        is_heading = ln.startswith("# ") or ln.startswith("## ")
        if m:
            if cur is not None:
                entries[cur] = "\n".join(buf).strip()
            cur, buf, note_mode = int(m.group(1)), [ln], False
        elif is_heading and cur is not None:
            entries[cur] = "\n".join(buf).strip()
            cur, buf = None, []
            note_mode = bool(re.search(r"NOTES FOR THE WRITER", ln, re.I))
            if note_mode:
                notes.append(ln)
        elif is_heading and entries:
            note_mode = bool(re.search(r"NOTES FOR THE WRITER", ln, re.I))
            if note_mode:
                notes.append(ln)
        elif cur is not None:
            buf.append(ln)
        elif note_mode:
            notes.append(ln)
        elif not entries:
            header.append(ln)
    if cur is not None:
        entries[cur] = "\n".join(buf).strip()
    return "\n".join(header).strip(), entries, "\n".join(notes).strip()


def find_plot(book, n):
    names = ["BEAT_MAP_BATCH%d.md" % i for i in range(4, 10)] + ["BEAT_MAP.md"]
    for name in names:
        p = book / name
        if not p.exists():
            continue
        header, entries, _ = parse_beat_file(read(p))
        if n in entries:
            return entries[n], (header if name != "BEAT_MAP.md" else ""), name
    return None, "", ""


def find_romance(book, n):
    for i in range(1, 10):
        p = book / ("ROMANCE_BATCH%d.md" % i)
        if not p.exists():
            continue
        _, entries, notes = parse_beat_file(read(p))
        if n in entries:
            return entries[n], notes
    return None, ""


def day_label(plot_entry):
    first = plot_entry.split("\n", 1)[0]
    m = re.search(r"\bDay \d+\b", first)
    if m:
        return m.group(0)
    if re.search(r"season later", first, re.I):
        return "A season later"
    return None


def pov_of(plot_entry):
    first = plot_entry.split("\n", 1)[0].upper()
    if "| SOL |" in first:
        return "SOL"
    if "| KAEL |" in first:
        return "KAEL"
    return None


# ---------- previous text and voice sample ----------

def chapter_path(book, n):
    return book / "chapters" / ("chapter_%02d.md" % n)


def previous_text(book, n):
    if n == 1:
        return read(B2_CHAPTERS / "chapter_45.md"), "Book 2, last chapter (the same night)"
    p = chapter_path(book, n - 1)
    if not p.exists():
        raise SystemExit("STOP: chapter %d does not exist yet. Chapters are written in strict order." % (n - 1))
    return read(p), "chapter %d" % (n - 1)


def voice_sample(book, n):
    if n >= 3 and chapter_path(book, n - 2).exists():
        p = chapter_path(book, n - 2)
    elif n == 2:
        p = B2_CHAPTERS / "chapter_45.md"
    else:
        p = B2_CHAPTERS / "chapter_44.md"
    body = re.sub(r"^<!--.*?-->\s*", "", read(p), flags=re.S)
    return " ".join(body.split()[:700])


# ---------- prompt ----------

def build_prompt(book, n, plot, header, romance, notes, prev, prev_label, sample, next_heading):
    canon = read(book / "CANON_LOCK.md")
    parts = [
        "=== CANON LOCK (authority 1; bracket tags are notes for you, never write them) ===\n" + canon,
        "=== BATCH RULES AND STATE (authority 2) ===\n"
        + (header if header else "(no separate batch rules for this chapter; the HARD RULES in your instructions apply)"),
        "=== ROMANCE SCENE FOR CHAPTER %d (opens the chapter, at least a quarter of it) ===\n%s%s"
        % (n, romance, ("\n\n" + notes) if notes else ""),
        "=== PLOT ENTRY FOR CHAPTER %d ===\n%s" % (n, plot),
        "=== NEXT CHAPTER (do NOT cover it; end at this chapter's last beat) ===\n"
        + (next_heading or "(this is the last chapter)"),
        "=== REAL TEXT OF THE PREVIOUS CHAPTER (%s). This has already happened. Continue straight from its last moment. ===\n%s"
        % (prev_label, prev),
        "=== VOICE SAMPLE (rhythm and tone only; do not reuse its events or lines) ===\n" + sample,
        "Write chapter %d now, following every HARD RULE. Output only the chapter prose." % n,
    ]
    return "\n\n".join(parts)


# ---------- the model ----------

def call_model(system, user):
    import os
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    model = os.environ.get("OPENAI_MODEL", "").strip()
    if key and model:
        import requests
        r = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
            json={"model": model,
                  "messages": [{"role": "system", "content": system},
                               {"role": "user", "content": user}],
                  "max_completion_tokens": 9000},
            timeout=600)
        r.raise_for_status()
        choice = r.json()["choices"][0]
        if choice.get("finish_reason") == "length":
            raise RuntimeError("model reply was cut off at its length limit")
        return choice["message"]["content"]
    sys.path.insert(0, str(ROOT))
    import content_provider
    return content_provider.call_raw(system, user, timeout=300)


# ---------- checks ----------

_COMMON = None


def call_chapter(system, user):
    """The model returns about 1,000 to 1,500 words per call, so each chapter
    is written in two calls: first half, then second half continuing from the
    real first-half text. Falls back to one call if --single is set."""
    if SINGLE_CALL:
        return call_model(system, user)
    first = clean_body(call_model(system, user + (
        "\n\nWRITE ONLY THE FIRST HALF OF THE CHAPTER NOW: about 1,300 words, from the opening "
        "up to roughly the middle of the plan. Stop at a natural beat in the middle of the chapter. "
        "Do NOT wrap up, do NOT write the chapter's ending, no title or heading line.")))
    second = clean_body(call_model(system, user + (
        "\n\nTHE FIRST HALF OF THIS CHAPTER IS ALREADY WRITTEN (below). Write ONLY THE SECOND HALF now: "
        "about 1,300 words, continuing exactly from its last line, through the rest of the plan to the "
        "chapter's closing beat. Do not repeat, summarise or rewrite the first half. No title or heading line.\n\n"
        "=== FIRST HALF (already written) ===\n" + first)))
    return first + "\n\n" + second


def common_lowercase():
    """Words that appear in lower case at least once in Books 1 and 2. A name is
    never written in lower case, so a capitalised word in this set (or a simple
    inflection of one, see is_ordinary) is an ordinary word."""
    global _COMMON
    if _COMMON is None:
        cnt = Counter()
        for d in (B1_CHAPTERS, B2_CHAPTERS):
            for p in sorted(d.glob("chapter_*.md")):
                cnt.update(re.findall(r"\b[a-z]{3,}\b", read(p)))
        _COMMON = {w for w, c in cnt.items() if c >= 1}
    return _COMMON


def is_ordinary(tok, common):
    """True if a capitalised token is an everyday word (plural, -ed, -ing, -ly,
    compounds like Everybody / Elsewhere / Ourselves), not an invented name."""
    low = tok.lower()
    if low in common:
        return True
    for suf in ("s", "es", "ed", "d", "ing", "er", "ers", "ly"):
        if low.endswith(suf) and low[:-len(suf)] in common:
            return True
    if low.endswith("ies") and low[:-3] + "y" in common:
        return True
    return low.endswith(("body", "where", "selves", "self", "wire"))


def length_gap(text):
    """How far a draft is outside the word target (0 if inside)."""
    n = words(text)
    if MIN_WORDS <= n <= MAX_WORDS:
        return 0
    return min(abs(n - MIN_WORDS), abs(n - MAX_WORDS))


def clean_body(text):
    text = text.strip()
    text = re.sub(r"^```[a-z]*\n|\n```$", "", text)
    text = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.S)
    text = re.sub(r"^(#+\s*)?(Chapter\s+\w+[^\n]*)\n+", "", text)
    return text.strip()


def check(body):
    """-> (hard_list, soft_list)"""
    hard, soft = [], []
    n_words = words(body)
    if n_words < MIN_HARD_WORDS:
        hard.append("only %d words (a chapter must reach about 2,300)" % n_words)
    elif n_words < MIN_WORDS or n_words > MAX_WORDS:
        soft.append("%d words (target %d to %d)" % (n_words, MIN_WORDS, MAX_WORDS))
    if body and body[-1] not in ".!?\"'\u201d\u2019*_)":
        hard.append("the chapter looks cut off (it ends with %r)" % body[-20:])

    for t in BANNED_TERMS:
        if t.lower() in body.lower():
            hard.append("banned term: %s" % t)
    for nm in BANNED_NAMES:
        if re.search(r"\b%s\b" % re.escape(nm), body):
            hard.append("banned name or month: %s" % nm)
    if re.search(r"\[(V|PROPOSED|UNSET)[^\]]*\]|\bPROPOSED\b|\bUNSET\b", body):
        hard.append("a planning tag leaked into the prose")
    if re.search(r"\bYear\s+(\d+|[A-Z][a-z]+)\b", body):
        hard.append("a year is written (Book 3 states no year)")
    if re.search(r"\b(%s) bell\b" % ORDINALS, body, re.I):
        hard.append("a bell is given as an hour")
    m_ch = re.search(r"\bchapter\s+(\d+|(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth)\b)", body, re.I)
    if m_ch:
        hard.append("a chapter number is referred to in the prose: %r (remove it; the narrator never mentions chapters)" % m_ch.group(0))
    m_ref = re.search(r"\bBook\s+(\d+|One|Two|Three|Four)\b|\bprotagonist\b|\b(?:this|the) series\b", body)
    if m_ref:
        hard.append("a book, series or protagonist reference: %r (remove it; the narrator never mentions books)" % m_ref.group(0))
    m_lab = re.search(r"(?m)^\s*[*_#]*\s*(Scene|Part|Section|Act)\b[^\n]{0,30}$", body)
    if m_lab:
        hard.append("a scene or section label line in the prose: %r (use a blank line or *** only)" % m_lab.group(0).strip())
    if re.search(r"\b\d+\s*(feet|foot|metres|meters|yards)\b", body, re.I):
        hard.append("a radius or distance in feet or metres")

    common = common_lowercase()
    seen = {}  # token -> [total count, mid-sentence count, first context]
    for m_tok in re.finditer(r"\b[A-Z][a-z]{2,}\b", body):
        tok = m_tok.group(0)
        if tok in ALLOWED or tok in ("Scene", "Part", "Section", "Act") or is_ordinary(tok, common):
            continue
        before = body[:m_tok.start()].rstrip(" \t\u201c\"'\u2018*_(")
        at_start = before == "" or before[-1] in ".!?:\n"
        if at_start and tok.lower().endswith(("ly", "ing", "ed", "ness", "ion", "ous", "ive", "ful", "less", "ment", "ity", "ward", "wards")):
            continue
        rec = seen.setdefault(tok, [0, 0, ""])
        rec[0] += 1
        if not at_start:
            rec[1] += 1
        if not rec[2]:
            rec[2] = body[max(0, m_tok.start() - 25):m_tok.end() + 25].replace("\n", " ")
    # A word only at a sentence start, once, is treated as an ordinary word.
    # It fails if it appears mid-sentence or at least twice.
    unknown = {t: r for t, r in seen.items() if r[1] >= 1 or r[0] >= 2}
    if unknown:
        items = sorted(unknown.items(), key=lambda kv: -kv[1][0])[:12]
        hard.append("names or capitalised words not on the cast: "
                    + "; ".join("%s (x%d, e.g. \"...%s...\")" % (t, r[0], r[2]) for t, r in items))

    style = Counter()
    for pat in STYLE_PATTERNS:
        for m in re.finditer(pat, body, re.I):
            style[m.group(0).lower()] += 1
    if style:
        soft.append("style words: " + ", ".join("%s x%d" % kv for kv in style.most_common()))
    dashes = body.count("\u2014") + body.count("\u2013")
    if dashes:
        soft.append("%d em or en dashes" % dashes)
    return hard, soft


# ---------- git ----------

def checkpoint(path, message):
    try:
        subprocess.run(["git", "add", str(path)], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "pull", "--rebase", "-q"], check=False)
        subprocess.run(["git", "push", "-q"], check=True)
        print("[kindling]   committed and pushed: %s" % message)
    except subprocess.CalledProcessError as e:
        print("[kindling]   WARNING: commit or push failed (%s). The file is saved on the runner." % e)


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book-dir", default=DEFAULT_BOOK)
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--end", type=int, default=5)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--checkpoint", action="store_true")
    ap.add_argument("--max-tries", type=int, default=3)
    ap.add_argument("--single", action="store_true", help="one model call per chapter instead of two halves")
    ap.add_argument("--check", help="run the checks on one existing file and exit")
    args = ap.parse_args()
    global SINGLE_CALL
    SINGLE_CALL = args.single

    if args.check:
        body = clean_body(read(args.check))
        hard, soft = check(body)
        print("words:", words(body))
        print("HARD:", hard or "none")
        print("SOFT:", soft or "none")
        return 0

    book = ROOT / args.book_dir
    system = read(book / "WRITER_COMMAND.md")
    (book / "chapters").mkdir(parents=True, exist_ok=True)
    report = []

    for n in range(args.start, args.end + 1):
        path = chapter_path(book, n)
        if path.exists() and path.read_text(encoding="utf-8").strip() and not args.force:
            print("[kindling] chapter %d already exists, keeping it" % n)
            continue
        plot, header, src = find_plot(book, n)
        romance, notes = find_romance(book, n)
        if not plot or not romance:
            raise SystemExit("STOP: chapter %d is missing its %s entry in the plan files."
                             % (n, "plot" if not plot else "romance"))
        day = day_label(plot)
        pov = pov_of(plot)
        if day is None or pov is None:
            raise SystemExit("STOP: could not read the day or point of view from chapter %d's plot heading." % n)
        if (pov == "SOL") != (n % 2 == 1):
            raise SystemExit("STOP: chapter %d heading says %s but odd chapters are Sol and even are Kael." % (n, pov))
        nxt_plot, _, _ = find_plot(book, n + 1)
        next_heading = nxt_plot.split("\n", 1)[0] if nxt_plot else None
        prev, prev_label = previous_text(book, n)
        sample = voice_sample(book, n)
        user = build_prompt(book, n, plot, header, romance, notes, prev, prev_label, sample, next_heading)
        print("[kindling] chapter %d | %s | %s | plot from %s | prompt %d words"
              % (n, pov, day, src, words(system) + words(user)))
        if args.dry_run:
            print(user[:1500])
            print("... [dry run, no model call]")
            continue

        feedback, best, best_soft = "", None, None
        saved = False
        for attempt in range(1, args.max_tries + 1):
            msg = user + (("\n\nYOUR PREVIOUS DRAFT WAS REJECTED. Write the whole chapter again from the start and fix exactly these problems:\n" + feedback) if feedback else "")
            try:
                raw = call_chapter(system, msg)
            except Exception as e:
                print("[kindling]   model call failed on try %d: %s" % (attempt, e))
                continue
            body = clean_body(raw)
            hard, soft = check(body)
            print("[kindling]   try %d: %d words, hard=%d soft=%d" % (attempt, words(body), len(hard), len(soft)))
            for h in hard:
                print("[kindling]     HARD: " + h)
            for s in soft:
                print("[kindling]     soft: " + s)
            if not hard:
                # keep the clean draft closest to the word target (ties: fewer soft findings)
                if (best is None or length_gap(body) < length_gap(best)
                        or (length_gap(body) == length_gap(best) and len(soft) <= len(best_soft))):
                    best, best_soft = body, soft
                if not soft:
                    break
            feedback = "\n".join("- " + x for x in hard + soft)
        if best is None:
            print("[kindling] chapter %d NOT saved: still broken after %d tries. Stopping (strict order)." % (n, args.max_tries))
            report.append((n, "NOT SAVED", hard))
            break
        text = "<!-- chapter_date: %s -->\n\n%s\n" % (day, best)
        path.write_text(text, encoding="utf-8")
        print("[kindling]   saved %s (%d words)" % (path.relative_to(ROOT), words(best)))
        report.append((n, "saved", best_soft))
        if args.checkpoint:
            checkpoint(path, "Kindling Line Book 3: chapter %d (%d words)" % (n, words(best)))

    print("\n[kindling] REPORT")
    flagged = False
    for n, status, items in report:
        print("  chapter %d: %s%s" % (n, status, ("  | " + "; ".join(items)) if items else ""))
        flagged = flagged or status != "saved"
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
