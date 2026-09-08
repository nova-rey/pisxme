"""Disposable AVDDL route with ordinary through-vias on east corridor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK_F_center.kicad_pcb';OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_AVDDL_viaeast.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p):return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def vi(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('JMS_AVDDL');u=b.FindFootprintByReference('U11');c=b.FindFootprintByReference('C83')
for q in list(b.GetTracks()):
 if q.GetNetCode()==n.GetNetCode():b.RemoveNative(q)
s=mm(u.FindPadByNumber('20').GetPosition());d=mm(c.FindPadByNumber('1').GetPosition());a=(149,138);z=(149,110)
tr(b,n,F,s,a);vi(b,n,a);tr(b,n,B,a,z);vi(b,n,z);tr(b,n,F,z,(d[0],110));tr(b,n,F,(d[0],110),d)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
