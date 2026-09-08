"""Disposable all-F.Cu VCCK corridors, native endpoints only."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_AVDD33.kicad_pcb'; F=pcbnew.F_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def at(b,r,p): return mm(b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition())
for name,x in {'west':128.0,'east':145.0,'center':133.0}.items():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('JMS_VCCK')
 for q in list(b.GetTracks()):
  if q.GetNetCode()==n.GetNetCode():b.RemoveNative(q)
 s=at(b,'U11',2);d=at(b,'C82',1); pts=[s,(x,s[1]),(x,110.0),(d[0],110.0),d]
 for a,z in zip(pts,pts[1:]):tr(b,n,a,z)
 out=R/f'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK_F_{name}.kicad_pcb';b.BuildListOfNets();b.Save(str(out));print(out)
