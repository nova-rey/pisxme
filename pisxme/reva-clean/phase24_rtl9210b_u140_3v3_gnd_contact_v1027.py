"""V1027: repair the V1026 GND replacement path's 0.2 mm via gap."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U140_3V3_GND_COAUTHOR_V1026.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U140_3V3_GND_CONTACT_V1027.kicad_pcb'; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); ng=b.FindNet('GND')
for q in list(b.GetTracks()):
 if q.GetNetCode()!=ng.GetNetCode() or q.GetLayer()!=B: continue
 s=q.GetStart(); e=q.GetEnd();
 if s.x/1e6<96 and e.x/1e6<96 and s.y/1e6<70 and e.y/1e6<70: b.Remove(q)
add(b,ng,[(94.0,62.0),(96.0,60.0),(89.2,60.0),(89.2,67.0)],B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
