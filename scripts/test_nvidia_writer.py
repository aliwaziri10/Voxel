#!/usr/bin/env python3
"""
test_nvidia_writer.py - SMALL TEST ONLY (2026-10-27, free only). Does not touch chapters, briefs or the
real writer. For each free NVIDIA NIM model it asks for ONE short passage (about 400 words) from the
opening of chapter 8 of Warm Enough, then prints and saves: HTTP status, errors, word count, dash count,
and the checker's HARD/SOFT findings. 4 requests in total. Output goes to nim_test_output/ (the test
workflow pushes it to the side branch nim-test-output, never to main).
Needs the NVIDIA_API_KEY secret (never printed).
"""
import json
import os
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "novels" / "warm-enough"
OUT = ROOT / "nim_test_output"
URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODELS = [
    "z-ai/glm-5.3",
    "z-ai/glm-5.3-flash",
    "nvidia/nemotron-3-ultra-550b-a55b",
    "nvidia/nemotron-3-super-120b-a12b",
]


def read(p):
    return Path(p).read_text(encoding="utf-8")


def main():
    key = os.environ.get("NVIDIA_API_KEY", "")
    OUT.mkdir(exist_ok=True)
    if not key:
        msg = "NVIDIA_API_KEY is not set in this run, so nothing could be tested."
        print(msg)
        (OUT / "RESULT.md").write_text("# NVIDIA writer test\n\n" + msg + "\n", encoding="utf-8")
        return 0
    brief = read(BOOK / "briefs" / "ch08.md")
    voice = read(BOOK / "VOICE_GUIDE.md")
    prev = re.sub(r"^<!--.*?-->\s*", "", read(BOOK / "chapters" / "chapter_07.md"), flags=re.S)
    tail = " ".join(prev.split()[-350:])
    plot = re.search(r"(?m)^PLOT:(.*)$", brief)
    system = ("You are a novelist writing a cozy fantasy slow-burn romance in close third person, past tense. "
              "No em dashes or en dashes anywhere. No digits. Do not name any month or weekday. "
              "Name only Hester and Ansel. Output only prose, no title and no notes.")
    user = ("=== VOICE GUIDE ===\n" + voice + "\n\n=== END OF THE PREVIOUS CHAPTER ===\n" + tail +
            "\n\n=== BRIEF FOR CHAPTER 8 (Hester's point of view) ===\n" + brief +
            "\n\nTEST: write ONLY the opening of chapter 8, about 400 words, up to the moment Ansel stands in "
            "the half-knit Blue. Continue from the world of the previous chapter. Output only the prose.")
    sys.path.insert(0, str(ROOT / "scripts"))
    try:
        import write_warm_enough as wm
    except Exception as e:  # the checker is optional
        wm = None
        print("checker not available:", e)
    lines = ["# NVIDIA writer test (chapter 8 opening, about 400 words each)", ""]
    for model in MODELS:
        print("\n=== %s ===" % model)
        t0 = time.time()
        try:
            r = requests.post(URL, headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
                              json={"model": model, "messages": [{"role": "system", "content": system},
                                                                  {"role": "user", "content": user}],
                                    "temperature": 0.8, "max_tokens": 4000}, timeout=300)
        except Exception as e:
            print("REQUEST FAILED:", type(e).__name__, str(e)[:200])
            lines += ["## " + model, "- REQUEST FAILED: %s" % str(e)[:200], ""]
            continue
        secs = int(time.time() - t0)
        if not r.ok:
            print("HTTP %d: %s" % (r.status_code, r.text[:300].replace("\n", " ")))
            lines += ["## " + model, "- HTTP %d: %s" % (r.status_code, r.text[:300].replace("\n", " ")), ""]
            continue
        body = r.json()
        try:
            ch = body["choices"][0]
            text = ((ch.get("message") or {}).get("content") or "").strip()
            finish = ch.get("finish_reason")
        except Exception:
            print("NO CHOICES:", json.dumps(body)[:300])
            lines += ["## " + model, "- 200 but no choices: %s" % json.dumps(body)[:300], ""]
            continue
        words = len(text.split())
        dashes = text.count("\u2014") + text.count("\u2013")
        print("OK in %ds, %d words, %d dashes, finish=%s" % (secs, words, dashes, finish))
        findings = ""
        if wm and text:
            try:
                hard, soft = wm.check(text, 8, brief)
                hard = [h for h in hard if not h.startswith("only ")]
                findings = "HARD (ignoring length): %s | SOFT: %s" % (hard or "none", soft or "none")
                print(findings)
            except Exception as e:
                findings = "checker error: %s" % e
        safe = model.replace("/", "_")
        (OUT / (safe + ".md")).write_text(text + "\n", encoding="utf-8")
        lines += ["## " + model, "- answered in %d s, %d words, %d dashes, finish_reason=%s" % (secs, words, dashes, finish)]
        if not text:
            lines.append("- EMPTY reply (the model may have spent its budget thinking)")
        if findings:
            lines.append("- " + findings)
        lines.append("- text saved in %s.md" % safe)
        lines.append("")
        time.sleep(3)
    (OUT / "RESULT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\nDone. Results in nim_test_output/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
