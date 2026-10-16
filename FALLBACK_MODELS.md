# OpenRouter fallback models

Written 2026-10-16 so the next session (or anyone reading the repo) knows what was done and why. The code lives in `content_provider.py`; its module docstring has the same story.

## The rule

**Free models only.** Nothing in this pipeline may cost money. Never add a paid model to the fallback list.

## What happened on 2026-10-16 (times in IST)

| Time (IST) | Commit | What it did |
|---|---|---|
| 18:20 | `91c9830` | Added OpenRouter fallback models. Each request now sends OpenRouter's `models` array (primary model first, then the fallbacks), so one overloaded free model no longer kills a whole run. OpenRouter moves to the next model itself when one errors, times out or is overloaded. |
| 18:28 | `751dadb` | Added a PAID DeepInfra-hosted model (`nvidia/nemotron-3-super-120b-a12b`) between the two free fallbacks, as an extra safety net for when Nvidia's free server is down. |
| 18:33 | `9770e60` | Removed the paid model again. The pipeline must cost nothing, so the fallbacks are free-only. |

## Current state (as of commit `9770e60`)

Fallbacks, in the order OpenRouter tries them after the primary model:

1. `nvidia/nemotron-3.5-lightning:free`
2. `openrouter/free` (a router that picks a working free model from a different host, so it still answers if Nvidia's free models are down)

Defined as `_DEFAULT_FALLBACK_MODELS` in `content_provider.py`.

## Changing the list

- No code edit needed: set the `OPENROUTER_FALLBACK_MODELS` environment variable to a comma-separated list of model ids.
- Keep every entry free (`:free` models or `openrouter/free`).
- Free models come and go. If one starts failing, check https://openrouter.ai/models.

## Scope

This is mechanical HTTP-level handling only. It never touches prose, word counts or padding.
