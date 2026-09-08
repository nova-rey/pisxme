"""Disposable local F.Cu VDDREG power-copper zone."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCO_rectangle_zone.kicad_pcb';OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VDDREG_local_zone.kicad_pcb';F=pcbnew.F_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('JMS_VDDREG_5V')
for q in list(b.GetTracks()):
 if q.GetNetCode()==n.GetNetCode():b.RemoveNative(q)
z=pcbnew.ZONE(b);z.SetLayer(F);z.SetNet(n);z.SetNetCode(n.GetNetCode());z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL);z.SetLocalClearance(pcbnew.FromMM(.20));z.SetMinThickness(pcbnew.FromMM(.20));p=pcbnew.VECTOR_VECTOR2I()
for x,y in [(135.9,124.6),(137.5,124.6),(137.5,132.3),(135.9,132.3)]:p.append(P(x,y))
z.AddPolygon(p);b.Add(z)
u=b.FindFootprintByReference('U11');l=b.FindFootprintByReference('L10')
for a,q in [((136.35,132.0),(136.05,132.0)),((137.15,125.0),(137.35,125.0))]:
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*q));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
