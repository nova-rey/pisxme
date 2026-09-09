"""V5: straight, order-preserving 0.20 mm USB TX pair on the VBUS basis."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb')); F=pcbnew.F_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,p):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def clear(name):
 n=b.FindNet(name)
 for x in list(b.GetTracks()):
  if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
 return n
# Keep source order (TXP right, TXN left) and never cross the pair.
p=clear('USB_TXP1'); tr(p,xy('U11',21),(141.4,144.0)); tr(p,(141.4,144.0),(146.5,144.0)); tr(p,(146.5,144.0),xy('C86',1))
n=clear('USB_TXN1'); tr(n,xy('U11',22),(141.0,146.0)); tr(n,(141.0,146.0),(146.5,146.0)); tr(n,(146.5,146.0),xy('C87',1))
b.BuildListOfNets(); out=R/'PHASE24_STORAGE_J8_V5_USB_TX_PAIR_STRAIGHT_V5.kicad_pcb'; b.Save(str(out)); print(out)
