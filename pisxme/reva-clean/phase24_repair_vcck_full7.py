"""Add a central upper native-pad JMS_VCCK corridor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_AVDD33.kicad_pcb'
OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def vi(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def at(b,r,p):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('JMS_VCCK')
for x in list(b.GetTracks()):
 if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
s=at(b,'U11',2);d=at(b,'C82',1);v1=(135.0,130.5);v2=(135.0,112.0)
tr(b,n,F,s,(135.0,s[1]));tr(b,n,F,(135.0,s[1]),v1);vi(b,n,v1)
tr(b,n,B,v1,v2);vi(b,n,v2);tr(b,n,F,v2,(d[0],112.0));tr(b,n,F,(d[0],112.0),d)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
