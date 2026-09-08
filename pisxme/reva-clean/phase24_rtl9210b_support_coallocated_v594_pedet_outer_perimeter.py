"""V594: complete PEDET perimeter with an explicit local handoff."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V590_PEDET_TOP_PERIMETER.kicad_pcb'
out = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V594_PEDET_OUTER_PERIMETER.kicad_pcb'
W = pcbnew.FromMM(0.20)

def P(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))

def seg(board, net, a, z):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(pcbnew.F_Cu)
    t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode())
    board.Add(t)

b = pcbnew.LoadBoard(str(base))
n = b.FindNet('PEDET')
for a, z in [
    ((140.75, 62.725), (143.0, 62.725)),
    ((143.0, 62.725), (143.0, 42.0)),
    ((143.0, 42.0), (106.4, 42.0)),
    ((106.4, 42.0), (106.4, 47.0)),
]:
    seg(b, n, a, z)
b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(out))
print(out)
