"""V492: add the second native RTL_5V source pad to the V491 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;src=H/'PHASE24_RTL9210B_RTL5V_U117_V491.kicad_pcb';out=H/'PHASE24_RTL9210B_RTL5V_U133_V492.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RTL_5V');u=b.FindFootprintByReference('U1');p=u.FindPadByNumber('33');q=p.GetPosition();a=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y));c=b.FindFootprintByReference('C5').FindPadByNumber('1');q=c.GetPosition();z=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))
s(b,n,F,a,(a[0],56.5));s(b,n,F,(a[0],56.5),(99.5,56.5));v(b,n,(99.5,56.5));s(b,n,B,(99.5,56.5),(99.5,40.5));s(b,n,B,(99.5,40.5),(z[0],40.5));v(b,n,(z[0],40.5));s(b,n,F,(z[0],40.5),z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
