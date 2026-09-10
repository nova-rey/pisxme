"""V1402: disposable local LANE0_RXN via relocation for U1.63 escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U160_1V1_TOP_SHELF_V1392.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RXN_RELOCATE_FOR_U163_V1402.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); rx=b.FindNet('LANE0_RXN'); one=b.FindNet('RTL_1V1'); assert rx and one
for x in list(b.GetTracks()):
 if x.GetNetname()=='LANE0_RXN': b.RemoveNative(x)
# Preserve the far launch; move only the source transition and its vertical.
tr(b,rx,F,[(94.05,72.0),(92.0,72.0),(91.0,71.0)]); via(b,rx,(91.0,71.0)); tr(b,rx,B,[(91.0,71.0),(91.0,84.0)]); via(b,rx,(91.0,84.0)); tr(b,rx,F,[(91.0,84.0),(92.8,84.0)])
# Add the U1.63 top shelf now freed from the original RXN transition.
tr(b,one,F,[(94.05,71.2),(93.6,71.2),(91.8,69.5)]); via(b,one,(91.8,69.5)); tr(b,one,B,[(91.8,69.5),(86.0,69.5),(86.0,56.0),(99.0,56.0)]); via(b,one,(99.0,56.0)); tr(b,one,F,[(99.0,56.0),(99.0,58.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
