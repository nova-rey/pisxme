"""V932: move RSET support outboard of the reserved RTL_1V1 fanout."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_V927_RTL1V1_CLEANFIELD_V930.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V930_RSET_RELOCATE_V932.kicad_pcb';F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));r=b.FindFootprintByReference('R1');r.SetPosition(r.GetPosition()+P(0,13));n=b.FindNet('RSET')
tr(b,n,[(94.05,73.2),(94.05,74.5),(90.0,74.5),(90.0,76.5),(88.0,76.5),(88.0,78.0)])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
