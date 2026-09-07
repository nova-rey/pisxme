#!/usr/bin/env python3
"""Path-B disposable: layer-separated XTAL_IN/XTAL_OUT routing."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CRYSTAL_V2.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(x,y)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def route(b,name,layers,points):
 n=b.FindNet(name)
 for l,a,z in zip(layers,points,points[1:]): seg(b,n,l,a,z)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 route(b,'XTAL_IN',[F,F,F,F],[(66.4,55.0),(66.4,53.4),(69.3,53.4),(69.3,55.0),(69.3,56.0)])
 n=b.FindNet('XTAL_IN'); via(b,n,69.3,56.0)
 route(b,'XTAL_IN',[B,B,B],[(69.3,56.0),(73.8,56.0),(73.8,59.2),(75.2,59.2)])
 via(b,n,75.2,59.2); seg(b,n,F,(75.2,59.2),(76.05,59.2))
 route(b,'XTAL_OUT',[F,F,F,F,F,F,F],[(72.4,55.0),(72.4,54.2),(70.7,54.2),(70.7,55.0),(70.7,57.8),(75.2,57.8),(75.2,59.6),(76.05,59.6)])
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
