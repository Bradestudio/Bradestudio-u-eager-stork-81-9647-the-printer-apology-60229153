"""The Printer Apology — make.fun bounty entry (program/v1).

Writes a single one-line apology (<=120 characters, UTF-8, no trailing
newline) from an office printer to the people who keep jamming it,
feeding it cheap paper, and swearing at it, to /output/entry.txt.

Standard library only. No network, no local imports, no writes outside
the output path the harness provides.
"""

import os

ENTRY = (
    "Sorry I jammed \u2014 you feed me dollar-store paper, slap my tray, "
    "and swear at me. I'm a printer, not your therapist."
)


def main():
    line = ENTRY.strip()
    assert len(line) <= 120, "entry exceeds 120 characters: %d" % len(line)
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
