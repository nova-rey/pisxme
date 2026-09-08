"""V469: TX pair coallocated above the PERST/connector control field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_ROTATED_SOURCE_PLANAR_V462.kicad_pcb'; out=H/'PHASE24_RTL9210B_TX_PERST_COALLOCATE_V469.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(src))
for name,q,mid,row,tr,dst in [('LANE0_TXN',(115,67.4),(120,67.4),(120,76),(130,76),(135.25,62.725)),('LANE0_TXP',(116,66.5),(121,66.5),(121,77),(131,77),(135.75,62.725))]:
 n=b.FindNet(name);seg(b,n,B,q,mid);seg(b,n,B,mid,row);seg(b,n,B,row,tr);via(b,n,tr);seg(b,n,F,tr,dst)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
