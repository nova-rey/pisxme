#!/usr/bin/env python3
"""Disposable local In3 planes for the two power-entry PTH networks."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CLOCK_COMPLETE_V2_ON_CURRENT.kicad_pcb'
OUT=R/'PHASE24_POWER_INPUT_PLANES_PROBE.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def zone(name,pts):
 n=b.FindNet(name); z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In3_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL)
 p=pcbnew.VECTOR_VECTOR2I()
 for x,y in pts:p.append(V(x,y))
 z.AddPolygon(p); b.Add(z)
zone('/POWER_INPUT/12V_IN_B',[(5,35),(25,35),(25,100),(42,113),(50,113),(50,125),(5,125)])
zone('/POWER_INPUT/FUSED_12V_B',[(5,100),(42,100),(50,113),(50,116),(60,116),(60,136),(5,136)])
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
