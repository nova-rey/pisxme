"""V1211: CLKREQ edge trunk with cleared outer transition and vertical J1 launch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U116_RECHANNEL_V1207.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CLKREQ_EDGE_CORRIDOR_V1211.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('CLKREQ_N'); add(b,n,[(99.6,73.95),(99.6,76.0)],F); via(b,n,(99.6,76.0)); add(b,n,[(99.6,76.0),(70.0,76.0),(70.0,45.0),(133.0,45.0),(133.0,72.0)],B); via(b,n,(133.0,72.0)); add(b,n,[(133.0,72.0),(120.0,72.0),(120.0,75.0)],F); add(b,n,[(133.0,45.0),(136.5,45.0),(136.5,68.5)],B); via(b,n,(136.5,68.5)); add(b,n,[(136.5,68.5),(136.5,70.275)],F); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
