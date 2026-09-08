"""V452: add exact V328 lane geometry to the V451 REFCLK basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_REFCLK_UPPER_N_JOG_V451.kicad_pcb'; out=H/'PHASE24_RTL9210B_REFCLK_LANE_EXACT_V452.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
rxp=b.FindNet('LANE0_RXP'); seg(b,rxp,F,(109.95,60.4),(110.6,60.4)); seg(b,rxp,F,(110.6,60.4),(110.6,66.5)); via(b,rxp,(110.6,66.5)); seg(b,rxp,B,(110.6,66.5),(132,66.5)); via(b,rxp,(132,66.5)); seg(b,rxp,F,(132,66.5),(134.25,66.5)); seg(b,rxp,F,(134.25,66.5),(134.25,62.725))
rxn=b.FindNet('LANE0_RXN'); seg(b,rxn,F,(109.95,60.0),(111.5,60.0)); seg(b,rxn,F,(111.5,60.0),(111.5,64.5)); via(b,rxn,(111.5,64.5)); seg(b,rxn,B,(111.5,64.5),(132,64.5)); via(b,rxn,(132,64.5)); seg(b,rxn,F,(132,64.5),(133.75,64.5)); seg(b,rxn,F,(133.75,64.5),(133.75,62.725))
txp=b.FindNet('LANE0_TXP'); seg(b,txp,F,(109.95,58.8),(135.75,58.8)); seg(b,txp,F,(135.75,58.8),(135.75,62.725))
txn=b.FindNet('LANE0_TXN'); seg(b,txn,F,(109.95,59.2),(135.25,59.2)); seg(b,txn,F,(135.25,59.2),(135.25,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
