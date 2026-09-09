"""V1302: keep RSET on F.Cu around the current V1279 crystal/rail field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RSET_FCU_DOGLEG_V1302.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RSET')
for q in list(b.GetTracks()):
    if q.GetNetname()=='RSET': b.RemoveNative(q)
for a,z in zip([(94.8,66.05),(93.0,66.05),(93.0,68.5),(88.0,68.5)],[(93.0,66.05),(93.0,68.5),(88.0,68.5),(88.0,65.0)]):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
