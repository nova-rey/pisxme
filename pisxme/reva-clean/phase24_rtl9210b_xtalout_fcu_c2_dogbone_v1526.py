"""V1526: move the C2.1 approach below its adjacent ground pad."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALOUT_FCU_C2_DOGBONE_V1526.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('XTAL_OUT'); F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def tr(a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
tr((94.05,67.6),(93.2,67.6)); tr((93.2,67.6),(93.2,62.8)); tr((93.2,62.8),(91.0,62.8)); tr((91.0,62.8),(91.0,62.0)); tr((91.0,62.0),(91.0,60.5)); tr((91.0,60.5),(89.4,59.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
