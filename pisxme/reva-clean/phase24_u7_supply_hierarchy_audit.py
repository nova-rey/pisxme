"""Audit U7 bridge-supply hierarchy without inventing electrical joins."""
from pathlib import Path
import re
R=Path(__file__).resolve().parent
xml=Path(__file__).resolve().parents[2]/'PiSXMe_RevA_Clean.xml'
storage=(R/'STORAGE.kicad_sch').read_text()
regs=(R/'REGULATORS.kicad_sch').read_text()
net=xml.read_text()
storage_ports=re.findall(r'\(hierarchical_label "([^"]+)"',storage)
reg_ports=re.findall(r'\(hierarchical_label "([^"]+)"',regs)
assert 'BRIDGE_3V3' not in storage_ports and 'BRIDGE_1V1' not in storage_ports
assert 'BRIDGE_3V3' not in reg_ports and 'BRIDGE_1V1' not in reg_ports
for name in ('/STORAGE/BRIDGE_3V3','/STORAGE/BRIDGE_1V1','/REGULATORS/BRIDGE_3V3','/REGULATORS/BRIDGE_1V1'):
    assert ('name="%s"' % name) in net, name
print('U7 supply hierarchy audit: FAIL CLOSED')
print('Missing STORAGE child ports: BRIDGE_3V3, BRIDGE_1V1')
print('Missing REGULATORS child ports: BRIDGE_3V3, BRIDGE_1V1')
print('No synthetic net join was added; hierarchy repair is required before U7 supply closure.')
