"""V94: individual J3 power dogbones into a common F.Cu south bus."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_AUTHORITY_REGEN_V91.kicad_pcb'; OUT=R/'PHASE24_STORAGE_AUTHORITY_J3_VERTICAL_V94.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
def tr(pts,w=.30):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.F_Cu); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr([(211.1,149.05),(280,140),(280,176),(211,176)])
for x in (211.0,211.5,213.5,214.0,214.5,215.0,228.0,228.5,229.0):
 tr([(x,167.275),(x,176)])
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
