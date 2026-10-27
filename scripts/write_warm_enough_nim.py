#!/usr/bin/env python3
"""
write_warm_enough_nim.py - runs scripts/write_warm_enough.py (unchanged) with a different
WRITER CHAIN. Written 2026-10-27, free only.

WHY: write_warm_enough.py pins the writer to ONE free OpenRouter model (google/gemma-4-31b-it:free)
and deliberately drops NVIDIA direct. That route is capped at about 50 requests a day per account and
often answers "temporarily rate-limited upstream", so the automatic writer never saved a chapter
(chapters 1 to 7 of Warm Enough were written by hand). NVIDIA NIM direct (build.nvidia.com, the
NVIDIA_API_KEY secret) is free and listed at about 40 requests a minute and about 10,000 a day.

CHAIN, in order (content_provider._post moves to the next entry on a 404, 429, bad key or hard error,
and remembers the entry that worked for the rest of the run):
  1. NVIDIA direct, z-ai/glm-5.3
  2. NVIDIA direct, z-ai/glm-5.3-flash
  3. NVIDIA direct, nvidia/nemotron-3-ultra-550b-a55b
  4. NVIDIA direct, nvidia/nemotron-3-super-120b-a12b
  5. every OpenRouter key (OPENROUTER_API_KEY, _2 ... _6), google/gemma-4-31b-it:free, last resort
Nothing here costs money. All checks, canon filtering, repair loop and brief check in
write_warm_enough.py are untouched; this file only replaces which model answers.

NVIDIA retires or un-frees model ids without warning (a 404 or 403 in the log). If that happens, edit
NVIDIA_WRITER_MODELS below to the current free ids from https://build.nvidia.com/models.

Usage (same arguments as write_warm_enough.py):
  python -u scripts/write_warm_enough_nim.py --auto --end 40 --checkpoint
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import write_warm_enough as wm  # noqa: E402

NVIDIA_WRITER_MODELS = [
    "z-ai/glm-5.3",
    "z-ai/glm-5.3-flash",
    "nvidia/nemotron-3-ultra-550b-a55b",
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


wm.pin_writer = pin_writer_nim

if __name__ == "__main__":
    sys.exit(wm.main())
