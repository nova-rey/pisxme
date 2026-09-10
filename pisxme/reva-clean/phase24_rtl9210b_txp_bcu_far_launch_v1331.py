"""V1331: move only TXP's long run to a far-right B.Cu corridor."""
from pathlib import Path
import runpy
import pcbnew
H=Path(__file__).resolve().parent
runpy.run_path(str(H/'phase24_rtl9210b_lane_original_j1_coauthored_v1329.py'))
src=H/'PHASE24_RTL9210B_V1058_SUPPORT_LANE_ORIGINAL_J1_V1329.kicad_pcb'
out=H/'PHASE24_RTL9210B_V1058_SUPPORT_LANE_ORIGINAL_J1_V1331.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); VW=pcbnew.FromMM(.60); VD=pcbnew.FromMM(.30)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('LANE0_TXP')
for x in list(b.GetTracks()):
    if x.GetNetname()=='LANE0_TXP': b.RemoveNative(x)
def tr(l,a,z):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def vi(p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(VW); q.SetDrill(VD); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr(F,(94.05,73.2),(90.8,73.2)); tr(F,(90.8,73.2),(90.8,76.8)); vi((90.8,76.8)); tr(B,(90.8,76.8),(90.8,88.0)); tr(B,(90.8,88.0),(136.0,88.0)); tr(B,(136.0,88.0),(136.0,61.0)); vi((136.0,61.0)); tr(B,(136.0,61.0),(135.75,61.0)); vi((135.75,61.0)); tr(F,(135.75,61.0),(135.75,62.725))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
