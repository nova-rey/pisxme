"""Structural audit for the live Phase 24 KiCad hierarchy.

This intentionally does not rewrite schematics.  It parses balanced native
S-expressions so later authoring transforms can address exact top-level
objects instead of matching formatting or unrelated nested symbols.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHILDREN = (
    "CORE_CM5", "V100_PCIE", "V100_POWER", "POWER_INPUT", "REGULATORS",
    "ETHERNET", "STORAGE", "SERVICE", "COOLING", "DEBUG",
)


def end_of_expr(text: str, start: int) -> int:
    depth = 0
    quoted = escaped = False
    for pos in range(start, len(text)):
        char = text[pos]
        if quoted and escaped:
            escaped = False
        elif quoted and char == "\\":
            escaped = True
        elif char == '"':
            quoted = not quoted
        elif not quoted:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    return pos + 1
    raise ValueError(f"unbalanced expression at {start}")


def top_level(text: str) -> list[str]:
    expressions = []
    pos = 0
    while True:
        start = text.find("(", pos)
        if start < 0:
            return expressions
        stop = end_of_expr(text, start)
        expressions.append(text[start:stop])
        pos = stop


def contract_stats(path: Path) -> tuple[int, int, int]:
    text = path.read_text()
    labels = len(re.findall(r'\(hierarchical_label "[^"]+"', text))
    definitions = len(re.findall(r'\(symbol "[^"]+_Contract_1_1"', text))
    instances = len(re.findall(r'\(lib_id "PiSXMeRevAClean:[^"]+_Contract"', text))
    if definitions != 1 or instances != 1:
        raise AssertionError(f"{path.name}: contract def/instance={definitions}/{instances}")
    return labels, definitions, instances


def main() -> None:
    root = ROOT / "PiSXMe_RevA_Clean.kicad_sch"
    root_text = root.read_text()
    assert root_text.startswith("(kicad_sch ")
    lib_end = end_of_expr(root_text, root_text.index("(lib_symbols"))
    instance_start = root_text.index("(sheet_instances", lib_end)
    expressions = top_level(root_text[lib_end:instance_start])
    assert sum(expr.startswith("(sheet") for expr in expressions) == 10
    for child in CHILDREN:
        labels, definitions, instances = contract_stats(ROOT / f"{child}.kicad_sch")
        print(f"{child}: labels={labels} contract_def={definitions} contract_instance={instances}")
    print("Phase 24 structural hierarchy audit: PASS; balanced native expressions")


if __name__ == "__main__":
    main()
