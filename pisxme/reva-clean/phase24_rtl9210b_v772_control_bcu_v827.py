"""V827: laterally separate control source vias from existing SPI corridors."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V772_CONTROL_BCU_V826.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V772_CONTROL_BCU_V827.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname() in ('PEDET','CLKREQ_N'): b.RemoveNative(item)
n=b.FindNet('PEDET'); T(b,n,F,[(101.95,70.4),(102.5,70.4)]); V(b,n,(102.5,70.4)); T(b,n,B,[(102.5,70.4),(102.5,82),(111.2,82),(111.2,60)]); V(b,n,(111.2,60)); T(b,n,F,[(111.2,60),(112,60)])
n=b.FindNet('CLKREQ_N'); T(b,n,F,[(101.95,68.4),(106,68.4)]); V(b,n,(106,68.4)); T(b,n,B,[(106,68.4),(106,57),(107.2,57),(107.2,63)]); V(b,n,(107.2,63)); T(b,n,F,[(107.2,63),(108,63)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
