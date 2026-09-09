"""V1232: co-author REFCLK source fanout with the PERST edge corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_PERST_EDGE_CORRIDOR_V1226.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_REFCLK_CONTROL_COAUTHOR_V1232.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); clk=b.FindNet('CLKREQ_N'); per=b.FindNet('PERST_N'); p=b.FindNet('REFCLK_P'); n=b.FindNet('REFCLK_N'); assert clk and per and p and n
# Reallocate only PERST_N's left/top wrap; retain its QFN and J1 endpoint semantics.
for q in list(b.GetTracks()):
    if q.GetNetname()=='PERST_N': b.RemoveNative(q)
add(b,per,[(100.0,73.95),(100.0,83.0)],F); via(b,per,(100.0,83.0)); add(b,per,[(100.0,83.0),(70.0,83.0),(70.0,43.0),(138.0,43.0),(138.0,68.5)],B); via(b,per,(138.0,68.5)); add(b,per,[(138.0,68.5),(138.0,71.5),(136.0,71.5),(136.0,70.275)],F)
# REFCLK source tracks leave the QFN pad field on the left before entering B.Cu.
add(b,p,[(94.05,70.4),(93.2,70.4),(93.2,77.8)],F); via(b,p,(93.2,77.8)); add(b,p,[(93.2,77.8),(68.5,77.8),(68.5,41.5),(141.0,41.5),(141.0,60.5)],B); via(b,p,(141.0,60.5)); add(b,p,[(141.0,60.5),(141.0,61.5),(137.25,61.5),(137.25,62.725)],F)
add(b,n,[(94.05,70.8),(92.2,70.8),(92.2,78.5)],F); via(b,n,(92.2,78.5)); add(b,n,[(92.2,78.5),(67.8,78.5),(67.8,42.2),(139.8,42.2),(139.8,60.5)],B); via(b,n,(139.8,60.5)); add(b,n,[(139.8,60.5),(139.8,60.8),(136.75,60.8),(136.75,62.725)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
