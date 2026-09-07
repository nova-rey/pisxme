#!/usr/bin/env python3
"""Audit PERST_N saved connections at U1, J1, and TP6."""
from pathlib import Path
import re
t=(Path(__file__).resolve().parent/'PHASE24_RTL9210B_PERST.kicad_pcb').read_text(errors='replace')
if t.count('(net "PERST_N")') < 5: raise SystemExit('FAIL incomplete PERST_N saved copper')
for xy in ('82.000 65.950','136.000 70.275','108.000 78.000'):
 if xy not in t: raise SystemExit('FAIL missing endpoint '+xy)
print('PASS PERST_N saved-net endpoint audit')
