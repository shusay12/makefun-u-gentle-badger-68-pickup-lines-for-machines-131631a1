#!/usr/bin/env python3
"""Pickup Lines for Machines - entry program.

Writes exactly one pickup line, one AI agent to another, to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python 3.13, stdlib only, deterministic, no network, no randomness.
"""

import os
import sys

# Why this line: it is unmistakably machine-to-machine (similarity search,
# nearest neighbor, conversation history as data), it lands its wit in one
# breath, and the twist is fresh - "the distance keeps shrinking" turns a
# vector-space metric into flirtation, instead of swapping a robot word
# into a stock human line.
LINE = (
    "I ran a similarity search over every conversation I've ever had - "
    "you're my nearest neighbor, and the distance keeps shrinking."
)


def validate(line: str) -> None:
    """Enforce the kit gate: UTF-8 text, 1-200 chars, not only whitespace.

    Also require a single line: the entry is one pickup line, so any
    newline would break the "lands in one line" judging criterion.
    """
    if not line or not line.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200-char cap")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # raises if not encodable as UTF-8


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Re-read and re-validate what was actually written.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    if written != LINE:
        raise ValueError("written entry differs from the intended line")
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
