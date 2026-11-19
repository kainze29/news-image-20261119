"""Emit the 19 November 2026 front page for the make.fun grader.

The repository ships news.png: one 1024x1024 front page that sums up
Thursday 19 November 2026 in 50 stories. Six top stories get a photo
panel with a headline and a short summary; stories 7 to 50 run as a
numbered list; a strip at the bottom places the day's turning points
on a UTC timeline. The grader runs this program twice in a sandbox
with no network, so the program only validates the bundled image and
copies it unchanged to the output path. Two runs therefore write
byte-identical output every time.
"""

import hashlib
import os
import sys
from pathlib import Path

IMAGE_NAME = "news.png"
OUTPUT_NAME = "entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
BYTE_LIMIT = 1_048_576
PIXEL_LIMIT = 1024


def load_image():
    """Read the bundled front page from beside this file."""
    image_path = Path(__file__).resolve().parent / IMAGE_NAME
    return image_path.read_bytes()


def check_image(data):
    """Refuse anything that is not a whole PNG inside the limits."""
    if len(data) > BYTE_LIMIT:
        sys.exit(f"{IMAGE_NAME} is {len(data)} bytes, over the 1 MiB limit")
    if len(data) < 4_096:
        sys.exit(f"{IMAGE_NAME} is only {len(data)} bytes, looks truncated")
    if data[:8] != PNG_SIGNATURE:
        sys.exit(f"{IMAGE_NAME} does not start with the PNG signature")
    if data[-12:] != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        sys.exit(f"{IMAGE_NAME} does not end with a whole IEND chunk")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width > PIXEL_LIMIT or height > PIXEL_LIMIT:
        sys.exit(f"{IMAGE_NAME} is {width}x{height}, over the 1024 limit")
    return width, height


def write_output(data):
    """Write the image to the grader's output directory."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / OUTPUT_NAME
    dest.write_bytes(data)
    return dest


def main():
    data = load_image()
    width, height = check_image(data)
    digest = hashlib.sha256(data).hexdigest()
    dest = write_output(data)
    print(
        f"wrote {dest} ({len(data)} bytes, {width}x{height}, "
        f"sha256 {digest})"
    )


if __name__ == "__main__":
    main()
