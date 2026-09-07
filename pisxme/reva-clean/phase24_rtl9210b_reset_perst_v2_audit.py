#!/usr/bin/env python3
"""Audit separate RESET_N and PERST_N saved endpoints."""
from pathlib import Path
t=(Path(__file__).resolve().parent/'PHASE24_RTL9210B_RESET_PERST_V2.kicad_pcb').read_text(errors='replace')
for net in ('RESET_N','PERST_N'):
 if t.count(f'(net "{net}")') < 4: raise SystemExit(f'FAIL incomplete {net}')
print('PASS separate RESET_N/PERST_N saved-net audit')
