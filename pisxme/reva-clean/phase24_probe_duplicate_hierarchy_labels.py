#!/usr/bin/env python3
"""Disposable probe for duplicate boundary/circuit hierarchy labels.

The live REGULATORS and STORAGE children contain a generated boundary label
and a later circuit-facing hierarchical label for two identical rail names.
This probe removes only the earlier boundary label/wire pair in those two
children, retaining the contract symbol and all circuit-facing wiring.
It never edits the source tree.
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

TARGETS = {
    "REGULATORS": {"BRIDGE_3V3": "20.32", "BRIDGE_1V1": "22.86"},
    "STORAGE": {"BRIDGE_3V3": "22.86", "BRIDGE_1V1": "25.4"},
}


def remove_boundary(text: str, name: str, y: str) -> str:
    label = re.compile(
        rf'\s*\(hierarchical_label "{re.escape(name)}"[^\n]*\(at 5\.08 {re.escape(y)} 180\)[\s\S]*?\)\n?'
    )
    text, labels = label.subn("\n", text, count=1)
    if labels != 1:
        raise ValueError(f"{name}@{y}: expected one boundary label, found {labels}")
    wire = re.compile(
        rf'\s*\(wire \(pts \(xy 5\.08 {re.escape(y)}\) \(xy 20\.32 {re.escape(y)}\)\)[\s\S]*?\)\n?'
    )
    text, wires = wire.subn("\n", text, count=1)
    if wires != 1:
        raise ValueError(f"{name}@{y}: expected one boundary wire, found {wires}")
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    src = args.source.resolve(); out = args.output.resolve()
    if out.exists():
        raise SystemExit(f"refusing to overwrite {out}")
    out.mkdir()
    for path in src.iterdir():
        if path.is_file() and path.suffix in {".kicad_sch", ".kicad_pro", ".kicad_sym"}:
            shutil.copy2(path, out / path.name)
    for name in ("sym-lib-table", "fp-lib-table"):
        if (src / name).exists(): shutil.copy2(src / name, out / name)
    pretty = src / "PiSXMe_RevA_Clean.pretty"
    if pretty.exists(): shutil.copytree(pretty, out / pretty.name)
    for child, rails in TARGETS.items():
        path = out / f"{child}.kicad_sch"
        text = path.read_text()
        for name, y in rails.items(): text = remove_boundary(text, name, y)
        path.write_text(text)
    print(out)


if __name__ == "__main__": main()
