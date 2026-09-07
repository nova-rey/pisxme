"""Disposable native USB3 route for the dual-mode storage island.

All terminals are resolved from saved PCB pads. The script only changes this
fixture's pad net ownership and emits ordinary outer-layer tracks; it does not
alter the production acreage PCB.
"""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent
BASE=Path(os.environ.get('PISXME_DUAL_USB3_BASE', str(R/'PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb')))
OUT=Path(os.environ.get('PISXME_DUAL_USB3_OUT', str(R/'PHASE24_DUAL_MODE_STORAGE_USB3_ROUTED.kicad_pcb')))
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(p): return pcbnew.VECTOR2I_MM(float(p[0]),float(p[1]))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def pad(b,r,n):
 f=next((q for q in b.GetFootprints() if q.GetReference()==r),None)
 if f is None: raise RuntimeError('missing footprint '+r)
 return next((p for p in f.Pads() if str(p.GetNumber())==str(n)),None)
def getnet(b,name):
 n=b.FindNet(name)
 if n is None: n=pcbnew.NETINFO_ITEM(b,name); n.SetNetCode(b.GetNetCount()+1); b.Add(n)
 return n
def setnet(p,n): p.SetNet(n); p.SetNetCode(n.GetNetCode())
def tr(b,n,a,z,layer=F,w=.15):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(a)); t.SetEnd(V(z)); t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); b.Add(t)
def path(b,name,refs,layer=F):
 n=getnet(b,name); pts=[]
 for r,k in refs: pts.append(xy(pad(b,r,k).GetPosition()))
 for a,z in zip(pts,pts[1:]): tr(b,n,a,z,layer)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 # Replace inherited CM5-to-old-U7 USB3 copper in this disposable fixture.
 for item in list(b.GetTracks()):
  if item.GetNetname() in ('/CORE_CM5/CM5_USB3_TX_P','/CORE_CM5/CM5_USB3_TX_N','/CORE_CM5/CM5_USB3_RX_P','/CORE_CM5/CM5_USB3_RX_N'):
   b.RemoveNative(item)
 # CM5 USB3 source authority from CORE_CM5/J7.
 src=[('/CORE_CM5/CM5_USB3_TX_P','142','11'),('/CORE_CM5/CM5_USB3_TX_N','140','12'),
      ('/CORE_CM5/CM5_USB3_RX_P','130','15'),('/CORE_CM5/CM5_USB3_RX_N','128','16')]
 for name,j7,u12 in src:
  n=getnet(b,name); setnet(pad(b,'J7',j7),n); setnet(pad(b,'U12',u12),n)
  a=xy(pad(b,'J7',j7).GetPosition()); z=xy(pad(b,'U12',u12).GetPosition())
  # compact monotonic source corridor in the open storage region
  lane={'142':70,'140':73,'130':76,'128':79}[j7]
  tr(b,n,a,(lane,a[1])); tr(b,n,(lane,a[1]),(lane,z[1])); tr(b,n,(lane,z[1]),z)
 # One USB3 lane through each required JMS583 TX coupling capacitor and U12.
 path(b,'USB_TXP1',[('U11','21'),('C86','1')],B); path(b,'JMS_USB3_TXP',[('C86','2'),('U12','25')],B)
 path(b,'USB_TXN1',[('U11','22'),('C87','1')],B); path(b,'JMS_USB3_TXN',[('C87','2'),('U12','24')],B)
 path(b,'USB_RXP1',[('U11','26'),('U12','23')],B); path(b,'USB_RXN1',[('U11','27'),('U12','22')],B)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
