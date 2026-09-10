"""V1428: compose accepted V1418 ground and V1420 SSD_3V3 primitives."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_SSD3V3_CONTACT_JOIN_V1420.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND'); assert n
q=pcbnew.PCB_TRACK(b); q.SetStart(pcbnew.VECTOR2I_MM(97.2,66.05)); q.SetEnd(pcbnew.VECTOR2I_MM(97.2,67.6)); q.SetLayer(pcbnew.F_Cu); q.SetWidth(pcbnew.FromMM(.20)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
