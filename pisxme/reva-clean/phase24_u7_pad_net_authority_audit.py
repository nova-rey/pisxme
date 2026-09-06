"""Audit U7 pad ownership against the repaired native KiCad netlist."""
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import pcbnew

R = Path(__file__).resolve().parent
# Keep the audit tied to the latest native export, including the VBUS support
# network.  This must never silently fall back to a stale receipt.
XML = R / 'PHASE24_CLEAN_TUSB_VBUS_DIVIDER.kicadxml'

def expected_u7():
    root = ET.parse(XML).getroot(); out = {}
    for net in root.findall('.//nets/net'):
        for node in net.findall('node'):
            if node.get('ref') == 'U7': out[node.get('pin')] = net.get('name')
    return out

def audit(path):
    b = pcbnew.LoadBoard(str(path)); f = b.FindFootprintByReference('U7')
    if f is None: raise AssertionError('missing U7')
    exp = expected_u7()
    pads = {str(p.GetNumber()): p for p in f.Pads()}
    errors = []
    for num, name in sorted(exp.items()):
        if num not in pads: errors.append(f'missing U7.{num}')
        elif not (pads[num].GetNetname() == name or pads[num].GetNetname().endswith('/' + name)):
            errors.append(f'U7.{num}: {pads[num].GetNetname()!r} != {name!r}')
    for num, pad in sorted(pads.items()):
        if num not in exp and pad.GetNetname():
            errors.append(f'U7.{num}: unsourced stale net {pad.GetNetname()!r}')
    if errors: raise AssertionError('; '.join(errors))
    return True

if __name__ == '__main__':
    audit(Path(sys.argv[1])); print('Phase24 repaired U7 pad-net authority: PASS')
