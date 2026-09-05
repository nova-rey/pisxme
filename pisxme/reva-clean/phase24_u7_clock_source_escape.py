"""Disposable U7 clock source escape from the rotated-U7 native oracle."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U7_CLOCK_NET_AUTHORITY.kicad_pcb"
OUT = ROOT / "PHASE24_U7_CLOCK_SOURCE_ESCAPE.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def t(name, layer, a, z):
    n = b.FindNet(name)
    q = pcbnew.PCB_TRACK(b); q.SetStart(p(*a)); q.SetEnd(p(*z))
    q.SetLayer(layer); q.SetWidth(pcbnew.FromMM(0.20)); q.SetNet(n); b.Add(q)


def v(name, q):
    n = b.FindNet(name)
    x = pcbnew.PCB_VIA(b); x.SetPosition(p(*q)); x.SetWidth(pcbnew.FromMM(0.50))
    x.SetDrill(pcbnew.FromMM(0.30)); x.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    x.SetNet(n); b.Add(x)


# Exact serialized source-pad positions and the oracle's source-side escape.
t("/STORAGE/BRIDGE_XI", pcbnew.F_Cu, (123.0, 135.5), (123.0, 128.0))
t("/STORAGE/BRIDGE_XI", pcbnew.F_Cu, (123.0, 128.0), (124.0, 125.5))
v("/STORAGE/BRIDGE_XI", (124.0, 125.5))
t("/STORAGE/BRIDGE_XO", pcbnew.F_Cu, (122.0, 135.5), (122.0, 137.5))
t("/STORAGE/BRIDGE_XO", pcbnew.F_Cu, (122.0, 137.5), (120.5, 137.5))
v("/STORAGE/BRIDGE_XO", (120.5, 137.5))
t("/STORAGE/BRIDGE_VSSOSC", pcbnew.F_Cu, (122.5, 135.5), (122.5, 126.5))
v("/STORAGE/BRIDGE_VSSOSC", (122.5, 126.5))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
