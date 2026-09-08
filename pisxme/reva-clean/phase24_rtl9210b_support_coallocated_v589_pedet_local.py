"""V589: route the local PEDET resistor-to-U1 connection on V583."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V583_5V_UPPER_CLEARANCE.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V589_PEDET_LOCAL.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('PEDET')
s(b,n,(98.9,53.0),(98.9,52.0),F); v(b,n,(98.9,52.0)); s(b,n,(98.9,52.0),(106.4,52.0),B); s(b,n,(106.4,52.0),(106.4,57.2),B); v(b,n,(106.4,57.2)); s(b,n,(106.4,57.2),(106.4,58.05),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
