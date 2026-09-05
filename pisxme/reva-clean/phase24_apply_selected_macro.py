"""Materialize the selected Phase 24 macro placement for route regeneration.

This is a disposable integration base, not a validation pass. Affected copper
is removed so no stale route can masquerade as connectivity after moves.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb'
OUT = R / 'PHASE24_SELECTED_MACRO_PLACEMENT.kicad_pcb'

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)

b = pcbnew.LoadBoard(str(BASE))
moves = {
    'J2': (12, 100, 180), 'U6': (25, 94, -90), 'U9': (25, 106, -90),
    'U7': (96, 124, 180), 'J3': (138, 124, 90),
    'C30': (103, 116, 180), 'C31': (103, 132, 180),
    'C32': (103, 120, 180), 'C33': (103, 128, 180),
    'Y1': (88, 136, 0), 'R23': (82, 136, 0),
    'C42': (82, 132, 0), 'C43': (82, 140, 0),
}
for ref, (x, y, rot) in moves.items():
    f = b.FindFootprintByReference(ref)
    if f is None: raise RuntimeError(f'missing footprint {ref}')
    f.SetPosition(V(x, y)); f.SetOrientationDegrees(rot)

affected = ('CM5_GBE_', 'ETH_', 'GBE_', 'CM5_USB3_',
            'BRIDGE_SATA_', 'BRIDGE_XI', 'BRIDGE_XO', 'BRIDGE_VSSOSC')
for item in list(b.GetTracks()):
    if any(k in item.GetNetname() for k in affected):
        b.Remove(item)

b.Save(str(OUT))
print(OUT)
