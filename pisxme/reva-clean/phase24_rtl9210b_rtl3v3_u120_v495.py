"""V495: add U1.20 RTL_3V3 to the retained C3 rail."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;src=H/'PHASE24_RTL9210B_RTL5V_U133_JOIN_V494.kicad_pcb';out=H/'PHASE24_RTL9210B_RTL3V3_U120_V495.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def sb(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(B);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(src));n=b.FindNet('RTL_3V3');u=b.FindFootprintByReference('U1');p=u.FindPadByNumber('20');q=p.GetPosition();a=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y));c=b.FindFootprintByReference('C3').FindPadByNumber('1');q=c.GetPosition();z=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))
s(b,n,a,(a[0],57.2));s(b,n,(a[0],57.2),(109.5,57.2));v(b,n,(109.5,57.2));sb(b,n,(109.5,57.2),(109.5,54.0));sb(b,n,(109.5,54.0),(110.2,54.0));v(b,n,(110.2,54.0));s(b,n,(110.2,54.0),z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
