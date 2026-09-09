"""V1049: attach U1.20 RTL_3V3 through the right-edge corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ORIENTATION0_QFN_RAILS_V1048.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ORIENTATION0_QFN_RAILS_V1049.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
# Existing V1048 via at (108,64) is the verified transition into the C3 rail.
add(b,n,[(101.95,72.4),(103.0,72.4),(103.0,64.0),(108.0,64.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
