"""V973: test a leftward SPISO3 transition around RTL_3V3 cell 100.0,64.6."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_3V3_SWEEP_100p0_64p6.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_V969_SPISO3_LEFT_TRANSITION_V973.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname()=='SPISO3': b.RemoveNative(item)
n=b.FindNet('SPISO3'); tr(b,n,F,[(99.6,66.05),(99.6,65.0),(98.6,64.5),(98.6,62.5),(101.0,60.5)]); via(b,n,(101,60.5)); tr(b,n,B,[(101,60.5),(103.5,60.5),(103.5,72.8)]); via(b,n,(103.5,72.8)); tr(b,n,F,[(103.5,72.8),(105,72.8)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
