"""Disposable local F.Cu VCCO copper zone; power copper only, not a signal plane."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK_F_center.kicad_pcb';OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCO_local_zone.kicad_pcb';F=pcbnew.F_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('JMS_VCCO')
for q in list(b.GetTracks()):
 if q.GetNetCode()==n.GetNetCode():b.RemoveNative(q)
z=pcbnew.ZONE(b);z.SetLayer(F);z.SetNet(n);z.SetNetCode(n.GetNetCode());z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL);z.SetLocalClearance(pcbnew.FromMM(.20));z.SetMinThickness(pcbnew.FromMM(.20));p=pcbnew.VECTOR_VECTOR2I()
for x,y in [(135.9,133.8),(136.6,133.8),(136.6,134.2),(130.4,134.2),(130.4,114.1),(130.0,114.1),(130.0,114.9),(129.6,114.9),(129.6,134.2),(135.9,134.2)]:p.append(P(x,y))
z.AddPolygon(p);b.Add(z)
for a,q in [((136.35,134.0),(135.9,134.0)),((130.0,114.5),(130.0,114.9))]:
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*q));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
