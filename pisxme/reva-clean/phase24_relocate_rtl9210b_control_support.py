#!/usr/bin/env python3
"""Disposable local support-placement variant: bring R2/R3 near RTL9210B."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RESET_PERST_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for ref,pos in {'R2':(71.0,48.0),'R3':(74.0,48.0)}.items():
 f=next((x for x in b.GetFootprints() if x.GetReference()==ref),None)
 if f is None: raise SystemExit('missing '+ref)
 # These imported local footprints have a zero anchor; move by the delta from
 # the current native pad-1 coordinate, not by assigning an absolute anchor.
 p1=next(p for p in f.Pads() if p.GetNumber()=='1').GetPosition()
 f.SetPosition(pcbnew.VECTOR2I_MM(pos[0]-p1.x/1e6,pos[1]-p1.y/1e6))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
