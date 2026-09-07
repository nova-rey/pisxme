"""Repair the source-authority names for HD3SS3412 Port A1.

The TI RUA0042A datasheet defines Port A as the shared M.2-side path.  The
prior generated symbol accidentally called A1 a second PCIe TX pair, so the
SATA receive pair could not be represented through U13.  This narrow repair
updates only the U13 library symbol and U13 instance labels in STORAGE.
"""
from pathlib import Path
from phase3_scaffold import balanced

ROOT = Path(__file__).resolve().parent
SCH = ROOT / "STORAGE.kicad_sch"
OLD = ("M2_PCIE_TXP1", "M2_PCIE_TXN1")
NEW = ("M2_SATA_B_P_PCIE_RXN0", "M2_SATA_B_N_PCIE_RXP0")

def replace_pair(text):
    for old, new in zip(OLD, NEW):
        text = text.replace(f'"{old}"', f'"{new}"')
    return text

def main():
    text = SCH.read_text()
    start = text.index('(symbol "PiSXMeRevAClean:HD3SS3412_RUA0042A"')
    end = start + len(balanced(text, start))
    lib = replace_pair(text[start:end])
    text = text[:start] + lib + text[end:]
    marker = '(symbol (lib_id "PiSXMeRevAClean:HD3SS3412_RUA0042A")'
    start = text.index(marker)
    end = start + len(balanced(text, start))
    inst = replace_pair(text[start:end])
    text = text[:start] + inst + text[end:]
    SCH.write_text(text)
    print(f"repaired {SCH}")

if __name__ == "__main__":
    main()
