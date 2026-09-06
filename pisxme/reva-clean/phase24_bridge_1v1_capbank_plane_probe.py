#!/usr/bin/env python3
"""Disposable local In2 plane for the bridge 1V1 capacitor bank."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_ETH_GROUND_LOCAL_CURRENT.kicad_pcb'; OUT=R/'PHASE24_BRIDGE_1V1_CAPBANK_PLANE_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); NET='/REGULATORS/BRIDGE_1V1'; n=b.FindNet(NET)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def via(x,y):
 q=pcbnew.PCB_VIA(b); q.SetNet(n); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); b.Add(q)
def tr(a,z):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.F_Cu); q.SetNet(n); q.SetWidth(pcbnew.FromMM(.25)); q.SetStart(V(*a)); q.SetEnd(V(*z)); b.Add(q)
for ref in [f'C{i}' for i in list(range(26,30))+list(range(34,42))]:
 f=b.FindFootprintByReference(ref); p=next(p for p in f.Pads() if p.GetNetname()==NET)
 x,y=p.GetPosition().x/1e6,p.GetPosition().y/1e6; q=(x,y-1.8 if y<164 else y+1.8)
 via(*q); tr((x,y),q)
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In2_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL)
poly=pcbnew.VECTOR_VECTOR2I()
for x,y in ((145,155),(210,155),(210,173),(145,173)): poly.append(V(x,y))
z.AddPolygon(poly); b.Add(z); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
