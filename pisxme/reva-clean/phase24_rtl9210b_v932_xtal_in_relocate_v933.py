"""V933: relocate crystal input support north and regenerate XTAL_IN only."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_V930_RSET_RELOCATE_V932.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V932_XTAL_IN_RELOCATE_V933.kicad_pcb';F=pcbnew.F_Cu;B=pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for ref in ('Y1','C1','C2'):
 f=b.FindFootprintByReference(ref);f.SetPosition(f.GetPosition()+P(0,-8))
n=b.FindNet('XTAL_IN');tr(b,n,[(95.2,73.95),(95.2,77.5),(97.0,77.5)],F);via(b,n,(97.0,77.5));tr(b,n,[(97.0,77.5),(97.0,51.0),(87.0,51.0)],B);via(b,n,(87.0,51.0));tr(b,n,[(87.0,51.0),(88.0,51.0),(88.0,54.0)],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
