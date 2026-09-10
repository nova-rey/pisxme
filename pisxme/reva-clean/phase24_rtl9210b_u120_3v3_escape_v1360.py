"""V1360: connect U1.20 to the existing RTL_3V3 F.Cu branch around U1.25."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U152_3V3_ESCAPE_V1359.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U120_3V3_ESCAPE_V1360.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3'); assert n
tr(b,n,(101.95,72.4),(103.0,72.4)); tr(b,n,(103.0,72.4),(103.0,66.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
