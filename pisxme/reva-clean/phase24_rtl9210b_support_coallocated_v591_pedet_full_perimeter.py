"""V591: complete PEDET from M.2 contact through the top perimeter."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V590_PEDET_TOP_PERIMETER.kicad_pcb'
out = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V591_PEDET_FULL_PERIMETER.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def seg(board, net, a, z, layer):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    board.Add(t)

def via(board, net, q):
    v = pcbnew.PCB_VIA(board)
    v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(0.60))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(F, B)
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

b = pcbnew.LoadBoard(str(base))
n = b.FindNet('PEDET')
# Stay outside the M.2 pad field, then use the top perimeter already proven
# locally in V590. No via is placed in a component pad.
seg(b, n, (140.75, 62.725), (143.0, 62.725), F)
via(b, n, (143.0, 62.725))
seg(b, n, (143.0, 62.725), (143.0, 47.0), B)
seg(b, n, (143.0, 47.0), (112.0, 47.0), B)
via(b, n, (112.0, 47.0))
seg(b, n, (112.0, 47.0), (106.4, 47.0), F)
b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(out))
print(out)
