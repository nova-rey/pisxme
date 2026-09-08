"""V561: deduplicate exact duplicate tracks only; preserve all vias."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V368.kicad_pcb';out=H/'PHASE24_RTL9210B_V368_DEDUP_TRACKS_V561.kicad_pcb'
b=pcbnew.LoadBoard(str(src));seen=set();removed=0
for item in list(b.GetTracks()):
 if item.GetClass()!='PCB_TRACK': continue
 a=item.GetStart();z=item.GetEnd();key=(item.GetNetCode(),item.GetLayer(),a.x,a.y,z.x,z.y,item.GetWidth());rev=(item.GetNetCode(),item.GetLayer(),z.x,z.y,a.x,a.y,item.GetWidth())
 if key in seen or rev in seen:b.RemoveNative(item);removed+=1
 else:seen.add(key)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out,'tracks removed',removed)
