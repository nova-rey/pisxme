"""Compare the native Phase 24 netlist reference set to a PCB baseline."""
from pathlib import Path
import re

R=Path(__file__).resolve().parent
NETLIST=R/'PHASE24_NETLIST_FINAL5.xml'
BOARD=R/'PHASE24_ALL_AUTHORITATIVE_PARTS.kicad_pcb'
EXPECTED_EXTRAS={'CCT','CCT1','CCT2','CCT3','CCT4','RCT1','RCT2','RCT3','RCT4','MECH_M2_2280',*[f'TP{i}' for i in range(1,14)]}
net_refs=set(re.findall(r'\(ref "([^"]+)"\)',NETLIST.read_text()))
pcb_refs=set(re.findall(r'\(property "Reference" "([^"]+)"',BOARD.read_text()))
missing=net_refs-pcb_refs;extras=pcb_refs-net_refs
assert not missing, f'missing schematic references: {sorted(missing)}'
assert extras==EXPECTED_EXTRAS, f'unexpected PCB-only references: {sorted(extras-EXPECTED_EXTRAS)} / missing expected extras: {sorted(EXPECTED_EXTRAS-extras)}'
print(f'Phase24 full reference-set audit: PASS; schematic={len(net_refs)} PCB={len(pcb_refs)} expected extras={len(extras)}')
