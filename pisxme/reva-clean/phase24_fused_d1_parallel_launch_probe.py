#!/usr/bin/env python3
"""Disposable parallel B.Cu D1 fused-A launch."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_FUSED_Q1_LAUNCH_CURRENT.kicad_pcb'; OUT=R/'PHASE24_FUSED_D1_PARALLEL_LAUNCH_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/POWER_INPUT/FUSED_12V_A')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
q=pcbnew.PCB_VIA(b); q.SetNet(n); q.SetPosition(V(108,20)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); b.Add(q)
for layer,a,z,w in [(pcbnew.F_Cu,(108,32),(108,20),.25),(pcbnew.B_Cu,(108,20),(212.46,20),1.0),(pcbnew.B_Cu,(212.46,20),(212.46,25),1.0)]:
 t=pcbnew.PCB_TRACK(b); t.SetLayer(layer); t.SetNet(n); t.SetWidth(pcbnew.FromMM(w)); t.SetStart(V(*a)); t.SetEnd(V(*z)); b.Add(t)
b.Save(str(OUT)); print(OUT)
