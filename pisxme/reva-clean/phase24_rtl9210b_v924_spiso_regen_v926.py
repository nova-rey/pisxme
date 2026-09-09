"""V926: move SPISO's U2-side B.Cu segment below SPICS."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V923_SPISO3_REGEN_V924.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V924_SPISO_REGEN_V926.kicad_pcb'
F=pcbnew.F_Cu;B=pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPISO')
tr(b,n,[(99.2,66.05),(99.2,64.5),(99.0,60.5)],F);via(b,n,99.0,60.5);tr(b,n,[(99.0,60.5),(99.0,84.0),(104.5,84.0),(104.5,78.8)],B);via(b,n,104.5,78.8);tr(b,n,[(104.5,78.8),(105.0,78.8)],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
