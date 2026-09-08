"""V438: probe 0.10-mm QFN-only REFCLK fanout, widening after vias."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_CLKREQ_QFN_CLEARANCE_V431.kicad_pcb'; out=H/'PHASE24_RTL9210B_REFCLK_NARROW_FANOUT_V438.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); NAR=pcbnew.FromMM(.10)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z,w=W):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(w); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname() in {'REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXP','LANE0_TXN','XTAL_OUT'}: b.RemoveNative(x)
np=b.FindNet('REFCLK_P'); seg(b,np,F,(109.95,61.6),(112.5,60.8),NAR); via(b,np,(112.5,60.8)); seg(b,np,B,(112.5,60.8),(132,58),W); seg(b,np,B,(132,58),(138,58),W); seg(b,np,B,(138,58),(138,62),W); via(b,np,(138,62)); seg(b,np,F,(138,62),(137.25,62.725),W)
nn=b.FindNet('REFCLK_N'); seg(b,nn,F,(109.95,61.2),(113.5,62.0),NAR); via(b,nn,(113.5,62.0)); seg(b,nn,B,(113.5,62.0),(132,66),W); seg(b,nn,B,(132,66),(136,66),W); seg(b,nn,B,(136,66),(136,63.5),W); via(b,nn,(136,63.5)); seg(b,nn,F,(136,63.5),(136.75,62.725),W)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
