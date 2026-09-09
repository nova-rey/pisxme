"""V1225: PERST_N B.Cu transit between the existing y=82/y=84 shelves."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_CLKREQ_EDGE_CORRIDOR_V1211.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_PERST_EDGE_CORRIDOR_V1225.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def rmseg(b,n,a,z,l):
    for q in list(b.GetTracks()):
        if q.GetNetname()==n and q.GetLayerName()==l and ((q.GetStart()==P(*a) and q.GetEnd()==P(*z)) or (q.GetStart()==P(*z) and q.GetEnd()==P(*a))): b.RemoveNative(q)
b=pcbnew.LoadBoard(str(BASE)); clk=b.FindNet('CLKREQ_N'); per=b.FindNet('PERST_N'); assert clk and per
rmseg(b,'CLKREQ_N',(99.6,73.95),(99.6,76.0),'F.Cu'); rmseg(b,'CLKREQ_N',(99.6,76.0),(70.0,76.0),'B.Cu')
for q in list(b.GetTracks()):
    if q.GetNetname()=='CLKREQ_N' and type(q).__name__=='PCB_VIA' and q.GetPosition()==P(99.6,76.0): b.RemoveNative(q)
add(b,clk,[(99.6,73.95),(99.6,75.0),(98.8,75.0)],F); add(b,clk,[(98.8,75.0),(98.8,76.0)],F); via(b,clk,(98.8,76.0)); add(b,clk,[(98.8,76.0),(70.0,76.0)],B)
add(b,per,[(100.0,73.95),(100.0,83.0)],F); via(b,per,(100.0,83.0)); add(b,per,[(100.0,83.0),(138.0,83.0),(138.0,68.5)],B); via(b,per,(138.0,68.5)); add(b,per,[(138.0,68.5),(138.0,71.5),(136.0,71.5),(136.0,70.275)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
