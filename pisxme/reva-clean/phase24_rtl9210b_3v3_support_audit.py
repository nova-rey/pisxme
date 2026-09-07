#!/usr/bin/env python3
"""Audit RTL_3V3 support from saved PCB geometry."""
from pathlib import Path
import re
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_3V3_SUPPORT.kicad_pcb'; t=PCB.read_text(errors='replace')
if '(net "RTL_3V3")' not in t: raise SystemExit('FAIL missing RTL_3V3')
if len(re.findall(r'\(segment .*?\(net "RTL_3V3"\)\)',t,re.S))<6: raise SystemExit('FAIL incomplete RTL_3V3 bus')
print('PASS RTL_3V3 support saved-net audit')
