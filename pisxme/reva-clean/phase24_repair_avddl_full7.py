"""Add a native-pad-aware AVDDL decoupler route to the promoted basis."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK_F_center.kicad_pcb';OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_AVDDL.kicad_pcb';F=pcbnew.F_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p):return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('JMS_AVDDL');u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C83')
for q in list(b.GetTracks()):
 if q.GetNetCode()==n.GetNetCode():b.RemoveNative(q)
s=mm(u.FindPadByNumber('20').GetPosition());d=mm(c.FindPadByNumber('1').GetPosition());pts=[s,(145,s[1]),(145,110),(d[0],110),d]
for a,z in zip(pts,pts[1:]):tr(b,n,a,z)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
