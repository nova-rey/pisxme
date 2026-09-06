#!/usr/bin/env python3
"""Disposable transplant of the passing complete clock fixture V2."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_STORAGE_PROVEN_USB3_SATA_RXN_STITCH_CAPS_BOTTOM_POWER_ORACLE.kicad_pcb'
ORACLE=R/'PHASE24_CLOCK_COMPLETE_ASTAR_V2.kicad_pcb'
OUT=R/'PHASE24_CLOCK_COMPLETE_V2_ON_CURRENT.kicad_pcb'
CLOCK={'/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'}
b=pcbnew.LoadBoard(str(BASE)); o=pcbnew.LoadBoard(str(ORACLE))
for ref in ('Y1','R23','C42','C43'):
 s=o.FindFootprintByReference(ref); d=b.FindFootprintByReference(ref)
 d.SetPosition(s.GetPosition()); d.SetOrientation(s.GetOrientation())
for i in o.GetTracks():
 name=str(i.GetNetname())
 if name not in CLOCK: continue
 n=b.FindNet(name)
 if isinstance(i,pcbnew.PCB_VIA):
  x=pcbnew.PCB_VIA(b); x.SetPosition(i.GetPosition()); x.SetWidth(i.GetWidth(pcbnew.F_Cu)); x.SetDrill(i.GetDrill()); x.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu)
 else:
  x=pcbnew.PCB_TRACK(b); x.SetStart(i.GetStart()); x.SetEnd(i.GetEnd()); x.SetLayer(i.GetLayer()); x.SetWidth(i.GetWidth())
 x.SetNet(n); b.Add(x)
b.Save(str(OUT)); print(OUT)
