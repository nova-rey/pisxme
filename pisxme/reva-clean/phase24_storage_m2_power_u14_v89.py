"""V89: source the M.2 rail from the non-QFN U14 storage-rail pad."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb'; OUT=R/'PHASE24_STORAGE_M2_POWER_U14_V89.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
def tr(layer,pts,w=.25):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetLayer(layer); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); b.Add(q)
# U14.5 is an existing authoritative storage-rail pad outside the QFN.
tr(pcbnew.F_Cu,[(211.1,149.05),(213.0,149.05)]); via(213.0,149.05)
tr(pcbnew.In1_Cu,[(213.0,149.05),(236.0,181.0)],.35)
for g in [(211.0,211.5),(213.5,214.0,214.5,215.0),(228.0,228.5,229.0)]:
 for a,z in zip(g,g[1:]): tr(pcbnew.F_Cu,[(a,167.275),(z,167.275)])
 qx=g[-1]; endx=236.0 if qx==229.0 else qx
 tr(pcbnew.F_Cu,[(qx,167.275),(endx,167.275),(endx,181)]); via(endx,181)
 tr(pcbnew.In1_Cu,[(endx,181),(236.0,181)],.35)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
