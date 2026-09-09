"""V950: move SPISO source transition below its U1 pad."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V944_SPISO_PAIR_REGEN_V949.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V949_SPISO_SOURCE_V950.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
n=b.FindNet('SPISO')
tr(b,n,[(99.2,66.05),(99.2,66.8)],F); via(b,n,(99.2,66.8))
tr(b,n,[(99.2,66.8),(99.2,84),(104.5,84),(104.5,78.8)],B); via(b,n,(104.5,78.8)); tr(b,n,[(104.5,78.8),(105,78.8)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
