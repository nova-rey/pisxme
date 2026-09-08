"""V493: alternate local F.Cu U1.33 RTL_5V branch on V491."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;src=H/'PHASE24_RTL9210B_RTL5V_U117_V491.kicad_pcb';out=H/'PHASE24_RTL9210B_RTL5V_U133_V493.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RTL_5V');u=b.FindFootprintByReference('U1');p=u.FindPadByNumber('33');q=p.GetPosition();a=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y));c=b.FindFootprintByReference('C5').FindPadByNumber('1');q=c.GetPosition();z=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))
s(b,n,a,(a[0],56.5));s(b,n,(a[0],56.5),(z[0],56.5));s(b,n,(z[0],56.5),z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
