"""Disposable ordinary-via GND return escapes for the RTL9210B QFN."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U136_DELAYED_BEND_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_GND_RETURN_PROBE.kicad_pcb'
F,W=pcbnew.F_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,pcbnew.B_Cu);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('GND')
# Depart from pad edges; each via is outside the QFN pad geometry.
s(b,n,(100.4,70.0),(101.0,70.0));v(b,n,(101.0,70.0))
s(b,n,(101.95,67.6),(103.0,67.6));v(b,n,(103.0,67.6))
s(b,n,(98.8,74.4),(98.8,75.0));s(b,n,(98.8,75.0),(99.5,76.0));v(b,n,(99.5,76.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
