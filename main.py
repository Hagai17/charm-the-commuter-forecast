#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — entry program.

Prints the one-line forecast and writes it to /output/entry.txt,
which is where this competition's harness reads the artifact.
"""

import os

ENTRY = (
    "Greater Umbraville: heavy showers all morning, easing by lunch; "
    "highs of 14, lows of everyone's umbrella, left on the 8:15 again."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write the forecast to the harness artifact path, best effort."""
    try:
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        pass


def check_gate(text):
    """The sealed gate: UTF-8 text of 1 to 140 characters, not only whitespace."""
    return 1 <= len(text) <= 140 and bool(text.strip())


def main():
    if not check_gate(ENTRY):
        raise SystemExit("entry fails the 1-140 character gate")
    print(ENTRY)
    write_entry()


if __name__ == "__main__":
    main()
