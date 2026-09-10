"""V1489: restore U1.50 RTL_1V1 around the new GND via pocket."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_GND_NORTH_POCKET_V1488.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_NORTH_POCKET_V1489.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE))
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('RTL_1V1'); assert n
def tr(a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
# U1.50 actual pad to the retained RTL_1V1 upper network, staying east of
# the adjacent GND escape and clear of the RSET/XTAL pads.
tr((95.2,66.05),(95.2,65.8)); tr((95.2,65.8),(96.2,65.8)); tr((96.2,65.8),(96.2,63.6)); tr((96.2,63.6),(97.8,63.6))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
