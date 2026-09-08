"""V468: TX pair upper separated endpoint corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_ROTATED_SOURCE_PLANAR_V462.kicad_pcb'; out=H/'PHASE24_RTL9210B_TX_PAIR_ENDPOINT_V468.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(src))
for name,q,x,y,dst in [('LANE0_TXN',(115,67.4),120,75,(135.25,62.725)),('LANE0_TXP',(116,66.5),121,74,(135.75,62.725))]:
 n=b.FindNet(name);seg(b,n,B,q,(x,q[1]));seg(b,n,B,(x,q[1]),(x,y));seg(b,n,B,(x,y),(dst[0],y));via(b,n,(dst[0],y));seg(b,n,F,(dst[0],y),dst)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
