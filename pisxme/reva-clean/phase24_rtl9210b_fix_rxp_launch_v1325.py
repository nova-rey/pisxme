"""V1325: move only the RXP connector handoff clear of the RXN transition."""
from pathlib import Path
import runpy
import pcbnew
H=Path(__file__).resolve().parent
runpy.run_path(str(H/'phase24_rtl9210b_outboard_j1_coauthored_v1324.py'))
src=H/'PHASE24_RTL9210B_OUTBOARD_J1_COAUTHORED_V1324.kicad_pcb'
out=H/'PHASE24_RTL9210B_OUTBOARD_J1_COAUTHORED_V1325.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('LANE0_RXP')
for item in list(b.GetTracks()):
    if item.GetNetname()!='LANE0_RXP': continue
    if isinstance(item,pcbnew.PCB_VIA) and abs(item.GetPosition().x/1e6-154.25)<.01 and abs(item.GetPosition().y/1e6-68)<.01:
        b.RemoveNative(item)
    elif not isinstance(item,pcbnew.PCB_VIA):
        a=item.GetStart(); z=item.GetEnd(); vals=[a.x/1e6,a.y/1e6,z.x/1e6,z.y/1e6]
        if (abs(vals[0]-150)<.01 and abs(vals[1]-68)<.01 and abs(vals[2]-154.25)<.01 and abs(vals[3]-68)<.01) or (abs(vals[0]-154.25)<.01 and abs(vals[1]-68)<.01 and abs(vals[2]-154.25)<.01 and abs(vals[3]-62.725)<.01):
            b.RemoveNative(item)
def tr(a,z):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr((150,82),(150,60)); tr((150,60),(154.25,60))
v=pcbnew.PCB_VIA(b); v.SetPosition(P(154.25,60)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
tr((154.25,60),(154.25,62.725))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
