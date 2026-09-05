"""Disposable test of the already-defined In3 protected-12V plane."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb';OUT=R/'PHASE24_PROTECTED12V_PLANE.kicad_pcb'
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('12V_PROTECTED')
if n is None:raise RuntimeError('missing 12V_PROTECTED')
z=pcbnew.ZONE(b);z.SetLayer(pcbnew.In3_Cu);z.SetNet(n);z.SetNetCode(n.GetNetCode());z.SetIsRuleArea(False);z.SetMinThickness(pcbnew.FromMM(.25));z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL);z.SetZoneName('REV_A_PROTECTED_12V_PLANE')
pts=pcbnew.VECTOR_VECTOR2I()
for p in ((1,1),(299,1),(299,179),(1,179)):pts.append(V(*p))
z.AddPolygon(pts);b.Add(z);pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
