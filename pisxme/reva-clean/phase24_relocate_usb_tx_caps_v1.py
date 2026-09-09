"""Disposable coherent relocation of USB TX AC-coupling capacitors."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb')); F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,p):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def clear(name):
 n=b.FindNet(name)
 for x in list(b.GetTracks()):
  if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
 return n
# Coherent local placement: C86/P above C87/N, close to U11 and away from AVDDL.
b.FindFootprintByReference('C86').SetPosition(V(145,140)); b.FindFootprintByReference('C87').SetPosition(V(145,142))
p=clear('USB_TXP1'); tr(p,xy('U11',21),(141.4,139.5),F); tr(p,(141.4,139.5),xy('C86',1),F)
n=clear('USB_TXN1'); tr(n,xy('U11',22),(141.0,141.5),F); tr(n,(141.0,141.5),xy('C87',1),F)
tp=clear('JMS_USB3_TXP'); via(tp,(146.0,139.5)); tr(tp,xy('C86',2),(146.0,139.5),F); tr(tp,(146.0,139.5),(151.0,137.0),B); via(tp,(151.0,137.0)); tr(tp,(151.0,137.0),xy('U12',25),F)
tn=clear('JMS_USB3_TXN'); via(tn,(146.0,141.5)); tr(tn,xy('C87',2),(146.0,141.5),F); tr(tn,(146.0,141.5),(151.0,137.4),B); via(tn,(151.0,137.4)); tr(tn,(151.0,137.4),xy('U12',24),F)
b.BuildListOfNets(); out=R/'PHASE24_STORAGE_USB_TX_CAP_RELOCATED_V1.kicad_pcb'; b.Save(str(out)); print(out)
