"""V987: co-authored upper source exits for SPISO3/3V3/SPICLK."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_V927_UPPER_THREE_SOURCE_V987.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname() in {'SPISO3','RTL_3V3','SPICLK'}: b.RemoveNative(item)
routes={'SPISO3':([(99.6,66.05),(99.6,63.0),(98.5,63.0)],(98.5,63.0)), 'RTL_3V3':([(100.4,66.05),(100.4,63.8),(99.5,63.8)],(99.5,63.8)), 'SPICLK':([(100.8,66.05),(100.8,64.5),(102.5,64.5)],(102.5,64.5))}
for name,(pts,v) in routes.items():
 n=b.FindNet(name); tr(b,n,pts,F); via(b,n,v)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
