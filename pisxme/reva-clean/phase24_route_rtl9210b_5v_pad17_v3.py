#!/usr/bin/env python3
"""Path-B disposable: move the pad-17 B.Cu transition clear of pad 16."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_1V1_QFN_COLLECTOR_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(x,y)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_5V')
 seg(b,n,F,(83.2,65.95),(83.6,65.95)); seg(b,n,F,(83.6,65.95),(83.6,67.0)); via(b,n,83.6,67.0)
 seg(b,n,B,(83.6,67.0),(84.5,67.0)); seg(b,n,B,(84.5,67.0),(84.5,59.2)); seg(b,n,B,(84.5,59.2),(85.0,59.2)); via(b,n,85.0,59.2)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
