"""Funniest Autocorrect Fail — one-line entry writer.

Writes the autocorrect fail to $MAKEFUN_OUTPUT_DIR/entry.txt.
Gate: UTF-8 text, 1-199 characters, not whitespace-only, one line.
"""

import os

MAX_CHARS = 199

ENTRY = "I texted my girlfriend 'I need a hug' \u2014 autocorrect sent 'I need a thug.'"


def main():
    if not ENTRY.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} gate")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
