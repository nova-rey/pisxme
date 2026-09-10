"""V92: source-corrected parent plus no-via perimeter J3 power corridor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_AUTHORITY_REGEN_V91.kicad_pcb'; OUT=R/'PHASE24_STORAGE_AUTHORITY_FCU_V92.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
def tr(pts,w=.30):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.F_Cu); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr([(211.1,149.05),(280,140),(280,176),(211.5,176)])
for g in [(211.0,211.5),(213.5,214.0,214.5,215.0),(228.0,228.5,229.0)]:
 for a,z in zip(g,g[1:]): tr([(a,167.275),(z,167.275)])
 tr([(g[-1],167.275),(g[-1],176)])
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
