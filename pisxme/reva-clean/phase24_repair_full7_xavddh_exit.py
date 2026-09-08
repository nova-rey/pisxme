"""Try a left/up XAVDDH departure around the FULL7 USB3 TX_N spine."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_THREE_EXITS.kicad_pcb'
OUT=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_XAVDDH_LEFT_EXIT.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def add(b,n,l,a,z,w=.20):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('JMS_XAVDDH')
for item in list(b.GetTracks()):
 if item.GetNetCode()==n.GetNetCode(): b.RemoveNative(item)
s=xy(b.FindFootprintByReference('U11').FindPadByNumber('52').GetPosition())
d=xy(b.FindFootprintByReference('C84').FindPadByNumber('1').GetPosition())
v1=(138.2,130.0); v2=(148.0,120.0)
add(b,n,F,s,(138.2,130.5)); add(b,n,F,(138.2,130.5),v1); via(b,n,v1)
for a,z in [(v1,(139.5,118.0)),((139.5,118.0),(148.0,118.0)),((148.0,118.0),v2)]: add(b,n,B,a,z)
via(b,n,v2); add(b,n,F,v2,d)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
