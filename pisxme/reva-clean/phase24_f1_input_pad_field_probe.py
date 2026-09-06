#!/usr/bin/env python3
"""Disposable F1 input-side same-net PTH field."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_BRIDGE_3V3_CAPBANK_LINKS_CURRENT.kicad_pcb'; OUT=R/'PHASE24_F1_INPUT_PAD_FIELD_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/POWER_INPUT/12V_IN_A')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(a,z):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.B_Cu); q.SetNet(n); q.SetWidth(pcbnew.FromMM(1.2)); q.SetStart(V(*a)); q.SetEnd(V(*z)); b.Add(q)
T((233.6,38.75),(237.1,38.75)); T((233.6,41.25),(237.1,41.25)); T((233.6,38.75),(233.6,41.25)); T((237.1,38.75),(237.1,41.25))
b.Save(str(OUT)); print(OUT)
