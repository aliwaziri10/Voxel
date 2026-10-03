#!/usr/bin/env python3
"""
fix_pass4.py - continuity pass 4, Book 1 only.

Canon decided 2026-10-03:
  - Valerius Ashworth wrote a dissent against the Vane denial, was overruled,
    and the Corrin majority stamped the denial with his own seal. So "his seal
    is on it" (public record) and "he dissented" (buried truth) are both true.
  - Valerius is the former Lord Auditor, now senior advisor to the Accord Council.
  - Sol's mother had a ward, but the binding was a lie. Never "no ward".
  - Mother's Reckoning was twelve years ago; Sol was twelve (she is now 24).
  - The Reckoning is 29 Frostveil, at noon.
  - The dead ward is Mira, who died on the Vane ledge, and had a sister.
  - Vane seat is on the western face. Sol's aunt is Rue.
  - Kael is reinstated as the five-year independent auditor (ch.42 stands).
  - Sol recounted her years at the new, lower burn rate (ch.44).
  - Characters fly in harnesses, not literal wings.
Idempotent. Usage: python scripts/fix_pass4.py <book1_chapters_dir>
"""
import os
import sys

RULES = [  # (chapter, old, new)
    # ch02
    (2, "A ward contract line blank for seven years.", "A ward contract line blank for twelve years."),
    (2, "Valerius Ashworth. Lord Auditor of the Reckoning Court. His father.",
        "Valerius Ashworth. Former Lord Auditor of the Reckoning Court, now senior advisor to the Accord Council. His father."),
    # ch04
    (4, "Six months of training without the fear", "Fifty-four days of training without the fear"),
    (4, "And in six months, the Reckoning would collect what was owed.", "And in fifty-four days, the Reckoning would collect what was owed."),
    (4, "*Six months,* his father had said.", "*Not long,* his father had said."),
    (4, "He is the ruling auditor now.", "He sits as senior advisor to the Accord now, and every ruling still crosses his desk."),
    # ch06
    (6, "House Vane had no ward. House Vane had never had a ward.",
        "House Vane had no ward now. It had paid for one once, and received a signature with nothing behind it."),
    (6, "for twenty years before the Accord reshaped the title", "for twenty-two years before the Accord reshaped the title"),
    # ch17
    (17, "She was twenty-three. By the old counts", "She was twenty-four. By the old counts"),
    (17, "My father was not the auditor on your mother's case.", "My father's seal is on your mother's denial. It is not the whole truth."),
    (17, "But Kael was saying no.", "But Kael was saying the seal was not the whole story."),
    (17, "Were sealed by Corrin. Not by my father. He recused himself. He wrote a dissent. It was buried.",
         "Were sealed by Corrin. My father wrote a dissent before the seal went on. The Corrin majority stamped the denial over it with his own seal. The dissent was buried."),
    (17, "Reckoning of House Vane, Year -20.", "Reckoning of House Vane, twelve years past."),
    (17, "a trap they built twenty years ago", "a trap they built twelve years ago"),
    # ch37
    (37, "Two years since the first transfer. Two years since the night chase across the ledges when Sol's desperation",
         "Seven weeks since the first transfer. Seven weeks since the night chase across the ledges when Sol's desperation"),
    (37, "He had spent twenty-seven years building a career on precision.", "He had spent ten years building a career on precision."),
    # ch38
    (38, "The one who died in the plaza.", "The one who died on this ledge."),
    # ch39
    (39, "Three days. That was all that remained.", "One day. That was all that remained."),
    (39, "Twelve weeks", "Six weeks"),
    (39, "twelve weeks", "six weeks"),
    (39, "\"Your mother had no ward,\" Kael said quietly.", "\"Your mother's ward never held,\" Kael said quietly."),
    (39, "My mother burned two point three years at her Reckoning. The average for a Vane bloodline flare is one point eight.",
         "My mother burned forty years at her Reckoning. The average for a Vane bloodline flare is one point eight."),
    (39, "Two point three years per flare. She did seven flares in her Reckoning. Sixteen years gone in twenty minutes. She was thirty-four. She looked fifty.",
         "Forty years gone in forty minutes. She was forty-two. She looked eighty."),
    (39, "Six strikes. The Reckoning would begin at first light on the thirty-first. Three days.",
         "Six strikes. The Reckoning would begin at noon tomorrow, the twenty-ninth. One day."),
    (39, "\"Three days,\" she whispered.", "\"One day,\" she whispered."),
    (39, "\"Three days.\"\n\n\"And then.\"", "\"One day.\"\n\n\"And then.\""),
    (39, "Then sleep. Three days.\"", "Then sleep. One day.\""),
    (39, "\"Three days,\" she agreed.", "\"One day,\" she agreed."),
    (39, "Chapter house. Ch.5. You were trying to reach the archive ledge. You flared for six seconds. The burn took eight months from you and three weeks from me.",
         "The lower ledge. You were trying to reach the archive. You flared for four seconds. The burn took months from you and three months from me."),
    (39, "\"Three weeks,\" Sol repeated. \"I didn't know. I didn't know it touched you.\"",
         "\"Three months,\" Sol repeated. \"I knew it touched you. I didn't know you'd kept the number.\""),
    (39, "\"I didn't tell you. I wrote it in my auditor's log as an anomaly. Environmental variance. I lied to myself for months.\"",
         "\"I didn't tell you. I redacted it from my incident report and called it investigation integrity. I lied to myself for months.\""),
    # ch40
    (40, "I know that Auditor Valerius Ashworth was paid fifteen thousand crowns to rule against my mother's appeal.",
         "I know that Auditor Valerius Ashworth wrote a dissent against my mother's denial, and that House Corrin paid fifteen thousand crowns to have his seal stamped over it anyway."),
    (40, "refused to provide a ward at the contracted rate", "sold her a ward who was never truly bound"),
    (40, "I suppressed this evidence for forty-three days.", "I suppressed this evidence for thirty days."),
    # ch41 (another session already fixed the countdown lines and the Valerius paragraph)
    (41, "Three weeks since the night she had climbed", "Four days since the night she had climbed"),
    (41, "Three weeks since he had looked at her", "Four days since he had looked at her"),
    (41, "between Year 17 of the Accord and Year 29", "over the last thirty years"),
    (41, "between Year 17 and Year 29", "over the last thirty years"),
    (41, "Mara Vane. Her mother's sister.", "Rue Vane. Her mother's sister."),
    (41, "Mara Vane was pushing through the representatives", "Rue Vane was pushing through the representatives"),
    (41, "in a locked drawer for thirteen years", "in a locked drawer for twelve years"),
    (41, "She died in the Reckoning of Year 20.", "She died in the Reckoning twelve years ago."),
    (41, "The Reckoning of Year 20 was conducted", "The Reckoning of twelve years past was conducted"),
    (41, "that had been shaking for sixteen years.", "that had been shaking for twelve years."),
    # ch43
    (43, "Corvin archives", "Corrin archives"),
    (43, "her lineage seat waiting on the eastern cliff face", "her lineage seat waiting on the western cliff face"),
    (43, "After the ward died in the plaza.", "After the ward died on the ledge."),
    (43, "\"The ward in the plaza,\" Sol said quietly. \"Her name was Mireille. She was twenty-three. She had a daughter.\"",
         "\"The ward on the ledge,\" Sol said quietly. \"Her name was Mira. She was twenty-three. She had a sister.\""),
    (43, "\"Her daughter will get the pension. That's something.\"",
         "\"Her sister and her mother will get the pension. That's something.\""),
    (43, "awaiting transport to whatever posting the review board assigned, if any. The auditor's medallion would be surrendered at dawn.",
         "awaiting transport to the independent auditor's quarters the Accord had assigned him. The old house medallion would be surrendered at dawn."),
    (43, "\"After that, I don't know. No posting. No house. No authority but what I earn.\"",
         "\"After that, five years of quarterly reviews. No house. No authority but what I earn.\""),
    # ch44
    (44, "Three days ago now.", "Six days ago now."),
    (44, "roughened by three days of too little sleep", "roughened by six days of too little sleep"),
    (44, "I had twenty-two before the Reckoning. Nineteen now.",
         "I counted nine at the old rate. At the new rate, with the burn a sixth of what it was, it was twenty-two before the Reckoning. Nineteen now."),
    (44, "\"Seven. Over the last six months.", "\"Seven. Over the last nine weeks."),
    # ch45 (wings and 'absorbed three' are already fixed in the live text)
    (45, "Kael landed on the balcony beside her, his wings folding with the slow deliberation of a man who had flown the Reckoning winds and survived. The new feathers at his wingtips still held the faint iridescence of borrowed years.",
         "Kael landed on the balcony beside her, shrugging out of his flight-harness with the slow deliberation of a man who had flown the Reckoning winds and survived. The new silver seams in the harness still held the faint sheen of borrowed years."),
    (45, "They launched from the balcony as one, wings catching the updraft that rose from the Reach's carved face.",
         "They launched from the balcony as one, harness lines taking the updraft that rose from the Reach's carved face."),
]

# (chapter, stale text that must be gone after the rules run)
STALE = [
    (2, "blank for seven years"),
    (4, "Six months of training"),
    (6, "never had a ward"),
    (17, "Year -20"),
    (17, "twenty years ago"),
    (37, "Two years since the first"),
    (39, "Twelve weeks"),
    (39, "twelve weeks"),
    (39, "thirty-first"),
    (39, "Ch.5"),
    (39, "Your mother had no ward"),
    (40, "forty-three days"),
    (40, "refused to provide a ward"),
    (41, "Year 17"),
    (41, "Year 20"),
    (41, "Mara Vane"),
    (41, "thirteen years"),
    (41, "sixteen years"),
    (43, "Corvin"),
    (43, "eastern cliff"),
    (43, "Mireille"),
    (43, "died in the plaza"),
    (44, "six months"),
    (45, "wingtips"),
    (45, "wings catching"),
]


def main():
    d = sys.argv[1] if len(sys.argv) > 1 else "novels/kindling-line-book-1/chapters"
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
    print("fix_pass4: chapters changed %d" % changed)
    bad = 0
    for r in report:
        print(r)
        bad += 1
    for ch, s in STALE:
        with open(os.path.join(d, "chapter_%02d.md" % ch), encoding="utf-8") as f:
            if s in f.read():
                print("CHECK FAIL ch%02d still has: %r" % (ch, s))
                bad += 1
    print("PASS4 RESULT:", "FAIL" if bad else "OK")
    return bad


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
