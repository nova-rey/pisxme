"""V595: route the local CLKREQ resistor-to-U1 escape."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V594_PEDET_OUTER_PERIMETER.kicad_pcb'
out = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb'
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def seg(board, net, a, z):
    t = pcbnew.PCB_TRACK(board); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(pcbnew.F_Cu); t.SetWidth(W); t.SetNet(net)
    t.SetNetCode(net.GetNetCode()); board.Add(t)

b = pcbnew.LoadBoard(str(base)); n = b.FindNet('CLKREQ_N')
for a, z in [((101.4, 53.0), (101.4, 50.0)),
             ((101.4, 50.0), (104.4, 50.0)),
             ((104.4, 50.0), (104.4, 58.05))]:
    seg(b, n, a, z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out))
print(out)
