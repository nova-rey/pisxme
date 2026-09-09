"""V980: five-SPI orthogonal source escape with separated B.Cu corridors."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ORTHOGONAL_SPI_ESCAPE_V980.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); local={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
for item in list(b.GetTracks()):
 if item.GetNetname() in local: b.RemoveNative(item)
def R(name,f,v1,back,v2,end):
 n=b.FindNet(name); tr(b,n,f,F); via(b,n,v1); tr(b,n,back,B); via(b,n,v2); tr(b,n,end,F)
R('SPICS',[(98.8,66.05),(98.8,64.0),(97.5,64.0)],(97.5,64.0),[(97.5,64.0),(97.5,80.0),(103.5,80.0)],(103.5,80.0),[(103.5,80.0),(105,80)])
R('SPISO',[(99.2,66.05),(99.2,63.6),(98.5,63.6)],(98.5,63.6),[(98.5,63.6),(98.5,84.0),(104.5,84.0),(104.5,78.8)],(104.5,78.8),[(104.5,78.8),(105,78.8)])
R('SPISO3',[(99.6,66.05),(99.6,63.2),(100.5,63.2)],(100.5,63.2),[(100.5,63.2),(100.5,55.0),(104.0,55.0),(104.0,72.8)],(104.0,72.8),[(104.0,72.8),(105,72.8)])
R('SPICLK',[(100.8,66.05),(100.8,62.8),(101.5,62.8)],(101.5,62.8),[(101.5,62.8),(101.5,56.0),(105.5,56.0),(105.5,74.0)],(105.5,74.0),[(105.5,74.0),(105,74)])
R('SPISI',[(101.2,66.05),(101.2,69.2),(103.5,69.2)],(103.5,69.2),[(103.5,69.2),(103.5,76.0),(104.5,76.0),(104.5,75.2)],(104.5,75.2),[(104.5,75.2),(105,75.2)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
