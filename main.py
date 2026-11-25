#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line, spoken by a hopeless tech support agent to a
desperate customer, to /output/entry.txt.
"""

import os

LINE = "Good news \u2014 your case is now with Tier 2, which is me again, but I\u2019ve had a coffee and a little cry."


def validate(line):
    """Entry must be a single line of 1-199 UTF-8 characters, not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 199:
        raise ValueError("entry must be 1-199 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    return line


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
