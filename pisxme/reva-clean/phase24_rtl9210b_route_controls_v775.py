"""V775: route PEDET/CLKREQ_N and the local RTL_3V3 control return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_RAIL_CONTROL_PLACEMENT_V774.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V760_CONTROL_ROUTED_V775.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,p):
 for a,z in zip(p,p[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
t(b,b.FindNet('PEDET'),[(101.95,70.4),(103.0,70.4),(107.0,67.0)])
t(b,b.FindNet('CLKREQ_N'),[(101.95,68.4),(103.0,68.4),(107.0,70.0)])
t(b,b.FindNet('RTL_3V3'),[(108.2,67.0),(108.2,70.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
