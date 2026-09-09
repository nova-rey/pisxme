"""V9: clear the TXN-to-adjacent-pad clearance in the retained V8 fanout."""
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
tr(n,xy('U11',22),(141.0,139.5),.15); tr(n,(141.0,139.5),(140.8,139.7),.15); tr(n,(140.8,139.7),(140.8,146),.2); tr(n,(140.8,146),(146.5,146),.2); tr(n,(146.5,146),xy('C87',1),.2)
b.BuildListOfNets(); out=R/'PHASE24_STORAGE_U11_STAGGERED_LOWER_FIELD_V9.kicad_pcb'; b.Save(str(out)); print(out)
