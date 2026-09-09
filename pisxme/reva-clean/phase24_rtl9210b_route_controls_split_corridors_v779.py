"""V779: split PEDET down and CLKREQ_N up around the SPI field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_ABOVE_SPI_PLACEMENT_V777.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CONTROL_SPLIT_CORRIDORS_V779.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,p):
 for a,z in zip(p,p[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
# PEDET uses the lower open corridor, approaching R2 from below.
t(b,b.FindNet('PEDET'),[(101.95,70.4),(102.5,70.4),(102.5,82.0),(107.5,82.0),(107.5,60.0),(108.0,60.0)])
# CLKREQ_N uses the upper open corridor, approaching R3 from above.
t(b,b.FindNet('CLKREQ_N'),[(101.95,68.4),(103.0,68.4),(103.0,58.0),(108.0,58.0),(108.0,63.0)])
t(b,b.FindNet('RTL_3V3'),[(109.2,60.0),(109.2,63.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
