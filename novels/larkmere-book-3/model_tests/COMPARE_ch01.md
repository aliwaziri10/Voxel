# Model comparison: chapter 1 (Bryony)

One raw draft per model, same prompt as the live writer. No repair loop, no brief check. Lower filler per 1,000 words is better. Higher sentence-length spread is more human. Read the drafts before choosing.

| model | status | words | hard | soft | filler/1k | distinct | sentence mean | sentence spread |
|---|---|---|---|---|---|---|---|---|
| `google/gemma-4-31b-it:free` | FAILED (transient): All 6 provider(s)/key(s) failed. Last error: OpenRouter key 6: HTTP 429 (rate/quota exceeded): {"error":{"message":"Prov | | | | | | | |
| `thinkingmachines/inkling:free` | FAILED (config): All 6 provider(s)/key(s) failed. Last error: OpenRouter key 6: HTTP 404 for https://openrouter.ai/api/v1/chat/completion | | | | | | | |
| `nvidia/nemotron-3.5-lightning:free` | ok | 645 | 1 | 1 | 15.5 | 0.471 | 20.8 | 9.9 |

## nvidia/nemotron-3.5-lightning:free
- HARD: only 645 words (a chapter must reach about 2,300)
- soft: style words: something x3, kind of x2, someone x1

