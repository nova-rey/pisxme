#!/usr/bin/env python3
"""Apply the previously validated global POWER_GND launch cluster."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_J1_PROTECTED_FIELD_CURRENT.kicad_pcb'
OUT=R/'PHASE24_PGND_CLUSTER_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('POWER_GND')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def launch(a,z):
 t=pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.20)); t.SetStart(V(*a)); t.SetEnd(V(*z)); b.Add(t)
 v=pcbnew.PCB_VIA(b); v.SetNet(n); v.SetPosition(V(*z)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); b.Add(v)
launch((21.45,73.55),(22.50,73.55)); launch((21.45,93.55),(22.50,93.55))
for y in (98.25,101.75):
 launch((43.00,y),(40.50,103.00) if y==101.75 else (41.50,y)); launch((47.00,y),(48.50,y))
launch((57.575,100.00),(56.50,100.00))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
