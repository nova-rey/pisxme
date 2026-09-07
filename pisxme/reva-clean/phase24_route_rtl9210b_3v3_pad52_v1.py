#!/usr/bin/env python3
"""Path-B disposable: west-side U1 RTL_3V3 pad-52 escape."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_PAD52_V1.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
 seg(b,n,(76.05,58.8),(75.2,58.8)); seg(b,n,(75.2,58.8),(75.2,48.0))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
