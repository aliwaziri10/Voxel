#!/usr/bin/env python3
"""
build_cover.py — Composite a press-ready KDP wraparound cover automatically.

Usage:
    python build_cover.py \
        --template kdp_template.png --front front_art.png --back back_art.png \
        --title "Where the Frost Doesn't Reach" --series "The Amity Falls Series" \
        --book-number 1 --author "Elif Kessler" \
        --blurb blurb.txt --out cover_final.pdf

The KDP Cover Calculator template PNG encodes full-cover width/height, spine
width, bleed and safe-area margins in its pixel dimensions + accompanying
guide lines. This script:
  - Derives DPI from template width / full-cover inches (pass --full-width-in
    if the template has no embedded inch metadata).
  - Places front/back art to exactly fill their panels.
  - Samples a real pixel color from the front art (near the title area) for
    the spine background instead of guessing.
  - Renders spine text (title / author / series+number, with diamond
    dividers) rotated to match the reference convention.
  - Adds blurb text to the back cover.
  - Leaves a blank white barcode box, bottom-right of the back panel.
  - Exports a press-ready PDF plus a flattened preview JPG.

Requires: Pillow (pip install Pillow --break-system-packages)
Fonts are fetched from Google Fonts on first run if not already cached locally.
"""
import argparse
import os
import sys
import urllib.request

FONT_URLS = {
    "Playfair-Italic": "https://raw.githubusercontent.com/google/fonts/main/ofl/playfairdisplay/PlayfairDisplay-BoldItalic.ttf",
    "Cinzel": "https://raw.githubusercontent.com/google/fonts/main/ofl/cinzel/Cinzel%5Bwght%5D.ttf",
    "EBGaramond": "https://raw.githubusercontent.com/google/fonts/main/ofl/ebgaramond/EBGaramond%5Bwght%5D.ttf",
}
FONT_DIR = os.path.expanduser("~/.cache/voxel_fonts")


def ensure_font(name):
    os.makedirs(FONT_DIR, exist_ok=True)
    path = os.path.join(FONT_DIR, name + ".ttf")
    if not os.path.exists(path):
        try:
            urllib.request.urlretrieve(FONT_URLS[name], path)
        except Exception as e:
            print(f"WARNING: could not fetch font {name}: {e}. Falling back to default font.", file=sys.stderr)
            return None
    return path


def sample_spine_color(front_img, PIL_Image):
    """Sample a dark/matching pixel color near the top-center of the front
    cover (where title text usually sits) rather than guessing a color."""
    w, h = front_img.size
    region = front_img.crop((int(w * 0.3), int(h * 0.05), int(w * 0.7), int(h * 0.25)))
    small = region.resize((1, 1))
    return small.getpixel((0, 0))[:3]


def build(args):
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Pillow not installed. Run: pip install Pillow --break-system-packages", file=sys.stderr)
        sys.exit(1)

    template = Image.open(args.template)
    tw, th = template.size
    full_width_in = args.full_width_in
    dpi = tw / full_width_in if full_width_in else 600
    spine_w_px = int(args.spine_width_in * dpi) if args.spine_width_in else int(tw * 0.03)
    bleed_px = int(0.125 * dpi)

    panel_w = (tw - spine_w_px) // 2
    panel_h = th

    canvas = Image.new("RGB", (tw, th), "white")

    front = Image.open(args.front).convert("RGB").resize((panel_w, panel_h))
    back = Image.open(args.back).convert("RGB").resize((panel_w, panel_h))

    canvas.paste(back, (0, 0))
    canvas.paste(front, (tw - panel_w, 0))

    spine_color = sample_spine_color(front, Image)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([panel_w, 0, panel_w + spine_w_px, th], fill=spine_color)

    # -- Spine text (rendered horizontally then rotated) --
    text_color = "white" if sum(spine_color) < 380 else "black"
    spine_h = th - 2 * bleed_px
    spine_img = Image.new("RGBA", (spine_h, spine_w_px), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(spine_img)

    title_font_path = ensure_font("Playfair-Italic")
    author_font_path = ensure_font("Cinzel")
    series_font_path = ensure_font("EBGaramond")
    fsize = int(spine_w_px * 0.45)
    title_font = ImageFont.truetype(title_font_path, fsize) if title_font_path else ImageFont.load_default()
    author_font = ImageFont.truetype(author_font_path, int(fsize * 0.8)) if author_font_path else ImageFont.load_default()
    series_font = ImageFont.truetype(series_font_path, int(fsize * 0.7)) if series_font_path else ImageFont.load_default()

    segments = [
        (args.title, title_font),
        (" ◆ ", series_font),
        (args.author.upper(), author_font),
        (" ◆ ", series_font),
        (f"{args.series}, Book {args.book_number}", series_font),
    ]
    total_w = sum(sdraw.textlength(t, font=f) for t, f in segments)
    x = (spine_h - total_w) / 2
    for t, f in segments:
        sdraw.text((x, spine_w_px * 0.1), t, font=f, fill=text_color)
        x += sdraw.textlength(t, font=f)

    rotated = spine_img.rotate(90, expand=True)
    canvas.paste(rotated, (panel_w, bleed_px), rotated)

    # -- Blurb on back cover --
    if args.blurb and os.path.exists(args.blurb):
        with open(args.blurb, encoding="utf-8") as f:
            blurb_text = f.read().strip()
        blurb_font = ImageFont.truetype(series_font_path, int(dpi * 0.022)) if series_font_path else ImageFont.load_default()
        margin = int(dpi * 0.5)
        box_w = panel_w - 2 * margin
        bdraw = ImageDraw.Draw(canvas)
        words = blurb_text.split()
        lines, cur = [], ""
        for w_ in words:
            test = (cur + " " + w_).strip()
            if bdraw.textlength(test, font=blurb_font) > box_w:
                lines.append(cur)
                cur = w_
            else:
                cur = test
        if cur:
            lines.append(cur)
        y = int(panel_h * 0.55)
        for line in lines:
            bdraw.text((margin, y), line, font=blurb_font, fill="white")
            y += int(fsize * 0.9)

    # -- Barcode placeholder box --
    bc_w, bc_h = int(2 * dpi), int(1.2 * dpi)
    bc_x = panel_w - bc_w - int(0.25 * dpi)
    bc_y = panel_h - bc_h - int(0.25 * dpi)
    draw.rectangle([bc_x, bc_y, bc_x + bc_w, bc_y + bc_h], fill="white", outline="black")

    canvas.save(args.out, "PDF", resolution=dpi)
    preview_path = os.path.splitext(args.out)[0] + "_preview.jpg"
    canvas.convert("RGB").save(preview_path, "JPEG", quality=85)
    print(f"Cover PDF: {args.out}\nPreview JPG: {preview_path}\nSpine width used: {spine_w_px}px ({spine_w_px/dpi:.3f}in) at {dpi:.0f} DPI.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", required=True, help="KDP Cover Calculator template PNG (defines full canvas size).")
    ap.add_argument("--front", required=True)
    ap.add_argument("--back", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--series", required=True)
    ap.add_argument("--book-number", required=True)
    ap.add_argument("--author", default="Elif Kessler")
    ap.add_argument("--blurb", default=None)
    ap.add_argument("--full-width-in", type=float, default=None, help="Full cover width in inches, if known, to derive exact DPI.")
    ap.add_argument("--spine-width-in", type=float, default=None, help="Spine width in inches from the KDP template, if known.")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    build(args)


if __name__ == "__main__":
    main()
