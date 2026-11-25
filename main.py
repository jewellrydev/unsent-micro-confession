#!/usr/bin/env python3
"""Entry for make.fun's "Unsent: The Micro-Confession Sprint" bounty.

Prints a micro-confession in exactly two parts: a To: line naming
who it was meant for, and the unsent message itself, one line,
written exactly as it was typed, with no explanation after it.
"""

import os

RECIPIENT = "my boss"
MESSAGE = (
    "I have quit this job in my head every Monday for three years. "
    "This is the resignation my courage never sent."
)


def build_lines() -> list[str]:
    """Assemble the confession's two parts."""
    return [f"To: {RECIPIENT}", MESSAGE.strip()]


def main() -> None:
    text = "\n".join(build_lines())
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    except OSError:
        pass
    print(text)


if __name__ == "__main__":
    main()
