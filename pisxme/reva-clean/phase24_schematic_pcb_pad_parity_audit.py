#!/usr/bin/env python3
"""Compare native schematic pin ownership with actual PCB pads.

No connectivity is synthesized.  This is an exact ref/pin/net ownership
audit against KiCad's exported native XML netlist.
"""
import argparse
import xml.etree.ElementTree as ET
import pcbnew

def norm_net(name):
    """Compare KiCad XML hierarchical names with PCB's flattened net names."""
    if not name:
        return ''
    return name.rsplit('/', 1)[-1]

def expected(xml):
    out = {}
    root = ET.parse(xml).getroot()
    for net in root.findall('.//nets/net'):
        name = net.get('name')
        for node in net.findall('node'):
            # X7 is the non-BOM, non-board storage contract marker in the
            # schematic; it intentionally has no PCB footprint.
            if node.get('ref') == 'X7':
                continue
            # TE M-key Socket 3 intentionally has no physical contacts 59..66
            # at the key gap.  Those schematic placeholders are mechanical
            # contract data, not missing PCB pads; every other absent pad
            # remains a hard parity failure below.
            if node.get('ref') == 'J3' and node.get('pin', '').isdigit() \
                    and 59 <= int(node.get('pin')) <= 66:
                continue
            out[(node.get('ref'), node.get('pin'))] = norm_net(name)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('pcb'); ap.add_argument('xml'); a=ap.parse_args()
    exp=expected(a.xml); b=pcbnew.LoadBoard(a.pcb)
    actual={(f.GetReference(), str(p.GetNumber())): norm_net(p.GetNetname())
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
