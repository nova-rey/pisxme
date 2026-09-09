"""V11: shorten TXN below the U11 field, preserving the V8 TXP path."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_U11_STAGGERED_LOWER_FIELD_V8.kicad_pcb')); F=pcbnew.F_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,p):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(n,a,z,w):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
n=b.FindNet('USB_TXN1')
for x in list(b.GetTracks()):
 if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
pts=[xy('U11',22),(141.0,139.4),(140.8,145.0),(146.5,149.0),xy('C87',1)]
for i,(a,z) in enumerate(zip(pts,pts[1:])): tr(n,a,z,.15 if i<2 else .2)
b.BuildListOfNets(); out=R/'PHASE24_STORAGE_USB_TX_PAIR_SHORTEN_TXN_V11.kicad_pcb'; b.Save(str(out)); print(out)
