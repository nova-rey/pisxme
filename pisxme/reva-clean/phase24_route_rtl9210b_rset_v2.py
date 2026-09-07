#!/usr/bin/env python3
"""Path-B disposable: jog RSET around the C1 ground pad."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_PAD17_V3.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_RSET_V2.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.2)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RSET')
 for a,z in [((69.4,51.0),(68.0,51.0)),((68.0,51.0),(68.0,53.0)),((68.0,53.0),(68.8,53.0)),((68.8,53.0),(68.8,57.0)),((68.8,57.0),(75.2,57.0)),((75.2,57.0),(76.8,58.05))]: seg(b,n,a,z)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
