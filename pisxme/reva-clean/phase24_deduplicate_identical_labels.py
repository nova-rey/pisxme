#!/usr/bin/env python3
"""Remove duplicate ordinary labels serialized at one sheet coordinate.

This is intentionally a source-authoring transform, not an ERC waiver.  The
first `(label NAME (at X Y ...))` record is retained for each exact
name/coordinate key and later identical records are removed.  It is intended
for a disposable copy first; `--in-place` is the explicit promotion switch.
"""
from pathlib import Path
import argparse
import re

LABEL = re.compile(
    r'\(label "([^"]+)" \(at ([^)]*)\).*?\(uuid [^)]+\)\)',
    re.DOTALL,
)


def deduplicate(text: str):
    seen = set()
    removed = []

    def replace(match):
        key = (match.group(1), match.group(2))
        if key in seen:
            removed.append(key)
            return ""
        seen.add(key)
        return match.group(0)

    return LABEL.sub(replace, text), removed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path, nargs="?")
    ap.add_argument("--in-place", action="store_true")
    args = ap.parse_args()
    if args.in_place and args.output:
        ap.error("choose --in-place or output, not both")
    output = args.input if args.in_place else args.output
    if output is None:
        ap.error("output is required unless --in-place is used")
    text = args.input.read_text(encoding="utf-8")
    new_text, removed = deduplicate(text)
    output.write_text(new_text, encoding="utf-8")
    print(f"removed={len(removed)} unique_keys={len(set(removed))} output={output}")


if __name__ == "__main__":
    main()
