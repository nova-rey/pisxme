"""Disposable native-endpoint VCCK corridor variants."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_AVDD33.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def tr(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def vi(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def pad(b,r,p): return mm(b.FindFootprintByReference(r).FindPadByNumber(str(p)).GetPosition())
variants={'east':[(145,132.4),(145,112)],'west':[(128,132.4),(128,112)],'farwest':[(122,132.4),(122,112)]}
for name,(a,z) in variants.items():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('JMS_VCCK');
 for x in list(b.GetTracks()):
  if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
 s=pad(b,'U11',2); d=pad(b,'C82',1)
 tr(b,n,F,s,(a[0],s[1])); tr(b,n,F,(a[0],s[1]),a); vi(b,n,a)
 tr(b,n,B,a,z); vi(b,n,z); tr(b,n,F,z,(d[0],z[1])); tr(b,n,F,(d[0],z[1]),d)
 out=R/f'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK_{name}.kicad_pcb'; b.BuildListOfNets(); b.Save(str(out)); print(out)
