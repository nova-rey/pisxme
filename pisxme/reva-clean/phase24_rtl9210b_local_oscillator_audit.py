#!/usr/bin/env python3
from pathlib import Path
import re
import sys

PCB = Path(__file__).resolve().parent / "PHASE24_RTL9210B_LOCAL_OSCILLATOR.kicad_pcb"
text = PCB.read_text(errors="replace") if PCB.exists() else ""
if not text:
    raise SystemExit(f"FAIL missing {PCB}")
for name in ("XTAL_IN", "XTAL_OUT", "RSET"):
    m = re.search(rf'\(net (\d+) "{name}"\)', text)
    if not m or not re.search(rf'\(segment .*?\(net {m.group(1)}\)\)', text, re.S):
        raise SystemExit(f"FAIL missing saved route {name}")
print("PASS local oscillator/RSET saved-track audit")
