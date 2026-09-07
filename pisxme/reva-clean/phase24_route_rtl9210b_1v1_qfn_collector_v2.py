#!/usr/bin/env python3
"""Path-B V19: V1 collector with SPI-safe right branch and CLKREQ jog."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V12.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_1V1_QFN_COLLECTOR_V2.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def path(b,n,pts,l):
    for a,z in zip(pts,pts[1:]):
        if a != z: tr(b,n,a,z,l)
def via(b,n,p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1')
    branches=[
      ((77.2,58.05),(77.2,56.5)), ((81.2,58.05),(81.2,56.5)),
      ((76.05,60.0),(74.5,60.0)), ((76.05,62.0),(74.5,62.0)),
      ((76.05,63.2),(74.5,63.2)), ((82.8,65.95),(82.8,67.5)),
    ]
    for padp,vp in branches: path(b,n,[padp,vp],F); via(b,n,vp)
    # Existing V12 via at (83.5,56.8) is reused; do not duplicate it.
    path(b,n,[(74.5,60),(74.5,56.5),(83.5,56.5),(83.5,56.8)],B)
    path(b,n,[(81.2,56.5),(83.5,56.5)],B)
    path(b,n,[(77.2,56.5),(81.2,56.5)],B)
    # Bottom return jogs around CLKREQ_N's vertical B.Cu corridor at x=81.6.
    path(b,n,[(74.5,60),(74.5,67.5),(80.5,67.5),(80.5,68.5),(82.8,68.5),(82.8,67.5)],B)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
