"""Disposable complete clock passive branches on the clean source escape."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U7_CLOCK_SOURCE_ESCAPE.kicad_pcb"
OUT = ROOT / "PHASE24_CLOCK_PASSIVE_BRANCHES.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def path(name, points):
    n = b.FindNet(name)
    for a, z in zip(points, points[1:]):
        t = pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.B_Cu); t.SetNet(n)
        t.SetWidth(pcbnew.FromMM(0.15)); t.SetStart(p(*a)); t.SetEnd(p(*z)); b.Add(t)


XI = "/STORAGE/BRIDGE_XI"
XO = "/STORAGE/BRIDGE_XO"
VS = "/STORAGE/BRIDGE_VSSOSC"

# Source via to C42, then the XI branch to R23 and crystal pad 1.
path(XI, [(124.0, 125.5), (110.0, 125.5), (110.0, 124.5), (100.5, 124.5), (100.5, 126.0)])
path(XI, [(100.5, 126.0), (104.0, 126.0), (104.0, 129.15), (106.9, 129.15)])
path(XI, [(100.5, 130.0), (104.0, 130.0), (104.0, 129.15), (106.9, 129.15)])

# XO uses the south perimeter and approaches crystal pad 3 from below.
path(XO, [(120.5, 137.5), (114.0, 137.5), (114.0, 136.5), (100.5, 136.5), (100.5, 134.0)])
path(XO, [(100.5, 134.0), (109.1, 134.0), (109.1, 130.85)])
path(XO, [(101.5, 130.0), (112.0, 130.0), (112.0, 130.85), (109.1, 130.85)])

# VSSOSC owns the west perimeter and returns to both crystal pads.
path(VS, [(122.5, 126.5), (122.5, 123.0), (98.5, 123.0), (98.5, 136.0), (101.5, 136.0), (101.5, 134.0)])
path(VS, [(101.5, 126.0), (97.5, 126.0), (97.5, 136.0), (98.5, 136.0)])
path(VS, [(106.9, 130.85), (105.0, 130.85), (105.0, 123.0), (98.5, 123.0)])
path(VS, [(109.1, 129.15), (111.0, 129.15), (111.0, 123.0), (98.5, 123.0)])

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
