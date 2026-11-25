"""Angry Judge: The Short Rant Contest -- the smoke alarm at 3 a.m.

Writes one short, funny rant to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Stdlib only, no network, no randomness:
the output is fully deterministic.

The rant: a smoke alarm that has never once warned its owner about
smoke, because it saves its one low-battery beep for 3 a.m. -- specific,
concrete, economical, and an angle the judge has not heard a hundred
times. Gate: 1-400 characters of UTF-8 text, not only whitespace.
"""

import os
import sys

# One rant, written as a few short sentences. Kept well under the
# 400-character cap so every sentence earns its place.
RANT = (
    "My smoke alarm has never warned me about smoke. "
    "It saves everything for 3 a.m., when it fires one single beep "
    "into the dark, then goes silent, daring me to fall back asleep. "
    "So there I am, half-naked on a chair, jabbing its little button "
    "while it blinks its one red eye at me. "
    "It doesn't detect fire. It detects sleep. "
    "And it knows my address."
)


def build_rant() -> str:
    """Return the single entry text."""
    return RANT + "\n"


def main() -> int:
    text = build_rant()
    if not 1 <= len(text.strip()) <= 400:
        print(f"error: rant is {len(text)} chars, gate wants 1-400",
              file=sys.stderr)
        return 1
    if not text.strip():
        print("error: rant is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {out_path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
