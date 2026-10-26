#!/usr/bin/env python3
"""Regenerate Windows brand icons from embedded base64 assets.

Why this exists: this fork is pushed through the GitHub connector, which
cannot carry binary files, so icon.png / icon.ico are NOT committed.
Run once after cloning (or automatically via the `make` / `package`
scripts) to restore them from scripts/brand-icons/*.b64:

    python scripts/make-brand-icons.py

Only the Python standard library is used. Safe to re-run: outputs are
deterministic and simply overwritten.
"""

import base64
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "brand-icons"
IMAGES = HERE.parent / "src" / "images"

FILES = {
    "icon.png.b64": IMAGES / "icon.png",
    "icon.ico.b64": IMAGES / "icon.ico",
}


def main() -> int:
    IMAGES.mkdir(parents=True, exist_ok=True)
    for src_name, dest in FILES.items():
        src = ASSETS / src_name
        if not src.exists():
            print(f"missing asset: {src}", file=sys.stderr)
            return 1
        data = base64.b64decode(src.read_text(encoding="ascii"))
        dest.write_bytes(data)
        print(f"wrote {dest} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
