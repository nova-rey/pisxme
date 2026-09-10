"""V85: V84 edge-access trial with the rightmost drop moved clear of C50."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb'
OUT=R/'PHASE24_STORAGE_M2_POWER_EDGE_V85.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
def tr(layer,pts,w=.25):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetLayer(layer); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); b.Add(q)
tr(pcbnew.F_Cu,[(181.5,135),(186,135)]); via(186,135); tr(pcbnew.In1_Cu,[(186,135),(186,182)],.35)
groups=[(211.0,211.5),(213.5,214.0,214.5,215.0),(228.0,228.5,229.0)]
for g in groups:
 for a,z in zip(g,g[1:]): tr(pcbnew.F_Cu,[(a,167.275),(z,167.275)])
 qx=g[-1]
 # Only the rightmost group uses an outboard dogleg around the C50 pad.
 if qx == 229.0:
  tr(pcbnew.F_Cu,[(qx,167.275),(231.0,167.275),(231.0,181)])
  via(231.0,181); tr(pcbnew.In1_Cu,[(231.0,181),(186,182)],.35)
 else:
  tr(pcbnew.F_Cu,[(qx,167.275),(qx,181)]); via(qx,181); tr(pcbnew.In1_Cu,[(qx,181),(186,182)],.35)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
