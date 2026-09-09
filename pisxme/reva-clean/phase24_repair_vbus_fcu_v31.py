"""V31: disposable F.Cu-only VBUS detour around the SATA B.Cu launch."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_STORAGE_JMS583_CRYSTAL_VIAS_V23_FILLED.kicad_pcb';OUT=R/'PHASE24_STORAGE_VBUS_FCU_V31.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(b,r,n):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('VBUS')
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode():b.RemoveNative(t)
pts=[xy(b,'R82','1'),(132,117),(132,136),(136.35,138),xy(b,'U11','16')]
for a,z in zip(pts,pts[1:]):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
