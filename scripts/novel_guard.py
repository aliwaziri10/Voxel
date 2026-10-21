#!/usr/bin/env python3
"""
novel_guard.py - deterministic checks and cleaners for AI-written novel chapters.

No network, no model, no cost. Used by scripts/write_novel.py (the OpenAI writer)
and runnable alone:

  python scripts/novel_guard.py --config novels/<book>/writer_config.json \
      --chapter novels/<book>/chapters/chapter_05.md --n 5

Every check here exists because of a real failure met while proofreading Voxel
books (Kindling Line Books 1-3, Proof of Home). The tag in brackets names the
failure it prevents. HARD findings mean "do not save this draft". SOFT findings
mean "retry, and if still present after the last try save it but flag it".

Nothing here rewrites the author's words. The only automatic repair is
normalize(), which changes characters, never wording.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NUMBER_WORDS = (
    "one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|"
    "fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|"
    "eighty|ninety|hundred|thousand|dozen|several|few|many|couple"
)
ORDINALS = "first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth"
TIME_UNITS = (
    "seconds?|minutes?|hours?|days?|nights?|weeks?|fortnights?|months?|years?|decades?|"
    "winters?|summers?|springs?|autumns?|falls?|seasons?"
)
MONTHS = ("January|February|March|April|June|July|August|September|October|November|December")
WEEKDAYS = "Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday"

# [Proof of Home ch.12, Kindling ch.25, ch.7-9: British spellings crept in from other models]
BRITISH = {
    "colour": "color", "colours": "colors", "coloured": "colored", "favour": "favor",
    "favourite": "favorite", "honour": "honor", "labour": "labor", "neighbour": "neighbor",
    "neighbours": "neighbors", "humour": "humor", "savour": "savor", "odour": "odor",
    "grey": "gray", "greying": "graying", "greyed": "grayed",
    "travelled": "traveled", "travelling": "traveling", "traveller": "traveler",
    "cancelled": "canceled", "levelled": "leveled", "labelled": "labeled",
    "modelled": "modeled", "marvelled": "marveled", "jewellery": "jewelry",
    "fibre": "fiber", "centre": "center", "metre": "meter", "metres": "meters",
    "theatre": "theater", "litre": "liter", "realise": "realize", "realised": "realized",
    "organise": "organize", "organised": "organized", "recognise": "recognize",
    "recognised": "recognized", "apologise": "apologize", "apologised": "apologized",
    "whilst": "while", "amongst": "among", "learnt": "learned", "spelt": "spelled",
    "towards": "toward", "afterwards": "afterward", "plough": "plow",
    "cosy": "cozy", "tyre": "tire", "kerb": "curb", "pyjamas": "pajamas",
    "sceptical": "skeptical", "defence": "defense", "offence": "offense",
    "licence": "license", "practise": "practice", "ageing": "aging", "storey": "story",
    "draught": "draft", "mould": "mold", "moulded": "molded", "smoulder": "smolder",
    "smouldering": "smoldering", "moustache": "mustache", "catalogue": "catalog",
    "programme": "program",
}
# Chicago/US: both are listed; the config picks which one is the standard.
GREY_GRAY = {"grey": "gray", "greying": "graying", "greyed": "grayed", "greyer": "grayer"}

# [Proof of Home, all Voxel books: planning words and tags leaked into the prose]
LEAK_PATTERNS = [
    r"\[(V|PROPOSED|UNSET|NOTE|TODO)[^\]]*\]", r"\bPROPOSED\b", r"\bUNSET\b",
    r"\bsub-?beat\b", r"\bbeat map\b", r"\bword count\b", r"\bPOV\b", r"\bprotagonist\b",
    r"\bEND OF CHAPTER\b", r"\[End of Chapter",
    r"(?i)\bhere is (the|your) (chapter|continuation)\b", r"(?i)^\s*(sure|certainly|of course)[,!. ]",
    r"\bWound:", r"\bCompetence:", r"\bHolds back:", r"\bEnds on:", r"\bEstablishes:",
]
# [Kindling: narrator wrote "chapter nine", "Book Two", "in this series"]
META_PATTERNS = [
    r"(?i)\bchapter\s+(\d+|%s|%s)\b" % (NUMBER_WORDS, ORDINALS),
    r"\bBook\s+(\d+|One|Two|Three|Four|Five)\b", r"(?i)\b(this|the) series\b",
    r"(?i)\bthe (reader|author|novel|story so far)\b",
]
# [Kindling: "first, second, third bell" given as hours; Book 2 wrong date math]
CLOCK_PATTERNS = [
    r"(?i)\b(%s) bell\b" % ORDINALS,
    r"\b\d{1,2}:\d{2}\b", r"(?i)\b\d{1,2}\s?(am|pm|a\.m\.|p\.m\.)\b", r"(?i)o'clock|o\u2019clock",
]
# [Book 2: wrong date math. Arithmetic must never appear on the page]
ARITHMETIC_PATTERNS = [
    r"(?i)\b(plus|minus|subtract(ed|ing)?|add(ed|ing)? up|adds up|sum of|total of|divided by|"
    r"multiplied by|twice as (many|much|long|old)|double(d)? the)\b",
    r"(?i)\b(%s) (less|more|fewer) than\b" % NUMBER_WORDS,
    r"(?i)\b(do|did|does|run|ran|working out) the (sum|math|maths|numbers|arithmetic|count)\b",
    r"(?i)\bcount(ed|ing)? (it )?(up|out|back)\b.{0,40}\b(%s)\b" % NUMBER_WORDS,
]
# Counted time: "three days", "forty years", "days later", "years ago".
COUNTED_TIME = [
    # number word + a span of a day or longer ("three weeks", "sixty years", "many months").
    # "one" is skipped for day/night/hour-sized spans because "one day" and "one night" are idiom.
    r"(?i)\b(?:(?:%s)|an? (?:few|couple of))\s+(?:more\s+|full\s+|long\s+|whole\s+)?(days|weeks?|fortnights?|months?|years?|decades?|winters|summers|springs|autumns|seasons)\b" % NUMBER_WORDS.replace("one|", ""),
    r"(?i)\bone\s+(week|fortnight|month|year|decade|season|winter|summer)\b",
    # "years ago", "days later" (plural span word on its own)
    r"(?i)\b(days|weeks|months|years|decades|seasons)\s+(later|ago|earlier|hence)\b",
    r"(?i)\b(%s)[- ](day|week|month|year)(s)?[- ]old\b" % NUMBER_WORDS,
    r"(?i)\b(%s)\s+years?\s+old\b" % NUMBER_WORDS,
    r"(?i)\b(%s) (week|month|year)\b" % ORDINALS,
]

# [LanguageTool pass: comma-free fillers; Voxel charter: banned tells]
DEFAULT_BANNED_WORDS = [
    r"particular", r"some", r"something", r"someone", r"somewhere", r"somebody", r"somehow",
    r"kind of", r"the specific", r"the kind of", r"one beat too long",
]
DEFAULT_STOCK = [
    "testament to", "tapestry", "unwavering", "woven", "seamless", "a dance of",
    "let out a breath she didn", "let out a breath he didn", "heart hammered", "shivers down",
    "orbs", "ministrations", "a mix of", "mixture of", "palpable", "electric", "something shifted",
    "the weight of", "etched", "bustling", "delve", "intricate", "sent a shiver",
]
STOP_REPEAT = set("""
about above after again against along also always another around because before behind below
between could every first found from have having here into just know like little might more
most never once only other over really right same should since still than that their them
then there these they thing things think this those through toward under until upon very want
were what when where which while with without would your hands hand eyes looked back down
""".split())

CURLY = {"\u201c": '"', "\u201d": '"', "\u2018": "'", "\u2019": "'"}


# ------------------------------------------------------------------ utils
def read(p):
    return Path(p).read_text(encoding="utf-8")


def words(text):
    return len(text.split())


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?\u201d])\s+", text) if s.strip()]


def squash(text):
    """lower-case words only, for phrase comparison across quote styles"""
    t = text.replace("\u2019", "'").replace("\u2018", "'")
    return re.findall(r"[a-z']+", t.lower())


def ngrams(toks, n):
    for i in range(len(toks) - n + 1):
        yield " ".join(toks[i:i + n])


# ------------------------------------------------------------------ cleaners
def normalize(text):
    """Character-level repair only. Never changes wording.
    [Proof of Home ch.1, 9: straight quotes. Rule 3: soft hyphens, zero-width characters]"""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    for ch in ("\u00ad", "\u200b", "\u200c", "\u200d", "\ufeff", "\u2060"):
        text = text.replace(ch, "")
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # double quotes
    out, prev = [], "\n"
    for ch in text:
        if ch == '"':
            out.append("\u201c" if (prev in " \n\t([\u2014\u2018" or prev == "\u2018") else "\u201d")
        elif ch == "'":
            if prev.isalnum():
                out.append("\u2019")          # apostrophe or closing single quote
            elif prev in " \n\t([\u201c":
                out.append("\u2018")          # opening single quote
            else:
                out.append("\u2019")
        else:
            out.append(ch)
        prev = out[-1]
    text = "".join(out)
    text = text.replace("...", "\u2026")
    return text.strip()


def clean_body(text, scene_break="***"):
    """Strip code fences, headings, title lines, html comments the model adds."""
    text = text.strip()
    text = re.sub(r"^```[a-z]*\n|\n```$", "", text)
    text = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.S)
    text = re.sub(r"(?m)^#{1,6}\s+.*\n+", "", text, count=1) if text.startswith("#") else text
    text = re.sub(r"^(Chapter\s+\w+[^\n]*)\n+", "", text)
    text = re.sub(r"(?m)^\s*(---+|\*\s?\*\s?\*|___+)\s*$", scene_break, text)
    return text.strip()


# ------------------------------------------------------------------ plan parsing
REQUIRED_KEYS = ["PLACE", "CAST", "PLOT", "WORLD", "LOCKED", "TIME", "INTERIOR",
                 "STAKES", "CALLBACK", "ESTABLISHES", "FIGURES", "ENDS ON"]


def parse_beat_file(text):
    """## CH.N | POV | time phrase   followed by KEY: value lines (PLOT may repeat)."""
    entries, cur = {}, None
    for ln in text.split("\n"):
        m = re.match(r"^##\s*CH\.?\s*(\d+)\s*\|\s*([^|]+?)\s*(?:\|\s*(.*))?$", ln)
        if m:
            cur = int(m.group(1))
            entries[cur] = {"pov": m.group(2).strip().upper(), "heading_time": (m.group(3) or "").strip(),
                            "lines": [], "keys": {}}
            continue
        if ln.startswith("#"):
            cur = None
            continue
        if cur is None or not ln.strip():
            continue
        entries[cur]["lines"].append(ln.rstrip())
        k = re.match(r"^([A-Z][A-Z /]+?):\s*(.*)$", ln.strip())
        if k:
            entries[cur]["keys"].setdefault(k.group(1).strip(), []).append(k.group(2).strip())
    return entries


def lint_entry(n, entry, min_lines=14):
    """The thick beat map rule (BEAT_MAP_PROTOCOL.md, Step 2)."""
    problems = []
    for key in REQUIRED_KEYS:
        if key not in entry["keys"] or not any(v for v in entry["keys"][key]):
            problems.append("missing %s:" % key)
    if len(entry["keys"].get("PLOT", [])) < 3:
        problems.append("PLOT: needs at least 3 lines of concrete plot")
    if len(entry["lines"]) < min_lines:
        problems.append("entry has %d lines, needs at least %d" % (len(entry["lines"]), min_lines))
    return problems


def figures_allowed(entry):
    raw = " ".join(entry["keys"].get("FIGURES", []))
    if not raw or raw.strip().lower().startswith("none"):
        return []
    return [f.strip().lower() for f in re.split(r"[;|]", raw) if f.strip()]


def echoes_allowed(entry):
    return [e.strip().strip('"\u201c\u201d').lower() for e in entry["keys"].get("ECHO", []) if e.strip()]


# ------------------------------------------------------------------ vocabulary
_VOCAB = None


def common_lowercase(extra_dirs=()):
    """Words seen in lower case anywhere in the repo's novels: a name is never
    written in lower case, so a capitalised token in this set is an ordinary word."""
    global _VOCAB
    if _VOCAB is None:
        cnt = Counter()
        dirs = list((ROOT / "novels").glob("*/chapters")) + [Path(d) for d in extra_dirs]
        for d in dirs:
            for p in sorted(Path(d).glob("*.md")):
                cnt.update(re.findall(r"\b[a-z]{3,}\b", read(p)))
        _VOCAB = set(cnt)
    return _VOCAB


def is_ordinary(tok, common):
    low = tok.lower()
    if low in common:
        return True
    for suf in ("s", "es", "ed", "d", "ing", "er", "ers", "ly", "ness"):
        if low.endswith(suf) and low[:-len(suf)] in common:
            return True
    if low.endswith("ies") and low[:-3] + "y" in common:
        return True
    return low.endswith(("body", "where", "selves", "self", "wire"))


# ------------------------------------------------------------------ the checks
def check(body, cfg, n, entry, earlier=None, vocab=None):
    """-> (hard, soft). `earlier` = {chapter_no: text} of the SAME book, chapters < n."""
    earlier = earlier or {}
    hard, soft = [], []
    wmin, wmax = cfg.get("words_min", 2300), cfg.get("words_max", 2700)
    whard = cfg.get("words_hard_min", 1800)
    nw = words(body)
    if nw < whard:
        hard.append("only %d words (a chapter must reach %d)" % (nw, wmin))
    elif nw < wmin or nw > wmax:
        soft.append("%d words (target %d to %d)" % (nw, wmin, wmax))
    if body and body[-1] not in ".!?\u201d\u2019\u2026*)":
        hard.append("the chapter looks cut off (ends with %r)" % body[-20:])

    # [Proof of Home ch.5: planning notes pasted into prose; Kindling: tags]
    for pat in LEAK_PATTERNS:
        m = re.search(pat, body, re.M)
        if m:
            hard.append("planning or assistant text leaked into the prose: %r" % m.group(0))
    for pat in META_PATTERNS:
        m = re.search(pat, body)
        if m:
            hard.append("the narrator mentions the book machinery: %r" % m.group(0))
    if re.search(r"(?m)^\s*#{1,6}\s", body) or "**" in body.replace(cfg.get("scene_break", "***"), ""):
        hard.append("markdown heading or bold marker in the prose")
    if re.search(r"(?m)^\s*(Scene|Part|Section|Act)\b[^\n]{0,30}$", body):
        hard.append("a scene or section label line (use only %s)" % cfg.get("scene_break", "***"))

    # [Zia: avoid dates and mathematical calculations. Proof of Home: no digits, no weekdays]
    if re.search(r"\d", body):
        hard.append("a digit appears in the prose (write every number as a word, and avoid figures not in FIGURES)")
    for pat, label in ((r"\b(%s)\b" % MONTHS, "a real month name"), (r"\b(%s)\b" % WEEKDAYS, "a weekday name")):
        m = re.search(pat, body)
        if m:
            hard.append("%s: %r (time is told by season, light, weather)" % (label, m.group(0)))
    for mon in cfg.get("calendar_words", []):
        if re.search(r"\b%s\b" % re.escape(mon), body):
            hard.append("a calendar word the book never writes: %s" % mon)
    if re.search(r"\b(year|years)\s+(one|two|three|four|five|six|seven|eight|nine|ten)\b|\bYear\s+\d+", body, re.I):
        hard.append("a numbered year is written")
    for pat in CLOCK_PATTERNS:
        m = re.search(pat, body)
        if m:
            hard.append("a clock time or a bell given as an hour: %r" % m.group(0))
    for pat in ARITHMETIC_PATTERNS:
        m = re.search(pat, body)
        if m:
            hard.append("arithmetic on the page: %r (state the result the entry gives, never the sum)" % m.group(0))
    allowed = figures_allowed(entry) + [a.lower() for a in cfg.get("always_allowed_figures", [])]
    time_phrase = (" ".join(entry["keys"].get("TIME", [])) + " " + entry.get("heading_time", "")).lower()
    for pat in COUNTED_TIME:
        for m in re.finditer(pat, body):
            phrase = m.group(0).lower()
            if any(a in phrase or phrase in a for a in allowed) or phrase in time_phrase:
                continue
            hard.append("a counted span of time or an age not allowed by this chapter's FIGURES: %r" % m.group(0))
    for bad in cfg.get("wrong_variants", []):
        if re.search(re.escape(bad), body, re.I):
            hard.append("a known wrong version of a canon fact: %r" % bad)

    # [Kindling: invented names, banned names/terms]
    for t in cfg.get("banned_terms", []):
        if t.lower() in body.lower():
            hard.append("banned term: %s" % t)
    for nm in cfg.get("banned_names", []):
        if re.search(r"\b%s\b" % re.escape(nm), body):
            hard.append("banned name: %s" % nm)
    hard.extend(unknown_names(body, cfg, vocab))

    # [Proof of Home ch.5, 11, 13: point of view slips; baking comparisons in Jack's chapters]
    pov = entry["pov"]
    povcfg = cfg.get("povs", {}).get(pov)
    if povcfg:
        for other in povcfg.get("other_names", []):
            for m in re.finditer(r"(?:(?<=[.!?\u201d\u201c] )|(?<=\n)|(?<=, and )|(?<=, but )|(?<=and )|(?<=but )|^)%s\s+"
                                 r"(thought|wondered|realized|knew|felt|wanted|decided|hoped|feared|remembered|understood)\b(?! aloud| out loud)"
                                 % re.escape(other), body):
                hard.append("point of view slip, a thought given to %s: %r" % (other, body[m.start():m.end() + 25].replace("\n", " ")))
                break
        for w in povcfg.get("banned_metaphor_words", []):
            m = re.search(r"(?i)\b(like|as if|as though|the way|as \w+ as|reminded (him|her) of)\b[^.!?]{0,70}\b%s\w*\b" % re.escape(w), body)
            if m:
                hard.append("metaphor domain leak into %s's chapter (a comparison drawn from the other lead's trade): %r" % (pov, m.group(0)[:80]))
        for w in povcfg.get("never_words", []):
            m = re.search(r"(?i)\b%s\w*\b" % re.escape(w), body)
            if m:
                hard.append("word never used in %s's chapters: %r" % (pov, m.group(0)))

    # [Kindling ch.8, 26; Proof of Home ch.25 vs 27: pasted-twice blocks, duplicated scenes, looping text]
    hard.extend(duplication(body, earlier, echoes_allowed(entry), cfg.get("loop_ngram", 9), cfg.get("copy_ngram", 12)))

    # [Book 2: locked line repeated; once-only beats]
    low = " ".join(squash(body))
    for lk in cfg.get("locked_lines", []):
        phrase = " ".join(squash(lk["text"]))
        if phrase and phrase in low and lk["chapter"] != n:
            hard.append("a once-only line belongs to chapter %d only: %r" % (lk["chapter"], lk["text"][:50]))
    for lk in cfg.get("locked_lines", []):
        phrase = " ".join(squash(lk["text"]))
        if lk["chapter"] == n and phrase and phrase not in low:
            soft.append("this chapter's once-only line is missing: %r" % lk["text"][:50])

    # quotes balance [Proof of Home ch.22-23: question marks, quote slips]
    if body.count("\u201c") != body.count("\u201d"):
        hard.append("unbalanced double quotes (%d open, %d close)" % (body.count("\u201c"), body.count("\u201d")))
    if re.search(r"[\"']", body):
        hard.append("straight quotes remain (normalize failed)")

    # spelling standard [Proof of Home ch.12, 16; Kindling grey]
    std = cfg.get("spelling", "american")
    for brit, us in BRITISH.items():
        if brit in ("grey", "greying", "greyed", "dialogue"):
            continue
        if re.search(r"\b%s\b" % brit, body, re.I):
            hard.append("%s spelling standard: found %r (use %r)" % (std, brit, us))
    gg = cfg.get("grey_or_gray", "gray")
    wrong = "grey" if gg == "gray" else "gray"
    if re.search(r"\b%s\w*\b" % wrong, body, re.I):
        hard.append("this book spells %r, found %r" % (gg, wrong))

    # soft: tells
    banned = cfg.get("banned_words", DEFAULT_BANNED_WORDS)
    style = Counter()
    for pat in banned:
        for m in re.finditer(r"\b%s\b" % pat, body, re.I):
            style[m.group(0).lower()] += 1
    for ph in cfg.get("stock_phrases", DEFAULT_STOCK):
        for m in re.finditer(re.escape(ph), body, re.I):
            style[m.group(0).lower()] += 1
    if style:
        soft.append("banned or stock words: " + ", ".join("%s x%d" % kv for kv in style.most_common()))
    dashes = body.count("\u2014") + body.count("\u2013")
    if dashes:
        soft.append("%d em or en dashes (use a comma, a full stop or a colon)" % dashes)
    if re.search(r"\w - \w", body):
        soft.append("a spaced hyphen standing in for a dash")
    castlow = {w.lower() for name in cfg.get("cast", []) for w in name.split()}
    toks = [w for w in squash(body) if len(w) >= 5 and w not in STOP_REPEAT and w not in castlow]
    heavy = [(w, c) for w, c in Counter(toks).most_common(12) if c >= cfg.get("repeat_limit", 8)]
    if heavy:
        soft.append("overused words (eight or more): " + ", ".join("%s x%d" % x for x in heavy))
    # [Charter: sentence length variance]
    lens = [words(s) for s in sentences(body)]
    if len(lens) > 20:
        mean = sum(lens) / len(lens)
        sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5
        if sd < cfg.get("min_sentence_sd", 5.0):
            soft.append("sentence lengths are too even (sd %.1f); vary the rhythm" % sd)
    return hard, soft


def unknown_names(body, cfg, vocab=None):
    """[Kindling ch.13 'Master Hender': invented person]"""
    allowed = set(cfg.get("cast", [])) | set(cfg.get("world_words", [])) | {"Scene", "Part", "Section", "Act"}
    allowed |= {w for name in cfg.get("cast", []) for w in name.split()}
    common = vocab if vocab is not None else common_lowercase()
    seen = {}
    for m in re.finditer(r"\b[A-Z][a-z]{2,}\b", body):
        tok = m.group(0)
        if tok in allowed or is_ordinary(tok, common):
            continue
        before = body[:m.start()].rstrip(" \t\u201c\"'\u2018*_(")
        at_start = before == "" or before[-1] in ".!?:\n\u2026"
        if at_start and tok.lower().endswith(("ly", "ing", "ed", "ness", "ion", "ous", "ive", "ful", "less", "ment", "ity", "ward", "wards")):
            continue
        rec = seen.setdefault(tok, [0, 0, ""])
        rec[0] += 1
        if not at_start:
            rec[1] += 1
        if not rec[2]:
            rec[2] = body[max(0, m.start() - 25):m.end() + 25].replace("\n", " ")
    bad = {t: r for t, r in seen.items() if r[1] >= 1 or r[0] >= 2}
    if not bad:
        return []
    items = sorted(bad.items(), key=lambda kv: -kv[1][0])[:12]
    return ["names or capitalised words not on the cast list: "
            + "; ".join("%s (x%d, e.g. \"...%s...\")" % (t, r[0], r[2]) for t, r in items)]


def mask_echoes(toks, echoes):
    """Replace every planned echo phrase with filler tokens so it is never counted as a copy."""
    if not echoes:
        return toks
    text = " " + " ".join(toks) + " "
    for e in echoes:
        et = " ".join(squash(e))
        if et:
            text = text.replace(" " + et + " ", " " + " ".join("_%d" % i for i in range(len(et.split()))) + " ")
    return text.split()


def duplication(body, earlier, echoes, n=9, cross=12):
    out = []
    paras = [p.strip() for p in body.split("\n\n") if len(p.split()) >= 12]
    dup = [p for p, c in Counter(paras).items() if c > 1]
    if dup:
        out.append("a paragraph is pasted twice in this chapter: %r" % dup[0][:60])
    toks = mask_echoes(squash(body), echoes)
    rep = [g for g, c in Counter(ngrams(toks, n)).items() if c > 1 and "_" not in g]
    if rep:
        out.append("text repeats inside the chapter (a loop or a pasted block): %r" % rep[0])
    cgrams = {g for g in ngrams(toks, cross) if "_" not in g}
    for num, text in sorted(earlier.items()):
        prev = set(ngrams(mask_echoes(squash(text), echoes), cross))
        hit = [g for g in cgrams if g in prev]
        if hit:
            out.append("copies text from chapter %d: %r (a once-only line or a duplicated scene; "
                       "list it under ECHO: only if the plan wants the echo)" % (num, hit[0]))
            break
    return out


# ------------------------------------------------------------------ cli
def load_config(path):
    cfg = json.loads(read(path))
    cfg["_dir"] = str(Path(path).resolve().parent)
    return cfg


def main():
    ap = argparse.ArgumentParser(description="Run the Voxel novel checks on one existing chapter.")
    ap.add_argument("--config", required=True)
    ap.add_argument("--chapter", required=True)
    ap.add_argument("--n", type=int, required=True)
    args = ap.parse_args()
    cfg = load_config(args.config)
    book = Path(cfg["_dir"])
    beat = parse_beat_file(read(book / cfg.get("beat_file", "beat_map.md")))
    entry = beat.get(args.n)
    if not entry:
        print("no entry for chapter %d in the beat file" % args.n)
        return 2
    earlier = {}
    for p in sorted((book / "chapters").glob("chapter_*.md")):
        k = int(re.search(r"(\d+)", p.name).group(1))
        if k < args.n:
            earlier[k] = read(p)
    body = normalize(clean_body(read(args.chapter), cfg.get("scene_break", "***")))
    hard, soft = check(body, cfg, args.n, entry, earlier)
    print("words:", words(body))
    print("HARD:", hard or "none")
    print("SOFT:", soft or "none")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
