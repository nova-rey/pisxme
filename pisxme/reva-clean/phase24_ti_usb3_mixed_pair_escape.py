"""Disposable mixed-layer TI-U7 USB3 pair escape control."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_TI_USB3_MINIMAL_NATIVE.kicad_pcb';OUT=R/'PHASE24_TI_USB3_MIXED_PAIR_ESCAPE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.15)
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(b,r,n):return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def net(b,s):
 for q in (s,'/CORE_CM5/'+s,'/STORAGE/'+s):
  n=b.FindNet(q)
  if n:return n
 raise RuntimeError(s)
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
def path(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):tr(b,n,a,z,l)
b=pcbnew.LoadBoard(str(BASE));jobs=[('CM5_USB3_RX_N','128','42'),('CM5_USB3_RX_P','130','43'),('CM5_USB3_TX_N','140','45'),('CM5_USB3_TX_P','142','46')]
for i,(name,jp,up) in enumerate(jobs):
 n=net(b,name);src=xy(pad(b,'J7',jp));dst=xy(pad(b,'U7',up))
 if i<2:
  # Reverse lateral via order so the native source row and target row remain
  # monotonic as the pair bundle advances toward U7.
  sv=((76.,76.)[i],(102.,104.)[i]);path(b,n,[src,sv],B);via(b,n,sv)
  gatey=dst[1]+(-.25 if i==0 else .25)
  path(b,n,[sv,(90.8,gatey),(91.3,gatey),dst],F)
 else:
  sv=(82.,(105.,109.)[i-2]);tv=((91.,87.)[i-2],dst[1])
  path(b,n,[src,sv],B);via(b,n,sv);path(b,n,[sv,tv],B);via(b,n,tv);path(b,n,[tv,dst],F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
