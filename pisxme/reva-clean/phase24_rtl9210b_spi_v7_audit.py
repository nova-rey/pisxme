#!/usr/bin/env python3
"""Audit SPI V7 from saved PCB objects only."""
from pathlib import Path
import re
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_SPI_V7.kicad_pcb'
text=PCB.read_text(errors='replace')
if not text: raise SystemExit(f'FAIL missing {PCB}')
for name in ('SPICS','SPISO','SPISO3','SPICLK','SPISI'):
    m=re.search(rf'\(net (\d+) "{name}"\)',text)
    if not m: raise SystemExit(f'FAIL missing net {name}')
    if len(re.findall(rf'\(segment .*?\(net {m.group(1)}\)\)',text,re.S)) < 4:
        raise SystemExit(f'FAIL insufficient saved segments {name}')
pad_xy={(float(x),float(y)) for x,y in re.findall(r'\(pad "[^"]+"[^\n]*\(at ([0-9.\-]+) ([0-9.\-]+)',text)}
via_xy={(float(x),float(y)) for x,y in re.findall(r'\(via \(at ([0-9.\-]+) ([0-9.\-]+)',text)}
if pad_xy & via_xy: raise SystemExit(f'FAIL via-in-pad coordinate collision: {sorted(pad_xy & via_xy)[:3]}')
print('PASS SPI V7 saved-track/net/via audit')
