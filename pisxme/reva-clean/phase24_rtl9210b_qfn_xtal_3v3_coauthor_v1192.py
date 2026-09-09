"""V1192: co-author XTAL_IN/U1.52 RTL_3V3 departures."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_1V1_U116_U125_MERGED_V1183.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_QFN_XTAL_3V3_COAUTHOR_V1192.kicad_pcb'; F,B,L=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu; WF=pcbnew.FromMM(.20); WP=pcbnew.FromMM(.50)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def same(a,b): return a.GetStart()==P(*b[0]) and a.GetEnd()==P(*b[1]) or a.GetStart()==P(*b[1]) and a.GetEnd()==P(*b[0])
def add(b,n,pts,l,w):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(w); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); xi=b.FindNet('XTAL_IN'); p32=b.FindNet('RTL_3V3')
remove=[]
for x in b.GetTracks():
 if x.GetNetname()=='XTAL_IN':
  if type(x).__name__=='PCB_VIA' and x.GetPosition()==P(92.5,66.8): remove.append(x)
  elif type(x).__name__!='PCB_VIA' and (same(x,((94.05,67.2),(93.5,67.2))) or same(x,((93.5,67.2),(92.5,66.8))) or same(x,((94.5,66.8),(94.5,75.0))) or same(x,((92.5,66.8),(94.5,66.8)))): remove.append(x)
for x in remove: b.RemoveNative(x)
add(b,xi,[(94.05,67.2),(90.5,67.2),(90.5,66.8)],F,WF); via(b,xi,(90.5,66.8)); add(b,xi,[(90.5,66.8),(90.5,75.0)],B,WF)
add(b,p32,[(94.05,66.8),(92.0,66.8)],F,WF); via(b,p32,(92.0,66.8)); add(b,p32,[(92.0,66.8),(92.0,64.0),(99.6,62.8)],L,WP); via(b,p32,(99.6,62.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
