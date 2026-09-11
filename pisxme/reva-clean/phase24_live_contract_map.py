#!/usr/bin/env python3
"""Extract the live root/child hierarchy contract by signal identity.

This is an authority-inspection tool, not a connectivity generator.  It reads
the saved KiCad source and reports the exact mapping available in both sides
of each sheet.  It refuses duplicate or missing identities so a later native
authoring step cannot silently fall back to positional association.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

CHILDREN = (
    "CORE_CM5", "V100_PCIE", "V100_POWER", "POWER_INPUT", "REGULATORS",
    "ETHERNET", "STORAGE", "SERVICE", "COOLING", "DEBUG",
)


def balanced(text: str, start: int) -> str:
    depth = 0
    quoted = escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if quoted and escaped:
            escaped = False
        elif quoted and char == "\\":
            escaped = True
        elif char == '"':
            quoted = not quoted
        elif not quoted:
            depth += char == "("
            depth -= char == ")"
            if depth == 0:
                return text[start:index + 1]
    raise ValueError("unbalanced KiCad expression")


def unique(values: list[str], label: str) -> list[str]:
    if len(values) != len(set(values)):
        duplicates = sorted({value for value in values if values.count(value) > 1})
        raise ValueError(f"{label}: duplicate identities: {duplicates}")
    return values


def root_sheets(text: str) -> dict[str, list[str]]:
    result = {}
    for match in re.finditer(r"\(sheet\s*\n", text):
        block = balanced(text, match.start())
        name_match = re.search(r'\(property "Sheetname" "([^"]+)"', block)
        if not name_match:
            continue
        name = name_match.group(1)
        pins = re.findall(r'\(pin "([^"]+)"\s+bidirectional', block)
        result[name] = unique(pins, f"root/{name}")
    return result


def child_labels(path: Path) -> list[str]:
    labels = re.findall(r'\(hierarchical_label "([^"]+)"', path.read_text())
    return unique(labels, str(path))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent / "PiSXMe_RevA_Clean.kicad_sch")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    sheets = root_sheets(root.read_text())
    missing = sorted(set(CHILDREN) - set(sheets))
    if missing:
        raise SystemExit(f"missing root sheets: {missing}")
    records = []
    for child in CHILDREN:
        labels = child_labels(root.parent / f"{child}.kicad_sch")
        pins = sheets[child]
        by_name = {name: index + 1 for index, name in enumerate(pins)}
        records.append({
            "child": child,
            "root_sheet_pin_count": len(pins),
            "child_label_count": len(labels),
            "identity_match": set(pins) == set(labels),
            "root_pins": [{"name": name, "root_pin_index": by_name[name]} for name in pins],
            "child_labels": labels,
        })
    result = {"schema": 1, "source_root": str(root), "children": records}
    output = args.output
    if output:
        output.write_text(json.dumps(result, indent=2) + "\n")
    else:
        print(json.dumps(result, indent=2))
    mismatches = [r["child"] for r in records if not r["identity_match"]]
    if mismatches:
        raise SystemExit(f"identity mismatch in live contract: {mismatches}")
    print(f"PASS live contract identity map: {len(records)} children")


if __name__ == "__main__":
    main()
