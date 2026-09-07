#!/usr/bin/env python3
"""Generate a support-island placement variant without changing net authority."""
from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_BRINGUP_FIXTURE.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb"

TARGETS = {
    "Y1": (70.0, 55.0), "C1": (67.0, 55.0), "C2": (73.0, 55.0),
    "R1": (70.0, 51.0), "U2": (95.0, 58.0),
    "C3": (101.0, 51.0), "C4": (104.0, 51.0), "C5": (107.0, 51.0),
    "R2": (110.0, 51.0), "R3": (113.0, 51.0),
}
ORIGINAL = {
    "Y1": (88.0, 48.0), "C1": (91.0, 48.0), "C2": (94.0, 48.0),
    "R1": (97.0, 48.0), "U2": (104.0, 48.0),
    "C3": (109.0, 48.0), "C4": (112.0, 48.0), "C5": (115.0, 48.0),
    "R2": (118.0, 48.0), "R3": (121.0, 48.0),
}


def blocks(text: str):
    start = 0
    while True:
        start = text.find('  (footprint "', start)
        if start < 0:
            return
        depth = 0
        end = start
        while end < len(text):
            if text[end] == '(':
                depth += 1
            elif text[end] == ')':
                depth -= 1
                if depth == 0:
                    yield start, end + 1, text[start:end + 1]
                    start = end + 1
                    break
            end += 1


def translate(block: str, dx: float, dy: float) -> str:
    def move(m):
        x, y, rest = float(m.group(1)), float(m.group(2)), m.group(3)
        return f'(at {x + dx:.3f} {y + dy:.3f}{rest})'
    return re.sub(r'\(at ([0-9.\-]+) ([0-9.\-]+)([^)]*)\)', move, block)


def main() -> None:
    text = BASE.read_text()
    replacements = []
    for start, end, block in blocks(text):
        ref = re.search(r'\(property "Reference" "([^"]+)"', block)
        if not ref or ref.group(1) not in TARGETS:
            continue
        name = ref.group(1)
        dx = TARGETS[name][0] - ORIGINAL[name][0]
        dy = TARGETS[name][1] - ORIGINAL[name][1]
        replacements.append((start, end, translate(block, dx, dy)))
    for start, end, replacement in reversed(replacements):
        text = text[:start] + replacement + text[end:]
    OUT.write_text(text)
    print(OUT)


if __name__ == "__main__":
    main()
