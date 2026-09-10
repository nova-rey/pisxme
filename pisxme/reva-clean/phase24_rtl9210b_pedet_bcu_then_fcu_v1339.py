"""V1339: PEDET B.Cu corridor to x=135, then F.Cu connector launch."""
from pathlib import Path
import runpy
import pcbnew
H=Path(__file__).resolve().parent
runpy.run_path(str(H/'phase24_rtl9210b_route_pedet_v1336.py'))
src=H/'PHASE24_RTL9210B_PEDET_VERTICAL_FIRST_V1336.kicad_pcb'
out=H/'PHASE24_RTL9210B_PEDET_BCU_THEN_FCU_V1339.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); VW=pcbnew.FromMM(.60); VD=pcbnew.FromMM(.30)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('PEDET')
for x in list(b.GetTracks()):
    if x.GetNetname()=='PEDET' and not isinstance(x,pcbnew.PCB_VIA):
        a=x.GetStart(); z=x.GetEnd(); vals=[a.x/1e6,a.y/1e6,z.x/1e6,z.y/1e6]
        if (abs(vals[0]-125)<.01 and abs(vals[1]-80)<.01) or (abs(vals[0]-140.75)<.01 and abs(vals[1]-80)<.01): b.RemoveNative(x)
for x in list(b.GetTracks()):
    if x.GetNetname()=='PEDET' and isinstance(x,pcbnew.PCB_VIA) and abs(x.GetPosition().x/1e6-140.75)<.01 and abs(x.GetPosition().y/1e6-80)<.01: b.RemoveNative(x)
def tr(l,a,z):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def vi(p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(VW); q.SetDrill(VD); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr(B,(125,80),(125,79)); tr(B,(125,79),(135,79)); vi((135,79)); tr(F,(135,79),(140.75,79)); tr(F,(140.75,79),(140.75,62.725))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
