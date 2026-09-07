#!/usr/bin/env python3
"""Correct native-frame lower-left R2/R3 placement from the V6 board."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOWER_V2.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
for ref,target in {'R2':(69.0,78.0),'R3':(72.0,78.0)}.items():
    f=next(x for x in b.GetFootprints() if x.GetReference()==ref)
    p=next(p for p in f.Pads() if p.GetNumber()=='1').GetPosition()
    fp=f.GetPosition()
    local=(p.x-fp.x,p.y-fp.y)
    f.SetPosition(pcbnew.VECTOR2I_MM(target[0]-local[0]/1e6,target[1]-local[1]/1e6))
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT)); print(OUT)
