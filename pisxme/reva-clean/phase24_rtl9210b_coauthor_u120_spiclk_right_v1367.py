"""V1367: co-author U1.20 with a right-side SPICLK transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U152_3V3_ESCAPE_V1359.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_COAUTHOR_U120_SPICLK_RIGHT_V1367.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def clear(board,name):
 for x in list(board.GetTracks()):
  if x.GetNetname()==name: board.RemoveNative(x)
b=pcbnew.LoadBoard(str(BASE)); clk=b.FindNet('SPICLK'); n=b.FindNet('RTL_3V3'); assert clk and n
clear(b,'SPICLK')
tr(b,clk,F,(101.95,72.8),(108.0,72.8)); tr(b,clk,F,(108.0,72.8),(108.0,72.0)); via(b,clk,(108.0,72.0)); tr(b,clk,B,(108.0,72.0),(117.4,72.0)); via(b,clk,(117.4,72.0)); tr(b,clk,F,(117.4,72.0),(117.4,76.4))
tr(b,n,F,(101.95,72.4),(106.0,72.4)); via(b,n,(106.0,72.4)); tr(b,n,B,(106.0,72.4),(98.5,72.4)); tr(b,n,B,(98.5,72.4),(98.5,66.8)); tr(b,n,B,(98.5,66.8),(99.6,66.8)); tr(b,n,B,(99.6,66.8),(99.6,62.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
