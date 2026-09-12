#!/usr/bin/env python3
"""Snap the root sheet graphical domain coherently to KiCad's 1.27 mm grid.

The transform starts at the first root `(sheet` form and applies the same
coordinate snap to every root `at`/`xy` pair, keeping sheet pins, wires,
labels, and sheet graphics together.  It is deliberately separate from child
sheet circuit geometry and must be proven by native ERC plus netlist parity.
"""
from pathlib import Path
import argparse
import re

COORD = re.compile(
    r'(\((?:at|xy)\s+)(-?(?:\d+(?:\.\d*)?|\.\d+))(\s+)'
    r'(-?(?:\d+(?:\.\d*)?|\.\d+))'
)


def snap(value: str) -> str:
    return f"{round(float(value) / 1.27) * 1.27:.8g}"


def normalize(text: str) -> str:
    start = text.index("(sheet")
    head, graph = text[:start], text[start:]
    graph = COORD.sub(
        lambda m: m.group(1) + snap(m.group(2)) + m.group(3) + snap(m.group(4)),
        graph,
    )
    return head + graph


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
    output.write_text(normalize(args.input.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"normalized={output}")


if __name__ == "__main__":
    main()
