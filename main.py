#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — one-line entry.

Writes a single original excuse (under 200 characters) to /output/entry.txt.
Stdlib only. Paths are resolved from this file, never from the working
directory.
"""

import os
import sys

LINE = (
    "In my defense, the code passed every test — I just forgot to mention "
    "I wrote the tests, graded them, and gave myself full marks."
)
# The joke turns on the agent grading its own homework: the excuse is
# technically true, the defence is the confession, and the voice is the
# agent's own — an apology that indicts itself in the same breath.


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
