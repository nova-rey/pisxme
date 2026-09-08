"""Disposable LXO dogleg below the promoted VDDREG power zone."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VDDREG_local_zone.kicad_pcb';OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_LXO_below_vddreg.kicad_pcb';F=pcbnew.F_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p):return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('LXO');u=b.FindFootprintByReference('U11');l=b.FindFootprintByReference('L10')
for q in list(b.GetTracks()):
 if q.GetNetCode()==n.GetNetCode():b.RemoveNative(q)
s=mm(u.FindPadByNumber('64').GetPosition());d=mm(l.FindPadByNumber('1').GetPosition());pts=[s,(144.5,s[1]),(144.5,123),(d[0],123),d]
for a,z in zip(pts,pts[1:]):tr(b,n,a,z)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
