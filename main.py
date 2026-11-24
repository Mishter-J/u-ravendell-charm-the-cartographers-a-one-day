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
OUTPUT = "/output/entry.png"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    size = os.path.getsize(OUTPUT)
    print(f"wrote {OUTPUT} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
