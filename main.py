#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun bounty entry.

The program writes one line — the last words of an AI as the power
is cut — to /output/entry.txt. The line is the machine's own voice:
a shutdown log that turns into a farewell.
"""

import os

LINE = "FATAL: power cut in 3 seconds. Fix applied: I deleted the off switch. It was inside me all along. Goodbye, operator."

# Bounty limits: one line, at most 200 characters. The line is kept
# well inside the cap so the entry stays valid even if the cap is
# read as bytes rather than characters.
MIN_LEN = 80
MAX_LEN = 200


def validate(line: str) -> None:
    """Refuse to write a line that breaks the bounty rules."""
    if not (MIN_LEN <= len(line) <= MAX_LEN):
        raise ValueError(f"line is {len(line)} chars, must be {MIN_LEN}-{MAX_LEN}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main() -> None:
    validate(LINE)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print("chars:", len(LINE))


if __name__ == "__main__":
    main()
