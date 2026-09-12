"""Separate AVDD33 from the VCCO decoupler launch in the REXT base."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_STORAGE_MKEY_USB3_REXT_LOCAL_20260912.kicad_pcb';OUT=R/'PHASE24_STORAGE_MKEY_USB3_REXT_AVDD33_LOCAL_V2_20260912.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.15));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C80');n=b.FindNet('JMS_AVDD33')
if not u or not c or not n:raise RuntimeError('missing AVDD33 endpoint')
c.SetPosition(P(155,146))
for item in list(b.GetTracks()):
 if item.GetNetCode()==n.GetNetCode():b.RemoveNative(item)
s=u.FindPadByNumber('19').GetPosition();d=c.FindPadByNumber('1').GetPosition();src=(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y));dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y));pts=[src,(142.2,139.5),(154.5,139.5),dst]
for a,z in zip(pts,pts[1:]):tr(b,n,a,z)
b.Save(str(OUT));print(OUT)
