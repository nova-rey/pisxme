"""V1444: move R1 west/south so RSET can stay on a clear F.Cu corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RSET_MOVE_WESTSOUTH_V1444.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); r=next(f for f in b.GetFootprints() if f.GetReference()=='R1'); r.SetPosition(r.GetPosition()+P(-4,5)); n=b.FindNet('RSET'); assert n
for a,z in [((94.8,66.05),(84.0,66.05)),((84.0,66.05),(84.0,70.0))]:
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
