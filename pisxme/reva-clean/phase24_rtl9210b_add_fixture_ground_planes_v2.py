#!/usr/bin/env python3
"""Add outer-layer GND planes with ordinary stitching vias."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SPI_V7.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SPI_V7_GND_PLANES_V2.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND')
if n is None: raise SystemExit('FAIL missing GND')
for layer in (pcbnew.F_Cu, pcbnew.B_Cu):
    z=pcbnew.ZONE(b); z.SetLayer(layer); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL)
    p=pcbnew.VECTOR_VECTOR2I()
    for x,y in ((62,40),(120,40),(120,82),(62,82)): p.append(pcbnew.VECTOR2I_MM(x,y))
    z.AddPolygon(p); b.Add(z)
for x,y in ((64,42),(118,42),(118,80),(64,80),(75,54),(105,54)):
    v=pcbnew.PCB_VIA(b); v.SetPosition(pcbnew.VECTOR2I_MM(x,y)); v.SetWidth(pcbnew.FromMM(0.6)); v.SetDrill(pcbnew.FromMM(0.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
