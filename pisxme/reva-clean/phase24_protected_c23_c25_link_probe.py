#!/usr/bin/env python3
"""Disposable dogbone field for C23/C24/C25 protected pads."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_PROTECTED_C14_C15_LINK_CURRENT.kicad_pcb'; OUT=R/'PHASE24_PROTECTED_C23_C25_LINK_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('12V_PROTECTED')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
pts=[(118.9,170),(127.05,170),(134.9,170)]
for x,y in pts:
 t=pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.2)); t.SetStart(V(x,y)); t.SetEnd(V(x,174.5)); b.Add(t)
for a,z in zip(pts,pts[1:]):
 t=pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.2)); t.SetStart(V(a[0],174.5)); t.SetEnd(V(z[0],174.5)); b.Add(t)
b.Save(str(OUT)); print(OUT)
