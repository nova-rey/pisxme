"""V1207: corrected U1.16 east rechannel with complete source removal."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_PEDET_LAYER_BOUNDARY_V1200.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U116_RECHANNEL_V1207.kicad_pcb'; F,L=pcbnew.F_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1'); remove=[]
for x in b.GetTracks():
 if x.GetNetname()!='RTL_1V1': continue
 if type(x).__name__=='PCB_VIA' and x.GetPosition()==P(98.5,76.0): remove.append(x)
 elif type(x).__name__!='PCB_VIA' and any({(pcbnew.ToMM(x.GetStart().x),pcbnew.ToMM(x.GetStart().y)),(pcbnew.ToMM(x.GetEnd().x),pcbnew.ToMM(x.GetEnd().y))}==set(map(lambda q:(float(q[0]),float(q[1])), pair)) for pair in [((100.8,73.95),(100.8,75.0)),((100.8,75.0),(100.8,76.0)),((100.8,73.95),(100.8,76.0)),((100.8,76.0),(98.5,76.0)),((98.5,76.0),(91.8,69.0))]): remove.append(x)
for x in remove: b.RemoveNative(x)
add(b,n,[(100.8,73.95),(100.8,77.0),(104.5,77.0)],F); via(b,n,(104.5,77.0)); add(b,n,[(104.5,77.0),(91.8,69.0)],L); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
