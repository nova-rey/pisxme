#!/usr/bin/env python3
"""Make a disposable native TI-U7 storage route-development fixture.

The fixture retains only the CM5 source, TI bridge, SATA socket, and the
authoritative local support footprints.  It removes inherited board copper
and zones so route quality is evaluated independently from acreage debt.
"""
from pathlib import Path
import argparse
import pcbnew

R = Path(__file__).resolve().parent
KEEP = {
    'J7', 'U7', 'J3', 'C16', 'C17', 'C19', 'C30', 'C31', 'C32', 'C33',
    'Y1', 'R23', 'C42', 'C43', 'R24', 'R32', 'R33'
}
def relevant(name):
    return any(x in name for x in (
        # Keep only the high-speed storage copper in this route-development
        # fixture.  Support footprints remain as real obstacles, but their
        # inherited power/return traces must not bias the escape experiment.
        'CM5_USB3_', 'BRIDGE_SATA_', 'SATA_M2_'))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pcb'); ap.add_argument('output')
    a = ap.parse_args()
    b = pcbnew.LoadBoard(a.pcb)
    if b is None: raise SystemExit('native board load failed')
    # Snapshot native collections before footprint mutation; KiCad 10's
    # Python wrapper invalidates collection proxies during Remove().
    tracks = list(b.GetTracks())
    zones = list(b.Zones())
    for f in list(b.GetFootprints()):
        if f.GetReference() not in KEEP: b.Remove(f)
    for t in tracks:
        if not relevant(t.GetNetname()): b.RemoveNative(t)
    for z in zones: b.RemoveNative(z)
    b.BuildListOfNets(); b.Save(a.output)
    print(f'isolated TI-U7 storage fixture: {a.output}')

if __name__ == '__main__': main()
