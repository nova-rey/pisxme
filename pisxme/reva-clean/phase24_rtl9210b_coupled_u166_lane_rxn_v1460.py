"""V1460: coupled U1.66 GND escape with a reallocated LANE0_RXN corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_COUPLED_U166_LANE_RXN_V1460.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
def net(name): n=b.FindNet(name); assert n; return n
def remove(name):
 n=net(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
def seg(name,a,z,l):
 n=net(name); t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(name,p):
 n=net(name); v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)

remove('LANE0_RXN'); remove('GND')
# Move the RXN source and its existing long corridor 1.6 mm west.
seg('LANE0_RXN',(94.05,72.0),(91.2,72.0),F)
seg('LANE0_RXN',(91.2,72.0),(91.2,70.8),F); via('LANE0_RXN',(91.2,70.8))
seg('LANE0_RXN',(91.2,70.8),(91.2,84.0),B); via('LANE0_RXN',(91.2,84.0))
seg('LANE0_RXN',(91.2,84.0),(131.0,84.0),F); via('LANE0_RXN',(131.0,84.0))
seg('LANE0_RXN',(131.0,84.0),(131.0,65.0),F); via('LANE0_RXN',(131.0,65.0))
seg('LANE0_RXN',(131.0,65.0),(132.75,65.0),B); seg('LANE0_RXN',(132.75,65.0),(133.75,62.725),F)
# Route U1.66 around the lower edge of the QFN and approach the exposed pad
# from the east, clear of RESET_N at (95.6,73.95).
seg('GND',(94.05,72.4),(92.5,72.4),F); seg('GND',(92.5,72.4),(92.5,75.2),F)
seg('GND',(92.5,75.2),(96.4,75.2),F); seg('GND',(96.4,75.2),(96.4,72.4),F)
seg('GND',(96.4,72.4),(95.6,72.4),F); via('GND',(92.5,75.2))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
