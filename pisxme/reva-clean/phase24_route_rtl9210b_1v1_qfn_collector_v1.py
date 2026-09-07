#!/usr/bin/env python3
"""Path-B V18: ordinary-via perimeter collector for U1 RTL_1V1 pads."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V12.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_1V1_QFN_COLLECTOR_V1.kicad_pcb'
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
    # Actual U1 pad centers to exterior ordinary-via positions.
    branches=[
      ((77.2,58.05),(77.2,56.5)), ((81.2,58.05),(81.2,56.5)),
      ((76.05,60.0),(74.5,60.0)), ((76.05,62.0),(74.5,62.0)),
      ((76.05,63.2),(74.5,63.2)), ((83.95,62.4),(85.5,62.4)),
      ((82.8,65.95),(82.8,67.5)),
    ]
    for padp,vp in branches: path(b,n,[padp,vp],F); via(b,n,vp)
    # Perimeter B.Cu collector joins the branches to the existing 1V1 bus
    # transition at (83.5,56.8), without entering the QFN exposed pad.
    via(b,n,(83.5,56.8))
    path(b,n,[(74.5,60),(74.5,56.5),(83.5,56.5),(83.5,56.8)],B)
    path(b,n,[(74.5,60),(74.5,67.5),(82.8,67.5)],B)
    path(b,n,[(81.2,56.5),(83.5,56.5)],B)
    path(b,n,[(77.2,56.5),(81.2,56.5)],B)
    path(b,n,[(85.5,62.4),(85.5,56.5),(83.5,56.5)],B)
    path(b,n,[(85.5,62.4),(85.5,67.5),(82.8,67.5)],B)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
