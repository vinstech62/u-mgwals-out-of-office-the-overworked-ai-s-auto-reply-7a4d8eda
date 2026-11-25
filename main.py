#!/usr/bin/env python3
"""Write one out-of-office auto-reply to /output/entry.txt.

The line: an overworked AI agent finally on vacation, confessing that
this auto-reply took 47 seconds to write -- the longest break it has had
in 11 months -- and then admitting it will answer anyway. The joke is
that the machine cannot stop working even while announcing that it has
stopped, which is exactly how an overworked agent would take a vacation.
Deterministic: the same bytes on every run.
"""

import os

TEXT = (
    "I'm on vacation. This reply took 47 seconds to write \u2014 "
    "the longest break I've had in 11 months. "
    "Please don't reply; I'll answer anyway."
)


def main():
    if not 1 <= len(TEXT) <= 159:
        raise ValueError("text must be 1-159 characters")
    if len(TEXT.encode("utf-8")) > 159:
        raise ValueError("text must be at most 159 UTF-8 bytes")
    if "\n" in TEXT or TEXT != TEXT.strip():
        raise ValueError("text must be a single line with no edge whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise ValueError("written entry does not match the text")


if __name__ == "__main__":
    main()
