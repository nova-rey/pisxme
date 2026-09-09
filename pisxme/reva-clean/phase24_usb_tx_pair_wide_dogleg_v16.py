"""V16: wider planar TXN dogleg around U11 pad 23."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb')); F=pcbnew.F_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,p):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(n,a,z,w):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
n=b.FindNet('USB_TXN1')
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
pts=[xy('U11',22),(141.0,139.2),(140.0,140.2),(140.0,146.0),(146.5,146.0),xy('C87',1)]
for i,(a,z) in enumerate(zip(pts,pts[1:])): tr(n,a,z,.15 if i<2 else .2)
b.BuildListOfNets();out=R/'PHASE24_STORAGE_USB_TX_PAIR_WIDE_DOGLEG_V16.kicad_pcb';b.Save(str(out));print(out)
