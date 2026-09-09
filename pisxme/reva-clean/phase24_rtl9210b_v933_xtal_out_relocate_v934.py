"""V934: add separated relocated XTAL_OUT from U1 to C2/Y1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_V932_XTAL_IN_RELOCATE_V933.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V933_XTAL_OUT_RELOCATE_V934.kicad_pcb';F=pcbnew.F_Cu;B=pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
n=b.FindNet('XTAL_OUT');tr(b,n,[(95.6,73.95),(95.0,80.0)],F);via(b,n,(95.0,80.0));tr(b,n,[(95.0,80.0),(95.0,54.0),(92.0,54.0)],B);via(b,n,(92.0,54.0));tr(b,n,[(92.0,54.0),(91.0,54.0),(89.4,51.0)],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
