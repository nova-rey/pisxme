"""V885: clean stale local GND copper and retain the passing RSET route."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V880_SUPPORT_NORTHWEST_V882.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V882_RSET_ROUTE_CLEAN_V885.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if q.GetNetname() in ('GND','RSET'):b.RemoveNative(q)
n=b.FindNet('RSET')
for a,z in [((94.05,73.2),(91.5,73.2)),((91.5,73.2),(91.5,63.5)),((91.5,63.5),(88,63.5)),((88,63.5),(88,65))]:
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
