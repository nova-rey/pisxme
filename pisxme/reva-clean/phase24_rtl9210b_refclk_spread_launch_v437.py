"""V437: fully spread REFCLK source and outer J1 launches."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_CLKREQ_QFN_CLEARANCE_V431.kicad_pcb'; out=H/'PHASE24_RTL9210B_REFCLK_SPREAD_LAUNCH_V437.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname() in {'REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXP','LANE0_TXN','XTAL_OUT'}: b.RemoveNative(x)
np=b.FindNet('REFCLK_P'); seg(b,np,F,(109.95,61.6),(112.5,60.0)); via(b,np,(112.5,60.0)); seg(b,np,B,(112.5,60.0),(132.0,58.0)); seg(b,np,B,(132.0,58.0),(138.0,58.0)); seg(b,np,B,(138.0,58.0),(138.0,62.0)); via(b,np,(138.0,62.0)); seg(b,np,F,(138.0,62.0),(137.25,62.725))
nn=b.FindNet('REFCLK_N'); seg(b,nn,F,(109.95,61.2),(113.5,62.8)); via(b,nn,(113.5,62.8)); seg(b,nn,B,(113.5,62.8),(132.0,66.0)); seg(b,nn,B,(132.0,66.0),(136.0,66.0)); seg(b,nn,B,(136.0,66.0),(136.0,63.5)); via(b,nn,(136.0,63.5)); seg(b,nn,F,(136.0,63.5),(136.75,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
