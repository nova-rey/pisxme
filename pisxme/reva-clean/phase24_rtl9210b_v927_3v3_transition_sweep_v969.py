"""V969: native-DRC sweep of RTL_3V3 transition cells."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for x in (99.0,99.4,100.0,100.4,101.0,101.4,102.0):
 for y in (64.0,64.6,65.2):
  b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
  tr(b,n,F,[(100.4,66.05),(100.4,65.6),(x,y)]); via(b,n,(x,y))
  tr(b,n,B,[(x,y),(x,56.0),(109.5,56.0),(109.5,58.0)]); via(b,n,(109.5,58.0))
  tag=f'{x:.1f}_{y:.1f}'.replace('.','p'); out=H/f'PHASE24_RTL9210B_3V3_SWEEP_{tag}.kicad_pcb'; b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
