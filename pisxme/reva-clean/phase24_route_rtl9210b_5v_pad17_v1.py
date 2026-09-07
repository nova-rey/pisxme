#!/usr/bin/env python3
"""Path-B V22: connect U1 RTL_5V pad 17 to the existing 5V bus."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_1V1_QFN_COLLECTOR_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_5V_PAD17_V1.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def path(b,n,pts):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def main():
    b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_5V')
    path(b,n,[(83.2,65.95),(87,65.95),(87,57),(85,57),(85,59.2)])
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
