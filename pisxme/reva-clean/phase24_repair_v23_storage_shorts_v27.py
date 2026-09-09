"""V27: disposable repair of the two storage-local V23 native shorts."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_JMS583_CRYSTAL_VIAS_V23_FILLED.kicad_pcb'
OUT=R/'PHASE24_STORAGE_V23_STORAGE_SHORTS_REPAIRED_V27.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def xy(p):
 q=p.GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def clear(b,name):
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
 return n
def seg(b,n,a,z,l,w=.2):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l)
 t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.55))
 v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu)
 v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
n=clear(b,'STORAGE_SEL')
seg(b,n,xy(pad(b,'U12','9')),(153.5,132.5),pcbnew.F_Cu); via(b,n,(153.5,132.5))
seg(b,n,(153.5,132.5),(211.1,132.5),pcbnew.B_Cu)
seg(b,n,(211.1,132.5),(211.1,148.95),pcbnew.B_Cu); via(b,n,(211.1,148.95))
seg(b,n,(211.1,148.95),xy(pad(b,'U14','4')),pcbnew.F_Cu)
n=clear(b,'VBUS')
seg(b,n,xy(pad(b,'R82','1')),(127.0,117.0),pcbnew.F_Cu); via(b,n,(127.0,117.0))
seg(b,n,(127.0,117.0),(127.0,140.0),pcbnew.B_Cu); via(b,n,(127.0,140.0))
seg(b,n,(127.0,140.0),xy(pad(b,'U11','16')),pcbnew.F_Cu)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
