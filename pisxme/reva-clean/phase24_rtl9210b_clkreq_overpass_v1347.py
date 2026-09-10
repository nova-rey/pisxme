"""V1347: route CLKREQ_N over the RXP/TXP transition fields."""
from pathlib import Path
import runpy
import pcbnew
H=Path(__file__).resolve().parent
runpy.run_path(str(H/'phase24_rtl9210b_clkreq_j1_launch_v1346.py'))
src=H/'PHASE24_RTL9210B_CLKREQ_J1_LAUNCH_V1346.kicad_pcb'
out=H/'PHASE24_RTL9210B_CLKREQ_OVERPASS_V1347.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); VW=pcbnew.FromMM(.60); VD=pcbnew.FromMM(.30)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('CLKREQ_N')
for x in list(b.GetTracks()):
    if x.GetNetname()=='CLKREQ_N': b.RemoveNative(x)
def tr(l,a,z):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def vi(p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(VW); q.SetDrill(VD); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr(F,(99.6,73.95),(99.6,77.0)); vi((99.6,77.0)); tr(B,(99.6,77.0),(107.0,77.0)); tr(B,(107.0,77.0),(107.0,74.0)); tr(B,(107.0,74.0),(119.2,74.0)); vi((119.2,74.0)); tr(F,(119.2,74.0),(120.0,75.0))
tr(F,(120.0,75.0),(120.0,72.0)); tr(F,(120.0,72.0),(128.0,72.0)); vi((128.0,72.0)); tr(B,(128.0,72.0),(128.0,58.0)); tr(B,(128.0,58.0),(138.0,58.0)); vi((138.0,58.0)); tr(F,(138.0,58.0),(138.0,68.5)); tr(F,(138.0,68.5),(136.5,68.5)); tr(F,(136.5,68.5),(136.5,70.275))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
