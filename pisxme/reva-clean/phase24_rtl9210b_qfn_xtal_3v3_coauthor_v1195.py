"""V1195: offset the V1194 XTAL_OUT transition clear of GND."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_QFN_XTAL_3V3_COAUTHOR_V1194.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_QFN_XTAL_3V3_COAUTHOR_V1195.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def same(a,b): return (a.GetStart()==P(*b[0]) and a.GetEnd()==P(*b[1])) or (a.GetStart()==P(*b[1]) and a.GetEnd()==P(*b[0]))
def add(b,n,a,z,l):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('XTAL_OUT'); remove=[]
for x in b.GetTracks():
 if x.GetNetname()=='XTAL_OUT':
  if type(x).__name__=='PCB_VIA' and x.GetPosition()==P(89.5,67.6): remove.append(x)
  elif type(x).__name__!='PCB_VIA' and (same(x,((94.05,67.6),(89.5,67.6))) or same(x,((89.5,67.6),(80.0,68.0)))): remove.append(x)
for x in remove: b.RemoveNative(x)
via(b,n,(88.5,67.6)); add(b,n,(94.05,67.6),(88.5,67.6),F); add(b,n,(88.5,67.6),(80.0,68.0),B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
