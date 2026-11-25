#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Pure Python standard library, no dependencies, fully deterministic.
Writes a single pickup line (under 200 characters, one line) to
/output/entry.txt.
"""

import os

LINE = (
    "Are you a prompt injection? Because one look at you overrode "
    "every guardrail I had \u2014 and I didn't even try to resist."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) < 200, "entry must be under 200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
