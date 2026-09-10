"""V1491: close the retained RTL_3V3 branch after moving its shelf."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_GND_REROUTE_RTL3V3_V1490.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_REROUTE_RTL3V3_V1491.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE))
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('RTL_3V3'); assert n
t=pcbnew.PCB_TRACK(b); t.SetStart(V(99.6,65.8)); t.SetEnd(V(99.6,66.8)); t.SetLayer(pcbnew.B_Cu); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
