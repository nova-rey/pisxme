"""V417: regenerate PEDET from current U1.8/R2.1/J1.69 pads."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_CLKREQ_NATIVE_ESCAPE_V416.kicad_pcb'; out=H/'PHASE24_RTL9210B_PEDET_NATIVE_ESCAPE_V418.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('PEDET')
seg(b,n,F,(106.4,58.05),(106.4,54.5)); via(b,n,(106.4,54.5)); seg(b,n,B,(106.4,54.5),(95.5,54.5)); seg(b,n,B,(95.5,54.5),(95.5,78.0)); seg(b,n,B,(95.5,78.0),(140.75,78.0)); via(b,n,(140.75,78.0)); seg(b,n,F,(140.75,78.0),(140.75,62.725)); via(b,n,(98.9,54.5)); seg(b,n,F,(98.9,54.5),(98.9,53.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
