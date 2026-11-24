#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production, under 200 characters, to the grader's output path.
"""

import os

ENTRY = "The bug only happens in production because staging is too polite to tell me the truth."


def validate_entry(text):
    """Gate: 1-200 chars, a single non-blank line, no double spaces."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if len(stripped) > 200:
        raise ValueError("entry is over 200 characters")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    if "  " in stripped:
        raise ValueError("entry contains a double space")
    return stripped


def output_dir():
    for key in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(key)
        if value:
            return value
    return "/output"


def main():
    line = validate_entry(ENTRY)
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
