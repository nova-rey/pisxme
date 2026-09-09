"""V1230: REFCLK differential pair source escape and mid-level B.Cu corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_PERST_EDGE_CORRIDOR_V1226.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_REFCLK_PAIR_CORRIDOR_V1230.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); p=b.FindNet('REFCLK_P'); n=b.FindNet('REFCLK_N'); assert p and n
add(b,p,[(94.05,70.4),(92.0,70.4)],F); via(b,p,(92.0,70.4)); add(b,p,[(92.0,70.4),(92.0,65.8)],B); add(b,p,[(92.0,65.8),(137.25,65.8),(137.25,64.5)],B); via(b,p,(137.25,64.5)); add(b,p,[(137.25,64.5),(137.25,62.725)],F)
add(b,n,[(94.05,70.8),(91.4,70.8)],F); via(b,n,(91.4,70.8)); add(b,n,[(91.4,70.8),(91.4,66.5)],B); add(b,n,[(91.4,66.5),(136.75,66.5),(136.75,64.5)],B); via(b,n,(136.75,64.5)); add(b,n,[(136.75,64.5),(136.75,62.725)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
