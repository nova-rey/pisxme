"""Disposable V3: paired F.Cu dogbones plus retained AVDDL basis."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb')); F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,p):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def clear(name):
 n=b.FindNet(name)
 for x in list(b.GetTracks()):
  if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
 return n
p=clear('USB_TXP1'); tr(p,xy('U11',21),(140.4,139.6),F); tr(p,(140.4,139.6),(140.4,144),F); tr(p,(140.4,144),(146.5,144),F); tr(p,(146.5,144),xy('C86',1),F)
n=clear('USB_TXN1'); tr(n,xy('U11',22),(141.1,139.6),F); tr(n,(141.1,139.6),(141.1,146),F); tr(n,(141.1,146),(146.5,146),F); tr(n,(146.5,146),xy('C87',1),F)
a=clear('JMS_AVDDL'); tr(a,xy('U11',20),(141.8,140.5),F)
v=pcbnew.PCB_VIA(b); v.SetPosition(V(141.8,140.5)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(a); v.SetNetCode(a.GetNetCode()); b.Add(v)
tr(a,(141.8,140.5),(154.5,142),B)
v=pcbnew.PCB_VIA(b); v.SetPosition(V(154.5,142)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(a); v.SetNetCode(a.GetNetCode()); b.Add(v)
tr(a,(154.5,142),(154.5,147),F); tr(a,(154.5,147),xy('C83',1),F)
b.BuildListOfNets(); out=R/'PHASE24_STORAGE_J8_V5_USB_TX_PAIR_AVDDL_V3.kicad_pcb'; b.Save(str(out)); print(out)
