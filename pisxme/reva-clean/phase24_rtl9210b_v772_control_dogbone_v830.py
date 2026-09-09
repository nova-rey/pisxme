"""V830: angle local control dogbones away from adjacent U1 pads."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V772_CONTROL_LOCAL_V829.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V772_CONTROL_DOGBONE_V830.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname() in ('PEDET','CLKREQ_N'): b.RemoveNative(item)
T(b,b.FindNet('PEDET'),[(101.95,70.4),(102.5,71.2),(108,70)])
T(b,b.FindNet('CLKREQ_N'),[(101.95,68.4),(102.5,67.6),(108,68)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
