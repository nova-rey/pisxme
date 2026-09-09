"""V1062: join the rotated-U2 3V3 island to the C3 3V3 trunk."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U2_3V3_V1061.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U2_3V3_V1062.kicad_pcb'; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
for a,z in zip([(119.8,74.0),(123.5,74.0),(123.5,49.0),(119.2,49.0),(119.2,51.0)],[(123.5,74.0),(123.5,49.0),(119.2,49.0),(119.2,51.0),(119.2,51.0)]):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(B); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
