"""Disposable native-pad JMS583 XAVDDH decoupler escape probe."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb';OUT=R/'PHASE24_JMS583_XAVDDH_PROBE.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
    v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C84');n=b.FindNet('JMS_XAVDDH')
if not u or not c or not n:raise RuntimeError('missing XAVDDH objects')
c.SetPosition(P(150,120))
for x in list(b.GetTracks()):
    if x.GetNetCode()==n.GetNetCode():b.RemoveNative(x)
s=u.FindPadByNumber('52').GetPosition();d=c.FindPadByNumber('1').GetPosition();src=(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y));dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y))
v1=(140.0,src[1]);v2=(149.0,121.5)
seg(b,n,src,v1);via(b,n,v1)
for a,z in [(v1,(140.0,140)),((140.0,140),v2)]:
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.B_Cu);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
via(b,n,v2);seg(b,n,v2,dst)
b.Save(str(OUT));print(OUT)
