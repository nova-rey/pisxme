"""V503: lower-edge F.Cu dogleg for the relocated C4 branch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_SOURCE_FIELD_V498.kicad_pcb'; out=H/'PHASE24_RTL9210B_RTL1V1_U116_V503.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_1V1'); u=b.FindFootprintByReference('U1'); c=b.FindFootprintByReference('C4'); c.SetPosition(P(114,59))
a=mm(u.FindPadByNumber('16').GetPosition()); z=mm(c.FindPadByNumber('1').GetPosition()); pts=[a,(108.0,a[1]),(108.0,64.5),(113.2,64.5),z]
for x,y in zip(pts,pts[1:]): tr(b,n,x,y)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
