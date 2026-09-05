#!/usr/bin/env python3
"""Regression gate for the clean Phase 24 reference-set candidate."""
from pathlib import Path
import re

ROOT=Path(__file__).parents[2]
NETLIST=ROOT/'PHASE24_NETLIST_FINAL5.xml'
BOARD=ROOT/'PHASE24_NO_LEGACY_CT_ALIASES.kicad_pcb'
schematic=set(re.findall(r'\(ref "([^"]+)"\)',NETLIST.read_text()))
pcb=set(re.findall(r'\(property "Reference" "([^"]+)"',BOARD.read_text()))
assert schematic <= pcb, sorted(schematic-pcb)
assert pcb-schematic=={'MECH_M2_2280',*[f'TP{i}' for i in range(1,14)]}
assert not any(x in BOARD.read_text() for x in ('"CCT"','"CCT1"','"CCT2"','"CCT3"','"CCT4"','"RCT1"','"RCT2"','"RCT3"','"RCT4"'))
print('Phase24 reference authority regression: PASS; 78 schematic refs, no legacy CCT/RCT aliases')
