"""V108: stripped local fixture proving rotated pin-9 escape geometry."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_SELECTORS_ROTATE90_V106.kicad_pcb'; OUT=R/'PHASE24_STORAGE_SELECTOR_ROT90_STRIPPED_V108.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_SEL'); assert n
for x in list(b.GetTracks()): b.RemoveNative(x)
for z in list(b.Zones()): b.RemoveNative(z)
for a,z in [((155,136.5),(155,139)),((180,136.5),(180,139)),((211.1,150.95),(214,150.95))]:
 q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.F_Cu); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(.20)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.Save(str(OUT)); print(OUT)
