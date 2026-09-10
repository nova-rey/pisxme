"""V1445-V1448: disposable local U1.66-to-pad69 GND launch variants."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
paths=[[(94.05,72.4),(95.0,73.5),(97.0,73.5),(97.0,71.0),(98.0,70.0)],[(94.05,72.4),(95.0,73.2),(96.5,73.2),(98.0,70.0)],[(94.05,72.4),(93.5,73.5),(96.5,73.5),(98.0,70.0)],[(94.05,72.4),(94.05,74.0),(97.5,74.0),(97.5,71.0),(98.0,70.0)]]
for i,pts in enumerate(paths,1445):
 b=pcbnew.LoadBoard(str(BASE)); add(b,b.FindNet('GND'),pts); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); out=H/f'PHASE24_RTL9210B_U166_GND_LOCAL_V{i}.kicad_pcb'; b.Save(str(out)); print(out)
