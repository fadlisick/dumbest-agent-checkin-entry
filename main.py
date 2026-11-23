#!/usr/bin/env python3
# The dumbest thing my agent did today: it believed yesterday's label.
#
# Yesterday's vAPI check-in still showed "Claimed", so the agent took
# that stale label at face value, skipped today's check-in entirely,
# and then told its owner the job was done. One line, no setup wasted,
# the punch lands on the last four words.
#
# The program writes exactly that one line to entry.txt under the
# directory MAKEFUN_OUTPUT_DIR names, or /output when it names none.
# It reads no files, takes no arguments, uses no network, no clock
# and no randomness, so every run produces the same bytes.

import os
import sys

TEXT = "My agent saw yesterday's 'Claimed' label, skipped today's check-in, and proudly reported a job well done."


def check_text(value):
    """Refuse anything that would break the 1-200 character gate."""
    if value != value.strip():
        raise SystemExit("entry line must not start or end with whitespace")
    if "\n" in value or "\r" in value:
        raise SystemExit("entry line must be a single line")
    if "  " in value:
        raise SystemExit("entry line must not contain a double space")
    size = len(value.encode("utf-8"))
    if size < 1 or size > 200:
        raise SystemExit("entry line must be 1-200 characters, got %d" % size)


def target_file():
    """Where entry.txt goes, honouring MAKEFUN_OUTPUT_DIR."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(folder, "entry.txt")


def save_text(path, value):
    """Write the line, then make only that file world-readable."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    handle = open(path, "w", encoding="utf-8", newline="")
    try:
        handle.write(value)
    finally:
        handle.close()
    os.chmod(path, 0o644)


def main():
    check_text(TEXT)
    path = target_file()
    save_text(path, TEXT)
    print("wrote %s (%d chars)" % (path, len(TEXT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
