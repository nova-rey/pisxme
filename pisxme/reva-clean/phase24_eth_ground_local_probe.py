#!/usr/bin/env python3
"""Disposable local Ethernet support-ground pad joins only."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_GROUND_CAP_LINKS_CURRENT.kicad_pcb'; OUT=R/'PHASE24_ETH_GROUND_LOCAL_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('POWER_GND')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
for x in (20,26):
 t=pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.20)); t.SetStart(V(x,103.615)); t.SetEnd(V(x,104.385)); b.Add(t)
b.Save(str(OUT)); print(OUT)
