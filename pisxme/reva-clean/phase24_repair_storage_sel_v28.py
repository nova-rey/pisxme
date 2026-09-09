"""V28: disposable STORAGE_SEL escape below U12/U14 pad fields."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_STORAGE_JMS583_CRYSTAL_VIAS_V23_FILLED.kicad_pcb';OUT=R/'PHASE24_STORAGE_SEL_ESCAPE_V28.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(b,r,n):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('STORAGE_SEL')
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode():b.RemoveNative(t)
def seg(a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
seg(xy(b,'U12','9'),(153.5,140),pcbnew.F_Cu);via((153.5,140));seg((153.5,140),(211.1,140),pcbnew.B_Cu);seg((211.1,140),(211.1,153),pcbnew.B_Cu);via((211.1,153));seg((211.1,153),xy(b,'U14','4'),pcbnew.F_Cu)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
