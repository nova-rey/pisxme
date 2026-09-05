"""Disposable bridge low-voltage exposed-pad field joins."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_J1_PROTECTED_PLANE.kicad_pcb"
OUT = ROOT / "PHASE24_BRIDGE_LV_PADFIELDS.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def add(name, a, z):
    n = b.FindNet(name)
    if n is None:
        raise RuntimeError(name)
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(pcbnew.F_Cu)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.20))
    t.SetStart(p(*a))
    t.SetEnd(p(*z))
    b.Add(t)


for name, ox, oy in (("/REGULATORS/BRIDGE_1V1", 235.0, 105.0),
                     ("/REGULATORS/BRIDGE_3V3", 225.0, 105.0)):
    # Pad 6 (POWER_GND) lies between low-voltage pads 5 and 8; leave the
    # package on the left and return at pad 8 instead of crossing pad 6.
    add(name, (ox - 2.25, oy + 0.25), (ox - 3.50, oy + 0.25))
    add(name, (ox - 3.50, oy + 0.25), (ox - 3.50, oy + 2.0))
    add(name, (ox - 3.50, oy + 2.0), (ox - 2.25, oy + 2.0))
    add(name, (ox - 2.25, oy + 2.0), (ox + 2.25, oy + 2.0))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
