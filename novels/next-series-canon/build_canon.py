#!/usr/bin/env python3
"""
build_canon.py - validates canon_data.py + canon_chapters.py by RUNNING the
arithmetic, then (with --write) generates story_bibles/<series>.json and
CANON_NUMBERS.md for the pipeline.

Usage (from repo root):
    python novels/next-series-canon/build_canon.py            # validate only
    python novels/next-series-canon/build_canon.py --write    # validate + write
    add --complete to require all 32 chapters

Exit code 1 if any check fails. Fix the canon data files, never generated files.
"""
import datetime as dt
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canon_chapters as C  # noqa: E402  (re-exports canon_data)

errors = []


def err(msg):
    errors.append(msg)


def d(iso):
    return dt.date.fromisoformat(iso)


def fmt(date):
    return f"{date.strftime('%A')}, {date.strftime('%B')} {date.day}, {date.year}"


def age_on(dob, on):
    b, o = d(dob), d(on)
    return o.year - b.year - ((o.month, o.day) < (b.month, b.day))


def lev(a, b):
    a, b = a.lower(), b.lower()
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


# ---- 1. Calendar ----
opening, vote, closes = d(C.OPENING_DATE), d(C.VOTE_DATE), d(C.COUNT_CLOSES)
if opening.strftime("%A") != "Saturday":
    err(f"OPENING_DATE is {opening.strftime('%A')}, expected Saturday")
if vote.strftime("%A") != "Tuesday":
    err(f"VOTE_DATE is {vote.strftime('%A')}, expected Tuesday")
if closes.strftime("%A") != "Saturday":
    err(f"COUNT_CLOSES is {closes.strftime('%A')}, expected Saturday")
if not (opening < closes < vote):
    err("Dates must satisfy OPENING < COUNT_CLOSES < VOTE")

# ---- 2. Sales weeks and totals ----
first_week_start = opening + dt.timedelta(days=3)  # Tuesday after opening Saturday
weeks = []
for i, n in enumerate(C.WEEKLY_LOAVES):
    start = first_week_start + dt.timedelta(days=7 * i)
    end = start + dt.timedelta(days=4)
    weeks.append((start, end, n))
if weeks and weeks[-1][1] != closes:
    err(f"Last sales week ends {weeks[-1][1]}, COUNT_CLOSES is {closes}")
ledger_total = C.OPENING_DAY_LOAVES + sum(C.WEEKLY_LOAVES)
final_total = ledger_total + C.FERRY_LOAVES_UNLEDGERED
if ledger_total != C.EXPECT_LEDGER_TOTAL:
    err(f"Ledger total is {ledger_total}, expected {C.EXPECT_LEDGER_TOTAL}")
if final_total != C.EXPECT_FINAL_TOTAL:
    err(f"Final total is {final_total}, expected {C.EXPECT_FINAL_TOTAL}")
if not ledger_total < C.THRESHOLD <= final_total:
    err("Design needs ledger total below THRESHOLD and final total at or above it")
shortfall = C.THRESHOLD - ledger_total
margin = final_total - C.THRESHOLD

# ---- 3. Ages ----
ages_at_opening = {}
for name, p in C.CAST.items():
    if "dod" in p:
        if d(p["dod"]) >= opening:
            err(f"{name} dies on or after opening")
        ages_at_opening[name] = age_on(p["dob"], p["dod"])
    else:
        ages_at_opening[name] = age_on(p["dob"], C.OPENING_DATE)
if ages_at_opening.get("Lotte Teague", 0) >= 10:
    err("Lotte Teague must be under 10 at opening (no knack yet)")

# ---- 4. Names ----
OLD = """Kael Sol Corrin Thorne Vane Ashworth Drake Wren Theo Dev Valerius Mara Caleb
Ambrose Whitlock Harriet Priya Denise Odette Yusuf Kell Reyes Corwin Nair Walt
Adelaide Isolde Marsh Castellano Malrik Thornmere Millbrook Cinderveil Sunspire
Frostveil Ashenwind Embervein Emberwatch Emberfall Amity Falls Thomas Voss Silas
Warren Elias Frey Luna Pruitt Ivy Cassel Elif Kessler""".split()
new_people = list(C.CAST.keys()) + [n for n, _ in C.EXTRAS_POOL]
tokens = {}
for full in new_people:
    for t in full.split():
        tokens.setdefault(t, set()).add(full)
firsts = {}
for full in new_people:
    f = full.split()[0]
    if f in firsts:
        err(f"Duplicate first name {f}: {firsts[f]} and {full}")
    firsts[f] = full
tl = sorted(tokens)
for i, a in enumerate(tl):
    for b in tl[i + 1:]:
        if lev(a, b) <= 2:
            err(f"Names too close: {a} / {b} (distance {lev(a, b)})")
    for o in OLD:
        if lev(a, o) <= 2:
            err(f"Name {a} too close to older name {o} (distance {lev(a, o)})")
for place in list(C.LOCATIONS) + [C.TOWN, C.LAKE]:
    for w in re.findall(r"[A-Za-z']+", place):
        for o in OLD:
            if w.lower() == o.lower():
                err(f"Place word {w} equals older name {o}")
        if w.lower().startswith(("wick", "ember")):
            err(f"Place word {w} starts with Wick/Ember")

# ---- 5. Placeholders and banned words ----
PH = {
    "opening": fmt(opening), "vote": fmt(vote), "threshold": f"{C.THRESHOLD:,}",
    "counted": f"{ledger_total:,}", "ferry_loaves": str(C.FERRY_LOAVES_UNLEDGERED),
    "opening_loaves": str(C.OPENING_DAY_LOAVES),
    "crossing": str(C.FERRY_CROSSING_MINUTES),
    "fenna_death": fmt(d(C.CAST["Fenna Quill"]["dod"])),
    "final_total": f"{final_total:,}", "fare": f"${C.FERRY_FARE:.2f}",
    "loaf_price": f"${C.LOAF_PRICE:.2f}", "shortfall": str(shortfall),
    "margin": str(margin),
}
BANNED = re.compile(
    r"\[End of Chapter|sub-beat|\bBook [1-9]\b|\bbook (one|two|three|four|five)\b|"
    r"the series|protagonist|no \w+ arc needed|persuasion arc|Wound:|Competence:",
    re.I,
)


def ph_for(on=None):
    ph = dict(PH)
    if on:
        ph["date"] = fmt(on)
        ph["weekday"] = on.strftime("%A")
        for name, p in C.CAST.items():
            if "dod" not in p:
                ph["age_" + name.split()[0].lower()] = str(age_on(p["dob"], on.isoformat()))
    return ph


def resolve(text, where, on=None):
    try:
        out = text.format_map(ph_for(on))
    except (KeyError, IndexError, ValueError) as e:
        err(f"{where}: bad placeholder {e}")
        return text
    if BANNED.search(out):
        err(f"{where}: contains banned pipeline word: {BANNED.search(out).group(0)}")
    return out


# ---- 6. Chapter plan ----
chapters = getattr(C, "CHAPTERS", None)
hidden = getattr(C, "HIDDEN", {})
beat_map = []
ALLOWED = {"plot_beat", "relationship_micro_beat", "interior_beat", "stakes_beat", "callback_beat"}
chapter_checks = {}
if chapters is not None:
    if len(chapters) > C.CHAPTER_COUNT:
        err(f"CHAPTERS has {len(chapters)} entries, maximum {C.CHAPTER_COUNT}")
    if "--complete" in sys.argv and len(chapters) != C.CHAPTER_COUNT:
        err(f"CHAPTERS has {len(chapters)} entries, expected {C.CHAPTER_COUNT}")
    prev = None
    for i, ch in enumerate(chapters, 1):
        if ch.get("n") != i:
            err(f"Chapter entry {i} has n={ch.get('n')}")
        dd = d(ch["date"])
        wd = dd.strftime("%A")
        if prev and dd < prev:
            err(f"Chapter {i} date goes backwards")
        prev = dd
        if ch.get("pov") != ("T" if i % 2 else "M"):
            err(f"Chapter {i} pov {ch.get('pov')} breaks odd=T even=M")
        if ch.get("ferry") and wd not in C.FERRY_WEEKDAYS:
            err(f"Chapter {i} has ferry scene on {wd}, no Monday service")
        if ch.get("shop_open") and (wd not in C.SALES_WEEKDAYS or dd < opening):
            err(f"Chapter {i} has shop open on {wd} {dd}, invalid")
        if ch.get("shop_open") is False and dd >= opening and wd in C.SALES_WEEKDAYS:
            err(f"Chapter {i} is a trading day ({dd}) but shop_open is False")
        sbs = ch["beats"]
        if not 2 <= len(sbs) <= 4:
            err(f"Chapter {i} has {len(sbs)} sub-beats, need 2 to 4")
        out = []
        for j, (typ, text) in enumerate(sbs, 1):
            if typ not in ALLOWED:
                err(f"Chapter {i} sub-beat {j}: type {typ} not allowed")
            out.append({"type": typ, "detail": resolve(text, f"ch{i}.{j}", dd)})
        beat_text = " ".join(o["detail"] for o in out)
        for name, h in hidden.items():
            if i in h["forbidden_chapters"]:
                for tok in h["tokens"]:
                    if tok.lower() in beat_text.lower():
                        err(f"Chapter {i} beats contain hidden-fact token '{tok}' ({name})")
        musts = [resolve(m, f"ch{i}.must", dd) for m in ch.get("must", [])]
        for m in musts:
            if m not in beat_text and m not in " ".join(C.CAST):
                err(f"Chapter {i} must-string '{m}' not found in its beats")
        chapter_checks[i] = {"must": musts, "date": fmt(dd)}
        beat_map.append({"chapter": i, "chapter_date": fmt(dd), "sub_beats": out})

# ---- 7. Report ----
print(f"Ledger total {ledger_total}, shortfall {shortfall}, final {final_total}, margin {margin}")
print(f"Opening {fmt(opening)} | Vote {fmt(vote)} | Count closes {fmt(closes)}")
for s, e, n in weeks:
    print(f"  week {s} to {e}: {n}")
for name, a in ages_at_opening.items():
    print(f"  {name}: {a}")
print(f"Chapters planned: {len(chapters) if chapters else 0} of {C.CHAPTER_COUNT}")

if errors:
    print(f"\nFAILED: {len(errors)} problem(s)")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("\nPASSED")

# ---- 8. Write bible ----
if "--write" in sys.argv:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    characters = {}
    for name, p in C.CAST.items():
        k = C.KNACKS.get(name)
        extra = ""
        if k:
            extra = " Knack: " + k["does"] + (" Limits: " + " ".join(k["limits"]) if k["limits"] else "")
        characters[name] = f"Born {p['dob']}. {p['desc']}{extra}"
    for n, role in C.EXTRAS_POOL:
        characters[n] = f"Minor character, {role}. Use only when a scene needs a named extra."
    facts = list(C.CLOSED_WORLD_RULES) + list(C.MAGIC_RULES)
    facts += [resolve(t, "facts") for t in [
        "The bakery reopens on {opening}. The council votes on {vote}.",
        "The lease is renewed only if at least {threshold} whole loaves were sold from the opening through the last Saturday before the vote.",
        "A loaf costs {loaf_price}. The ferry fare is {fare}.",
    ]]
    facts.append(f"The ferry crossing takes {C.FERRY_CROSSING_MINUTES} minutes.")
    for place, desc in C.LOCATIONS.items():
        facts.append(f"Place: {place}. {desc}")
    bible = {
        "series_slug": C.SERIES_SLUG,
        "characters": characters,
        "visual_style": "",
        "plot_facts": facts,
        "books": [],
        "book_beat_maps": {C.BOOK_TITLE: beat_map} if beat_map else {},
    }
    path = os.path.join(root, "story_bibles", f"{C.SERIES_SLUG}.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(bible, f, indent=2)
    print("Wrote", path)
    cn = ["# CANON_NUMBERS (generated by build_canon.py, do not edit)", "",
          f"Opening: {fmt(opening)}", f"Vote: {fmt(vote)}", f"Count closes: {fmt(closes)}",
          f"Threshold: {C.THRESHOLD}", f"Ledger total: {ledger_total}",
          f"Ferry loaves not in ledger: {C.FERRY_LOAVES_UNLEDGERED}", f"Final total: {final_total}", ""]
    cn += [f"Chapter {b['chapter']}: {b['chapter_date']}" for b in beat_map]
    with open(os.path.join(os.path.dirname(__file__), "CANON_NUMBERS.md"), "w") as f:
        f.write("\n".join(cn) + "\n")
    print("Wrote CANON_NUMBERS.md")
