"""Disposable local F.Cu AVDDL power-copper corridor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_LXO_below_vddreg.kicad_pcb';OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_AVDDL_local_zone.kicad_pcb';F=pcbnew.F_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('JMS_AVDDL')
for q in list(b.GetTracks()):
 if q.GetNetCode()==n.GetNetCode():b.RemoveNative(q)
z=pcbnew.ZONE(b);z.SetLayer(F);z.SetNet(n);z.SetNetCode(n.GetNetCode());z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL);z.SetLocalClearance(pcbnew.FromMM(.20));z.SetMinThickness(pcbnew.FromMM(.20));p=pcbnew.VECTOR_VECTOR2I()
for x,y in [(141.3,139.0),(142.4,139.0),(142.4,113.9),(136.7,113.9),(136.7,115.1),(141.3,115.1)]:p.append(P(x,y))
z.AddPolygon(p);b.Add(z);pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
