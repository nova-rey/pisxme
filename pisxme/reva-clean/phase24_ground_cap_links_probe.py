#!/usr/bin/env python3
"""Disposable same-net capacitor-field probe, split from Ethernet support."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_PGND_CLUSTER_CURRENT.kicad_pcb'; OUT=R/'PHASE24_GROUND_CAP_LINKS_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('POWER_GND')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(layer,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(layer); q.SetNet(n); q.SetWidth(pcbnew.FromMM(.20)); q.SetStart(V(*a)); q.SetEnd(V(*z)); b.Add(q)
# Dogbone around the opposite pad of each capacitor; no pad-field crossing.
for layer, links in [(pcbnew.F_Cu,[((71.1,120),(71.1,117.5)),((71.1,117.5),(79.1,117.5)),((79.1,117.5),(79.1,120))]),
                     (pcbnew.B_Cu,[((96.35,118),(96.35,115.5)),((96.35,115.5),(102.35,115.5)),((102.35,115.5),(102.35,118)),
                                   ((102.35,118),(102.35,115.5)),((102.35,115.5),(108.35,115.5)),((108.35,115.5),(108.35,118))])]:
 for a,z in links:T(layer,a,z)
b.Save(str(OUT)); print(OUT)
