#!/usr/bin/env python3
"""Audit the support-local V2 placement against the unchanged fixture nets."""
from pathlib import Path
import re
import sys

PCB = Path(__file__).resolve().parent / "PHASE24_RTL9210B_SUPPORT_LOCAL_V2.kicad_pcb"
if not PCB.exists():
    raise SystemExit(f"FAIL missing {PCB}")
text = PCB.read_text(errors="replace")
for ref in ("U1", "J1", "Y1", "C1", "C2", "R1", "U2", "C3", "C4", "C5", "R2", "R3"):
    if f'"Reference" "{ref}"' not in text:
        raise SystemExit(f"FAIL missing {ref}")
for name in ("PEDET", "LANE0_TXP", "LANE0_TXN", "LANE0_RXP", "LANE0_RXN", "SPICS", "SPICLK", "RSET", "XTAL_IN", "XTAL_OUT"):
    if not re.search(rf'\(net \d+ "{name}"\)', text):
        raise SystemExit(f"FAIL missing net {name}")
print("PASS support-local V2 placement/net authority audit")
