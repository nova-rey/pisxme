"""V1579: move the frozen-orientation XTAL_IN transition west of lane fields."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / "PHASE24_RTL9210B_XTALOUT_ON_U155_V1520.kicad_pcb"
out = H / "PHASE24_RTL9210B_XTALIN_WEST_CORRIDOR_V1579.kicad_pcb"
b = pcbnew.LoadBoard(str(base)); F, B = pcbnew.F_Cu, pcbnew.B_Cu
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))

def xy(item):
    return tuple(round(v / 1e6, 3) for v in (item.GetStart().x, item.GetStart().y,
                                               item.GetEnd().x, item.GetEnd().y))

# Rehome only the U1.52 local transition that obstructed the crystal source.
for item in list(b.GetTracks()):
    if item.GetNetname() != "RTL_3V3": continue
    if type(item).__name__ == "PCB_VIA":
        p = item.GetPosition()
        if abs(p.x / 1e6 - 93.0) < .01 and abs(p.y / 1e6 - 66.8) < .01: b.RemoveNative(item)
    elif xy(item) == (94.05, 66.8, 93.0, 66.8): b.RemoveNative(item)

def tr(net, a, z, layer, width=.20):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)

def via(net, p, width=.50):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(width))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)

v3 = b.FindNet("RTL_3V3")
for a, z, l in [((94.05,66.8),(91.8,66.8),F), ((91.8,66.8),(91.8,65.8),B),
                ((91.8,65.8),(93.0,65.8),B)]: tr(v3, a, z, l)
via(v3, (91.8,66.8))

xt = b.FindNet("XTAL_IN")
u1 = b.FindFootprintByReference("U1")
for pad in u1.Pads(): pad.SetLocalClearance(pcbnew.FromMM(.15))
tr(xt, (94.05,67.2), (90.0,67.2), F)
via(xt, (90.0,67.2))
tr(xt, (90.0,67.2), (84.0,67.2), B)
tr(xt, (84.0,67.2), (84.0,62.0), B)
via(xt, (84.0,62.0))
tr(xt, (84.0,62.0), (88.0,62.0), F)
tr(xt, (88.0,62.0), (88.0,59.0), F)

pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
