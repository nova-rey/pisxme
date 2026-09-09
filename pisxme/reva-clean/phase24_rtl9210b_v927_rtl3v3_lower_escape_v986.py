"""V986: RTL_3V3 lower-side source escape against accepted V927 SPI."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_V927_RTL3V3_LOWER_ESCAPE_V986.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname()=='RTL_3V3': b.RemoveNative(item)
n=b.FindNet('RTL_3V3'); tr(b,n,[(100.4,66.05),(100.4,67.4),(101.4,67.4)],F); via(b,n,(101.4,67.4)); tr(b,n,[(101.4,67.4),(108.0,67.4)],B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
