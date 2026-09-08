"""Disposable U1.52-to-C3 RTL_3V3 branch join."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_3V3_SOURCE_JOIN_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_3V3_C3_JOIN_PROBE.kicad_pcb'
F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
s(b,n,F,(101.95,73.2),(103.0,73.2));v(b,n,(103.0,73.2));s(b,n,B,(103.0,73.2),(103.0,68.5));s(b,n,B,(103.0,68.5),(110.4,68.5));v(b,n,(110.4,68.5));s(b,n,F,(110.4,68.5),(110.4,69.0))
s(b,n,B,(103.0,68.5),(92.0,68.5));s(b,n,B,(92.0,68.5),(92.0,67.6))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
