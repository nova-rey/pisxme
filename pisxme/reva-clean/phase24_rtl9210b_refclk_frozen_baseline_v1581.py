"""V1581: REFCLK pair implementation on the frozen V1517 baseline."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / "PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb"
out = H / "PHASE24_RTL9210B_REFCLK_FROZEN_BASELINE_V1581.kicad_pcb"
b = pcbnew.LoadBoard(str(base)); F, B = pcbnew.F_Cu, pcbnew.B_Cu
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
for pad in b.FindFootprintByReference("U1").Pads():
    pad.SetLocalClearance(pcbnew.FromMM(0.15))

def tr(net, a, z, layer, width=.20):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)

def via(net, x, y):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(x, y)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)

for name, source, yb, xfan, xj in (
    ("REFCLK_P", (94.05,70.4), 56.0, 106.0, 137.25),
    ("REFCLK_N", (94.05,70.8), 57.0, 106.0, 136.75),
):
    n = b.FindNet(name); assert n
    tr(n, source, (90.0, source[1]), F)
    tr(n, (90.0, source[1]), (90.0, yb), F)
    via(n, 90.0, yb)
    tr(n, (90.0, yb), (xfan, yb), B)
    via(n, xfan, yb)
    tr(n, (xfan, yb), (xj, yb), F)
    tr(n, (xj, yb), (xj, 62.725), F)

pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
