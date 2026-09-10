"""V1457: disposable edge-access test for RTL9210B QFN grounds."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_U166_GND_EDGE_V1457.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def seg(a, z, layer, net):
    q = pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z))
    q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); b.Add(q)

b = pcbnew.LoadBoard(str(BASE)); net = b.FindNet('GND'); assert net
# Leave the QFN field through the bottom edge, then use one ordinary through-via.
seg((94.05, 72.40), (93.00, 72.40), F, net)
seg((93.00, 72.40), (93.00, 74.00), F, net)
seg((93.00, 74.00), (95.00, 74.00), F, net)
# Exposed-pad edge access joins the same via without via-in-pad.
seg((95.60, 72.40), (95.00, 74.00), F, net)
v = pcbnew.PCB_VIA(b); v.SetPosition(P(95.00, 74.00)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(net); v.SetNetCode(net.GetNetCode()); b.Add(v)
# Short B.Cu handoff to the existing GND via at (94,62).
seg((95.00, 74.00), (95.00, 62.00), B, net)
seg((95.00, 62.00), (94.00, 62.00), B, net)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
