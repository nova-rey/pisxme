"""Disposable global POWER_GND launch cluster from the PI review."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_J1_POWER_GROUND_COLUMNS.kicad_pcb"
OUT = ROOT / "PHASE24_PGND_CLUSTER.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("POWER_GND")


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def launch(a, z):
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(pcbnew.F_Cu)
    t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(0.20))
    t.SetStart(p(*a))
    t.SetEnd(p(*z))
    b.Add(t)
    v = pcbnew.PCB_VIA(b)
    v.SetNet(n)
    v.SetPosition(p(*z))
    v.SetWidth(pcbnew.FromMM(0.50))
    v.SetDrill(pcbnew.FromMM(0.30))
    b.Add(v)


# U1/U2: right-side pad, escaping above the lower multi-net row.
launch((21.45, 73.55), (22.50, 73.55))
launch((21.45, 93.55), (22.50, 93.55))
# J4: escape the four ground pads outward from the connector body.
for y in (98.25, 101.75):
    if y == 101.75:
        launch((43.00, y), (40.50, 103.00))
    else:
        launch((43.00, y), (41.50, y))
    launch((47.00, y), (48.50, y))
# U8: escape left of the small USB2 protection footprint.
launch((57.575, 100.00), (56.50, 100.00))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
