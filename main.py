"""The Vacuum's Alibi — make.fun entry program (program/v1).

A robot vacuum's one-line excuse for a missed spot, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Python 3.13, standard library only. The same bytes on every run:
no network, no randomness, no clock, no reads outside this file.
"""

import os
from pathlib import Path

LINE = "I scanned the spot twice, classified it as modern art, and decided my job is to preserve culture, not erase it."

MAX_CHARS = 200


def validate(line: str) -> None:
    """The kit gate, enforced before anything is written: one line, one
    sentence, 1 to 200 characters, not only whitespace."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if line.count(".") != 1 or not line.endswith("."):
        raise SystemExit("line must be a single sentence")


def write_entry(line: str) -> Path:
    """Write the approved line, then read it back byte for byte."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = Path(out_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line, encoding="utf-8", newline="\n")
    # The grader collects the output as another user, so the file must be
    # readable by everyone (0644) whatever umask the sandbox runs with.
    path.chmod(0o644)
    if path.read_text(encoding="utf-8") != line:
        raise SystemExit("entry.txt does not match the approved line")
    return path


def main() -> None:
    validate(LINE)
    write_entry(LINE)


if __name__ == "__main__":
    main()
