"""V1222: PERST_N source jog and raised lower corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_CLKREQ_EDGE_CORRIDOR_V1211.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_PERST_EDGE_CORRIDOR_V1222.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('PERST_N'); assert n
add(b,n,[(100.0,73.95),(100.3,74.5),(100.3,78.5),(128.0,78.5)],F); via(b,n,(128.0,78.5))
add(b,n,[(128.0,78.5),(138.0,78.5),(138.0,68.5)],B); via(b,n,(138.0,68.5))
add(b,n,[(138.0,68.5),(138.0,71.5),(136.0,71.5),(136.0,70.275)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
