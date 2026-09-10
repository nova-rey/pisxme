"""V1469: move RXN below the existing TXP via and complete its J1 join."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U166_JOIN_RXP_EAST_UP_V1466.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U163_RXN_REHOME_V1469.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); b=pcbnew.LoadBoard(str(BASE))
def n(s): q=b.FindNet(s); assert q is not None; return q
def p(x,y): return pcbnew.VECTOR2I_MM(x,y)
def rm(s):
 c=n(s).GetNetCode()
 for q in list(b.GetTracks()):
  if q.GetNetCode()==c: b.RemoveNative(q)
def seg(s,a,z,l):
 q=n(s); t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(s,xy):
 q=n(s); v=pcbnew.PCB_VIA(b); v.SetPosition(p(*xy)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)

# U1.63 is the second RTL_1V1 source pad; U1.60's original branch stays.
seg('RTL_1V1',(94.05,71.20),(92.80,71.20),F); seg('RTL_1V1',(92.80,71.20),(92.80,69.80),F); via('RTL_1V1',(92.80,69.80)); seg('RTL_1V1',(92.80,69.80),(88.0,69.80),B); seg('RTL_1V1',(88.0,69.80),(88.0,70.0),B)

# RXN source and remote corridor, with a distinct x=88.8 transition.
rm('LANE0_RXN')
seg('LANE0_RXN',(94.05,72.00),(88.80,72.00),F); seg('LANE0_RXN',(88.80,72.00),(88.80,70.80),F); via('LANE0_RXN',(88.80,70.80)); seg('LANE0_RXN',(88.80,70.80),(88.80,84.00),B); via('LANE0_RXN',(88.80,84.00)); seg('LANE0_RXN',(88.80,84.00),(131.00,84.00),F); seg('LANE0_RXN',(131.00,84.00),(131.00,65.00),F); via('LANE0_RXN',(131.00,65.00)); seg('LANE0_RXN',(131.00,65.00),(132.75,65.00),B); via('LANE0_RXN',(132.75,65.00)); seg('LANE0_RXN',(132.75,65.00),(133.75,62.725),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
