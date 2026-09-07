#!/usr/bin/env python3
"""Path-B V16: connect the four SPI test pads to existing routed endpoints."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_TEST_ACCESS_V1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def path(b,n,pts,l):
    for a,z in zip(pts,pts[1:]):
        if a != z: tr(b,n,a,z,l)
def main():
    b=pcbnew.LoadBoard(str(BASE))
    routes={
      'SPICS':('TP1',(85.0,62.8),(88.0,78.0),F,[(85,62.8),(85,74),(88,74),(88,78)]),
      'SPISO':('TP4',(87.0,62.0),(100.0,78.0),B,[(87,62),(87,76),(100,76),(100,78)]),
      'SPISI':('TP3',(95.6,70.0),(96.0,78.0),F,[(95.6,70),(96,70),(96,78)]),
      'SPICLK':('TP2',(83.95,64.8),(92.0,78.0),B,[(83.95,64.8),(83.95,76),(92,76),(92,78)]),
    }
    for name,(_,a,_,layer,pts) in routes.items():
        n=b.FindNet(name); path(b,n,pts,layer)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
