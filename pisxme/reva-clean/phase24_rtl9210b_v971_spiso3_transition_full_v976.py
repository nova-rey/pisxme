"""V976: full SPISO3 transition relocation around the best RTL_3V3 cell."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_3V3_SWEEP_100p0_64p6.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_V971_SPISO3_TRANSITION_FULL_V976.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname()=='SPISO3': b.RemoveNative(item)
n=b.FindNet('SPISO3'); tr(b,n,F,[(99.6,66.05),(99.6,63.5)]); via(b,n,(99.6,63.5)); tr(b,n,B,[(99.6,63.5),(99.6,58.0),(101.0,58.0),(101.0,60.5)]); via(b,n,(101,60.5)); tr(b,n,B,[(101,60.5),(103.5,60.5),(103.5,72.8)]); via(b,n,(103.5,72.8)); tr(b,n,F,[(103.5,72.8),(105,72.8)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
