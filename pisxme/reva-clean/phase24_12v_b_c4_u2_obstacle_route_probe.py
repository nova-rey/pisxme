#!/usr/bin/env python3
"""Disposable obstacle-aware C4/U2 12V_IN_B route."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_FUSED_D1_PARALLEL_LAUNCH_CURRENT.kicad_pcb'; OUT=R/'PHASE24_12V_B_C4_U2_OBSTACLE_ROUTE_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/POWER_INPUT/12V_IN_B')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
for x,y in ((17,90),(22.5,96.45)):
 q=pcbnew.PCB_VIA(b); q.SetNet(n); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.5)); q.SetDrill(pcbnew.FromMM(.3)); b.Add(q)
for layer,a,z,w in [(pcbnew.F_Cu,(15.8,90),(17,90),.2),(pcbnew.B_Cu,(17,90),(17,96.45),.4),(pcbnew.B_Cu,(17,96.45),(22.5,96.45),.4),(pcbnew.F_Cu,(22.5,96.45),(21.45,96.45),.2)]:
 t=pcbnew.PCB_TRACK(b); t.SetLayer(layer); t.SetNet(n); t.SetWidth(pcbnew.FromMM(w)); t.SetStart(V(*a)); t.SetEnd(V(*z)); b.Add(t)
b.Save(str(OUT)); print(OUT)
