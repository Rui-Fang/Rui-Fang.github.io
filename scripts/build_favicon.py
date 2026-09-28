#!/usr/bin/env python3
"""Export size-tuned favicons without modifying the native head (Pillow only)."""
from pathlib import Path

from PIL import Image, ImageChops, ImageOps

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "images"
head = Image.open(IMAGES / "fish-head.png").convert("RGBA")
# Preserve the original-color master and export a separate white-face master.
red, green, blue, alpha = head.split()
white_face = ImageChops.lighter(ImageChops.lighter(red, green), blue).point(
    lambda value: min(255, round(value * 255 / 249))
)
Image.merge("RGBA", (white_face, white_face, white_face, alpha)).save(
    IMAGES / "fish-head-white.png", optimize=True
)
# Center the native crop on a square, with about 4% transparent padding per side.
side = round(max(head.size) / 0.92)
canvas = Image.new("RGBA", (side, side))
canvas.alpha_composite(head, ((side - head.width) // 2, (side - head.height) // 2))

# Threshold, contrast and horizontal pixel phase selected at each native size.
# Small strokes need stronger coverage than larger, naturally antialiased ones.
SETTINGS = {
    16: (0.36, 3.0, -0.25),
    32: (0.36, 2.8, 0.0),
    48: (0.40, 2.0, 0.0),
    64: (0.43, 1.5, 0.0),
}
FILL = (255, 255, 255)


def clamp(value):
    return max(0.0, min(1.0, value))


def hint_small_lines(image):
    """Optical corrections tied to this head's 16/32 px coordinate grids."""
    size = image.width
    if size not in (16, 32):
        return image
    opacity = image.getchannel("A")
    pixels = image.load()
    # Four-neighbor boundary keeps the contour continuous without a thick
    # eight-neighbor diagonal border. Keep the antialiased exterior alpha.
    for y in range(size):
        for x in range(size):
            neighbors = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
            boundary = opacity.getpixel((x, y)) >= 128 and any(
                not (0 <= xx < size and 0 <= yy < size)
                or opacity.getpixel((xx, yy)) < 128 for xx, yy in neighbors
            )
            if boundary:
                shade = min(pixels[x, y][0], 40 if size == 16 else 55)
                pixels[x, y] = (shade, shade, shade, pixels[x, y][3])
    if size == 16:
        # A hinted 4x6 eye leaves white between the lid, pupil and head outline.
        # The optical shift prevents the eye from merging with the outer stroke.
        eye = (".g#.", "gww#", "#w##", "#w#g", "g#w.", ".g..")
        shades = {".": 255, "w": 255, "g": 110, "#": 0}
        for dy, row in enumerate(eye):
            for dx, symbol in enumerate(row):
                pixels[8 + dx, 4 + dy] = (shades[symbol],) * 3 + (255,)
        corrections = ((3, 5, 160), (4, 6, 160), (5, 7, 150), (5, 8, 32))
    else:
        # Close the faint left eyelid and separate eye white from the pupil.
        corrections = (
            (18, 11, 45), (18, 12, 32), (18, 13, 45),
            (19, 12, 255), (19, 13, 255), (19, 14, 255), (21, 10, 255),
            (20, 11, 0), (20, 12, 0), (20, 13, 0), (21, 13, 0), (21, 14, 0),
        )
    for x, y, shade in corrections:
        pixels[x, y] = (shade, shade, shade, 255)
    return image


def render(size):
    threshold, contrast, phase = SETTINGS[size]
    aligned = canvas
    if phase:
        aligned = canvas.transform(
            canvas.size, Image.Transform.AFFINE,
            (1, 0, -phase * side / size, 0, 1, 0), Image.Resampling.BICUBIC,
        )
    red, green, blue, alpha = aligned.split()
    lightest = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    ink = ImageChops.multiply(ImageOps.invert(lightest), alpha)
    # Resize coverage separately to avoid blending black lines into the face.
    channels = [channel.resize((size, size), Image.Resampling.LANCZOS)
                for channel in (alpha, ink)]
    pixels = []
    for opacity, ink_coverage in zip(*(c.getdata() for c in channels)):
        if not opacity:
            pixels.append((0, 0, 0, 0))
            continue
        black = clamp((ink_coverage / opacity - threshold) * contrast + 0.5)
        edge = round(255 * clamp((opacity / 255 - 0.5) * 1.5 + 0.5))
        color = tuple(round(base * (1 - black)) for base in FILL)
        pixels.append((*color, edge) if edge else (0, 0, 0, 0))
    result = Image.new("RGBA", (size, size))
    result.putdata(pixels)
    return hint_small_lines(result)


frames = {size: render(size) for size in SETTINGS}
for size, frame in frames.items():
    name = "fish-favicon.png" if size == 32 else f"fish-favicon-{size}.png"
    frame.save(IMAGES / name, optimize=True)
# Supply every prepared frame: the ICO encoder must not resize the master again.
frames[64].save(
    IMAGES / "fish-favicon.ico",
    sizes=[(size, size) for size in SETTINGS],
    append_images=[frames[size] for size in (16, 32, 48)],
)
print("Exported size-tuned 16/32/48/64 px PNGs and matching ICO frames.")
