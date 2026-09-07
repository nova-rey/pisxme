#!/usr/bin/env python3
"""Path-B V21: local F.Cu RTL_3V3 power zone around U1/QFN support."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_1V1_QFN_COLLECTOR_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_QFN_ZONE_V1.kicad_pcb'
def main():
    b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
    if n is None: raise SystemExit('missing RTL_3V3')
    z=pcbnew.ZONE(b); z.SetLayer(pcbnew.F_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode())
    z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL); p=pcbnew.VECTOR_VECTOR2I()
    for x,y in ((74.0,56.0),(94.5,56.0),(94.5,66.5),(74.0,66.5)): p.append(pcbnew.VECTOR2I_MM(x,y))
    z.AddPolygon(p); b.Add(z); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
