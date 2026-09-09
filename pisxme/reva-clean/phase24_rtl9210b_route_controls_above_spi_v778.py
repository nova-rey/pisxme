"""V778: F.Cu monotonic PEDET/CLKREQ_N routes above the SPI field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_ABOVE_SPI_PLACEMENT_V777.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CONTROL_ROUTED_ABOVE_SPI_V778.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,p):
 for a,z in zip(p,p[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
t(b,b.FindNet('PEDET'),[(101.95,70.4),(102.5,70.4),(102.5,60.0),(108.0,60.0)])
t(b,b.FindNet('CLKREQ_N'),[(101.95,68.4),(106.0,68.4),(106.0,63.0),(108.0,63.0)])
t(b,b.FindNet('RTL_3V3'),[(109.2,60.0),(109.2,63.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
