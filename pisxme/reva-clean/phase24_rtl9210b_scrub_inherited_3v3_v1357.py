"""V1357: remove the explicitly identified inherited dangling RTL_3V3 stub."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_PERST_LOWER_SHELF_V1355.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_SCRUBBED_V1357.kicad_pcb'
P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); removed=0
for t in list(b.GetTracks()):
    ends={(t.GetStart().x,t.GetStart().y),(t.GetEnd().x,t.GetEnd().y)}
    wanted={(P(99.6,62.8).x,P(99.6,62.8).y),(P(99.6,61.5).x,P(99.6,61.5).y)}
    if t.GetNetname()=='RTL_3V3' and t.GetLayerName()=='B.Cu' and ends==wanted:
        b.RemoveNative(t); removed+=1
assert removed==1
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
