"""V1341: co-author CLKREQ_N around the accepted lane/PEDET fields."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_PEDET_BCU_THEN_FCU_V1340.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CLKREQ_COAUTHORED_V1341.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('CLKREQ_N')
tr(b,n,(99.6,73.95),(99.6,77.0)); tr(b,n,(99.6,77.0),(120.0,77.0)); tr(b,n,(120.0,77.0),(120.0,75.0)); tr(b,n,(120.0,75.0),(120.0,72.0)); tr(b,n,(120.0,72.0),(133.0,72.0)); tr(b,n,(133.0,72.0),(136.5,68.5)); tr(b,n,(136.5,68.5),(136.5,70.275))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
