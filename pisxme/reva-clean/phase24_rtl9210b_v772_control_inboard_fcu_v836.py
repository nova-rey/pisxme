"""V836: in-outline control corridors on F.Cu around the SPI field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V772_CONTROL_ISLAND_INBOARD_V834.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V772_CONTROL_INBOARD_FCU_V836.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
T(b,b.FindNet('PEDET'),[(101.95,70.4),(108,70.4),(108,75),(119.2,75)])
T(b,b.FindNet('CLKREQ_N'),[(101.95,68.4),(110,68.4),(110,80),(119.2,80)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
