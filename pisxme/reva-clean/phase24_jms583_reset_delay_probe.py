"""Disposable native-pad JMS583 reset pull-up/delay support probe."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_JMS583_RESET_SOUTH_PROBE.kicad_pcb';OUT=R/'PHASE24_JMS583_RESET_DELAY_PROBE.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def xy(p):return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
b=pcbnew.LoadBoard(str(BASE));r=b.FindFootprintByReference('R81');c=b.FindFootprintByReference('C85');n=b.FindNet('JMS_RESET_N')
if not r or not c or not n:raise RuntimeError('missing reset delay objects')
c.SetPosition(P(130,145))
for x in list(b.GetTracks()):
    if x.GetNetCode()==n.GetNetCode():b.RemoveNative(x)
a=xy(r.FindPadByNumber('1').GetPosition());z=xy(c.FindPadByNumber('1').GetPosition())
seg(b,n,a,(123,145));seg(b,n,(123,145),(128.5,147));seg(b,n,(128.5,147),(128.5,145));seg(b,n,(128.5,145),z)
u=b.FindFootprintByReference('U11');s=xy(u.FindPadByNumber('15').GetPosition())
seg(b,n,s,(133,s[1]));seg(b,n,(133,s[1]),(133,143));seg(b,n,(133,143),(122,143));seg(b,n,(122,143),(122,145));seg(b,n,(122,145),a)
b.Save(str(OUT));print(OUT)
