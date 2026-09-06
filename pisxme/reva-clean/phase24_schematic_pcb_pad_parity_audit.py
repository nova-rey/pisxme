#!/usr/bin/env python3
"""Compare native schematic pin ownership with actual PCB pads.

No connectivity is synthesized.  This is an exact ref/pin/net ownership
audit against KiCad's exported native XML netlist.
"""
import argparse
import xml.etree.ElementTree as ET
import pcbnew

def expected(xml):
    out = {}
    root = ET.parse(xml).getroot()
    for net in root.findall('.//nets/net'):
        name = net.get('name')
        for node in net.findall('node'):
            out[(node.get('ref'), node.get('pin'))] = name
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('pcb'); ap.add_argument('xml'); a=ap.parse_args()
    exp=expected(a.xml); b=pcbnew.LoadBoard(a.pcb)
    actual={(f.GetReference(), str(p.GetNumber())): p.GetNetname()
            for f in b.GetFootprints() for p in f.Pads()}
    mismatches=[]
    for key,name in sorted(exp.items()):
        if key not in actual: mismatches.append(f'MISSING {key[0]}.{key[1]} expected {name}')
        elif actual[key] != name: mismatches.append(f'WRONG {key[0]}.{key[1]}: {actual[key]!r} != {name!r}')
    print(f'authoritative schematic nodes: {len(exp)}; PCB pads: {len(actual)}')
    print(f'expected-pad mismatches: {len(mismatches)}')
    for line in mismatches[:200]: print(line)
    if mismatches: raise SystemExit(1)
    print('schematic-to-PCB pad-net parity: PASS')

if __name__ == '__main__': main()
