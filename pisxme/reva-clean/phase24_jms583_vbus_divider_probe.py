"""Disposable native-pad VBUS/sense-divider placement and routing probe."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb'
OUT=R/'PHASE24_JMS583_VBUS_DIVIDER_PROBE.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu)
    t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def endpoints(a,z): return (pcbnew.ToMM(a.x),pcbnew.ToMM(a.y)),(pcbnew.ToMM(z.x),pcbnew.ToMM(z.y))
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');r82=b.FindFootprintByReference('R82');r83=b.FindFootprintByReference('R83')
if not u or not r82 or not r83: raise RuntimeError('missing VBUS divider objects')
r82.SetPosition(P(125,148));r83.SetPosition(P(130,148))
for name in ('VBUS','JMS_VBUS_SENSE'):
    n=b.FindNet(name)
    for x in list(b.GetTracks()):
        if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
v=b.FindNet('VBUS');s=b.FindNet('JMS_VBUS_SENSE')
src,dst=endpoints(u.FindPadByNumber('16').GetPosition(),r82.FindPadByNumber('1').GetPosition())
seg(b,v,src,(133,src[1]));seg(b,v,(133,src[1]),(133,145));seg(b,v,(133,145),(123.5,145));seg(b,v,(123.5,145),(123.5,dst[1]));seg(b,v,(123.5,dst[1]),dst)
src,dst=endpoints(r82.FindPadByNumber('2').GetPosition(),r83.FindPadByNumber('1').GetPosition());seg(b,s,src,dst)
b.Save(str(OUT));print(OUT)
