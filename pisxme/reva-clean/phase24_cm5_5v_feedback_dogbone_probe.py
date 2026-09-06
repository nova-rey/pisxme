#!/usr/bin/env python3
"""Disposable CM5 5V feedback chain dogbone."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_PROTECTED_C23_C25_LINK_CURRENT.kicad_pcb'
OUT=R/'PHASE24_CM5_5V_FEEDBACK_DOGBONE_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/REGULATORS/FB_CM5_5V')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(a,z):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.F_Cu); q.SetNet(n); q.SetWidth(pcbnew.FromMM(.2)); q.SetStart(V(*a)); q.SetEnd(V(*z)); b.Add(q)
pts=[(80.05,164),(85.5,164),(89.5,164)]
for x,y in pts: T((x,y),(x,161.5))
T((80.05,161.5),(85.5,161.5)); T((85.5,161.5),(89.5,161.5))
b.Save(str(OUT)); print(OUT)
