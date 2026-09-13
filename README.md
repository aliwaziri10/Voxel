# Voxel

Content generation pipeline - topic in, finished deck/asset out.

Started as a lesson-deck generator for classroom teaching (topic to
ready-to-use narrated PowerPoint), built to grow into a wider content
engine (books, templates, etc.) later without needing a rewrite. It has
since grown into that wider engine - see `HANDOFF.md` for the full
current picture (picture books, coloring books, and novels are also
built by this repo now, via `voxel_cli.py`). This README still only
covers the original lesson-deck generator (`make_lesson.py`); read
`HANDOFF.md` for everything else.

## What it does today

`make_lesson.py` takes a topic and produces:
1. A structured lesson outline (via Nemotron 3 Ultra, free on OpenRouter)
2. A .pptx deck built from that outline (via python-pptx)
3. Per-slide narration audio (via Piper, free local TTS)
4. Per-slide background music/SFX matched to mood (via Freesound.org, free API)
5. A mixed audio track per slide (via ffmpeg)
6. Per-slide illustrations (via Google Gemini - see `image_provider.py`)

Free aside from the Gemini key (free tier, daily quota), no GPU required.

## Setup

```bash
pip install -r requirements.txt --break-system-packages
```

Install Piper (free local text-to-speech) and download a voice model:
https://github.com/rhasspy/piper

Make sure `ffmpeg` is installed and on your PATH.

Set these environment variables before running:

```bash
export OPENROUTER_API_KEY=your_openrouter_key
export FREESOUND_API_KEY=your_freesound_key
export GEMINI_API_KEY=your_gemini_key
```

Get a free Freesound key at: https://freesound.org/apiv2/apply/
Get a free Gemini key at: https://aistudio.google.com/apikey

## Usage

```bash
python make_lesson.py "Present perfect tense for intermediate ESL students"
```

Output lands in `output/<topic_name>/`, including the .pptx, narration
audio, background audio, and mixed per-slide audio tracks.

## Known limitations (current version)

- **Audio is not yet auto-embedded into the .pptx file itself** -
  python-pptx has limited native audio-embedding support. For now, mixed
  audio files are generated alongside the deck and need to be manually
  inserted per slide via PowerPoint's Insert > Audio menu. Full
  auto-embed is a planned next step.
- This is a first working skeleton - built to run end-to-end, not yet
  polished or tested against real classroom content.

## Roadmap (not yet built)

- Automatic audio embedding into the .pptx
- See `ARCHITECTURE.md`/`HANDOFF.md` for the wider publishing-house
  roadmap (storybooks, coloring books, novels) - most of that is already
  built via `voxel_cli.py`, this README just hasn't been the place that
  tracks it.
