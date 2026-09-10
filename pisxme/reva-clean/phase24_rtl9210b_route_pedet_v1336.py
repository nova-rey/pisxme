"""V1336: vertical-first PEDET escape from U1.8, then B.Cu support handoff."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V1058_SUPPORT_LANE_ORIGINAL_J1_V1332.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_PEDET_VERTICAL_FIRST_V1336.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); VW=pcbnew.FromMM(.60); VD=pcbnew.FromMM(.30)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def vi(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(VW); q.SetDrill(VD); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('PEDET')
tr(b,n,F,(97.6,73.95),(97.6,76.0)); tr(b,n,F,(97.6,76.0),(96.4,76.0)); vi(b,n,(96.4,76.0)); tr(b,n,B,(96.4,76.0),(96.4,79.5)); tr(b,n,B,(96.4,79.5),(119.0,79.5)); vi(b,n,(119.0,79.5)); tr(b,n,F,(119.0,79.5),(120.0,80.0)); vi(b,n,(120.0,80.0)); tr(b,n,B,(120.0,80.0),(125.0,80.0)); vi(b,n,(125.0,80.0)); tr(b,n,F,(125.0,80.0),(140.75,80.0)); tr(b,n,F,(140.75,80.0),(140.75,62.725))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
