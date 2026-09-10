"""V1503: RSET escape after removing the obsolete GND triangle."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_GND_FIELD_REPLACE_V1502.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RSET_FCU_NORTH_V1503.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('RSET'); assert n
for a,z in [((94.8,66.05),(94.8,65.5)),((94.8,65.5),(88.0,65.5)),((88.0,65.5),(88.0,65.0))]:
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
