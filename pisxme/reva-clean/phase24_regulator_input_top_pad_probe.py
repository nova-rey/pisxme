#!/usr/bin/env python3
"""Disposable same-net top-edge joins for U4/U5 protected inputs."""
from pathlib import Path
import pcbnew
R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_BRIDGE_1V1_U5_FIELD_CURRENT.kicad_pcb'
OUT = R / 'PHASE24_REGULATOR_INPUT_TOP_PAD_CURRENT.kicad_pcb'
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet('12V_PROTECTED')
def V(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))
for x1, x2 in ((232.75, 237.25),):
    t = pcbnew.PCB_TRACK(b)
    t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.25))
    t.SetStart(V(x1, 103)); t.SetEnd(V(x2, 103)); b.Add(t)
b.Save(str(OUT)); print(OUT)
