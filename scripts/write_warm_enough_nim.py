#!/usr/bin/env python3
"""
write_warm_enough_nim.py - runs scripts/write_warm_enough.py (unchanged) with a different
WRITER CHAIN. Written 2026-10-27, free only.

WHY: write_warm_enough.py pins the writer to ONE free OpenRouter model (google/gemma-4-31b-it:free)
and deliberately drops NVIDIA direct. That route is capped at about 50 requests a day per account and
often answers "temporarily rate-limited upstream", so the automatic writer never saved a chapter
(chapters 1 to 7 of Warm Enough were written by hand). NVIDIA NIM direct (build.nvidia.com, the
NVIDIA_API_KEY secret) is free and listed at about 40 requests a minute and about 10,000 a day.

UPDATE 2026-10-27 (after the first bridge run, chapter 8 failed on repeated sentences): the model's second
half re-told parts of the first half, 12 to 15 sentences repeated word for word, and the repair rounds fixed
only the one the checker named each time. fix_mechanical is now wrapped (below) to drop the extra copies of
any sentence of six words or more before the checks run. NVIDIA nemotron-3-ultra is now first because it
was the one that answered while glm-5.3 and glm-5.3-flash returned 504 for the first hour.

CHAIN, in order (content_provider._post moves to the next entry on a 404, 429, bad key or hard error,
and remembers the entry that worked for the rest of the run):
  1. NVIDIA direct, nvidia/nemotron-3-ultra-550b-a55b
  2. NVIDIA direct, z-ai/glm-5.3
  3. NVIDIA direct, z-ai/glm-5.3-flash
  4. NVIDIA direct, nvidia/nemotron-3-super-120b-a12b
  5. every OpenRouter key (OPENROUTER_API_KEY, _2 ... _6), google/gemma-4-31b-it:free, last resort
Nothing here costs money. All checks, canon filtering, repair loop and brief check in
write_warm_enough.py are untouched; this file only replaces which model answers.

NVIDIA retires or un-frees model ids without warning (a 404 or 403 in the log). If that happens, edit
NVIDIA_WRITER_MODELS below to the current free ids from https://build.nvidia.com/models.

Usage (same arguments as write_warm_enough.py):
  python -u scripts/write_warm_enough_nim.py --auto --end 40 --checkpoint
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import write_warm_enough as wm  # noqa: E402

NVIDIA_WRITER_MODELS = [
    "nvidia/nemotron-3-ultra-550b-a55b",
    "z-ai/glm-5.3",
    "z-ai/glm-5.3-flash",
    "nvidia/nemotron-3-super-120b-a12b",
]


def pin_writer_nim(cp):
    nvidia = [p for p in cp._PROVIDERS if p.get("label") == "NVIDIA direct"]
    openrouter = [p for p in cp._PROVIDERS if str(p.get("label", "")).startswith("OpenRouter")]
    if not nvidia and not openrouter:
        raise SystemExit("STOP: no NVIDIA_API_KEY and no OPENROUTER_API_KEY is set, so there is no writer.")
    chain = []
    for model in NVIDIA_WRITER_MODELS:
        if nvidia:
            entry = dict(nvidia[0])
            entry["model"] = model
            entry["label"] = "NVIDIA direct " + model
            entry["fallback_models"] = []
            chain.append(entry)
    for p in openrouter:
        p["model"] = wm.WRITER_MODEL
        p["fallback_models"] = []
        chain.append(p)
    cp._PROVIDERS = chain
    cp._active_provider_index = 0
    original_build = cp._build_payload

    def build_payload(provider, system_prompt, user_content):
        payload = original_build(provider, system_prompt, user_content)
        payload["model"] = provider["model"]
        payload.pop("models", None)
        payload["temperature"] = wm.WRITER_TEMPERATURE
        payload["max_tokens"] = wm.WRITER_MAX_TOKENS
        return payload

    cp._build_payload = build_payload
    wm._PINNED = True
    print("[warm-enough] writer chain: %d NVIDIA model(s) first, then %d OpenRouter key(s) with %s (free only)"
          % (len(nvidia) * len(NVIDIA_WRITER_MODELS), len(openrouter), wm.WRITER_MODEL))
    if not nvidia:
        print("[warm-enough] WARNING: NVIDIA_API_KEY is not set, so only OpenRouter will be used")


def dedupe_repeats(body):
    """Keep one copy of every sentence of six words or more. The first copy is kept, except that a
    sentence repeating the chapter's FINAL sentence is kept at the end (the closing image stays last).
    Returns (body, removed)."""
    pattern = r"[^.!?]+[.!?]+[\s\"\u201d\u2019']*|[^.!?]+$"

    def key(sent):
        return re.sub(r"[^a-z ]", "", wm.norm(sent)).strip()

    paras = [re.findall(pattern, p) for p in re.split(r"\n\s*\n", body)]
    flat = [key(sent) for para in paras for sent in para if key(sent)]
    final_key = flat[-1] if flat else ""
    total = {}
    for k in flat:
        total[k] = total.get(k, 0) + 1
    seen_count, seen_first, removed, out = {}, set(), 0, []
    for para in paras:
        kept = []
        for sent in para:
            k = key(sent)
            if len(k.split()) < 6:
                kept.append(sent)
                continue
            seen_count[k] = seen_count.get(k, 0) + 1
            if k == final_key:
                keep = seen_count[k] == total[k]
            else:
                keep = k not in seen_first
                seen_first.add(k)
            if keep:
                kept.append(sent)
            else:
                removed += 1
        text = "".join(kept).strip()
        if text:
            out.append(text)
    return "\n\n".join(out), removed


_original_fix_mechanical = wm.fix_mechanical


def fix_mechanical_with_dedupe(body):
    """The writer's own punctuation fixes, then: if sentences are repeated word for word (this model
    re-tells parts of the first half in the second half), drop the extra copies instead of failing the
    whole chapter. The log line says how many were removed, so the chapter can be read for flow."""
    body, notes = _original_fix_mechanical(body)
    if wm.repeated_sentences(body):
        body, removed = dedupe_repeats(body)
        if removed:
            notes.append("removed %d repeated sentence(s)" % removed)
    return body, notes


wm.fix_mechanical = fix_mechanical_with_dedupe
wm.pin_writer = pin_writer_nim

if __name__ == "__main__":
    sys.exit(wm.main())
