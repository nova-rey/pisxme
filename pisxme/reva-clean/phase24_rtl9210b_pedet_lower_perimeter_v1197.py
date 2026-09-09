"""V1197: PEDET right-side source escape and raised lower perimeter."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_QFN_XTAL_3V3_COAUTHOR_V1195.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_PEDET_LOWER_PERIMETER_V1197.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('PEDET'); add(b,n,[(97.6,73.95),(98.8,73.95),(98.8,78.5)],F); via(b,n,(98.8,78.5)); add(b,n,[(98.8,78.5),(120.0,78.5)],B); via(b,n,(120.0,78.5)); add(b,n,[(120.0,78.5),(140.75,78.5)],B); via(b,n,(140.75,78.5)); add(b,n,[(140.75,78.5),(140.75,62.725)],F); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
