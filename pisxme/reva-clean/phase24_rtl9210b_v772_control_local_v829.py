"""V829: local PEDET/CLKREQ resistor placement beside U1 control pads."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_GROUND_V772.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V772_CONTROL_LOCAL_V829.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for ref,target in {'R2':(108,70),'R3':(108,68)}.items():
 f=b.FindFootprintByReference(ref); q=f.FindPadByNumber('1').GetPosition(); f.SetPosition(f.GetPosition()+P(*target)-q)
T(b,b.FindNet('PEDET'),[(101.95,70.4),(108,70)])
T(b,b.FindNet('CLKREQ_N'),[(101.95,68.4),(108,68)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
