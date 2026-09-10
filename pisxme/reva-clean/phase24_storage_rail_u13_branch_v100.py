"""V100 diagnostic: repeat V95 without a full-board zone refill."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_AUTHORITY_J3_VERTICAL_V94.kicad_pcb'; OUT=R/'PHASE24_STORAGE_RAIL_U13_BRANCH_V100.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
for a,z in zip([(181.5,135),(186,128),(211.1,128),(211.1,149.05)],[(186,128),(211.1,128),(211.1,149.05)]):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.F_Cu); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(.25)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
# Deliberately do not refill unrelated zones; this isolates saved-copper effect.
b.Save(str(OUT)); print(OUT)
