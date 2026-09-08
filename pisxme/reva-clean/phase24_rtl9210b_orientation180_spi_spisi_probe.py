"""Disposable SPISI source-to-flash-controller channel."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_3V3_C3_JOIN_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_SPISI_PROBE.kicad_pcb'
F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPISI')
s(b,n,F,(94.05,66.8),(90.0,66.8));v(b,n,(90.0,66.8));s(b,n,B,(90.0,66.8),(76.6,66.8));v(b,n,(76.6,66.8));s(b,n,F,(76.6,66.8),(76.6,80.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
