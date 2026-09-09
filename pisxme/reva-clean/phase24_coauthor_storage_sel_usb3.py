"""Disposable coordinated STORAGE_SEL + CM5 USB3 source-field regeneration."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb'));F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,n):
 p=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition();return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(n,a,z,l,w=.15):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*q));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
nset=('STORAGE_SEL','CM5_USB3_TX_P','CM5_USB3_TX_N','CM5_USB3_RX_P','CM5_USB3_RX_N')
for name in nset:
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode():b.RemoveNative(t)
# Selector: U12 left escape -> U13 left escape -> U14 right-side branch.
n=b.FindNet('STORAGE_SEL');q12=(151.8,135.0);q13=(176.5,135.0);q14=(212.5,153.0)
via(n,q12);tr(n,xy('U12',9),q12,F);via(n,q13);tr(n,q12,q13,B);tr(n,q13,xy('U13',9),F)
via(n,q14);tr(n,xy('U14',4),q14,F);tr(n,q14,(212.5,146.0),B);tr(n,(212.5,146.0),q13,B)
# Four USB3 routes, with transitions outside the QFN fields and explicit
# source/target dogbones.
for name,jpin,upin,src,old,q in [
 ('CM5_USB3_TX_P','142','11',(79,94),(161,135.8),(151,135.8)),
 ('CM5_USB3_TX_N','140','12',(77,92),(159,136.2),(149.8,136.2)),
 ('CM5_USB3_RX_P','130','15',(75,90),(157,137.4),(151.9,137.4)),
 ('CM5_USB3_RX_N','128','16',(73,88),(155,137.8),(150.9,137.8))]:
 n=b.FindNet(name);via(n,src);tr(n,xy('J7',jpin),src,F);tr(n,src,old,B);tr(n,old,q,B);via(n,q);tr(n,q,xy('U12',upin),F)
b.BuildListOfNets();out=R/'PHASE24_STORAGE_J8_V5_COAUTHORED_SEL_USB3_V1.kicad_pcb';b.Save(str(out));print(out)
