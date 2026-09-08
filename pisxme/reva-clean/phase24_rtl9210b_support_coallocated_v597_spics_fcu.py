"""V597: test an all-F.Cu SPICS staircase with no transition via."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb'
out = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V597_SPICS_FCU.kicad_pcb'
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def seg(board, net, a, z):
    t = pcbnew.PCB_TRACK(board); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(pcbnew.F_Cu); t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode()); board.Add(t)

b = pcbnew.LoadBoard(str(base)); n = b.FindNet('SPICS')
for a, z in [((102.05, 61.2), (100.0, 61.2)),
             ((100.0, 61.2), (100.0, 69.0)),
             ((100.0, 69.0), (91.3, 69.0)),
             ((91.3, 69.0), (91.3, 70.0))]:
    seg(b, n, a, z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
