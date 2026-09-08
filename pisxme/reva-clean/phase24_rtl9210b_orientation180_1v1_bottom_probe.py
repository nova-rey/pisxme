"""Disposable bottom-edge RTL_1V1 sub-field on V631."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_RAILS_PROBE_V7.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_BOTTOM_PROBE.kicad_pcb'
F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
for x in ((95.2,73.95),(96.8,73.95),(100.8,73.95)):
 s(b,n,F,x,(x[0],78.5));v(b,n,(x[0],78.5));s(b,n,B,(x[0],78.5),(x[0],85.0))
s(b,n,B,(95.2,85.0),(104.0,85.0));v(b,n,(104.0,85.0));s(b,n,F,(104.0,85.0),(104.0,82.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
