"""V1240: disposable REFCLK source-field co-authoring after local rail clear."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_PERST_EDGE_CORRIDOR_V1226.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_REFCLK_SOURCE_FIELD_CLEAR_V1240.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def inside(v): return 90<=pcbnew.ToMM(v.x)<=100 and 63<=pcbnew.ToMM(v.y)<=80
def add(b,n,pts,l):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
    if q.GetNetname() in {'RTL_1V1','RTL_3V3','GND'} and (inside(q.GetStart()) or inside(q.GetEnd())): b.RemoveNative(q)
for q in list(b.GetTracks()):
    if type(q).__name__=='PCB_VIA' and q.GetNetname() in {'RTL_1V1','RTL_3V3','GND'} and inside(q.GetPosition()): b.RemoveNative(q)
p=b.FindNet('REFCLK_P'); n=b.FindNet('REFCLK_N'); assert p and n
add(b,p,[(94.05,70.4),(91.5,70.4),(91.5,78.5)],F); via(b,p,(91.5,78.5)); add(b,p,[(91.5,78.5),(72.0,78.5)],B); via(b,p,(72.0,78.5)); add(b,p,[(72.0,78.5),(72.0,41.5)],F); via(b,p,(72.0,41.5)); add(b,p,[(72.0,41.5),(141.0,41.5),(141.0,60.5)],B); via(b,p,(141.0,60.5)); add(b,p,[(141.0,60.5),(141.0,61.5),(137.25,61.5),(137.25,62.725)],F)
add(b,n,[(94.05,70.8),(92.5,70.8),(92.5,79.2)],F); via(b,n,(92.5,79.2)); add(b,n,[(92.5,79.2),(70.8,79.2)],B); via(b,n,(70.8,79.2)); add(b,n,[(70.8,79.2),(70.8,42.2)],F); via(b,n,(70.8,42.2)); add(b,n,[(70.8,42.2),(139.8,42.2),(139.8,60.5)],B); via(b,n,(139.8,60.5)); add(b,n,[(139.8,60.5),(139.8,60.8),(136.75,60.8),(136.75,62.725)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
