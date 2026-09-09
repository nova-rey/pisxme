"""Correct the live U13 instance labels from the reviewed MUX authority.

This is deliberately narrow and fail-closed: it edits only the two exact
labels belonging to U13 pin 6/7 in STORAGE.kicad_sch.  It does not synthesize
PCB connectivity or alter any other schematic instance.
"""
from pathlib import Path

SCH = Path(__file__).resolve().parent / "STORAGE.kicad_sch"

REPLACEMENTS = {
    '(label "M2_PCIE_TXP1" (at 170 184.685 0)':
        '(label "M2_SATA_B_P_PCIE_RXN0" (at 170 184.685 0)',
    '(label "M2_PCIE_TXN1" (at 170 183.415 0)':
        '(label "M2_SATA_B_N_PCIE_RXP0" (at 170 183.415 0)',
}

def main():
    text = SCH.read_text()
    for old, new in REPLACEMENTS.items():
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"expected exactly one U13 label {old!r}, found {count}")
        text = text.replace(old, new, 1)
    SCH.write_text(text)
    print("corrected U13 pins 6/7 to M.2 SATA-B / PCIe lane-0 RX authority")

if __name__ == "__main__":
    main()
