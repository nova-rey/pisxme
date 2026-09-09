"""V698: remove the two unused RTL_5V transition vias from V697."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_OVERPASS_V697.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_OVERPASS_CLEAN_V698.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and q.GetNetname()=='RTL_5V':
  p=q.GetPosition();xy=(round(pcbnew.ToMM(p.x),3),round(pcbnew.ToMM(p.y),3))
  if xy==(104.0,52.0):b.RemoveNative(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
