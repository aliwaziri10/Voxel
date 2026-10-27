#!/usr/bin/env python3
"""
write_warm_enough_nim.py - runs scripts/write_warm_enough.py (unchanged) with a different
WRITER CHAIN and four fixes. Written 2026-10-27, free only.

WHY: write_warm_enough.py pins the writer to ONE free OpenRouter model (google/gemma-4-31b-it:free)
and deliberately drops NVIDIA direct. That route is capped at about 50 requests a day per account and
often answers "temporarily rate-limited upstream", so the automatic writer never saved a chapter
(chapters 1 to 7 of Warm Enough were written by hand). NVIDIA NIM direct (build.nvidia.com, the
NVIDIA_API_KEY secret) is free, about 40 requests a minute per model.

UPDATE 2026-10-27 (second bridge run, chapter 8 failed all three tries). Read the rejected drafts:
  try 1: the writer ignored "about 1,450 words" per half and returned 3143 + 2098 words (over 3000).
  try 2: the FIRST half already told the whole one-scene brief and reached the ENDS ON image; the SECOND
         half then kept going after it (brief check: continues after ENDS ON, Grey worn by Ansel).
  try 3: the model's own reasoning leaked into the reply ("Perfect. This is exactly ~1,450 words ... Let me
         re-read ...") followed by a list of fragments. That is where the digit, the word "chapter" and the
         cut-off ending came from.
FIXES in this file:
  1. ONE call per chapter (no halves). Chapter briefs are one scene, so a half has nothing to stop at.
  2. Nemotron models are called with chat_template_kwargs {"enable_thinking": false} (NVIDIA / sglang /
     CoreWeave docs: Nemotron 3 Ultra and Super think by default; this flag turns it off).
  3. clean_body now cuts any leaked reasoning (<think> blocks and "Perfect. This is exactly ...",
     "Let me re-read ..." style notes) before the checks run.
  4. "Purl" and "Cable" are allowed words (the cast check flagged "Knit. Purl. Cable four back.").
  5. Every model call now logs "answered by: <model>" (content_provider is silent on success).

CHAIN, in order (content_provider._post moves to the next entry on a 404, 429, bad key or hard error,
and remembers the entry that worked for the rest of the run):
  1. NVIDIA direct, nvidia/nemotron-3-ultra-550b-a55b
  2. NVIDIA direct, z-ai/glm-5.3
  3. NVIDIA direct, z-ai/glm-5.3-flash
  4. NVIDIA direct, nvidia/nemotron-3-super-120b-a12b
  5. every OpenRouter key (OPENROUTER_API_KEY, _2 ... _6), google/gemma-4-31b-it:free, last resort
Nothing here costs money. All checks, canon filtering, repair loop and brief check in
write_warm_enough.py are untouched; this file only changes which model answers and how its reply is cleaned.

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

wm.ALLOWED.update({"Purl", "Cable"})


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
        if str(provider["model"]).startswith("nvidia/nemotron"):
            payload["chat_template_kwargs"] = {"enable_thinking": False}
        return payload

    cp._build_payload = build_payload
    wm._PINNED = True
    print("[warm-enough] writer chain: %d NVIDIA model(s) first, then %d OpenRouter key(s) with %s (free only)"
          % (len(nvidia) * len(NVIDIA_WRITER_MODELS), len(openrouter), wm.WRITER_MODEL))
    print("[warm-enough] one call per chapter; Nemotron thinking off; leaked reasoning is cut from every reply")
    if not nvidia:
        print("[warm-enough] WARNING: NVIDIA_API_KEY is not set, so only OpenRouter will be used")


# ---------- leaked reasoning ----------

LEAK_MARKERS = re.compile(
    r"Perfect\.\s+This is|Perfect\.\s+That is|Let me re-?read|Let me rewrite|Let me (?:check|count|fix|redo)|"
    r"Looking at my (?:draft|text)|Actually, (?:looking|I need|the brief|the instruction)|"
    r"I need to (?:rewrite|re-?read|stop|cut|check)|I should (?:stop|cut|rewrite|re-?read)|"
    r"Word count:|\(\s*~?\s*\d[\d,]*\s+words\s*\)|The (?:user|instruction) (?:wants|asked|says)|"
    r"But the instruction says|So I should|So I need to"
)
THINK_BLOCK = re.compile(r"<think>.*?</think>", re.S | re.I)


def strip_leak(text):
    """Remove <think> blocks and reasoning notes the model sometimes appends to (or after) the prose.
    Cuts from the first marker that appears after at least 500 characters of prose, then makes sure the
    prose ends on a full stop. Returns the text unchanged when nothing matches."""
    text = THINK_BLOCK.sub("", text)
    text = re.sub(r"^.*?</think>", "", text, flags=re.S | re.I)   # reply that starts mid-thought
    text = re.sub(r"<think>.*$", "", text, flags=re.S | re.I)      # unterminated block at the end
    for m in LEAK_MARKERS.finditer(text):
        if m.start() >= 500:
            text = text[:m.start()].rstrip()
            if text and text[-1] not in ".!?\"'”’*":
                text += "."
            break
    return text


_original_clean_body = wm.clean_body


def clean_body_no_leak(text):
    return _original_clean_body(strip_leak(text))


# ---------- one call per chapter ----------

def call_chapter_single(system, user):
    """The brief is one scene, so the chapter is written in one call. The length and the stop line are
    repeated at the end of the prompt because the writer follows the last instruction best."""
    prompt = user + (
        "\n\nWRITE THE WHOLE CHAPTER NOW, in one piece, 2,300 to 2,700 words. Cover every part of the brief's PLOT, "
        "in the order given, with real scene (dialogue, hands, wool, the room). The chapter ends on the image named "
        "in ENDS ON and STOPS there: not one line after it. Output only the prose: no notes, no word count, "
        "no thinking, no remarks about the task.")
    text = clean_body_no_leak(wm.call_model(system, prompt))
    print("[warm-enough]   whole chapter: %d words (one call)" % wm.words(text))
    return text


# ---------- repeated sentences ----------

def dedupe_repeats(body):
    """Keep one copy of every sentence of six words or more. The first copy is kept, except that a
    sentence repeating the chapter's FINAL sentence is kept at the end (the closing image stays last).
    Returns (body, removed)."""
    pattern = r"[^.!?]+[.!?]+[\s\"”’']*|[^.!?]+$"

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
    """The writer's own punctuation fixes, then: if sentences are repeated word for word, drop the extra
    copies instead of failing the whole chapter. The log line says how many were removed."""
    body, notes = _original_fix_mechanical(body)
    if wm.repeated_sentences(body):
        body, removed = dedupe_repeats(body)
        if removed:
            notes.append("removed %d repeated sentence(s)" % removed)
    return body, notes


_original_call_model = wm.call_model


def call_model_logged(system, user):
    """Same call, plus one log line naming the model that answered (content_provider is silent on success)."""
    text = _original_call_model(system, user)
    try:
        import content_provider as cp
        print("[warm-enough]   answered by: %s" % cp._PROVIDERS[cp._active_provider_index]["label"])
    except Exception:
        pass
    return text


wm.call_model = call_model_logged
wm.fix_mechanical = fix_mechanical_with_dedupe
wm.clean_body = clean_body_no_leak
wm.call_chapter = call_chapter_single
wm.pin_writer = pin_writer_nim

if __name__ == "__main__":
    sys.exit(wm.main())
