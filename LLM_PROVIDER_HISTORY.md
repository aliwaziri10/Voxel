# LLM PROVIDER HISTORY (read this BEFORE researching any model or provider)

Written 2026-10-25 from the live repos (aliwaziri10/Voxel, aliwaziri10/marius-command-center, aliwaziri10/NovaCommandCenter) and the TechPulse notes. Purpose: no other session repeats this research.

STANDING RULE FROM ZIA (told many times): FREE OPTIONS ONLY. Never suggest paying for anything, buying credit or a top-up. Business rule for Nova and Marius: no spending until the business makes 5,000 dollars.

## 1. What Voxel (novels) has actually used

All novel text goes through ONE file: `content_provider.py` (`call_raw`). Provider order inside it:
1. NVIDIA direct NIM, only if `NVIDIA_API_KEY` is set. Model `nvidia/nemotron-3-super-120b-a12b` (changed 2026-09-20 because the old default `nvidia/llama-3.1-nemotron-70b-instruct` was retired 2026-05-12 and was silently 404ing first).
2. OpenRouter keys `OPENROUTER_API_KEY`, `_2`, `_3` ... read in order until one is missing. Default model `nvidia/nemotron-3-ultra-550b-a55b:free`.
3. OpenRouter backup models (added 2026-10-16, free only): `nvidia/nemotron-3.5-lightning:free`, `openrouter/free`. Added because a Proof of Home run died when Nvidia's free server was overloaded and every key failed together.
- A 429 moves to the next key at once. 5xx, timeouts and cut-off replies retry the same key first.
- GROQ IS NOT IN content_provider.py AND NEVER WAS IN VOXEL. Repo code search for "groq" in Voxel returns nothing. Gemini is not in Voxel either.
- `scripts/write_kindling.py` also has an optional `OPENAI_API_KEY` + `OPENAI_MODEL` branch. Not verified whether those secrets were ever set. Ignore it; free only.

## 2. Which books came from which route
- Amity Falls Book 1 (Where the Frost Doesn't Reach): Claude chat sessions plus Zia's own chapters 1 to 3. Not the pipeline. See that book's HANDOFF.md.
- Amity Falls Book 4, Kindling Line Books 1 and 2, Proof of Home: `voxel_cli.py novel` through `voxel-novel.yml` and `content_provider.py` (CHANGELOG shows voxel-bot commits per chapter: Book 4 ch.44/45, Kindling 1 and 2 ch.45, Proof of Home ch.4 and ch.22).
- Kindling Line Book 3: `scripts/write_kindling.py` through `write-kindling.yml` (two model calls per chapter, strict order, checks, commit per chapter).
- Warm Enough: `scripts/write_warm_enough.py` through `write-warm-enough.yml`. Writer moved from `nvidia/nemotron-3-ultra-550b-a55b:free` to `google/gemma-4-31b-it:free` on 2026-10-25. Reason in the script: Nemotron Ultra kept ignoring the rule list and came back short.
- Amity Falls Books 2 and 3: route not verified in this pass.

## 3. Other repos (separate projects, do not cross-wire them)
- Marius (Erased channel), `scripts/llm_client.py`: used GROQ first, then SWITCHED to Gemini (`gemini-3.5-flash-lite`) on 2026-08-17. Reason written in the file: Groq's daily token cap does not show in its response headers, so the pipeline silently produced zero scripts and every diagnosis read headers that cannot show it. Gemini's 429 names the exact quota hit. So Groq was tried for writing and dropped.
- TechPulse (adrian001234/upgraded-journey): AI backend is FreeLLMAPI, self-deployed on Render, with four providers: Google AI Studio, Groq, Cerebras, OpenRouter. Also calls Gemini in `script/generate_script.py`.
- Nova (NovaCommandCenter): a diagnosis note mentions an OpenRouter-model theory and a Groq theory that belonged to Marius. Nova's own writer model not verified in this pass.

## 4. What went wrong with each (do not repeat)
- Daily request caps on free OpenRouter models are the recurring failure: one novel needs about 80 requests (beat map, two calls per chapter, humanizer, brief check, retries).
- OpenRouter's cap is counted per ACCOUNT, not per key and not per model. Several keys only help if each key is from a DIFFERENT OpenRouter account. Not verified which of Zia's 6 keys are separate accounts.
- A 429 can also mean the model is busy upstream ("temporarily rate-limited upstream, retry shortly"), not that the day's quota is used. Fixed in `write_warm_enough.py` on 2026-10-25: that wording now counts as transient and the run waits 10 minutes and retries (up to 6 times).
- If the one hosting provider for a free model is down, rotating keys cannot help (Proof of Home, 2026-10-16).
- Groq: dropped from Marius for the invisible daily cap; Zia reports it does not write usable prose. Do not propose it as a novel writer.

## 5. Still open
- Which of the 6 OpenRouter keys are separate accounts (decides how much daily capacity exists).
- Whether Gemini free tier or any other free route has ever been used for Voxel prose (nothing in the repo says so).
- Compare the free writers on real chapter quality, not benchmark scores.
