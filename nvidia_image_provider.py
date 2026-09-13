#!/usr/bin/env python3
"""
nvidia_image_provider.py - Phase 9. NVIDIA NIM image generation, as an
alternative image source to image_provider.py's Gemini calls.

Two things this adds that Gemini (image_provider.py) doesn't do here yet:
  1. generate_image_nvidia() - plain text-to-image via FLUX.1-dev.
  2. generate_batch_from_reference() - the "give one reference photo, get
     N consistent variations" workflow: takes one existing image (e.g.
     Luna's picture) and a list of prompts, and generates one output image
     per prompt using FLUX.1-Kontext-dev, which is built specifically to
     keep a character/subject consistent across edits from a reference
     image (unlike base FLUX.1-dev, which only takes a text prompt).

Requires NVIDIA_API_KEY (same key already used by content_provider.py's
Phase 8b direct-NVIDIA text path). Get one at https://build.nvidia.com -
Setup - Generate API Key. No separate key needed for images vs text.

Endpoint reference: https://ai.api.nvidia.com/v1/genai/{vendor}/{slug}
(NVIDIA's hosted, model-specific generation host - different from the
integrate.api.nvidia.com host content_provider.py uses for chat/text).
Response shape: {"artifacts": [{"base64": "..."}]}.
If a model slug below ever 404s, check https://build.nvidia.com/explore/discover
for the current slug and update FLUX_TEXT2IMG_MODEL / FLUX_KONTEXT_MODEL.
"""

import base64
import os
import time
from pathlib import Path

import requests


NVIDIA_API_KEY = os.environ.get("NVIDIA_API_KEY", "")

NVIDIA_GENAI_BASE = "https://ai.api.nvidia.com/v1/genai"

# Plain text-to-image, no reference image.
FLUX_TEXT2IMG_MODEL = os.environ.get(
    "NVIDIA_FLUX_MODEL", "black-forest-labs/flux.1-dev"
)

# Reference-image-conditioned generation ("keep this character/subject,
# change the scene/pose/setting"). This is the model for the "give one
# photo of Luna, get 20-40 consistent pictures" workflow.
FLUX_KONTEXT_MODEL = os.environ.get(
    "NVIDIA_FLUX_KONTEXT_MODEL", "black-forest-labs/flux.1-kontext-dev"
)


def _require_key():
    if not NVIDIA_API_KEY:
        raise RuntimeError(
            "NVIDIA_API_KEY environment variable is not set. Get a key at "
            "https://build.nvidia.com (Setup -> Generate API Key)."
        )


def _image_to_data_url(image_path):
    image_path = Path(image_path)
    ext = image_path.suffix.lower().lstrip(".") or "png"
    mime = "jpeg" if ext in ("jpg", "jpeg") else ext
    b64 = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:image/{mime};base64,{b64}"


def _infer(model_slug, payload, timeout=120):
    _require_key()
    url = f"{NVIDIA_GENAI_BASE}/{model_slug}"
    resp = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {NVIDIA_API_KEY}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=timeout,
    )
    resp.raise_for_status()
    data = resp.json()
    try:
        b64 = data["artifacts"][0]["base64"]
    except (KeyError, IndexError) as e:
        raise RuntimeError(f"Unexpected NVIDIA image response shape: {data}") from e
    return base64.b64decode(b64)


def generate_image_nvidia(prompt, out_path, seed=0, steps=50):
    """Plain text-to-image via FLUX.1-dev. No reference image."""
    image_bytes = _infer(
        FLUX_TEXT2IMG_MODEL,
        {"prompt": prompt, "mode": "base", "seed": seed, "steps": steps},
    )
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(image_bytes)
    return out_path


def generate_batch_from_reference(reference_image_path, prompts, out_dir,
                                   filename_prefix="ref", seed_base=0,
                                   steps=50, polite_delay=2):
    """
    Takes ONE reference image (e.g. Luna's picture) and a list of prompts,
    generates one image per prompt with that subject kept consistent,
    using FLUX.1-Kontext-dev. This is the "give one photo, get 20-40
    pictures in one go" workflow - one call per prompt, same reference
    image reused each time.

    reference_image_path: path to the one source image.
    prompts: list of strings, each describing the scene/pose/setting to
        put the reference subject into for that output image.
    Returns a list of Path (or None on a failed prompt) matching `prompts`
    order, same convention as image_provider.generate_all_images().
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ref_data_url = _image_to_data_url(reference_image_path)

    results = []
    for i, prompt in enumerate(prompts):
        out_path = out_dir / f"{filename_prefix}_{i + 1:03d}.png"
        try:
            print(f"  [nvidia] Generating {i + 1}/{len(prompts)}: {prompt}")
            image_bytes = _infer(
                FLUX_KONTEXT_MODEL,
                {
                    "prompt": prompt,
                    "image": ref_data_url,
                    "mode": "image_edit",
                    "seed": seed_base + i,
                    "steps": steps,
                },
            )
            out_path.write_bytes(image_bytes)
            results.append(out_path)
        except (requests.RequestException, RuntimeError) as e:
            print(f"  [warn] NVIDIA image generation failed for prompt {i + 1}: {e}")
            results.append(None)

        if polite_delay:
            time.sleep(polite_delay)

    return results
