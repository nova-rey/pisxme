"""Disposable native-pad JMS583 AVDDL decoupler escape probe."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb';OUT=R/'PHASE24_JMS583_AVDDL_PROBE.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C83');n=b.FindNet('JMS_AVDDL')
if not u or not c or not n:raise RuntimeError('missing AVDDL objects')
c.SetPosition(P(148,147))
for x in list(b.GetTracks()):
    if x.GetNetCode()==n.GetNetCode():b.RemoveNative(x)
s=u.FindPadByNumber('20').GetPosition();d=c.FindPadByNumber('1').GetPosition();src=(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y));dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y))
seg(b,n,src,(src[0],143));seg(b,n,(src[0],143),(147,143));seg(b,n,(147,143),(147,dst[1]));seg(b,n,(147,dst[1]),dst)
b.Save(str(OUT));print(OUT)
