"""V1461: co-author all lane-0 source fields with U1.66 GND access."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_COUPLED_QFN_FIELD_V1461.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
def N(s): n=b.FindNet(s); assert n; return n
def rm(s):
 n=N(s)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
def seg(s,a,z,l):
 n=N(s); t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(s,p):
 n=N(s); v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
for s in ('LANE0_RXN','LANE0_RXP','LANE0_TXN','LANE0_TXP','GND'): rm(s)
# Keep the existing remote trunks, but allocate separated source transitions.
seg('LANE0_RXN',(94.05,72.0),(91.2,72.0),F); seg('LANE0_RXN',(91.2,72.0),(91.2,70.8),F); via('LANE0_RXN',(91.2,70.8)); seg('LANE0_RXN',(91.2,70.8),(91.2,84.0),B); via('LANE0_RXN',(91.2,84.0)); seg('LANE0_RXN',(91.2,84.0),(131.0,84.0),F); seg('LANE0_RXN',(131.0,84.0),(131.0,65.0),F); via('LANE0_RXN',(131.0,65.0)); seg('LANE0_RXN',(131.0,65.0),(132.75,65.0),B); seg('LANE0_RXN',(132.75,65.0),(133.75,62.725),F)
seg('LANE0_RXP',(94.05,71.6),(89.8,71.6),F); seg('LANE0_RXP',(89.8,71.6),(89.8,70.0),F); via('LANE0_RXP',(89.8,70.0)); seg('LANE0_RXP',(89.8,70.0),(89.8,82.0),B); via('LANE0_RXP',(89.8,82.0)); seg('LANE0_RXP',(89.8,82.0),(130.0,82.0),F); seg('LANE0_RXP',(130.0,82.0),(130.0,65.0),F); via('LANE0_RXP',(130.0,65.0)); seg('LANE0_RXP',(130.0,65.0),(131.75,65.0),B); seg('LANE0_RXP',(131.75,65.0),(132.75,62.725),F)
seg('LANE0_TXN',(94.05,72.8),(88.4,72.8),F); seg('LANE0_TXN',(88.4,72.8),(88.4,72.6),F); via('LANE0_TXN',(88.4,72.6)); seg('LANE0_TXN',(88.4,72.6),(88.4,86.0),B); via('LANE0_TXN',(88.4,86.0)); seg('LANE0_TXN',(88.4,86.0),(132.0,86.0),F)
seg('LANE0_TXP',(94.05,73.2),(87.0,73.2),F); seg('LANE0_TXP',(87.0,73.2),(87.0,76.8),F); via('LANE0_TXP',(87.0,76.8)); seg('LANE0_TXP',(87.0,76.8),(87.0,88.0),B); via('LANE0_TXP',(87.0,88.0)); seg('LANE0_TXP',(87.0,88.0),(136.0,88.0),B)
# Lower/right exposed-pad approach, avoiding RESET_N and the moved lane field.
seg('GND',(94.05,72.4),(93.5,72.4),F); seg('GND',(93.5,72.4),(93.5,75.4),F); seg('GND',(93.5,75.4),(100.8,75.4),F); seg('GND',(100.8,75.4),(100.8,69.5),F); seg('GND',(100.8,69.5),(100.4,69.5),F); via('GND',(93.5,75.4))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
