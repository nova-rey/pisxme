"""V7: package-edge 0.15 mm neckdown, normal corridor thereafter."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb')); F=pcbnew.F_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,p):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(n,a,z,w):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def clear(name):
 n=b.FindNet(name)
 for x in list(b.GetTracks()):
  if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
 return n
p=clear('USB_TXP1'); tr(p,xy('U11',21),(141.4,139.3),.15); tr(p,(141.4,139.3),(141.4,144),.2); tr(p,(141.4,144),(146.5,144),.2); tr(p,(146.5,144),xy('C86',1),.2)
n=clear('USB_TXN1'); tr(n,xy('U11',22),(141.0,139.3),.15); tr(n,(141.0,139.3),(141.0,146),.2); tr(n,(141.0,146),(146.5,146),.2); tr(n,(146.5,146),xy('C87',1),.2)
b.BuildListOfNets(); out=R/'PHASE24_STORAGE_J8_V5_USB_TX_PAIR_QFN_NECKDOWN_V7.kicad_pcb'; b.Save(str(out)); print(out)
