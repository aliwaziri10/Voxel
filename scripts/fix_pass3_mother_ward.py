#!/usr/bin/env python3
"""
fix_pass3_mother_ward.py - mother-mechanism continuity fix, Book 1 only.

Decision (Zia, 2026-10-02): Book 2's mechanism is canon (Sol's mother was a
contract-bound ward-taker who "went under a plate"). Book 1's mentions of
"she had no ward / none could be afforded" contradicted this AND Book 1's own
ch.17 line that the Corrin ward-contract on her mother's flight was falsified.

Fix: she HAD a ward, paid for at House Corrin's price. The binding was
falsified/never truly bound, so it failed to take the cost. Also standardizes
ch.41 on the single forty-year flight (not "burned alone for eight years").

Touches Book 1 chapters 2, 4, 6, 17, 41. Does not touch Book 2.
The ch.41 ward paragraph (with the Valerius dissent) was already fixed directly
in the live text, so only the speech rule remains for ch.41.
Also runs fix_pass4 first (continuity pass 4, ch.2-45), so one workflow run
applies both.
Idempotent. Usage: python scripts/fix_pass3_mother_ward.py <book1_chapters_dir>
"""
import os
import sys

RULES = [  # (chapter, old, new)
    (2,
     "My mother burned forty years because she had no ward and no choice. "
     "The flight path required it. The Reckoning required it. The Accord required it.",
     "My mother burned forty years because the ward bound to her flight was "
     "never truly bound. House Corrin falsified the contract, and the plate "
     "took nothing from the man who signed it. The flight path required a "
     "ward. The Reckoning required a ward. The Accord required a ward, and "
     "gave her only the paper of one."),
    (4,
     "Mother didn't have a ward. Mother didn't have me.",
     "Mother's ward was a lie on paper. Mother didn't have me."),
    (4,
     "Without a ward, the burns accumulate. The Reckoning requires sustained "
     "flight over the Ascension Spire, minimum four hours continuous "
     "manifestation. At her current rate, that costs six to seven years. "
     "With a ward, the cost transfers. Without one, it comes from her. "
     "Her mother burned forty years in her final flight. It took the rest.",
     "Without a true ward, the burns accumulate. The Reckoning requires "
     "sustained flight over the Ascension Spire, minimum four hours "
     "continuous manifestation. At her current rate, that costs six to "
     "seven years. With a ward, the cost transfers. With a false one, it "
     "still comes from her, and no one is warned in time. Her mother's "
     "ward failed beneath the plate, and she burned forty years in her "
     "final flight. It took the rest."),
    (6,
     "whose mother had died three winters after her Reckoning, twelve years "
     "past, because no ward could be afforded",
     "whose mother had died three winters after her Reckoning, twelve years "
     "past, because the ward House Vane had paid for was never bound as sworn"),
    (17,
     "No technique could redirect it. No ward contract could shield against "
     "it unless the ward was bound and consenting and paid. House Vane had "
     "never been able to afford a ward. Her mother had flown the Reckoning "
     "route with no one to catch the cost but the empty air.",
     "No technique could redirect it. A ward contract could shield against "
     "it only if the binding itself was true. House Vane had paid Corrin's "
     "price for one and received a signature with nothing behind it. Her "
     "mother had flown the Reckoning route with a ward beneath the plate "
     "who had never truly been bound to catch anything at all."),
    (41,
     "I am the last Kindling-wielder of House Vane,\" Sol said. Her voice "
     "carried. \"My mother was the last before me. She died in the Reckoning "
     "of Year 20. The official finding was insufficient Kindling control. "
     "The truth is that she had no ward. House Vane could not afford the "
     "Corrin price. She burned alone for eight years. The cost took her "
     "sight, then her memory, then her ability to fly. When she stood for "
     "her Reckoning, she had nothing left to give.",
     "I am the last Kindling-wielder of House Vane,\" Sol said. Her voice "
     "carried. \"My mother was the last before me. She died in the Reckoning "
     "twelve years ago. The official finding was insufficient Kindling control. "
     "The truth is that her ward was a lie. House Vane paid the Corrin "
     "price in full, and the man who went under the plate was never bound "
     "to pay back a single year of it. She burned forty years in that one "
     "flight. It took her sight, then her memory, then her life, inside a "
     "single afternoon. When she stood for her Reckoning, she had nothing "
     "left to give."),
]


def main():
    d = sys.argv[1] if len(sys.argv) > 1 else "novels/kindling-line-book-1/chapters"
    # pass 4 runs first so this file's final-wording 'new' strings match
    import fix_pass4
    bad4 = fix_pass4.main()
    report = []
    changed = 0
    for ch in sorted({r[0] for r in RULES}):
        p = os.path.join(d, "chapter_%02d.md" % ch)
        with open(p, encoding="utf-8") as f:
            t = f.read()
        o = t
        for c, old, new in RULES:
            if c != ch:
                continue
            if old in t:
                t = t.replace(old, new)
            elif new not in t:
                report.append("MISSING ch%02d: %r" % (ch, old[:70]))
        if t != o:
            with open(p, "w", encoding="utf-8") as f:
                f.write(t)
            changed += 1
    print("fix_pass3_mother_ward: chapters changed %d" % changed)
    bad = 0
    for r in report:
        print(r)
        bad += 1
    # sanity checks: old phrasing gone, no stray "no ward" left over on these lines
    text = "\n".join(
        open(os.path.join(d, "chapter_%02d.md" % i), encoding="utf-8").read()
        for i in (2, 4, 6, 17, 41)
    )
    checks = {
        "no ward and no choice": "no ward and no choice" in text,
        "never afforded a ward": "never afforded a ward" in text,
        "burned alone for eight years": "burned alone for eight years" in text,
        "em-dashes": text.count("\u2014") > 0,
    }
    for k, v in checks.items():
        if v:
            print("CHECK FAIL: %s still present" % k)
            bad += 1
    print("PASS3 RESULT:", "FAIL" if bad else "OK")
    return bad + bad4


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
