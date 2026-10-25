# Warm Enough: SESSION HANDOFF (fifth session of 2026-10-25, Claude chat, written at 95 percent of the session)

Read AFTER `novels/warm-enough/HANDOFF.md` (that file has the older sessions; this one is newer). Also read `LLM_PROVIDER_HISTORY.md` at the repo root. Repo: `aliwaziri10/Voxel`. Zia is a non-coder, dictates by voice (names come out garbled), wants short answers, every link or path in a code block, no stopping to ask, and ALWAYS checks GitHub first. Publisher name is always "Voxel Publications".

HARD RULES FROM ZIA (told many times, do not break): FREE OPTIONS ONLY. Never mention or suggest credit, paying, top-ups or spending money. Do the work yourself instead of sending him to dashboards.

## What happened this session
1. Zia pasted three identical failed runs of the writer: all 6 OpenRouter keys got HTTP 429 on `google/gemma-4-31b-it:free`, chapter 1 PAUSED, nothing written.
2. Claude read the live script and found the cause: the 429 text said "temporarily rate-limited upstream. Please retry shortly" (Google's shared free pool busy, NOT the daily limit), but `classify_error` treated every 429 as "daily quota used up" and paused at once.
3. FIX PUSHED: commit `10a9b4205e2afff5ca72df80afdb5bc4eb6a5c0d` on `scripts/write_warm_enough.py` (45,512 bytes). A 429 whose text contains "upstream", "retry shortly" or "temporarily" is now "transient": the run waits 10 minutes and asks again, up to 6 times (an hour), without using a draft try. A real daily-limit 429 still pauses cleanly. Model pin (Gemma, free only, OpenRouter only, no fallback models) was NOT changed. Docstring has a new UPSTREAM 429 paragraph.
4. CONFIRMED LIVE: Zia ran the workflow after the fix. Log showed `writer call failed (transient)` then `Waiting 10 minutes, then asking again (wait 1 of 6)`. OUTCOME OF THAT RUN UNKNOWN (session ended while it was waiting). Check the Actions tab and `chapters/` folder first.
5. Zia asked how Where the Frost Doesn't Reach and the Kindling books were made. Answers from the live repo: Frost = Zia's chapters 1 to 3 plus Claude chat sessions (not the pipeline). Amity Falls Book 4, Kindling Books 1 and 2, Proof of Home = `voxel_cli.py novel` / `voxel-novel.yml` via `content_provider.py` (voxel-bot commits in CHANGELOG.md). Kindling Book 3 = `scripts/write_kindling.py` + `write-kindling.yml` (default start chapter 9, two model calls per chapter). Amity Falls Books 2 and 3: route NOT verified.
6. Zia decided: the way forward is the script writes the whole draft in one run, and Claude profiles only proofread and fix.
7. Claude researched free provider limits (web). FINDING: OpenRouter's free-model daily cap is counted per ACCOUNT, not per key or model, so several keys help only if each key is from a different OpenRouter account. NOT VERIFIED which of Zia's 6 keys are separate accounts. (Claude also mentioned paid options in that answer; Zia objected strongly. Never again.)
8. Zia asked Claude to research which LLMs every project has used and write it on GitHub. DONE: `LLM_PROVIDER_HISTORY.md` at the repo root (commit `56488902814c965955f6fdcf150d55bbd7780dee`). Key facts: Voxel novels only ever used NVIDIA direct and OpenRouter (Nemotron Ultra free, then Gemma); Groq was never in Voxel; Marius used Groq first and dropped it on 2026-08-17 for Gemini (`gemini-3.5-flash-lite`) because Groq's daily cap is invisible; TechPulse's FreeLLMAPI wraps Google AI Studio, Groq, Cerebras and OpenRouter.
9. LAST CLARIFICATION FROM ZIA: the Groq/Gemini experiments were for the VIDEO projects (Marius, TechPulse, Nova scripts), not for novels. Claude's final answer recommended "Gemma first, Gemini Flash fallback" for novels. That is a proposal only, based on Marius using Gemini without daily-cap trouble. It has NOT been tested for novel prose.

## State right now (verify live, do not trust)
- Warm Enough: no chapters existed at last check. Writer = Gemma 4 31B free via OpenRouter, workflow also scheduled four times a day (05:40, 11:40, 17:40, 23:40 India time). Zia's manual run was waiting out the busy writer when the session ended.
- `content_provider.py` is unchanged; it has no Gemini or Groq provider.
- `scripts/write_kindling.py` has an optional `OPENAI_API_KEY` + `OPENAI_MODEL` branch. Ignore it (free only).
- HANDOFF.md of the book was NOT edited this session (it is long and other profiles edit it); this file is the pointer.

## Open question waiting for Zia
"Do you want me to add a Gemini Flash fallback to the writer?" It would need a Google AI Studio key as a repo secret (`https://aistudio.google.com/apikey`). Google may use free-tier prompts to improve its products, which matters for unpublished manuscripts. Zia has not answered. If he says yes: add a Gemini provider as a second writer tried when Gemma is busy or used up, keep Gemma first, keep free only, test with a mock before pushing, and ask him for exactly one thing (the key).

## NEXT STEPS, in order
1. `git pull`/fetch live. Read the latest run log of `write-warm-enough.yml`, then `chapters/`. If chapter 1 exists, read it against `briefs/ch01.md` (see HANDOFF.md NEXT STEP list).
2. If runs keep ending "PAUSED ... busy or down for about an hour", do not change the model without Zia: tell him and offer the free fallback options in `LLM_PROVIDER_HISTORY.md`.
3. Ask which of the 6 OpenRouter keys are separate accounts (only if it is needed to judge capacity).
4. Verify how Amity Falls Books 2 and 3 were written and add it to `LLM_PROVIDER_HISTORY.md` section 2.
5. The factory plan (novels/FACTORY_HANDOFF.md, FACTORY_SESSION_HANDOFF.md) is still not built; Warm Enough comes first.
