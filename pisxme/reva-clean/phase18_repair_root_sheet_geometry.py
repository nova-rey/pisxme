"""Repair the existing root hierarchy's overlapping second sheet row.

This is a deterministic migration for the already-populated clean project;
it does not regenerate child sheets or change their electrical contracts.
"""
from pathlib import Path
import re
from phase3_scaffold import balanced

ROOT = Path(__file__).resolve().parent
ROOT_SCH = ROOT / "PiSXMe_RevA_Clean.kicad_sch"
SHIFT = 35.0


def shift_sheet(block: str) -> str:
    def repl(match):
        x, y = match.group(1), match.group(2)
        try:
            value = float(y)
        except ValueError:
            return match.group(0)
        return "(at %s %g" % (x, value + SHIFT)
    return re.sub(r"\(at ([^ ]+) ([^ )]+)", repl, block)


def shift_wire(block: str) -> str:
    def repl(match):
        x, y = match.group(1), match.group(2)
        return "(xy %s %g" % (x, float(y) + SHIFT)
    return re.sub(r"\(xy ([^ ]+) ([^ )]+)", repl, block)


def main() -> None:
    text = ROOT_SCH.read_text()
    pos = 0
    sheets = []
    for _ in range(10):
        start = text.index("  (sheet", pos)
        block = balanced(text, start)
        sheets.append((start, start + len(block), block))
        pos = start + len(block)
    for index in range(5, 10):
        start, end, block = sheets[index]
        sheets[index] = (start, end, shift_sheet(block))
    out = []
    cursor = 0
    for start, end, block in sheets:
        out.append(text[cursor:start])
        out.append(block)
        cursor = end
    text = "".join(out) + text[cursor:]

    # Root wiring is emitted per sheet with b000... UUIDs.  UUID suffixes
    # 0x258..0x3eb are the second-row contracts; shift only those wires.
    def wire_repl(match):
        block = match.group(0)
        uuid = re.search(r"\(uuid [0-9a-f-]*([0-9a-f]{12})\)", block)
        if uuid and int(uuid.group(1), 16) >= 0x258:
            return shift_wire(block)
        return block
    text = re.sub(r"  \(wire\n.*?\n    \(uuid [0-9a-f-]+\)\)", wire_repl, text, flags=re.S)
    ROOT_SCH.write_text(text)
    print("Phase 18 root hierarchy geometry repaired: second-row sheets and wires separated")


if __name__ == "__main__":
    main()
