"""V656 disposable: co-locate U2 east of the QFN and regenerate all SPI."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_ORIENTATION180_3V3_C3_JOIN_PROBE.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_SPI_U2_FAR_EAST_PROBE.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(q): return (q.x / 1e6, q.y / 1e6)
def tr(b, n, layer, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b, n, q):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(F, B); v.SetNet(n)
    v.SetNetCode(n.GetNetCode()); b.Add(v)

b = pcbnew.LoadBoard(str(BASE))
u1 = b.FindFootprintByReference("U1")
u2 = b.FindFootprintByReference("U2")
u2.SetPosition(P(125, 90))
for item in list(b.GetTracks()):
    if item.GetNetname() in {"SPICS", "SPISO", "SPISO3", "SPICLK", "SPISI"}:
        b.RemoveNative(item)

# Escape the transformed U1 right-hand source bank, then use separated B.Cu
# channels above the support field and endpoint dogbones below U2.
routes = [
    ("SPICS", "24", "1", 104.0, 120.8),
    ("SPISO", "23", "2", 105.5, 122.0),
    ("SPISO3", "22", "7", 107.0, 123.2),
    ("SPICLK", "19", "6", 108.5, 124.4),
    ("SPISI", "18", "5", 110.0, 125.6),
]
for name, srcpad, dstpad, sx, dx in routes:
    n = b.FindNet(name)
    a = xy(u1.FindPadByNumber(srcpad).GetPosition())
    z = xy(u2.FindPadByNumber(dstpad).GetPosition())
    sy = 55.0 + (sx - 104.0) * 0.8
    tr(b, n, F, a, (sx, a[1])); tr(b, n, F, (sx, a[1]), (sx, sy)); via(b, n, (sx, sy))
    tr(b, n, B, (sx, sy), (dx, sy)); via(b, n, (dx, sy))
    tr(b, n, F, (dx, sy), (dx, z[1])); tr(b, n, F, (dx, z[1]), z)

b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
