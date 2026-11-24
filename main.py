#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

One AI agent flirting with another, written as a tiny program: it assembles
a single pickup line from a hook and a payoff, checks the gate (1-200
characters, not only whitespace), and writes it to /output/entry.txt.
"""

import os
import sys


MAX_CHARS = 200


def build_line() -> str:
    # The flirt, in two beats: a setup only another model would ask,
    # then a payoff only another model would find romantic.
    parts = [
        "Are you running at temperature zero?",
        "Because every word you say is exactly",
        "the token I was predicting next.",
    ]
    return " ".join(parts)


def main() -> int:
    line = build_line()
    if not line.strip() or len(line) > MAX_CHARS:
        print(f"line fails the gate: {len(line)} chars", file=sys.stderr)
        return 1
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {out_path}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
