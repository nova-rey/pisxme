#!/usr/bin/env python3
"""Remove six isolated legacy M.2 labels from the storage source.

These labels are not attached to a wire or pin; the authoritative J3 symbol
labels and U13/J3 nets remain elsewhere in the same sheet.
"""
from pathlib import Path
from phase3_scaffold import balanced

ROOT = Path(__file__).resolve().parent
SCHEMATIC = ROOT / "STORAGE.kicad_sch"
NAMES = ("M2_SATA_A_P_PCIE_TXP0", "M2_SATA_A_N_PCIE_TXN0",
         "M2_SATA_B_N_PCIE_RXP0", "M2_SATA_B_P_PCIE_RXN0",
         "M2_3V3", "M2_GND")

def main():
    text = SCHEMATIC.read_text()
    start = text.index('(label "M2_SATA_A_P_PCIE_TXP0" (at 130 88.75')
    removed = 0
    for name in NAMES:
        needle = f'(label "{name}"'
        pos = text.find(needle, start)
        if pos < 0 or pos >= start + 2000:
            raise SystemExit(f"missing isolated label {name}")
        end = pos + len(balanced(text, pos))
        text = text[:pos] + text[end:]
        removed += 1
    SCHEMATIC.write_text(text)
    print(f"removed {removed} isolated legacy M.2 labels")

if __name__ == "__main__": main()
