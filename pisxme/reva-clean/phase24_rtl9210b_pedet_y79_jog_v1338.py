"""V1338: move PEDET's post-R2 run to a y=79 F.Cu corridor."""
from pathlib import Path
import runpy
import pcbnew
H=Path(__file__).resolve().parent
runpy.run_path(str(H/'phase24_rtl9210b_route_pedet_v1336.py'))
src=H/'PHASE24_RTL9210B_PEDET_VERTICAL_FIRST_V1336.kicad_pcb'
out=H/'PHASE24_RTL9210B_PEDET_Y79_JOG_V1338.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('PEDET')
for x in list(b.GetTracks()):
    if x.GetNetname()=='PEDET' and not isinstance(x,pcbnew.PCB_VIA):
        a=x.GetStart(); z=x.GetEnd(); vals=[a.x/1e6,a.y/1e6,z.x/1e6,z.y/1e6]
        if (abs(vals[0]-125)<.01 and abs(vals[1]-80)<.01 and abs(vals[2]-140.75)<.01 and abs(vals[3]-80)<.01) or (abs(vals[0]-140.75)<.01 and abs(vals[1]-80)<.01 and abs(vals[2]-140.75)<.01 and abs(vals[3]-62.725)<.01): b.RemoveNative(x)
for x in list(b.GetTracks()):
    if x.GetNetname()=='PEDET' and isinstance(x,pcbnew.PCB_VIA) and abs(x.GetPosition().x/1e6-140.75)<.01 and abs(x.GetPosition().y/1e6-80)<.01: b.RemoveNative(x)
def tr(a,z):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr((125,80),(125,79)); tr((125,79),(140.75,79)); tr((140.75,79),(140.75,62.725))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
