#!/usr/bin/env python3
"""Disposable same-net dogbones for the regulator 3V3 capacitor bank."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_REGULATOR_INPUT_TOP_PAD_CURRENT.kicad_pcb'; OUT=R/'PHASE24_BRIDGE_3V3_CAPBANK_LINKS_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); NET='/REGULATORS/BRIDGE_3V3'; n=b.FindNet(NET)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(a,z):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.B_Cu); q.SetNet(n); q.SetWidth(pcbnew.FromMM(.20)); q.SetStart(V(*a)); q.SetEnd(V(*z)); b.Add(q)
# Route below the opposite POWER_GND pads on C16/C17/C19.
for x in (93.65,99.65,105.65): T((x,118),(x,120.5))
T((93.65,120.5),(99.65,120.5)); T((99.65,120.5),(105.65,120.5))
for x in (99.65,): T((x,120.5),(x,118))
b.Save(str(OUT)); print(OUT)
