"""Disposable U3 POWER_GND exposed-field stitch."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_BRIDGE_LV_PADFIELDS.kicad_pcb"
OUT = ROOT / "PHASE24_U3_GROUND_FIELD.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def add(a, z):
    n = b.FindNet("POWER_GND")
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(pcbnew.F_Cu)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.20))
    t.SetStart(p(*a))
    t.SetEnd(p(*z))
    b.Add(t)


ox, oy = 60.0, 165.0
# Leave the package to the right of the central thermal row, then join the
# side pads on the lower horizontal rail.
add((ox, oy - 1.125), (ox + 1.50, oy - 1.125))
add((ox + 1.50, oy - 1.125), (ox + 1.50, oy + 1.125))
add((ox + 1.50, oy + 1.125), (ox, oy + 1.125))
add((ox - 2.25, oy + 0.75), (ox, oy + 0.75))
add((ox, oy + 0.75), (ox + 2.25, oy + 0.75))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
