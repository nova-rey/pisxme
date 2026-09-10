"""V1374: replace the short U1.50 endpoint stub with the full via contact."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U150_1V1_UPPER_V1372.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U150_1V1_UPPER_V1374.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1'); assert n; removed=0
for x in list(b.GetTracks()):
    if (x.GetNetname()=='RTL_1V1' and x.GetLayerName()=='F.Cu' and
        ((x.GetStart()==P(97.8,65.0) and x.GetEnd()==P(97.8,64.8)) or
         (x.GetStart()==P(97.8,64.8) and x.GetEnd()==P(97.8,65.0)))):
        b.RemoveNative(x); removed+=1
assert removed==1
q=pcbnew.PCB_TRACK(b); q.SetStart(P(97.8,65.0)); q.SetEnd(P(97.8,63.6)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
