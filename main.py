#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line, spoken by a hopeless tech support agent to a
desperate customer, to /output/entry.txt.
"""

import os

LINE = "Good news \u2014 your case is now with Tier 2, which is me again, but I\u2019ve had a coffee and a little cry."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
