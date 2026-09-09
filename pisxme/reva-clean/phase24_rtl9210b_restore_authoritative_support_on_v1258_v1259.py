"""V1259: restore V1243 local rail/GND support onto the proven V1258 lane path."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_J1_PAD_ALIGNED_LAUNCH_V1258.kicad_pcb';DONOR=H/'PHASE24_RTL9210B_RAILS_REFCLK_FIXED_V1243.kicad_pcb';OUT=H/'PHASE24_RTL9210B_SUPPORT_RESTORE_ON_LANE_V1259.kicad_pcb'
def xy(p):return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def local(p):
 x,y=xy(p);return 90<=x<=104 and 63<=y<=80
b=pcbnew.LoadBoard(str(BASE));d=pcbnew.LoadBoard(str(DONOR))
for q in d.GetTracks():
 if q.GetNetname() in ('RTL_1V1','RTL_3V3','GND') and (local(q.GetStart()) or local(q.GetEnd())):b.Add(q.Duplicate())
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
