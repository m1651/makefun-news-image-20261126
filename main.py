#!/usr/bin/env python3
"""Copy entry.png to the output directory.

The image is the entry itself: a newspaper front page summing up the
world news of Thursday 26 November 2026, drawn programmatically.
This program does no network access and writes the same bytes every run.
"""
import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")

    with open(src, "rb") as f:
        data = f.read()

    if not data.startswith(PNG_MAGIC):
        print("entry.png: bad PNG signature", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"entry.png: {len(data)} bytes exceeds 1 MiB", file=sys.stderr)
        return 1
    if len(data) < 8:
        print("entry.png: file too short to be a PNG", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
