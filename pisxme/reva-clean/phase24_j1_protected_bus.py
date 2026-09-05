"""Disposable J1 12V_PROTECTED connector-field bus.

Coordinates are derived from the serialized J1 pads, grouped by exact X
coordinate. The bus is B.Cu, leaving In3 available for the later distributed
protected-12V plane and keeping interleaved J1 ground columns untouched.
"""
from collections import defaultdict
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
OUT = ROOT / "PHASE24_J1_PROTECTED_BUS_V2.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
j1 = next(fp for fp in b.GetFootprints() if fp.GetReference() == "J1")
n = b.FindNet("12V_PROTECTED")
if n is None:
    raise RuntimeError("missing 12V_PROTECTED")


def mm(v):
    return float(v) / 1_000_000.0


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def add(layer, a, z):
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(layer)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.50))
    t.SetStart(p(*a))
    t.SetEnd(p(*z))
    b.Add(t)


cols = defaultdict(list)
for pad in j1.Pads():
    if pad.GetNetCode() == n.GetNetCode():
        pos = pad.GetPosition()
        cols[round(mm(pos.x), 6)].append(mm(pos.y))

if len(cols) != 13 or any(len(v) != 10 for v in cols.values()):
    raise RuntimeError(f"unexpected J1 field shape: {sorted((k, len(v)) for k,v in cols.items())}")

for x, ys in sorted(cols.items()):
    add(pcbnew.F_Cu, (x, min(ys)), (x, max(ys)))
    # Drop below the last connector row rather than between the protected and
    # interleaved ground columns.  This gives the ordinary via more copper
    # clearance while remaining outside every J1 pad aperture.
    vx, vy = x, 96.50
    v = pcbnew.PCB_VIA(b)
    v.SetNet(n)
    v.SetPosition(p(vx, vy))
    v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30))
    b.Add(v)
    add(pcbnew.F_Cu, (x, max(ys)), (vx, vy))
    add(pcbnew.B_Cu, (vx, vy), (vx, 97.0))
left, right = min(cols), max(cols)
add(pcbnew.B_Cu, (left, 97.0), (right, 97.0))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
