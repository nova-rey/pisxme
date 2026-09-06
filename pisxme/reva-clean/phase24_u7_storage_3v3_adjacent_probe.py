#!/usr/bin/env python3
"""Disposable adjacent U7 storage-3V3 pad join."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CM5_5V_FEEDBACK_DOGBONE_CURRENT.kicad_pcb'; OUT=R/'PHASE24_U7_STORAGE_3V3_ADJACENT_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/STORAGE/BRIDGE_3V3')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
t=pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.15)); t.SetStart(V(122,144.5)); t.SetEnd(V(122.5,144.5)); b.Add(t)
b.Save(str(OUT)); print(OUT)
