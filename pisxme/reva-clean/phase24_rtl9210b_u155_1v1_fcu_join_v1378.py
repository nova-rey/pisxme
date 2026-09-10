"""V1378: join U1.55 to the accepted U1.50 F.Cu upper rail corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U150_1V1_UPPER_V1374.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U155_1V1_FCU_JOIN_V1378.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1'); assert n
tr(b,n,(94.05,68.0),(96.0,68.0)); tr(b,n,(96.0,68.0),(96.0,65.0)); tr(b,n,(96.0,65.0),(97.8,65.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
