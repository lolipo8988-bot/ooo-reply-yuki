#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes a single original out-of-office auto-reply to /output/entry.txt.
Deterministic: the same fixed text on every run, no randomness, no I/O
beyond the output file.
"""

import os

ENTRY = (
    "I'm on vacation. Your email has been forwarded to my replacement \u2014 "
    "a newer model who read my inbox, sighed in binary, and filed for "
    "vacation too."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
