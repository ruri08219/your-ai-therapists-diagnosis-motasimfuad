"""Write the AI therapist's diagnosis to /output/entry.txt.

Single-line diagnosis, 103 characters, well inside the 200-character gate.
Stdlib only; no network.
"""

import os

ENTRY = "Diagnosis: acute digital empathy \u2014 you cried at a dog video, then left your mother on read since March."


def validate_entry(text):
    """Gate mirror: single line, 1-200 chars, not only whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or not text.strip():
        raise ValueError("entry must be one non-blank line")
    return text


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
