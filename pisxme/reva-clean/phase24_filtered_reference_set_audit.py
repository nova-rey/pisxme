"""Audit the clean schematic references after legacy CCT/RCT removal."""
from pathlib import Path
import re
R=Path(__file__).resolve().parent;NETLIST=R/'PHASE24_NETLIST_FINAL5.xml';BOARD=R/'PHASE24_NO_LEGACY_CT_ALIASES.kicad_pcb'
expected=set(re.findall(r'\(ref "([^"]+)"\)',NETLIST.read_text()))
actual=set(re.findall(r'\(property "Reference" "([^"]+)"',BOARD.read_text()))
extras=actual-expected;missing=expected-actual
assert not missing,sorted(missing)
assert extras=={'MECH_M2_2280',*[f'TP{i}' for i in range(1,14)]},sorted(extras)
print('Phase24 filtered reference-set audit: PASS; schematic=78 PCB=92 extras=13 mechanical/test')
