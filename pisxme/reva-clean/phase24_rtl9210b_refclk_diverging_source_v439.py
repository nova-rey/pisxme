"""V439: disposable diverging REFCLK source fanout from native U1 pads."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_CLKREQ_QFN_CLEARANCE_V431.kicad_pcb'; out=H/'PHASE24_RTL9210B_REFCLK_DIVERGING_SOURCE_V439.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname() in {'REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXP','LANE0_TXN','XTAL_OUT'}: b.RemoveNative(x)
np=b.FindNet('REFCLK_P'); seg(b,np,F,(109.95,61.6),(112.5,60.2)); via(b,np,(112.5,60.2)); seg(b,np,B,(112.5,60.2),(120,58.0))
nn=b.FindNet('REFCLK_N'); seg(b,nn,F,(109.95,61.2),(113.5,62.6)); via(b,nn,(113.5,62.6)); seg(b,nn,B,(113.5,62.6),(120,66.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
