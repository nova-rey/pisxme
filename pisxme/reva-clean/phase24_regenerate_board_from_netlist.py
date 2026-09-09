"""Regenerate PCB pad ownership from a native KiCad XML netlist.

This is an authority-boundary tool, not a router.  It preserves the donor
board's copper and placement, adds only explicitly listed absent support
footprints, and derives every assigned pad net from schematic nodes.  Output
is always a new file.
"""
from pathlib import Path
import argparse
import re
import uuid
import xml.etree.ElementTree as ET
import pcbnew

ROOT = Path(__file__).resolve().parent
LIB = ROOT / 'PiSXMe_RevA_Clean.pretty'
PAD_ALIASES = {
    # EDAC MagJack logical schematic pins 1..18 map to its numbered lands.
    'J2': {'1': ('1',), '2': ('2',), '3': ('3',), '4': ('6',),
           '5': ('7',), '6': ('8',), '7': ('9',), '8': ('10',),
           '9': ('11',), '10': ('12',), '11': ('13',), '12': ('14',),
           '13': ('15',), '14': ('16',), '15': ('17',), '16': ('18',),
           '17': ('19',), '18': ('20',)},
    'F1': {'1': tuple(str(x) for x in range(1, 5)),
           '2': tuple(str(x) for x in range(5, 9))},
    'F2': {'1': tuple(str(x) for x in range(1, 5)),
           '2': tuple(str(x) for x in range(5, 9))},
    'J4': {'1': ('A6', 'B6'), '2': ('A7', 'B7'),
           '3': ('A4', 'A9', 'B4', 'B9'),
           '4': ('A1', 'A12', 'B1', 'B12'),
           '5': ('A5',), '6': ('B5',)},
}
ADD = {
    'C48': ('C_0603_1608Metric', (220, 180)),
    'C49': ('C_0603_1608Metric', (224, 180)),
    'C50': ('C_0603_1608Metric', (228, 180)),
    'C51': ('C_0603_1608Metric', (232, 180)),
    'C52': ('C_1206_3216Metric', (228, 184)),
    'R26': ('R_0402_1005Metric', (220, 184)),
    'R27': ('R_0402_1005Metric', (224, 184)),
    'R28': ('R_0402_1005Metric', (232, 184)),
    'R29': ('R_0402_1005Metric', (236, 184)),
    'R30': ('R_0402_1005Metric', (220, 188)),
    'R31': ('R_0402_1005Metric', (224, 188)),
}

def flat(name):
    return name.rsplit('/', 1)[-1] if name else ''

def add_net(board, name):
    n = board.FindNet(name)
    if n is None:
        n = pcbnew.NETINFO_ITEM(board, name)
        board.Add(n)
    return n

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('board'); ap.add_argument('xml'); ap.add_argument('output')
    a = ap.parse_args()
    b = pcbnew.LoadBoard(a.board)
    tree = ET.parse(a.xml).getroot()
    components = {c.get('ref'): c.findtext('footprint', '')
                  for c in tree.find('components')}
    refs = {f.GetReference(): f for f in b.GetFootprints() if f.GetReference()}
    io = pcbnew.PCB_IO_KICAD_SEXPR()
    for ref, fpname in components.items():
        if ref in refs or ref not in ADD:
            continue
        short = fpname.split(':', 1)[-1]
        if fpname.startswith('Capacitor_SMD:'):
            short = 'C_0805_2012Metric'
        f = io.FootprintLoad(str(LIB), short)
        if f is None:
            raise SystemExit(f'cannot load missing source footprint {ref}: {short}')
        f.SetReference(ref)
        f.SetPosition(pcbnew.VECTOR2I_MM(*ADD[ref][1]))
        b.Add(f); refs[ref] = f

    expected = []
    for net in tree.find('nets'):
        name = flat(net.get('name', ''))
        if not name: continue
        for node in net.findall('node'):
            ref, pin = node.get('ref'), node.get('pin')
            if ref not in refs or ref == 'X7': continue
            if ref == 'J1' and pin in {'PWR', 'GND'}:
                continue
            if ref == 'J3' and pin.isdigit() and 59 <= int(pin) <= 66:
                continue
            pads = PAD_ALIASES.get(ref, {}).get(pin, (pin,))
            for padno in pads:
                p = refs[ref].FindPadByNumber(str(padno))
                if p is None:
                    raise SystemExit(f'missing physical pad {ref}.{padno} for source node {ref}.{pin}')
                expected.append((ref, str(padno), name))

    source_refs = {ref for ref, _, _ in expected}
    for ref in source_refs:
        for p in refs[ref].Pads():
            p.SetNet(None); p.SetNetCode(0)
    nets = {name: add_net(b, name) for _, _, name in expected}
    for ref, padno, name in expected:
        p = refs[ref].FindPadByNumber(padno); n = nets[name]
        p.SetNet(n); p.SetNetCode(n.GetNetCode())
    # Copper inherited from a hierarchical donor may carry the old path
    # spelling.  Normalize only that spelling to the newly exported native
    # net object; geometry is untouched and no connectivity is synthesized.
    for item in list(b.GetPads()) + list(b.GetTracks()) + list(b.Zones()):
        old = item.GetNetname()
        if old and old != flat(old) and flat(old) in nets:
            item.SetNet(nets[flat(old)])
            item.SetNetCode(nets[flat(old)].GetNetCode())
    b.BuildListOfNets(); b.Save(a.output)
    print(f'components={len(components)} assigned_nodes={len(expected)} '
          f'added={sorted(set(ADD)&set(components)-set(refs))} output={a.output}')

if __name__ == '__main__': main()
