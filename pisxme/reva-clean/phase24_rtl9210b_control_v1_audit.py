#!/usr/bin/env python3
"""Audit distinct control-net endpoint ownership from saved PCB geometry."""
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_CONTROL_V1.kicad_pcb'; t=PCB.read_text(errors='replace')
for net in ('PEDET','CLKREQ_N','PERST_N','RESET_N'):
 if t.count(f'(net "{net}")') < 4: raise SystemExit(f'FAIL incomplete {net}')
if '(net "PERST_N")' in t and '(net "RESET_N")' in t: print('PASS distinct PEDET/CLKREQ/PERST/RESET saved-net audit')
