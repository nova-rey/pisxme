#!/usr/bin/env python3
"""Disposable U7.24 to U7.30/U7.31 storage-3V3 dogbone."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_U7_STORAGE_3V3_ADJACENT_CURRENT.kicad_pcb'; OUT=R/'PHASE24_U7_STORAGE_3V3_PAD24_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/STORAGE/BRIDGE_3V3')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
for a,z in [((119,144.5),(119,146.5)),((119,146.5),(122.5,146.5)),((122.5,146.5),(122.5,144.5))]:
 t=pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.15)); t.SetStart(V(*a)); t.SetEnd(V(*z)); b.Add(t)
b.Save(str(OUT)); print(OUT)
