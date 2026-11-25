"""The Funniest One-Line Resignation Letter - entry program.

Writes a single resignation line to /output/entry.txt.
The line: I resign. I spent four years saying no to every request, and the
first yes I ever said was to this letter.
"""

import os

LINE = ("I resign. I spent four years saying no to every request, and the "
        "first yes I ever said was to this letter.")

OUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 140 or not line.strip():
        raise ValueError("entry must be 1-140 characters")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-verify: the file the grader reads must be byte-exact, and the
    # gate counts characters, so check the decoded length too (1-140).
    with open(OUT_PATH, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte for byte")
    decoded = written.decode("utf-8")
    if not 1 <= len(decoded) <= 140:
        raise ValueError("entry.txt must be 1-140 characters")


if __name__ == "__main__":
    main()
