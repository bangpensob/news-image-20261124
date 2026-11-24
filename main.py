#!/usr/bin/env python3
"""Entry program for Make.fun bounty news-image-20261124.
Copies the bundled infographic to /output/entry.png, deterministically.
No network, no randomness, no external files beyond entry.png in this repo.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"

def main():
    if not os.path.isfile(SRC):
        raise FileNotFoundError(f"bundled infographic not found: {SRC}")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Deterministic by construction: a byte-for-byte copy, no timestamps in the output.
    if os.path.getsize(DST) != os.path.getsize(SRC):
        raise RuntimeError("output size does not match the bundled infographic")
    return 0

if __name__ == "__main__":
    sys.exit(main())
  
