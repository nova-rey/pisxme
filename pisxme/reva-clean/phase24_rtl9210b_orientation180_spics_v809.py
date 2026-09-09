"""V809: transplant the native-clean V718 SPICS dogleg to V808."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_CONTROLS_V808.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_SPICS_V809.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('SPICS')
path=[(94.05,69.2),(92.5,69.2),(92.5,64),(93.5,63),(93.5,49),(83.3,49),(83.3,50)]
for a,z in zip(path,path[1:]):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
