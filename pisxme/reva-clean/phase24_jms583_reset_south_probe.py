"""Disposable reset-support relocation and native-pad route probe."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb'
OUT=R/'PHASE24_JMS583_RESET_SOUTH_PROBE.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z,l=pcbnew.F_Cu):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l)
    t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)

b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');r=b.FindFootprintByReference('R81');n=b.FindNet('JMS_RESET_N')
if not u or not r or not n: raise RuntimeError('missing reset objects')
r.SetPosition(P(125,145))
for x in list(b.GetTracks()):
    if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
s=u.FindPadByNumber('15').GetPosition();d=r.FindPadByNumber('1').GetPosition()
src=(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y));dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y))
seg(b,n,src,(133,src[1]));seg(b,n,(133,src[1]),(133,140));seg(b,n,(133,140),(122,140));seg(b,n,(122,140),(122,145));seg(b,n,(122,145),dst)
b.Save(str(OUT));print(OUT)
