"""Disposable power-plane-access trial; signals remain off plane layers."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb'
OUT=R/'PHASE24_STORAGE_M2_POWER_PLANE_V83.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
def tr(layer,a,z,w=.25):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(layer); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); b.Add(q)
# One source pad and three connector groups; internal In1 is power copper.
tr(pcbnew.F_Cu,(181.5,135),(183.0,135)); via(183.0,135)
tr(pcbnew.In1_Cu,(183.0,135),(183.0,180),.35)
for xs, qx in [((211.0,211.5),211.5),((213.5,214.0,214.5,215.0),215.0),((228.0,228.5,229.0),229.0)]:
 for x in xs[:-1]: tr(pcbnew.F_Cu,(x,167.275),(x+0.5,167.275))
 tr(pcbnew.F_Cu,(qx,167.275),(qx,169.0)); via(qx,169.0)
 tr(pcbnew.In1_Cu,(qx,169.0),(183.0,180),.35)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
