#!/usr/bin/env python3
"""Audit the SPI B.Cu experiment for real saved tracks and ordinary vias."""
from pathlib import Path
import re
import sys

PCB = Path(__file__).resolve().parent / "PHASE24_RTL9210B_SPI_BCU_FIXTURE.kicad_pcb"
NAMES = ("SPICS", "SPISO", "SPISI", "SPICLK", "SPISO3")

text = PCB.read_text(errors="replace") if PCB.exists() else ""
if not text:
    raise SystemExit(f"FAIL missing {PCB}")
for name in NAMES:
    m = re.search(rf'\(net (\d+) "{name}"\)', text)
    if not m:
        raise SystemExit(f"FAIL missing net {name}")
    code = m.group(1)
    if not re.search(rf'\(segment .*?\(net {code}\)\)', text, re.S):
        raise SystemExit(f"FAIL missing saved segment {name}")
    if not re.search(rf'\(via .*?\(net {code}\)\)', text, re.S):
        raise SystemExit(f"FAIL missing ordinary via {name}")
    # Compare actual saved pad/via coordinates rather than using a broad text
    # window that can confuse unrelated later objects.
    pad_xy = {
        (float(x), float(y))
        for x, y in re.findall(r'\(pad "[^"]+"[^\n]*\(at ([0-9.\-]+) ([0-9.\-]+)', text)
    }
    via_xy = {
        (float(x), float(y))
        for x, y in re.findall(r'\(via \(at ([0-9.\-]+) ([0-9.\-]+)', text)
    }
    if pad_xy & via_xy:
        raise SystemExit(f"FAIL via-in-pad coordinate collision: {sorted(pad_xy & via_xy)[:3]}")
print("PASS SPI B.Cu saved-track/via audit")
