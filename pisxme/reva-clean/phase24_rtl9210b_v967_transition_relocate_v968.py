"""V968: relocate SPICLK and SPISI transitions around V967 conflicts."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V927_SPI_3V3_PARTITION_V967.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_V967_TRANSITION_RELOCATE_V968.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname() in {'SPICLK','SPISI'}: b.RemoveNative(item)
n=b.FindNet('SPISI'); tr(b,n,F,[(101.2,66.05),(106.5,66.05),(106.5,67.5)]); via(b,n,(106.5,67.5)); tr(b,n,B,[(106.5,67.5),(106.5,75.2)]); via(b,n,(106.5,75.2)); tr(b,n,F,[(106.5,75.2),(105,75.2)])
n=b.FindNet('SPICLK'); tr(b,n,F,[(100.8,66.05),(100.8,64.5),(99.8,64.0),(104,60)]); via(b,n,(104,60)); tr(b,n,B,[(104,60),(104.5,60),(104.5,74)]); via(b,n,(104.5,74)); tr(b,n,F,[(104.5,74),(105,74)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
