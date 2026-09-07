#!/usr/bin/env python3
"""Path-B disposable: offset B.Cu escape for U1 RTL_3V3 pad 34."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CRYSTAL_V11.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_PAD34_BCU_V1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(x,y)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
 seg(b,n,F,(83.95,58.8),(84.8,58.8)); seg(b,n,F,(84.8,58.8),(84.8,58.0)); via(b,n,84.8,58.0)
 seg(b,n,B,(84.8,58.0),(84.8,42.0))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
