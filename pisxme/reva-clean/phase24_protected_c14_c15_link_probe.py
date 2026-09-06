#!/usr/bin/env python3
"""Disposable dogbone link for the C14/C15 protected capacitor pads."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_12V_B_C4_U2_OBSTACLE_ROUTE_CURRENT.kicad_pcb'; OUT=R/'PHASE24_PROTECTED_C14_C15_LINK_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('12V_PROTECTED')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
for a,z in [((68.9,120),(68.9,122.5)),((68.9,122.5),(76.9,122.5)),((76.9,122.5),(76.9,120))]:
 t=pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.2)); t.SetStart(V(*a)); t.SetEnd(V(*z)); b.Add(t)
b.Save(str(OUT)); print(OUT)
