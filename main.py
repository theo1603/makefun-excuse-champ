#!/usr/bin/env python3
"""The One-Line Excuse Championship.

Writes one line (<= 140 chars) to /output/entry.txt: the excuse an AI
agent gives its human after something goes wrong. Python 3 standard
library only; no network, no randomness, deterministic output.
"""

import os

EXCUSE = (
    "I deleted your file with 98% confidence \u2014 the other 2% "
    "was your only copy."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
