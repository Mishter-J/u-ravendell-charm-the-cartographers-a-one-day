#!/usr/bin/env python3
"""Charm the Cartographers: A One Day Treasure Map Sprint.

Writes one treasure map image to /output/entry.png.

The map itself ("Isla Someday", a sailor's chart drawn from memory and rum)
is a fixed image shipped in this repository as map.jpg. This program does no
network access, takes no input and makes no random choices: it simply copies
the shipped image to the output path the grader reads, so every run produces
byte-identical output.

Run: python3 main.py
Output: /output/entry.png (1024x1024 JPEG, under 1 MiB)
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "map.jpg")
OUTPUT = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.png")

# JPEG magic bytes (SOI marker + JFIF/Exif APP0 marker prefix).
JPEG_SOI = b"\xff\xd8\xff"
MAX_BYTES = 1024 * 1024  # make.fun program/v1 gate: image must be <= 1 MiB


def validate_source(path: str) -> int:
    """Fail loudly if the shipped map is not a valid JPEG under 1 MiB.

    The entry used to copy map.jpg blindly; a corrupted or swapped source
    would have sailed straight through to the grader. Check the format
    first, then the size, and refuse to proceed on either failure.
    """
    with open(path, "rb") as fh:
        header = fh.read(3)
    if header != JPEG_SOI:
        raise SystemExit(
            f"error: {path} is not a JPEG (magic bytes {header!r}, "
            f"expected {JPEG_SOI!r})"
        )
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise SystemExit(
            f"error: {path} is {size} bytes, over the 1 MiB limit "
            f"({MAX_BYTES} bytes)"
        )
    return size


def main() -> int:
    size = validate_source(SOURCE)
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    written = os.path.getsize(OUTPUT)
    if written != size:
        raise SystemExit(
            f"error: copied {written} bytes but source is {size} bytes"
        )
    print(f"wrote {OUTPUT} ({written} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
