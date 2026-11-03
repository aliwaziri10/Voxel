#!/usr/bin/env python3
"""
humanizer_revise_pov.py - runs scripts/humanizer_revise.py with ONE extra safety gate: point of view.

Why: the Ansel chapters (odd numbers) are written from Ansel's eyes and the Hester chapters (even numbers) from
Hester's. A rewrite that turns "he watched her face" into "she watched his face" keeps every fact, name, line
of dialogue and word count, so none of the existing checks notice, but it moves the camera into the wrong head.

The gate: in the narration (spoken lines are ignored) of an ODD chapter a rewrite may not gain any
"she + perception verb" (she watched, she saw, she felt, she knew, she thought, she wanted ...) that the original
paragraph did not already have. In an EVEN chapter the same rule applies to "he + perception verb".
A rejected rewrite is shown the reason ("point of view slipped: she watched") on its second ask.

Same command line as humanizer_revise.py. It imports that file and does not change it:
  python scripts/humanizer_revise_pov.py --book warm-enough --chapters 20 --max-paragraphs 25
"""
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import humanizer_revise as R

PERCEIVE = ("watched", "saw", "heard", "felt", "knew", "thought", "wanted", "noticed", "understood", "realized",
            "realised", "remembered", "wondered", "decided", "hoped", "feared", "wished", "believed")
POV_RX = {w: re.compile(r"\b" + w + r" (?:" + "|".join(PERCEIVE) + r")\b", re.I) for w in ("she", "he")}


def narration(p):
    """The paragraph without its spoken lines."""
    return re.sub(r"[\"\u201c][^\"\u201d]*[\"\u201d]", " ", p).replace("\u2019", "'")


def pov_violation(orig, new, n):
    wrong = "she" if n % 2 == 1 else "he"
    a = Counter(m.group(0).lower() for m in POV_RX[wrong].finditer(narration(orig)))
    b = Counter(m.group(0).lower() for m in POV_RX[wrong].finditer(narration(new)))
    extra = [k for k, v in b.items() if v > a.get(k, 0)]
    return ("point of view slipped: " + ", ".join(extra)) if extra else None


_state = {"n": 0}
_revise = R.revise_chapter
_validate = R.validate_paragraph


def revise_chapter(hp, h, wm, base, writer, path, n, *args, **kwargs):
    _state["n"] = n
    return _revise(hp, h, wm, base, writer, path, n, *args, **kwargs)


def validate_paragraph(orig, new, chapter_caps):
    return _validate(orig, new, chapter_caps) or pov_violation(orig, new, _state["n"])


R.revise_chapter = revise_chapter
R.validate_paragraph = validate_paragraph

if __name__ == "__main__":
    sys.exit(R.main())
