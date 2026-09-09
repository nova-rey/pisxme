#!/usr/bin/env python3
"""Correct the live U12 TX-side instance labels in STORAGE.kicad_sch.

The U12 symbol pin functions and the C86/C87 bridge-side labels already use
JMS_USB3_TXP/N.  These two instance labels were stale USB_TXP/N1 labels,
which made the native schematic netlist disagree with the reviewed source
map.  Coordinates identify only this generated U12 label frame; no PCB or
connectivity edges are synthesized.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCH = ROOT / "STORAGE.kicad_sch"
REPLACEMENTS = {
    '(label "USB_TXN1" (at 120 161.825 0)':
        '(label "JMS_USB3_TXN" (at 120 161.825 0)',
    '(label "USB_TXP1" (at 120 160.555 0)':
        '(label "JMS_USB3_TXP" (at 120 160.555 0)',
}
text = SCH.read_text()
for old, new in REPLACEMENTS.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected one U12 instance label {old!r}, found {count}")
    text = text.replace(old, new, 1)
SCH.write_text(text)
print("corrected U12.24/U12.25 instance labels to JMS_USB3_TXN/P")
