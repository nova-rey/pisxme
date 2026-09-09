"""V1135: XTAL_OUT GND-diagonal overpass with a local layer return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb';OUT=H/'PHASE24_RTL9210B_XTALOUT_GND_OVERPASS_V1135.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));ni,no=b.FindNet('XTAL_IN'),b.FindNet('XTAL_OUT')
# Retained clean XTAL_IN route from V1119.
t(b,ni,F,[(94.05,67.2),(93.5,67.2),(93.0,67.5),(91.5,68.6)]);v(b,ni,(91.5,68.6));t(b,ni,B,[(91.5,68.6),(91.5,75),(85.5,75),(85.5,62)]);v(b,ni,(85.5,62));t(b,ni,F,[(85.5,62),(88,62),(88,59)])
# XTAL_OUT crosses the retained GND B.Cu diagonal on F.Cu at the local overpass.
t(b,no,F,[(94.05,67.6),(90.5,68.8)]);v(b,no,(90.5,68.8));t(b,no,B,[(90.5,68.8),(90.5,66.2)]);v(b,no,(90.5,66.2));t(b,no,F,[(90.5,66.2),(90.5,57.5),(89.4,57.5),(89.4,59)])
t(b,no,F,[(90.5,57.5),(90.5,61),(91,62)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
