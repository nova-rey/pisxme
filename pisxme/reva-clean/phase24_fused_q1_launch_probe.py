#!/usr/bin/env python3
"""Disposable Q1 fused-A launch to its existing native B.Cu segment."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_F1_FUSED_OUTPUT_PAD_FIELD_CURRENT.kicad_pcb'; OUT=R/'PHASE24_FUSED_Q1_LAUNCH_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/POWER_INPUT/FUSED_12V_A')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
t=pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.B_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.5)); t.SetStart(V(27.46,78)); t.SetEnd(V(22.5,80)); b.Add(t)
b.Save(str(OUT)); print(OUT)
