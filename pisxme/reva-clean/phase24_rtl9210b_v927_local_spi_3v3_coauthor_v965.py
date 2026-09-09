"""V965: co-author local SPICLK/RTL_5V with an up-first RTL_3V3 trunk."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_V927_LOCAL_SPI_3V3_COAUTHOR_V965.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
LOCAL={'SPICLK','RTL_5V','RTL_3V3'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname() in LOCAL: b.RemoveNative(item)
n=b.FindNet('SPICLK'); tr(b,n,F,[(100.8,66.05),(100.8,64.0),(101.2,63.5),(104.0,60.0)]); via(b,n,(104,60)); tr(b,n,B,[(104,60),(104.5,60),(104.5,74)]); via(b,n,(104.5,74)); tr(b,n,F,[(104.5,74),(105,74)])
n=b.FindNet('RTL_5V'); tr(b,n,F,[(101.95,66.8),(102.5,66.8),(102.5,63.0)]); via(b,n,(102.5,63.0)); tr(b,n,B,[(102.5,63.0),(96,63.0)]); tr(b,n,B,[(96,63),(95.2,64.5)])
n=b.FindNet('RTL_3V3'); tr(b,n,F,[(100.4,66.05),(100.4,65.2)]); via(b,n,(100.4,65.2)); tr(b,n,B,[(100.4,65.2),(100.4,56.0),(109.5,56.0),(109.5,58.0)]); via(b,n,(109.5,58.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
