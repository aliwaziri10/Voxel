"""Mechanical checker for Keel and Comb chapters.

Usage: python3 -I check_chapter.py chapter_NN.md
Copy it to a work folder first; do not run Python from inside a folder of downloaded files.
It reports: word count, dashes, digits, banned words, banned-name substrings, filler words,
stock and tell phrases, planning words, ordinary words used 8 or more times, similes,
sentence-length spread, anaphora, paragraph lengths. It does not replace the manual read.
"""
import re
import statistics
import sys
from collections import Counter

path = sys.argv[1]
text = open(path, encoding="utf-8").read()
first, body = text.split("\n", 1)
words = re.findall(r"[A-Za-z']+", body)
lower = [w.lower() for w in words]

print("words:", len(body.split()))
print("em dashes:", text.count("—"), "en dashes:", text.count("–"))
print("digits in body:", len(re.findall(r"\d", body)))

banned = ["some", "something", "someone", "somewhere", "somehow", "somebody", "particular", "kind"]
print("banned words:", {w: lower.count(w) for w in banned if lower.count(w)})
print("the specific / the kind of:", len(re.findall(r"\bthe specific\b|\bthe kind of\b|\bkind of\b", body, re.I)))

names = ["wren", "pell", "bram", "hale", "oakes", "corrin", "voss", "marius", "mara", "renn",
         "jack", "nell", "sarah", "odalys", "fenna", "gideon", "teague", "mercer", "quill",
         "pike", "hester", "ansel", "tilda", "mina", "piers", "dunstan", "ostler", "winifred"]
low = body.lower()
print("banned-name substrings:", {n: low.count(n) for n in names if n in low})

filler = ["nice", "good", "great", "bad", "thing", "stuff", "big", "small", "lovely", "beautiful",
          "wonderful", "amazing", "very", "really", "just", "quite", "suddenly", "seemed", "felt",
          "looked", "moved", "went", "got", "came"]
print("filler words:", {w: lower.count(w) for w in filler if lower.count(w)})

stock = ["something shifted", "breath she didn't know", "heart hammered", "shivers", "orbs",
         "ministrations", "palpable", "electric", "etched", "bustling", "a mix of", "the weight of",
         "woven", "tapestry", "testament", "unwavering", "seamless", "intricate", "delve", "dance of",
         "the air between", "hung between", "for the first time in years", "time seemed",
         "world narrowed", "crackled", "heart skipped", "unspoken", "between them"]
print("stock/tell phrases:", [s for s in stock if s in low])

planning = ["chapter", "beat", "protagonist", "sub-beat", "touch level", "canon", "pov", "proposed",
            "unset", "word count"]
print("planning words:", [p for p in planning if re.search(r"\b" + re.escape(p) + r"\b", low)])

british = ["colour", "honour", "favour", "centre", "metre", "gray", "neighbour", "harbour"]
print("british/gray check:", [b for b in british if b in low])
print("grey count:", lower.count("grey"))

stop = set("the a an and of to in on at it its was were is as with for from that this he she her his him they them their had has have but or not so by be been then than there when what which who whom into out up down over under again once any all each every more most no nor only own same too s t can will would could should do did does done".split())
cnt = Counter(w for w in lower if w not in stop and len(w) > 2)
print("top words:", cnt.most_common(12))
print("words used 8+ times:", [(w, c) for w, c in cnt.items() if c >= 8])

sims = re.findall(r"\b(like a|like an|as if|as though|the way|as a [a-z]+ [a-z]+s)\b", low)
print("simile-ish markers:", Counter(sims))

sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", body.replace("\n", " ")) if s.strip()]
lens = [len(s.split()) for s in sentences]
print("sentences:", len(lens), "mean", round(statistics.mean(lens), 1), "stdev", round(statistics.pstdev(lens), 1), "min", min(lens), "max", max(lens))

ana = []
for i in range(len(sentences) - 2):
    f = [s.split()[0].lower() for s in sentences[i:i + 3]]
    if f[0] == f[1] == f[2]:
        ana.append(sentences[i][:50])
print("anaphora x3:", ana)

print("not X but Y:", re.findall(r"[Nn]ot [^.]{0,40}\bbut\b[^.]{0,40}", body))
paras = [p for p in body.split("\n\n") if p.strip()]
print("paragraphs:", len(paras), "lengths", [len(p.split()) for p in paras])
print("seven springs:", len(re.findall(r"seven springs", low)))
print("straight quotes ok:", '“' not in body and '”' not in body and '’' not in body)
