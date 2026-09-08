"""V499: add U1.16 RTL_1V1 to C4.1 on the V498 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;src=H/'PHASE24_RTL9210B_SOURCE_FIELD_V498.kicad_pcb';out=H/'PHASE24_RTL9210B_RTL1V1_U116_V499.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RTL_1V1');u=b.FindFootprintByReference('U1');p=u.FindPadByNumber('16');q=p.GetPosition();a=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y));c=b.FindFootprintByReference('C4').FindPadByNumber('1');q=c.GetPosition();z=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))
s(b,n,a,(108.0,a[1]));s(b,n,(108.0,a[1]),(108.0,57.0));s(b,n,(108.0,57.0),(113.0,57.0));s(b,n,(113.0,57.0),(113.0,55.0));s(b,n,(113.0,55.0),z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
