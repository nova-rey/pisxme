#!/usr/bin/env python3
"""Disposable lower-left R2/R3 support placement from the V6 saved board."""
from pathlib import Path
import pcbnew

HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOWER.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for ref,pos in {'R2':(69.0,78.0),'R3':(72.0,78.0)}.items():
    f=next(x for x in b.GetFootprints() if x.GetReference()==ref)
    p1=next(p for p in f.Pads() if p.GetNumber()=='1').GetPosition()
    f.SetPosition(pcbnew.VECTOR2I_MM(pos[0]-p1.x/1e6,pos[1]-p1.y/1e6))
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
