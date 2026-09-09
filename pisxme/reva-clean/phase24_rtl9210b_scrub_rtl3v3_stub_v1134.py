"""V1134: remove only the inherited dangling RTL_3V3 branch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb';OUT=H/'PHASE24_RTL9210B_RTL3V3_STUB_SCRUB_V1134.kicad_pcb';P=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if q.GetNetname()=='RTL_3V3' and type(q).__name__=='PCB_TRACK' and q.GetStart()==P(99.6,62.8) and q.GetEnd()==P(99.6,61.5): b.RemoveNative(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
