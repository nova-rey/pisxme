#!/usr/bin/env python3
"""Path-B disposable: coherent pad-55 move plus separated crystal exits."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CRYSTAL_V11.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def near(p,x,y): return abs(p.x-pcbnew.FromMM(x))<2 and abs(p.y-pcbnew.FromMM(y))<2
def same(a,z,x1,y1,x2,y2): return (near(a,x1,y1) and near(z,x2,y2)) or (near(a,x2,y2) and near(z,x1,y1))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(x,y)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def add(b,name,l,pts):
 n=b.FindNet(name)
 for a,z in zip(pts,pts[1:]): seg(b,n,l,a,z)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n1=b.FindNet('RTL_1V1')
 for item in list(b.GetTracks()):
  if item.GetNetname()=='RTL_1V1':
   if isinstance(item,pcbnew.PCB_VIA) and near(item.GetPosition(),74.5,60.0): b.RemoveNative(item)
   elif not isinstance(item,pcbnew.PCB_VIA) and same(item.GetStart(),item.GetEnd(),76.05,60,74.5,60): b.RemoveNative(item)
 seg(b,n1,F,(76.05,60),(74.0,60)); seg(b,n1,F,(74.0,60),(74.0,60.2)); via(b,n1,74.0,60.2); seg(b,n1,B,(74.0,60.2),(74.5,62.0))
 ni=b.FindNet('XTAL_IN'); no=b.FindNet('XTAL_OUT')
 add(b,'XTAL_IN',F,[(66.4,55),(66.4,53.4),(69.3,53.4),(69.3,55),(69.3,56.0)]); via(b,ni,69.3,56.0)
 add(b,'XTAL_IN',B,[(69.3,56),(69.3,57),(72.0,57),(72.0,59.2)]); via(b,ni,72.0,59.2); seg(b,ni,F,(72.0,59.2),(76.05,59.2))
 add(b,'XTAL_OUT',F,[(72.4,55),(72.4,54.2),(70.7,54.2),(70.7,55),(70.7,57.8)]); via(b,no,70.7,57.8)
 add(b,'XTAL_OUT',B,[(70.7,57.8),(70.7,61),(72.8,61),(72.8,60.6)]); via(b,no,72.8,60.6)
 add(b,'XTAL_OUT',F,[(72.8,60.6),(72.8,59.6),(76.05,59.6)])
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
