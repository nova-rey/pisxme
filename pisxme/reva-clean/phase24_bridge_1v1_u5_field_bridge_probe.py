#!/usr/bin/env python3
"""Disposable offset-via bridge for U5's repeated 1V1 output pads."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_BRIDGE_1V1_CAPBANK_PLANE_CURRENT.kicad_pcb'; OUT=R/'PHASE24_BRIDGE_1V1_U5_FIELD_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); NET='/REGULATORS/BRIDGE_1V1'; n=b.FindNet(NET)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def via(x,y):
 q=pcbnew.PCB_VIA(b); q.SetNet(n); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); b.Add(q)
def tr(layer,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(layer); q.SetNet(n); q.SetWidth(pcbnew.FromMM(.20)); q.SetStart(V(*a)); q.SetEnd(V(*z)); b.Add(q)
# Left escape avoids the intervening U5.6/U5.7 pads.
via(231.25,105.25); via(231.25,107.5); via(238.75,107.5)
tr(pcbnew.F_Cu,(232.75,105.25),(231.25,105.25)); tr(pcbnew.F_Cu,(232.75,107),(231.25,107)); tr(pcbnew.F_Cu,(231.25,107),(231.25,107.5))
tr(pcbnew.B_Cu,(231.25,107.5),(238.75,107.5)); tr(pcbnew.F_Cu,(238.75,107.5),(237.25,107))
b.Save(str(OUT)); print(OUT)
