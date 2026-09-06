"""Minimal monotonic TI-U7 USB3 escape control; native DRC is authoritative."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_TI_USB3_MINIMAL_NATIVE.kicad_pcb';OUT=R/'PHASE24_TI_USB3_DIRECT_ESCAPE_CONTROL.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.15)
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def net(b,s):
 for q in (s,'/CORE_CM5/'+s,'/STORAGE/'+s):
  n=b.FindNet(q)
  if n:return n
 raise RuntimeError(s)
def pad(b,r,n):return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
b=pcbnew.LoadBoard(str(BASE));jobs=[('CM5_USB3_RX_N','128','42'),('CM5_USB3_RX_P','130','43'),('CM5_USB3_TX_N','140','45'),('CM5_USB3_TX_P','142','46')]
for i,(name,jp,up) in enumerate(jobs):
 n=net(b,name);src=xy(pad(b,'J7',jp));dst=xy(pad(b,'U7',up));sv=(76.+i*2.,src[1])
 tr(b,n,src,sv,B);via(b,n,sv);tr(b,n,sv,dst,F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
