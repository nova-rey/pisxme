"""Disposable delayed-bend U1.36 RTL_1V1 escape from the V640 field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U140_DELAYED_BEND_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U136_DELAYED_BEND_PROBE.kicad_pcb'
F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
s(b,n,F,(95.2,73.95),(95.2,74.7));s(b,n,F,(95.2,74.7),(92.5,74.7));s(b,n,F,(92.5,74.7),(92.5,74.3));v(b,n,(92.5,74.3));s(b,n,B,(92.5,74.3),(107,74.3));v(b,n,(107,74.3));s(b,n,F,(107,74.3),(107,70))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
