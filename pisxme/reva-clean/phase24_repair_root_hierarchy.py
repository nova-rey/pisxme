"""Repair root-sheet connectivity using native sheet-edge stubs and labels.

The early scaffold emitted wires into the sheet interior and diagonal wires
between unrelated sheet edges.  KiCad parses those wires but does not treat
them as connected hierarchical pins.  This deterministic repair keeps the
child sheets and their UUID associations unchanged and emits one outward stub
and one root net label for every root sheet pin.
"""

from pathlib import Path
from uuid import UUID
import re

ROOT = Path(__file__).resolve().parent
SCHEMATIC = ROOT / "PiSXMe_RevA_Clean.kicad_sch"


def balanced(text: str, start: int) -> int:
    depth = 0
    quoted = False
    escaped = False
    for i in range(start, len(text)):
        c = text[i]
        if quoted and escaped:
            escaped = False
        elif quoted and c == "\\":
            escaped = True
        elif c == '"':
            quoted = not quoted
        elif not quoted:
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    return i + 1
    raise ValueError("unbalanced KiCad expression")


def uuid_for(index: int) -> str:
    return str(UUID(int=0xD0000000000000000000000000000000 + index))


def top_level_expressions(text: str, start: int, end: int):
    pos = start
    while pos < end:
        opening = text.find("(", pos, end)
        if opening < 0:
            break
        closing = balanced(text, opening)
        yield opening, closing, text[opening:closing]
        pos = closing


def main() -> None:
    text = SCHEMATIC.read_text()
    lib_start = text.index("(lib_symbols")
    lib_end = balanced(text, lib_start)
    tail_end = text.rindex("  (sheet_instances")

    sheets = []
    for start, end, expression in top_level_expressions(text, lib_end, tail_end):
        if expression.startswith("(sheet\n") or expression.startswith("(sheet\r"):
            # A legacy scaffold allowed the final CM5 pin to fall one mm below
            # the sheet border.  Extend only such sheets to the last pin; this
            # changes no pin UUID, placement, or child association.
            coords = [
                (float(x), float(y))
                for x, y in re.findall(r'\(pin "[^"]+"[^\n]*\(at\s+([0-9.+-]+)\s+([0-9.+-]+)', expression)
            ]
            top_match = re.search(r'\(at\s+([0-9.+-]+)\s+([0-9.+-]+)\)\n\s+\(size\s+([0-9.+-]+)\s+([0-9.+-]+)\)', expression)
            if coords and top_match:
                top_y = float(top_match.group(2))
                height = float(top_match.group(4))
                required = max(y for _x, y in coords) - top_y
                if required > height:
                    expression = expression[:top_match.start(4)] + f"{required:g}" + expression[top_match.end(4):]
            sheets.append(expression)

    pins = []
    for sheet in sheets:
        pin_search = 0
        while True:
            marker = sheet.find('(pin "', pin_search)
            if marker < 0:
                break
            pin_end = balanced(sheet, marker)
            pin = sheet[marker:pin_end]
            header = pin.splitlines()[0]
            name = header.split('"', 2)[1]
            match = re.search(r"\(at\s+([0-9.+-]+)\s+([0-9.+-]+)", pin)
            if not match:
                raise ValueError(f"sheet pin lacks coordinates: {name}")
            x, y = match.groups()
            pins.append((name, x, y))
            pin_search = pin_end

    # Remove only root-level wire expressions.  Existing labels and sheets are
    # preserved, including native project sheet-instance associations.
    kept = list(sheets)
    for start, end, expression in top_level_expressions(text, lib_end, tail_end):
        if not expression.startswith("(sheet") and not expression.startswith("(wire") and not expression.startswith('(global_label "POWER_GND"'):
            kept.append(expression)

    additions = []
    for index, (name, x, y) in enumerate(pins):
        left = f"{float(x) - 10:g}"
        additions.append(
            f'''  (wire (pts (xy {left} {y}) (xy {x} {y}))
    (stroke (width 0) (type default))
    (uuid {uuid_for(index)}))
  (global_label "{name}" (shape bidirectional) (at {left} {y} 0)
    (effects (font (size 1.27 1.27)) (justify right))
    (uuid {uuid_for(1000 + index)}))'''
        )

    rebuilt = text[:lib_end] + "\n" + "\n".join(kept) + "\n" + "\n".join(additions) + "\n" + text[tail_end:]
    SCHEMATIC.write_text(rebuilt)
    print(f"repaired root hierarchy: {len(sheets)} sheets, {len(pins)} pins, {len(additions)} labelled stubs")


if __name__ == "__main__":
    main()
