"""Disposable clock passive-pad launches with layer-separated F.Cu buses."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_U7_CLOCK_SOURCE_ESCAPE.kicad_pcb"
OUT = ROOT / "PHASE24_CLOCK_ISOLATED_LAUNCHES.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def track(name, layer, a, z):
    n = b.FindNet(name)
    q = pcbnew.PCB_TRACK(b); q.SetLayer(layer); q.SetNet(n)
    q.SetWidth(pcbnew.FromMM(0.15)); q.SetStart(p(*a)); q.SetEnd(p(*z)); b.Add(q)


def via(name, q):
    n = b.FindNet(name)
    x = pcbnew.PCB_VIA(b); x.SetPosition(p(*q)); x.SetWidth(pcbnew.FromMM(0.50))
    x.SetDrill(pcbnew.FromMM(0.30)); x.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    x.SetNet(n); b.Add(x)


XI = "/STORAGE/BRIDGE_XI"; XO = "/STORAGE/BRIDGE_XO"; VS = "/STORAGE/BRIDGE_VSSOSC"
# Backside passive pads -> offset vias.  Offsets are selected outside each
# 0402/crystal aperture; no via is placed in a pad.
launches = {
    XI: [((100.5, 126.0), (100.5, 125.0)), ((100.5, 130.0), (99.5, 130.0)),
         ((106.9, 129.15), (106.9, 128.0))],
    XO: [((100.5, 134.0), (99.5, 134.0)), ((101.5, 130.0), (102.5, 130.0)),
         ((109.1, 130.85), (109.1, 132.0))],
    VS: [((101.5, 126.0), (101.5, 125.0)), ((101.5, 134.0), (102.5, 134.0)),
         ((106.9, 130.85), (105.5, 130.85)), ((109.1, 129.15), (110.5, 129.15))],
}
for name, pairs in launches.items():
    for pad, q in pairs:
        via(name, q); track(name, pcbnew.B_Cu, pad, q)

# Isolated source-to-island and island-to-crystal corridors on F.Cu.
track(XI, pcbnew.F_Cu, (124.0, 125.5), (100.5, 125.0))
track(XI, pcbnew.F_Cu, (99.5, 130.0), (104.0, 130.0))
track(XI, pcbnew.F_Cu, (104.0, 130.0), (104.0, 128.0))
track(XI, pcbnew.F_Cu, (104.0, 128.0), (106.9, 128.0))
track(XI, pcbnew.F_Cu, (100.5, 125.0), (100.5, 123.5))
track(XI, pcbnew.F_Cu, (100.5, 123.5), (106.9, 123.5))
track(XI, pcbnew.F_Cu, (106.9, 123.5), (106.9, 128.0))

track(XO, pcbnew.F_Cu, (120.5, 137.5), (99.5, 134.0))
track(XO, pcbnew.F_Cu, (102.5, 130.0), (109.1, 130.0))
track(XO, pcbnew.F_Cu, (109.1, 130.0), (109.1, 132.0))
track(XO, pcbnew.F_Cu, (99.5, 134.0), (109.1, 134.0))
track(XO, pcbnew.F_Cu, (109.1, 134.0), (109.1, 132.0))

track(VS, pcbnew.F_Cu, (122.5, 126.5), (101.5, 125.0))
track(VS, pcbnew.F_Cu, (101.5, 125.0), (98.0, 125.0))
track(VS, pcbnew.F_Cu, (98.0, 125.0), (98.0, 136.0))
track(VS, pcbnew.F_Cu, (98.0, 136.0), (102.5, 136.0))
track(VS, pcbnew.F_Cu, (102.5, 136.0), (102.5, 134.0))
track(VS, pcbnew.F_Cu, (105.5, 130.85), (105.5, 123.5))
track(VS, pcbnew.F_Cu, (105.5, 123.5), (98.0, 123.5))
track(VS, pcbnew.F_Cu, (110.5, 129.15), (110.5, 123.5))
track(VS, pcbnew.F_Cu, (110.5, 123.5), (105.5, 123.5))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
