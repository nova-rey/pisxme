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
LATER_Y = {
    "REGULATORS": {"BRIDGE_3V3": "157", "BRIDGE_1V1": "207"},
    "STORAGE": {"BRIDGE_3V3": "101.25", "BRIDGE_1V1": "103.75"},
}


def end_of_expr(text: str, start: int) -> int:
    depth = 0; quoted = escaped = False
    for i in range(start, len(text)):
        c = text[i]
        if quoted and escaped: escaped = False
        elif quoted and c == "\\": escaped = True
        elif c == '"': quoted = not quoted
        elif not quoted:
            if c == "(": depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0: return i + 1
    raise ValueError("unbalanced expression")


def top_level(text: str, start: int, stop: int) -> list[str]:
    result = []; pos = start
    while pos < stop:
        opening = text.find("(", pos, stop)
        if opening < 0: break
        closing = end_of_expr(text, opening)
        result.append(text[opening:closing]); pos = closing
    return result


def remove_boundary(text: str, name: str, y: str) -> str:
    lib_end = end_of_expr(text, text.index("(lib_symbols"))
    tail = text.index("(sheet_instances", lib_end)
    expressions = top_level(text, lib_end, tail)
    label_re = re.compile(rf'\(hierarchical_label "{re.escape(name)}"[\s\S]*?\(at 5\.08 {re.escape(y)} 180\)')
    wire_re = re.compile(rf'\(wire[\s\S]*?\(xy 5\.08 {re.escape(y)}\)[\s\S]*?\(xy 20\.32 {re.escape(y)}\)')
    kept = []; labels = wires = 0
    for expr in expressions:
        if expr.startswith("(hierarchical_label ") and label_re.search(expr) and labels == 0:
            labels += 1; continue
        if expr.startswith("(wire ") and wire_re.search(expr) and wires == 0:
            wires += 1; continue
        kept.append(expr)
    if labels != 1 or wires != 1:
        raise ValueError(f"{name}@{y}: expected one boundary label/wire, found {labels}/{wires}")
    return text[:lib_end] + "\n" + "\n".join(kept) + "\n" + text[tail:]


def localize_boundary(text: str, name: str, y: str) -> str:
    """Keep the contract connection but demote its duplicate label to local."""
    lib_end = end_of_expr(text, text.index("(lib_symbols"))
    tail = text.index("(sheet_instances", lib_end)
    expressions = top_level(text, lib_end, tail)
    label_re = re.compile(rf'\(hierarchical_label "{re.escape(name)}"[\s\S]*?\(at 5\.08 {re.escape(y)} 180\)')
    kept = []; found = 0
    for expr in expressions:
        if expr.startswith("(hierarchical_label ") and label_re.search(expr) and found == 0:
            uuid = re.search(r"\(uuid ([^)]+)\)", expr).group(1)
            kept.append(
                f'  (label "{name}" (at 5.08 {y} 180) '
                f'(effects (font (size 1.27 1.27)) (justify right)) (uuid {uuid}))'
            )
            found += 1
        else:
            kept.append(expr)
    if found != 1:
        raise ValueError(f"{name}@{y}: expected one boundary label, found {found}")
    return text[:lib_end] + "\n" + "\n".join(kept) + "\n" + text[tail:]


def localize_circuit(text: str, name: str, y: str) -> str:
    """Keep the boundary hierarchy label; demote the later circuit label."""
    lib_end = end_of_expr(text, text.index("(lib_symbols"))
    tail = text.index("(sheet_instances", lib_end)
    expressions = top_level(text, lib_end, tail)
    label_re = re.compile(rf'\(hierarchical_label "{re.escape(name)}"[\s\S]*?\(at 5 {re.escape(y)} 180\)')
    kept = []; found = 0
    for expr in expressions:
        if expr.startswith("(hierarchical_label ") and label_re.search(expr) and found == 0:
            uuid = re.search(r"\(uuid ([^)]+)\)", expr).group(1)
            kept.append(
                f'  (label "{name}" (at 5 {y} 180) '
                f'(effects (font (size 1 1)) (justify right)) (uuid {uuid}))'
            )
            found += 1
        else:
            kept.append(expr)
    if found != 1:
        raise ValueError(f"{name}@{y}: expected one circuit label, found {found}")
    return text[:lib_end] + "\n" + "\n".join(kept) + "\n" + text[tail:]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--mode", choices=("remove", "local", "circuit-local"), default="remove")
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
        for name, y in rails.items():
            if args.mode == "local":
                text = localize_boundary(text, name, y)
            elif args.mode == "circuit-local":
                text = localize_circuit(text, name, LATER_Y[child][name])
            else:
                text = remove_boundary(text, name, y)
        path.write_text(text)
    print(out)


if __name__ == "__main__": main()
