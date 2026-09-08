"""Disposable coordinated RTL_5V rail field on the retained 180-degree basis."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_ORIENTATION180_U134_PROBE_V2.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_ORIENTATION180_RAILS_PROBE_V7.kicad_pcb'
F, B, W = pcbnew.F_Cu, pcbnew.B_Cu, pcbnew.FromMM(.20)
def p(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def s(b, n, l, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l)
    t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b, n, q):
    x = pcbnew.PCB_VIA(b); x.SetPosition(p(*q)); x.SetWidth(pcbnew.FromMM(.60))
    x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F, B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)

b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet('RTL_5V')
# U1.17 exits north-west; U1.33 exits west and joins the same outboard
# B.Cu collector. The shared collector returns to C5.1.
s(b,n,F,(94.8,66.05),(94.8,64.8)); s(b,n,F,(94.8,64.8),(92.0,64.8)); v(b,n,(92.0,64.8))
s(b,n,F,(94.05,72.8),(92.5,72.8)); s(b,n,F,(92.5,72.8),(92.5,71.5)); s(b,n,F,(92.5,71.5),(89.0,71.5)); v(b,n,(89.0,71.5))
s(b,n,B,(89.0,71.5),(89.0,64.8)); s(b,n,B,(89.0,64.8),(116.4,64.8)); s(b,n,B,(116.4,64.8),(116.4,69.0)); v(b,n,(116.4,69.0))
s(b,n,F,(116.4,69.0),(116.4,69.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
