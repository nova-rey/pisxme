"""V454: coordinate REFCLK/lane vias and route N over the P corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_REFCLK_UPPER_N_JOG_V451.kicad_pcb'; out=H/'PHASE24_RTL9210B_REFCLK_LANE_COALLOCATE_V454.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname() in {'REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXP','LANE0_TXN','XTAL_IN','XTAL_OUT'}: b.RemoveNative(x)
np=b.FindNet('REFCLK_P'); seg(b,np,F,(109.95,61.6),(112.5,61.6)); via(b,np,(112.5,61.6)); seg(b,np,B,(112.5,61.6),(112.5,58)); seg(b,np,B,(112.5,58),(137.25,58)); seg(b,np,B,(137.25,58),(137.25,60.5)); via(b,np,(137.25,60.5)); seg(b,np,F,(137.25,60.5),(137.25,62.725))
nn=b.FindNet('REFCLK_N'); seg(b,nn,F,(109.95,61.2),(111.5,61.2)); seg(b,nn,F,(111.5,61.2),(111.5,60.8)); via(b,nn,(111.5,60.8)); seg(b,nn,B,(111.5,60.8),(111.5,57)); seg(b,nn,B,(111.5,57),(139,57)); via(b,nn,(139,57)); seg(b,nn,F,(139,57),(139,64.5)); seg(b,nn,F,(139,64.5),(136.75,64.5)); seg(b,nn,F,(136.75,64.5),(136.75,62.725))
rxp=b.FindNet('LANE0_RXP'); seg(b,rxp,F,(109.95,60.4),(110.8,60.4)); via(b,rxp,(110.8,60.4)); seg(b,rxp,B,(110.8,60.4),(110.8,66.5)); via(b,rxp,(110.8,66.5)); seg(b,rxp,B,(110.8,66.5),(132,66.5)); via(b,rxp,(132,66.5)); seg(b,rxp,F,(132,66.5),(134.25,66.5)); seg(b,rxp,F,(134.25,66.5),(134.25,62.725))
rxn=b.FindNet('LANE0_RXN'); seg(b,rxn,F,(109.95,60.0),(113.5,60.0)); via(b,rxn,(113.5,60.0)); seg(b,rxn,B,(113.5,60.0),(113.5,64.5)); seg(b,rxn,B,(113.5,64.5),(132,64.5)); via(b,rxn,(132,64.5)); seg(b,rxn,F,(132,64.5),(133.75,64.5)); seg(b,rxn,F,(133.75,64.5),(133.75,62.725))
txp=b.FindNet('LANE0_TXP'); seg(b,txp,F,(109.95,58.8),(135.75,58.8)); seg(b,txp,F,(135.75,58.8),(135.75,62.725))
txn=b.FindNet('LANE0_TXN'); seg(b,txn,F,(109.95,59.2),(135.25,59.2)); seg(b,txn,F,(135.25,59.2),(135.25,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
