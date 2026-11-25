#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun bounty entry.

Writes one line (1-199 characters) that reads as a hilarious
autocorrect fail to /output/entry.txt. Stdlib only, no network.
"""

import os

ENTRY = (
    "I texted my wife 'I'll be home in a sec' but autocorrect sent "
    "'I'll be home in a sex' — she replied 'hurry up then.'"
)

MAX_CHARS = 199


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    # Read it back and confirm what was actually written.
    with open("/output/entry.txt", encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        raise SystemExit("verification failed: /output/entry.txt mismatch")
    print(f"wrote /output/entry.txt ({len(written)} characters)")


if __name__ == "__main__":
    main()
