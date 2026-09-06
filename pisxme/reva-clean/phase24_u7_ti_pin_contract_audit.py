#!/usr/bin/env python3
"""Fail-closed audit of mandatory TUSB9261 PVP package pins in the netlist."""
from pathlib import Path
import xml.etree.ElementTree as ET

R=Path(__file__).resolve().parent
XML=R/'PHASE24_CLEAN_HIERARCHY_REPAIRED.kicadxml'
MANDATORY={
 '1','7','12','19','24','32','33','34','40','41','47','48','49','50','51',
 '55','61','62','63','65', # supplies, USB VBUS, thermal pad
 '35','36','38','39','44','53','58', # USB2/reference/ground/oscillator
}

root=ET.parse(XML).getroot()
nodes={n.get('pin'): net.get('name') for net in root.findall('.//nets/net')
       for n in net.findall('node') if n.get('ref')=='U7'}
missing=sorted(MANDATORY-set(nodes))
print('mandatory TI U7 pins:', ', '.join(sorted(MANDATORY,key=int)))
print('represented in clean netlist:', ', '.join(sorted(nodes,key=int)))
print('missing from clean symbol/netlist:', ', '.join(missing) or 'none')
if missing: raise SystemExit(1)
print('TUSB9261 mandatory pin contract: PASS')
