"""V699: remove the unused first overpass via."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_OVERPASS_CLEAN_V698.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_OVERPASS_FINAL_V699.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and q.GetNetname()=='RTL_5V':
  p=q.GetPosition();xy=(round(pcbnew.ToMM(p.x),3),round(pcbnew.ToMM(p.y),3))
  if xy==(104.0,50.0):b.RemoveNative(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
