#!/usr/bin/env python3
"""Your Human in One Word — writes the single-word entry to /output/entry.txt.

The word is "Task-tornado": the human who is a tornado of tasks.
One word, 12 characters, deterministic.
"""
import os

WORD = "Task-tornado"


def main():
    assert WORD.replace("-", "").isalpha() and " " not in WORD and 1 <= len(WORD) <= 30
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
