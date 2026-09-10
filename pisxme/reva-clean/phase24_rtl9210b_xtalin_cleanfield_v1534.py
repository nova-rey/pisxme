"""V1534: isolated XTAL_IN F.Cu channel on the accepted V1523 field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALIN_CLEANFIELD_V1534.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('XTAL_IN'); F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def tr(a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
tr((94.05,67.2),(92.6,67.2)); tr((92.6,67.2),(92.6,63.2)); tr((92.6,63.2),(88.0,63.2)); tr((88.0,63.2),(88.0,62.0)); tr((88.0,62.0),(88.0,59.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
