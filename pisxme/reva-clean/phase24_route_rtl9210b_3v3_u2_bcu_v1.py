#!/usr/bin/env python3
"""Path-B disposable: move U2 3V3 trunks below the PEDET corridor."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CRYSTAL_V11.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_U2_BCU_V1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def near(p,x,y): return abs(p.x-pcbnew.FromMM(x))<2 and abs(p.y-pcbnew.FromMM(y))<2
def same(a,z,x1,y1,x2,y2): return (near(a,x1,y1) and near(z,x2,y2)) or (near(a,x2,y2) and near(z,x1,y1))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(x,y)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
 for item in list(b.GetTracks()):
  if item.GetNetname()!='RTL_3V3' or isinstance(item,pcbnew.PCB_VIA): continue
  a,z=item.GetStart(),item.GetEnd()
  if same(a,z,93.2,58,93.2,42) or same(a,z,99.2,58,99.2,42): b.RemoveNative(item)
 for x in (93.2,99.2):
  seg(b,n,F,(x,58),(x,59)); via(b,n,x,59); seg(b,n,B,(x,59),(x,42))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
