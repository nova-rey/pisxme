"""Disposable native-pad JMS583 LXO-to-L10 escape probe."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb';OUT=R/'PHASE24_JMS583_LXO_PROBE.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');l=b.FindFootprintByReference('L10');n=b.FindNet('LXO')
if not u or not l or not n:raise RuntimeError('missing LXO objects')
l.SetPosition(P(136,125));l.SetOrientationDegrees(180)
y=b.FindFootprintByReference('Y10')
if not y: raise RuntimeError('missing Y10')
y.SetPosition(P(150,115))
for x in list(b.GetTracks()):
    if x.GetNetCode()==n.GetNetCode():b.RemoveNative(x)
s=u.FindPadByNumber('64').GetPosition();d=l.FindPadByNumber('1').GetPosition();src=(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y));dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y))
seg(b,n,src,(146,src[1]));seg(b,n,(146,src[1]),(146,125));seg(b,n,(146,125),dst)
b.Save(str(OUT));print(OUT)
