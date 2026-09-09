"""V15: ordinary-via TXN escape through the dense U11 lower field."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
b = pcbnew.LoadBoard(str(R / "PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb"))
F, B = pcbnew.F_Cu, pcbnew.B_Cu

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(ref, pad):
    p = b.FindFootprintByReference(ref).FindPadByNumber(str(pad)).GetPosition()
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def tr(net, a, z, layer, width=.2):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
def via(net, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5))
    v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F, B); v.SetNet(net); b.Add(v)

net = b.FindNet("USB_TXN1")
for item in list(b.GetTracks()):
    if item.GetNetCode() == net.GetNetCode(): b.RemoveNative(item)

source = xy("U11", 22); c87 = xy("C87", 1)
source_via = (140.0, 139.8)
return_via = (146.5, 139.8)
tr(net, source, (141.0, 139.4), F, .15)
tr(net, (141.0, 139.4), source_via, F, .15)
via(net, source_via)
tr(net, source_via, (146.5, 139.8), B)
tr(net, (146.5, 139.8), return_via, B)
via(net, return_via)
tr(net, return_via, (146.5, 146.0), F)
tr(net, (146.5, 146.0), c87, F)

b.BuildListOfNets()
out = R / "PHASE24_STORAGE_USB_TX_PAIR_LAYER_TRANSITION_V15.kicad_pcb"
b.Save(str(out)); print(out)
