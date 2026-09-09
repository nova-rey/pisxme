"""V906: move the inherited U1.52 3V3 transition below the crystal corridors."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V885_SUPPORT_GND_RETURN_V888.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V888_RESTORE_3V3_STAGGERED_CRYSTAL_V906.kicad_pcb'
F=pcbnew.F_Cu;B=pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));p=b.FindNet('RTL_3V3')
for x in list(b.GetTracks()):
 pts=[x.GetStart(),x.GetEnd()]
 if x.GetNetname()=='RTL_3V3' and any(92.0<=q.x/1e6<=95.5 and 73.0<=q.y/1e6<=77.5 for q in pts): b.RemoveNative(x)
tr(b,p,[(94.8,73.95),(94.8,78.0),(93.0,78.0)],F);via(b,p,93.0,78.0)
n=b.FindNet('XTAL_IN');tr(b,n,[(95.2,73.95),(95.2,76.5),(100.0,76.5)],F);via(b,n,100.0,76.5)
tr(b,n,[(100.0,76.5),(100.0,55.0),(86.0,55.0)],B);via(b,n,86.0,55.0);tr(b,n,[(86.0,55.0),(88.0,59.0),(88.0,62.0)],F)
n=b.FindNet('XTAL_OUT');tr(b,n,[(95.6,73.95),(95.6,76.0),(96.0,76.0)],F);via(b,n,96.0,76.0)
tr(b,n,[(96.0,76.0),(82.0,76.0),(82.0,54.0),(90.2,54.0)],B);via(b,n,90.2,54.0);tr(b,n,[(90.2,54.0),(89.4,59.0),(91.0,62.0)],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
