"""Add an upper native-pad JMS_AVDD33 corridor to the current basis."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_RESET.kicad_pcb'
OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_AVDD33.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def vi(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def at(b,r,p):
 f=b.FindFootprintByReference(r);q=f.FindPadByNumber(str(p)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('JMS_AVDD33')
for x in list(b.GetTracks()):
 if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
s=at(b,'U11',19);d=at(b,'C80',1);v1=(144.0,139.5);v2=(126.5,108.5)
tr(b,n,F,s,(144.0,s[1]));tr(b,n,F,(144.0,s[1]),v1);vi(b,n,v1)
tr(b,n,B,v1,(144.0,108.5));tr(b,n,B,(144.0,108.5),v2);vi(b,n,v2);tr(b,n,F,v2,d)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
