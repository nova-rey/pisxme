"""Audit U7 bridge-supply hierarchy without inventing electrical joins."""
from pathlib import Path
import re
R=Path(__file__).resolve().parent
xml=R/'PHASE24_CLEAN_HIERARCHY_REPAIRED.kicadxml'
storage=(R/'STORAGE.kicad_sch').read_text()
regs=(R/'REGULATORS.kicad_sch').read_text()
net=xml.read_text()
storage_ports=re.findall(r'\(hierarchical_label "([^"]+)"',storage)
reg_ports=re.findall(r'\(hierarchical_label "([^"]+)"',regs)
for port in ('BRIDGE_3V3','BRIDGE_1V1'):
    assert port in storage_ports, ('STORAGE missing', port)
    assert port in reg_ports, ('REGULATORS missing', port)
for name in ('BRIDGE_3V3','BRIDGE_1V1'):
    m=re.search(r'<net code="[^"]+" name="'+name+r'"[^>]*>(.*?)</net>',net,re.S)
    assert m, name
    assert '<node ref="U7" pin="' in m.group(1), name
print('U7 supply hierarchy audit: PASS')
print('Native STORAGE and REGULATORS ports present for BRIDGE_3V3 and BRIDGE_1V1')
print('Native exported netlist contains U7 membership on both canonical rails')
