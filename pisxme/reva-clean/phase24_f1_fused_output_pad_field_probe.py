#!/usr/bin/env python3
"""Disposable F1 fused-output same-net PTH field."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_F1_INPUT_PAD_FIELD_CURRENT.kicad_pcb'; OUT=R/'PHASE24_F1_FUSED_OUTPUT_PAD_FIELD_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/POWER_INPUT/FUSED_12V_A')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(a,z):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.B_Cu); q.SetNet(n); q.SetWidth(pcbnew.FromMM(1.2)); q.SetStart(V(*a)); q.SetEnd(V(*z)); b.Add(q)
T((242.9,38.75),(246.4,38.75)); T((242.9,41.25),(246.4,41.25)); T((242.9,38.75),(242.9,41.25)); T((246.4,38.75),(246.4,41.25))
b.Save(str(OUT)); print(OUT)
