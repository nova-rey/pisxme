"""V825: separate PEDET and CLKREQ_N resistor approaches on V772."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_ABOVE_SPI_PLACEMENT_V777.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V772_CONTROL_CORRIDOR_V825.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
r2=b.FindFootprintByReference('R2'); r2.SetPosition(r2.GetPosition()+P(4,0))
T(b,b.FindNet('PEDET'),[(101.95,70.4),(103,70.4),(103,82),(112,82),(112,60)])
T(b,b.FindNet('CLKREQ_N'),[(101.95,68.4),(105,68.4),(105,57),(108,57),(108,63)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
