"""Disposable source-owned STORAGE_SEL reroute around U13/U14 pad fields."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb'));F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(r,n):
 p=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition();return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
n=b.FindNet('STORAGE_SEL')
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
# U12 is escaped to the left of its exposed-pad field; U13 is approached
# from its left edge. The U14 branch uses a separate B.Cu corridor.
q12=(151.8,135.0);q13=(176.5,135.0);q14=(212.5,153.0)
via(n,q12);tr(n,xy('U12',9),q12,F)
via(n,q13);tr(n,q12,q13,B);tr(n,q13,xy('U13',9),F)
via(n,q14);tr(n,xy('U14',4),q14,F);tr(n,q14,(212.5,146.0),B);tr(n,(212.5,146.0),q13,B)
b.BuildListOfNets();out=R/'PHASE24_STORAGE_J8_V5_STORAGE_SEL_V1.kicad_pcb';b.Save(str(out));print(out)
