"""V511: lower V510's U1.40 handoff to clear U1 GND pad 45."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; src=H/'PHASE24_RTL9210B_RTL1V1_U116_V506.kicad_pcb'; out=H/'PHASE24_RTL9210B_RTL1V1_U140_V511.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('RTL_1V1'); u=b.FindFootprintByReference('U1'); a=mm(u.FindPadByNumber('40').GetPosition()); j=(99.5,61.2); pts=[a,(103.0,a[1]),(103.0,64.0),(99.5,64.0),j]
for x,y in zip(pts,pts[1:]): tr(b,n,x,y)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
