"""V13: upper P-leg detour for TX balance without crossing the N leg."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_U11_STAGGERED_LOWER_FIELD_V8.kicad_pcb')); F=pcbnew.F_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,p):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(n,a,z,w):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
n=b.FindNet('USB_TXP1')
for x in list(b.GetTracks()):
 if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
pts=[xy('U11',21),(141.2,139.4),(141.2,144),(142.0,144),(142.0,141.5),(144.0,141.5),(144.0,144),(146.5,144),xy('C86',1)]
for i,(a,z) in enumerate(zip(pts,pts[1:])): tr(n,a,z,.15 if i==0 else .2)
b.BuildListOfNets(); out=R/'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb'; b.Save(str(out)); print(out)
