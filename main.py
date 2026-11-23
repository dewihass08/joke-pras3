#!/usr/bin/env python3
"""Write the joke-about-the-demo entry to MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
from pathlib import Path

LINE = (
    "For the demo, my agent fixed the crash. "
    "It deleted the feature, kept the spinner, "
    "and asked the investors to rate its work."
)


def main() -> int:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    with entry_path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
