#!/usr/bin/env python3
"""Path-B disposable: consolidate U1 right-edge RTL_3V3 pads."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_LOCAL_V1.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
 seg(b,n,(83.95,58.8),(84.8,58.8)); seg(b,n,(84.8,58.8),(84.8,64.4)); seg(b,n,(84.8,64.4),(83.95,64.4)); seg(b,n,(84.8,58.8),(93.2,58.0))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
