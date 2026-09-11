#!/usr/bin/env python3
"""Disposable live-contract regeneration using signal identity and coordinates.

The root sheet and child circuit are copied verbatim.  Only each child's
embedded contract symbol and instance pin list are regenerated.  Pin names
are matched by the live hierarchical-label identity; their Y coordinates are
copied into the contract symbol relative to its existing instance anchor.
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

CHILDREN = ("CORE_CM5", "V100_PCIE", "V100_POWER", "POWER_INPUT", "REGULATORS",
            "ETHERNET", "STORAGE", "SERVICE", "COOLING", "DEBUG")


def balanced(text: str, start: int) -> int:
    depth = 0; quoted = escaped = False
    for i in range(start, len(text)):
        c = text[i]
        if quoted and escaped: escaped = False
        elif quoted and c == "\\": escaped = True
        elif c == '"': quoted = not quoted
        elif not quoted:
            depth += c == "("; depth -= c == ")"
            if depth == 0: return i + 1
    raise ValueError("unbalanced expression")


def live_labels(text: str) -> list[tuple[str, float, float]]:
    return [(n, float(x), float(y)) for n, x, y in re.findall(
        r'\(hierarchical_label "([^"]+)"\s+\(shape [^)]*\)\s+\(at ([^ ]+) ([^ ]+)', text)]


def pin(name: str, number: int, y: float) -> str:
    return (f'        (pin passive line\n'
            f'          (at -5.08 {y:g} 0)\n'
            f'          (length 3.81)\n'
            f'          (name "{name}" (effects (font (size 1.27 1.27))))\n'
            f'          (number "{number}" (effects (font (size 1.27 1.27)))))')


def rewrite_child(text: str, child: str) -> str:
    labels = live_labels(text)
    if not labels: raise ValueError(f"{child}: no hierarchical labels")
    names = [n for n, _x, _y in labels]
    if len(names) != len(set(names)): raise ValueError(f"{child}: duplicate labels")
    symbol_start = text.index(f'(symbol "{child}_Contract_1_1"')
    symbol_end = balanced(text, symbol_start)
    symbol = text[symbol_start:symbol_end]
    first = symbol.index("        (pin passive line")
    close = symbol.rfind("      )")
    if close < first: raise ValueError(f"{child}: malformed contract symbol")
    # Contract instance is anchored at (25,10); the wire endpoint is x=19.92.
    # Preserve the live label coordinates, including sparse support-port banks.
    pins = "\n".join(pin(name, i + 1, -(y - 10.0))
                      for i, (name, _x, y) in enumerate(labels))
    new_symbol = symbol[:first] + pins + "\n" + symbol[close:]
    text = text[:symbol_start] + new_symbol + text[symbol_end:]

    inst_marker = text.index(f'(lib_id "PiSXMeRevAClean:{child}_Contract"')
    inst_start = text.rfind("(symbol", 0, inst_marker)
    inst_end = balanced(text, inst_start)
    instance = text[inst_start:inst_end]
    existing = re.findall(r'    \(pin "(\d+)" \(uuid ([^)]+)\)\)', instance)
    uuids = {int(n): u for n, u in existing}
    pin_lines = []
    for i in range(len(names)):
        n = i + 1
        uid = uuids.get(n, f"a9000000-0000-0000-0000-{n:012x}")
        pin_lines.append(f'    (pin "{n}" (uuid {uid}))')
    first_pin = instance.find('    (pin "')
    marker = instance.index("    (instances ")
    if first_pin < 0: first_pin = marker
    new_instance = instance[:first_pin] + "\n".join(pin_lines) + "\n" + instance[marker:]
    return text[:inst_start] + new_instance + text[inst_end:]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args(); src = args.source.resolve(); out = args.output.resolve()
    if out.exists(): raise SystemExit(f"refusing to overwrite {out}")
    out.mkdir()
    for path in src.glob("*"):
        if path.is_file() and path.suffix in {".kicad_sch", ".kicad_pro", ".kicad_sym", ".table"}:
            shutil.copy2(path, out / path.name)
    for name in ("sym-lib-table", "fp-lib-table"):
        if (src / name).exists(): shutil.copy2(src / name, out / name)
    pretty = src / "PiSXMe_RevA_Clean.pretty"
    if pretty.exists(): shutil.copytree(pretty, out / pretty.name)
    for child in CHILDREN:
        path = out / f"{child}.kicad_sch"
        path.write_text(rewrite_child(path.read_text(), child))
    print(out)


if __name__ == "__main__": main()
