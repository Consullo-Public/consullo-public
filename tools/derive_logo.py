#!/usr/bin/env python3
"""Derive compact, theme-aware logo assets without altering the mark's geometry."""

from __future__ import annotations

import argparse
import hashlib
import statistics
from pathlib import Path

from PIL import Image


SOURCE_SHA256 = "cc0880d5c3c51b94304d078e19bbdaa81af648f4892046a2aae5f8075fb61632"
LIGHT_INK = (8, 8, 7)
DARK_INK = (244, 242, 235)
BACKGROUND_NOISE_FLOOR = 24
OPAQUE_INK_THRESHOLD = 64
DELIVERY_WIDTH = 400
FAVICON_SIZE = 128


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sampled_background(image: Image.Image) -> tuple[int, int, int]:
    """Return the median RGB value of the full outer border."""
    rgb = image.convert("RGB")
    width, height = rgb.size
    pixels = []
    for x in range(width):
        pixels.append(rgb.getpixel((x, 0)))
        pixels.append(rgb.getpixel((x, height - 1)))
    for y in range(height):
        pixels.append(rgb.getpixel((0, y)))
        pixels.append(rgb.getpixel((width - 1, y)))
    return tuple(int(statistics.median(p[channel] for p in pixels)) for channel in range(3))


def alpha_mask(image: Image.Image, background: tuple[int, int, int]) -> Image.Image:
    """Convert darkness relative to the border into an antialiased opacity mask."""
    rgb = image.convert("RGB")
    span = OPAQUE_INK_THRESHOLD - BACKGROUND_NOISE_FLOOR
    alpha = []
    for pixel in rgb.getdata():
        darkness = max(background[channel] - pixel[channel] for channel in range(3))
        value = round(255 * (darkness - BACKGROUND_NOISE_FLOOR) / span)
        alpha.append(max(0, min(255, value)))
    mask = Image.new("L", rgb.size)
    mask.putdata(alpha)
    return mask


def padded_crop(mask: Image.Image) -> tuple[int, int, int, int]:
    bbox = mask.getbbox()
    if bbox is None:
        raise ValueError("source contains no mark after background removal")
    left, top, right, bottom = bbox
    padding = round(max(right - left, bottom - top) * 0.035)
    return (
        max(0, left - padding),
        max(0, top - padding),
        min(mask.width, right + padding),
        min(mask.height, bottom + padding),
    )


def colored_mark(mask: Image.Image, color: tuple[int, int, int]) -> Image.Image:
    mark = Image.new("RGBA", mask.size, color + (255,))
    mark.putalpha(mask)
    return mark


def save_optimized(image: Image.Image, path: Path) -> None:
    image.save(path, format="PNG", optimize=True, compress_level=9)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("assets"))
    args = parser.parse_args()

    if digest(args.source) != SOURCE_SHA256:
        raise SystemExit("refusing an unrecognized logo source digest")

    source = Image.open(args.source)
    if source.size != (2048, 2080):
        raise SystemExit(f"unexpected source dimensions: {source.size}")

    background = sampled_background(source)
    mask = alpha_mask(source, background)
    crop = padded_crop(mask)
    cropped_mask = mask.crop(crop)

    target_height = round(cropped_mask.height * DELIVERY_WIDTH / cropped_mask.width)
    delivery_mask = cropped_mask.resize((DELIVERY_WIDTH, target_height), Image.Resampling.LANCZOS)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    save_optimized(colored_mark(delivery_mask, LIGHT_INK), args.output_dir / "logo-light.png")
    save_optimized(colored_mark(delivery_mask, DARK_INK), args.output_dir / "logo-dark.png")

    inner = FAVICON_SIZE - 16
    scale = min(inner / cropped_mask.width, inner / cropped_mask.height)
    favicon_mask = cropped_mask.resize(
        (round(cropped_mask.width * scale), round(cropped_mask.height * scale)),
        Image.Resampling.LANCZOS,
    )
    square_mask = Image.new("L", (FAVICON_SIZE, FAVICON_SIZE), 0)
    square_mask.paste(
        favicon_mask,
        ((FAVICON_SIZE - favicon_mask.width) // 2, (FAVICON_SIZE - favicon_mask.height) // 2),
    )
    favicon = Image.new("RGBA", (FAVICON_SIZE, FAVICON_SIZE), (248, 246, 240, 255))
    favicon.alpha_composite(colored_mark(square_mask, LIGHT_INK))
    save_optimized(favicon, args.output_dir / "favicon.png")

    print(f"source background: rgb{background}")
    print(f"ink crop: {crop}; output: {DELIVERY_WIDTH}x{target_height}")
    for name in ("logo-light.png", "logo-dark.png", "favicon.png"):
        path = args.output_dir / name
        print(f"{name}: {path.stat().st_size} bytes; sha256={digest(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
