#!/usr/bin/env python3
"""Path-B disposable: complete crystal and load-cap support routes."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CRYSTAL_V1.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def route(b,name,points):
 n=b.FindNet(name)
 for a,z in zip(points,points[1:]): seg(b,n,a,z)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 route(b,'XTAL_IN',[(66.4,55.0),(66.4,53.8),(69.3,53.8),(69.3,55.0),(69.3,57.4),(74.8,57.4),(74.8,59.2),(76.05,59.2)])
 route(b,'XTAL_OUT',[(72.4,55.0),(72.4,53.8),(70.7,53.8),(70.7,55.0),(70.7,57.8),(75.2,57.8),(75.2,59.6),(76.05,59.6)])
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
