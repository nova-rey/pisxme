#!/usr/bin/env python3
"""Audit the V7 oscillator/RSET route without supplying graph edges."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
PCB = HERE / "PHASE24_RTL9210B_LOCAL_OSCILLATOR_V7.kicad_pcb"
text = PCB.read_text(errors="replace")
if not text:
    raise SystemExit(f"FAIL missing {PCB}")
for name in ("XTAL_IN", "XTAL_OUT", "RSET"):
    m = re.search(rf'\(net (\d+) "{name}"\)', text)
    if not m:
        raise SystemExit(f"FAIL missing net {name}")
    if len(re.findall(rf'\(segment .*?\(net {m.group(1)}\)\)', text, re.S)) < 4:
        raise SystemExit(f"FAIL insufficient saved segments {name}")
if text.count('(via (at ') < 6:
    raise SystemExit("FAIL expected ordinary-via transitions")
print("PASS V7 local oscillator/RSET authority and saved-track audit")
