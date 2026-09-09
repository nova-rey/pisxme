"""V22: add the missing physical vias at the native XIN/XOUT layer changes."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb'
OUT = R / 'PHASE24_STORAGE_JMS583_CRYSTAL_VIAS_V22.kicad_pcb'

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(b, ref, num):
    q = b.FindFootprintByReference(ref).FindPadByNumber(str(num)).GetPosition()
    return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)
def segment(b, net, a, z, layer, width=.15):
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    b.Add(t)
def via(b, net, q):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.55))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); b.Add(v)
def clear(b, net):
    for item in list(b.GetTracks()):
        if item.GetNetCode() == net.GetNetCode(): b.RemoveNative(item)
def route(b, name, up, crystal, low, high):
    net = b.FindNet(name); clear(b, net)
    src = xy(b, 'U11', up); dst = xy(b, 'Y10', crystal)
    segment(b, net, src, low, pcbnew.F_Cu)
    via(b, net, low)
    segment(b, net, low, high, pcbnew.B_Cu, .15)
    via(b, net, high)
    segment(b, net, high, dst, pcbnew.F_Cu)
route(b := pcbnew.LoadBoard(str(BASE)), 'XIN', 50, 1, (137.4, 129.8), (147.0, 110.5))
route(b, 'XOUT', 51, 2, (137.8, 129.2), (146.5, 112.0))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
