"""V18: co-locate USB TX coupling caps and regenerate both TX sides."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb'))
F=pcbnew.F_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(ref,pad):
 q=b.FindFootprintByReference(ref).FindPadByNumber(str(pad)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(n,a,z,w=.15):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def clear(name):
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
 return n
for ref,pos in (('C86',(148.0,140.0)),('C87',(148.0,142.0))):
 f=b.FindFootprintByReference(ref); f.SetPosition(V(*pos)); f.SetOrientationDegrees(0)
p=clear('USB_TXP1'); n=clear('USB_TXN1'); pp=clear('JMS_USB3_TXP'); nn=clear('JMS_USB3_TXN')
# U11 -> capacitor pad 1; retain V13's ordering at the QFN escape.
tr(p,xy('U11',21),(141.2,139.4));tr(p,(141.2,139.4),(141.2,140.0),.2);tr(p,(141.2,140.0),xy('C86',1),.2)
tr(n,xy('U11',22),(141.0,139.0));tr(n,(141.0,139.0),(140.6,139.4));tr(n,(140.6,139.4),(140.6,142.0),.2);tr(n,(140.6,142.0),xy('C87',1),.2)
# Capacitor pad 2 -> U12 native pads; monotonic pair order, no vias.
tr(pp,xy('C86',2),(151.0,140.0),.2);tr(pp,(151.0,140.0),(154.0,137.0),.2);tr(pp,(154.0,137.0),xy('U12',25),.15)
tr(nn,xy('C87',2),(151.0,142.0),.2);tr(nn,(151.0,142.0),(154.5,137.4),.2);tr(nn,(154.5,137.4),xy('U12',24),.15)
b.BuildListOfNets();out=R/'PHASE24_STORAGE_USB_TX_CAP_RELOC_COHERENT_V18.kicad_pcb';b.Save(str(out));print(out)
