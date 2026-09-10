"""V1372: U1.50 RTL_1V1 upper dogbone around the USB pad row."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U2_3V3_SUPPORT_V1370.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U150_1V1_UPPER_V1372.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1'); assert n
tr(b,n,(95.2,66.05),(95.2,65.0)); tr(b,n,(95.2,65.0),(97.8,65.0)); tr(b,n,(97.8,65.0),(97.8,64.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
