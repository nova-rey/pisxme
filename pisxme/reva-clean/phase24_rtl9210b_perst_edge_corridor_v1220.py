"""V1220: PERST_N co-authored QFN escape on the V1211 CLKREQ basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CLKREQ_EDGE_CORRIDOR_V1211.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_PERST_EDGE_CORRIDOR_V1220.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(board,net,points,layer):
    for a,z in zip(points,points[1:]):
        q=pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
        q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
def via(board,net,xy):
    q=pcbnew.PCB_VIA(board); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30))
    q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('PERST_N'); assert n
# Immediate south departure avoids the adjacent CLKREQ_N and U1.16 launches.
add(b,n,[(100.0,73.95),(100.0,79.0),(104.5,79.0)],F)
via(b,n,(104.5,79.0))
# Dedicated upper edge corridor; CLKREQ_N remains on y=45 and x=133/136.5.
add(b,n,[(104.5,79.0),(104.5,42.0),(136.0,42.0),(136.0,68.5)],B)
via(b,n,(136.0,68.5))
add(b,n,[(136.0,68.5),(136.0,70.275)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
