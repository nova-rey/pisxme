"""V1458: farther-bottom ordinary-via U1.66/U1.69 ground access probe."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U166_GND_EDGE_V1458.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(a,z,n):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND'); assert n
seg((94.05,72.4),(92.7,72.4),n); seg((92.7,72.4),(92.7,74.8),n); seg((92.7,74.8),(95.6,74.8),n); seg((95.6,74.8),(95.6,72.4),n)
v=pcbnew.PCB_VIA(b); v.SetPosition(P(92.7,74.8)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
