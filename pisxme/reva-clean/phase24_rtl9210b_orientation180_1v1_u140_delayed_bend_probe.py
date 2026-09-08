"""Disposable U1.40 delayed-bend escape beside retained U1.39 exit."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U155_U163_PROBE_V2.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U140_DELAYED_BEND_PROBE.kicad_pcb'
F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
s(b,n,F,(96.8,73.95),(96.8,74.7));s(b,n,F,(96.8,74.7),(98.2,75.4));v(b,n,(98.2,75.4));s(b,n,B,(98.2,75.4),(98.2,77.5));s(b,n,B,(98.2,77.5),(107,77.5));v(b,n,(107,77.5));s(b,n,F,(107,77.5),(107,70))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
