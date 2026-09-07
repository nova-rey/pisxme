#!/usr/bin/env python3
"""Path-B V17: V12-based four-lane SPI test-access routing."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V12.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_TEST_ACCESS_V2.kicad_pcb'
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
    b=pcbnew.LoadBoard(str(BASE))
    routes={
      'SPICS':((85,62.8),(84,63.5),[(84,63.5),(84,75),(88,75)],(88,77),(88,78)),
      'SPISO':((87,62),(90,63),[(90,63),(90,76),(100,76)],(100,77),(100,78)),
      'SPISI':((95.6,70),(104,70.8),[(104,70.8),(104,77),(96,77)],(96,77),(96,78)),
      'SPICLK':((83.95,64.8),(78,65.5),[(78,65.5),(78,78),(92,78)],(92,77),(92,78)),
    }
    for name,(src,sv,bpts,tv,dst) in routes.items():
        n=b.FindNet(name); path(b,n,[src,sv],F); via(b,n,sv); path(b,n,bpts,B); via(b,n,tv); path(b,n,[tv,dst],F)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
