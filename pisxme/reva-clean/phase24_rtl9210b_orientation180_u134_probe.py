"""Disposable second lower RTL_3V3 channel on the 180-degree basis."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / 'PHASE24_RTL9210B_ORIENTATION180_U139_PROBE.kicad_pcb'
OUT = HERE / 'PHASE24_RTL9210B_ORIENTATION180_U134_PROBE_V2.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def p(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def seg(b, n, layer, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z))
    t.SetLayer(layer); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b, n, q):
    v = pcbnew.PCB_VIA(b); v.SetPosition(p(*q)); v.SetWidth(pcbnew.FromMM(.60))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)

b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet('RTL_3V3')
# U1.34 leaves the west lower edge, crosses the open B.Cu corridor, and
# returns beside the U2.3 endpoint without using a plane layer.
seg(b, n, F, (94.05, 73.20), (90.00, 73.20)); via(b, n, (90.00, 73.20))
seg(b, n, B, (90.00, 73.20), (74.20, 73.20)); via(b, n, (74.20, 73.20))
seg(b, n, F, (74.20, 73.20), (74.20, 80.00))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
