"""V560: remove exact duplicate saved-board tracks/vias from the V368 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V368.kicad_pcb';out=H/'PHASE24_RTL9210B_V368_DEDUP_V560.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); seen=set(); removed=0
for item in list(b.GetTracks()):
 a=item.GetStart(); z=item.GetEnd();
 key=(item.GetClass(),item.GetNetCode(),item.GetLayer(),a.x,a.y,z.x,z.y,item.GetWidth(),getattr(item,'GetDrill',lambda:0)())
 rev=(item.GetClass(),item.GetNetCode(),item.GetLayer(),z.x,z.y,a.x,a.y,item.GetWidth(),getattr(item,'GetDrill',lambda:0)())
 if key in seen or rev in seen:
  b.RemoveNative(item);removed+=1
 else: seen.add(key)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out,'duplicates removed',removed)
