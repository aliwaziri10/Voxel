#!/usr/bin/env python3
"""Kindling Line mechanical scan (token saver for proofreading).

Usage:  python3 scripts/kindling_scan.py 1      (book number 1, 2 or 3)
Fetches every chapter of that book from GitHub main into /tmp/kl_book<N>/ and prints one line per chapter that has a finding,
plus cross-chapter duplicate paragraphs and every chapter's last paragraph.
This is a MAP, not a proofread. A chapter is only stamped after it is READ in full (see novels/KINDLING_LINE_PROOFREAD_PROTOCOL.md).
"""
import sys, re, os, collections, urllib.request

book = sys.argv[1] if len(sys.argv) > 1 else "1"
base = f"https://raw.githubusercontent.com/aliwaziri10/Voxel/main/novels/kindling-line-book-{book}/chapters/chapter_"
out = f"/tmp/kl_book{book}"
os.makedirs(out, exist_ok=True)

texts = {}
for i in range(1, 46):
    n = f"{i:02d}"
    p = f"{out}/c{n}.md"
    if not os.path.exists(p):
        try:
            data = urllib.request.urlopen(f"{base}{n}.md").read().decode("utf-8")
        except Exception as e:
            print(f"c{n}: FETCH FAILED {e}")
            continue
        open(p, "w", encoding="utf-8").write(data)
    texts[n] = open(p, encoding="utf-8").read()

AI = (r"tapestry|testament to|underscore[sd]?|\bdelve|navigat(?:e|ing)|myriad|unwavering|poignant|resonat|robust|seamless|"
      r"\bboasts|elevate|harness|worth noting|in many ways|at its core|particular|\baye\b|the kind of|the specific")
if book == "3":
    AI += r"|Frostveil"   # Frostveil is a real month in Books 1 and 2 and banned only in Book 3

for n, t in texts.items():
    body = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    hdrs = re.findall(r"<!--.*?-->", t)
    f = []
    d = len(re.findall("[\u2014\u2013]", body))
    if d: f.append(f"dashes={d}")
    dbl = [m.group(0) for m in re.finditer(r"(?<!\.)\.\.(?!\.)|,,|, ,|\.,", body)]
    if dbl: f.append(f"punct={dbl[:3]}")
    g = len(re.findall(r"[^\n\s]---", body))
    if g: f.append(f"glued---={g}")
    leak = re.findall(r"\b(?:Ch\.|ch\.)\s?\d+|\bchapter \d+|BEAT|CANON|PROPOSED", body)
    if leak: f.append(f"LEAK={leak[:3]}")
    ai = collections.Counter(m.group(0).lower() for m in re.finditer(AI, body, flags=re.I))
    if ai: f.append(f"words={dict(ai)}")
    hed = len(re.findall(r"\b(?:something|someone|somewhere)\b", body, flags=re.I))
    if hed >= 8: f.append(f"hedges={hed}")
    held = len(re.findall(r"held (?:its|his|her|their) breath", body))
    if held > 1: f.append(f"held-breath={held}")
    paras = [p.strip() for p in body.split("\n") if len(p.strip()) > 60]
    dup = sum(1 for p, c in collections.Counter(paras).items() if c > 1)
    if dup: f.append(f"DUPLICATE-PARAGRAPHS={dup}")
    if len(hdrs) != 1: f.append(f"headers={len(hdrs)}")
    end = t.rstrip()[-1:]
    if end not in '.!?"*\u201d)': f.append("BAD-ENDING")
    if re.search(r"^#", t, flags=re.M): f.append("markdown-heading")
    words = len(body.split())
    print(f"c{n} {words}w", " ".join(f) if f else "clean")

print("== cross-chapter duplicate paragraphs (over 80 chars)")
seen = {}
for n, t in texts.items():
    for p in set(x.strip() for x in t.split("\n") if len(x.strip()) > 80):
        seen.setdefault(p, []).append(n)
for p, ns in seen.items():
    if len(ns) > 1:
        print(ns, p[:90])
print("== last paragraph of each chapter")
for n, t in texts.items():
    ps = [x.strip() for x in t.split("\n") if x.strip() and x.strip() != "---"]
    print(f"c{n}", ps[-1][:110])
