"""Disposable J1 POWER_GND field columns into existing ground planes."""
from collections import defaultdict
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_J1_PROTECTED_PLANE.kicad_pcb"
OUT = ROOT / "PHASE24_J1_POWER_GROUND_COLUMNS.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
j1 = next(fp for fp in b.GetFootprints() if fp.GetReference() == "J1")
n = b.FindNet("POWER_GND")
if n is None:
    raise RuntimeError("missing POWER_GND")


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def track(a, z):
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(pcbnew.F_Cu)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.45))
    t.SetStart(p(*a))
    t.SetEnd(p(*z))
    b.Add(t)


def via(x, y):
    v = pcbnew.PCB_VIA(b)
    v.SetNet(n)
    v.SetPosition(p(x, y))
    v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30))
    b.Add(v)


cols = defaultdict(list)
for pad in j1.Pads():
    if pad.GetNetCode() == n.GetNetCode():
        pos = pad.GetPosition()
        cols[round(float(pos.x) / 1_000_000.0, 6)].append(float(pos.y) / 1_000_000.0)
if len(cols) != 7 or any(len(v) != 10 for v in cols.values()):
    raise RuntimeError("unexpected J1 ground field shape")

for x, ys in sorted(cols.items()):
    track((x, min(ys)), (x, max(ys)))
    via(x, 98.00)
    track((x, max(ys)), (x, 98.00))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
