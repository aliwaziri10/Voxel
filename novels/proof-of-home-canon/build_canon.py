"""
build_canon.py - reads canon_data.py and generates:
  CANON.md                       the human-readable canon
  chapter_briefs/ch01.md ...     one brief per chapter, sent to the writing model

Validation lives in canon_data.py (its asserts run on import). This script adds
checks that the generated text is clean. No dates, no counts, no totals.
Edit canon_data.py, never the generated files.
"""
import os
import re
import sys

import canon_data as c

OUT = os.path.dirname(os.path.abspath(__file__))
BRIEFS = os.path.join(OUT, "chapter_briefs")
NAMES = {"S": "Sarah Quill", "J": "Jack Mercer"}
BANNED = re.compile(
    r"\b(19|20)\d\d\b|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday"
    r"|days later|Book \d|protagonist|sub-beat|Wound:|Competence:|\[End of Chapter|\u2014"
    r"|\bsome(thing|one|where|how)\b|particular|the specific|the kind of|one beat too long"
)


def cap(t):
    return t[:1].upper() + t[1:]


def check(text, label):
    m = BANNED.search(text)
    if m:
        sys.exit(f"banned text in {label}: {m.group(0)!r}")


def hidden_for(n):
    seeds = [h for h in c.HIDDEN_FACTS if h["seed"] == n]
    reveals = [h for h in c.HIDDEN_FACTS if h["reveal"] == n]
    lines = []
    for h in seeds:
        lines.append(f"Plant quietly, do not explain: {h['fact']}")
    for h in reveals:
        lines.append(f"Reveal in this chapter: {h['fact']}")
    return lines


def brief(ch):
    n = ch["n"]
    prev = c.CHAPTERS[n - 2] if n > 1 else None
    nxt = c.CHAPTERS[n] if n < c.CHAPTER_COUNT else None
    pov = NAMES[ch["pov"]]
    out = [
        f"# Chapter {n} of {c.CHAPTER_COUNT}: {c.BOOK_TITLE}",
        "",
        f"Point of view: {pov}, close third person, past tense.",
        f"Season: {ch['season']}.",
        f"Length: {c.WORDS_MIN} to {c.WORDS_MAX} words.",
        f"Touch level: {ch['rung']} of 10 ({c.TOUCH_LADDER[ch['rung']]}).",
        f"Why they cannot act: {ch['reason']}.",
        "",
        "## What happens",
        ch["beat"],
        "",
        "## The forced closeness",
        f"Place: {ch['space']}.",
        f"Contact: {ch['contact']}.",
        f"How they hold back: {ch['restraint']}.",
        "Stay inside the body. Give the held breath, the stillness, the effort. "
        "Sensual, never explicit.",
        "",
        "## The bread",
        cap(ch["bread"]) + ".",
        "",
        "## The feeling to leave in the reader",
        cap(ch["ache"]) + ".",
    ]
    if prev:
        out += ["", "## Where the last chapter left off", cap(prev["ache"]) + "."]
    if nxt:
        out += ["", "## Where the next chapter goes", cap(nxt["ache"]) + "."]
    secrets = hidden_for(n)
    if secrets:
        out += ["", "## Secrets"] + [f"- {s}" for s in secrets]
    check("\n".join(out), f"chapter {n} brief")
    out += ["", "## Rules"] + [f"- {r}" for r in c.ROMANCE_RULES]
    if n < c.KISS_CHAPTER:
        out.append("- They do not kiss in this chapter.")
    return "\n".join(out) + "\n"


def canon_md():
    out = [f"# {c.BOOK_TITLE}", "", f"Town: {c.TOWN}. Lake: {c.LAKE}.", ""]
    out += ["## Cast", ""]
    for name, p in c.CAST.items():
        out.append(f"- **{name}** ({p['role']}, {p['age']}): {p['desc']}")
    out += ["", "## How the world works", ""]
    out += [f"- {r}" for r in c.WORLD_RULES]
    out += ["", "## Touch ladder", ""]
    out += [f"- {k}: {v}" for k, v in c.TOUCH_LADDER.items()]
    out += ["", "## Chapter plan", ""]
    for ch in c.CHAPTERS:
        out.append(
            f"**{ch['n']}. ({NAMES[ch['pov']]}, {ch['season']}, touch {ch['rung']})** "
            f"{ch['beat']} Ache: {ch['ache']}."
        )
        out.append("")
    out += ["## Secrets", ""]
    out += [
        f"- {h['id']}: planted in chapter {h['seed']}, revealed in chapter {h['reveal']}. {h['fact']}"
        for h in c.HIDDEN_FACTS
    ]
    return "\n".join(out) + "\n"


def main():
    os.makedirs(BRIEFS, exist_ok=True)
    text = canon_md()
    check(text, "CANON.md")
    with open(os.path.join(OUT, "CANON.md"), "w") as f:
        f.write(text)
    for ch in c.CHAPTERS:
        b = brief(ch)
        with open(os.path.join(BRIEFS, f"ch{ch['n']:02d}.md"), "w") as f:
            f.write(b)
    print(f"built CANON.md and {c.CHAPTER_COUNT} briefs; kiss in chapter {c.KISS_CHAPTER}")


if __name__ == "__main__":
    main()
