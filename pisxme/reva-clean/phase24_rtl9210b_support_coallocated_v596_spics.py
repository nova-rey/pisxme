"""V596: trial the SPICS local-to-flash route from the V595 basis."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
base = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb'
out = H / 'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V596_SPICS.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def seg(board, net, layer, a, z):
    t = pcbnew.PCB_TRACK(board); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(layer); t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode()); board.Add(t)
def via(board, net, q):
    v = pcbnew.PCB_VIA(board); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(0.50))
    v.SetDrill(pcbnew.FromMM(0.25)); v.SetLayerPair(F, B); v.SetNet(net); v.SetNetCode(net.GetNetCode()); board.Add(v)

b = pcbnew.LoadBoard(str(base)); n = b.FindNet('SPICS')
via(b, n, (98.8, 57.0))
seg(b, n, F, (98.8, 58.05), (98.8, 57.0))
seg(b, n, B, (98.8, 57.0), (96.5, 57.0))
seg(b, n, B, (96.5, 57.0), (96.5, 72.0))
seg(b, n, B, (96.5, 72.0), (83.3, 72.0))
seg(b, n, B, (83.3, 72.0), (83.3, 68.0))
via(b, n, (83.3, 68.0))
seg(b, n, F, (83.3, 68.0), (83.3, 70.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
