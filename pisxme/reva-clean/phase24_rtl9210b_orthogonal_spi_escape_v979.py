"""V979: orthogonal QFN escape with separated through-via transitions."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORTHOGONAL_SOURCE_ESCAPE_V978.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORTHOGONAL_SPI_ESCAPE_V979.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(board,net,pts,layer):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
def via(board,net,xy):
    q=pcbnew.PCB_VIA(board); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
b=pcbnew.LoadBoard(str(BASE))
def R(name, f, v1, back, v2, end):
    n=b.FindNet(name); tr(b,n,f,F); via(b,n,v1); tr(b,n,back,B); via(b,n,v2); tr(b,n,end,F)
R('SPICS',[(98.8,66.05),(98.8,64.0),(97.5,64.0)],(97.5,64.0),[(97.5,64.0),(97.5,80.0),(103.5,80.0)],(103.5,80.0),[(103.5,80.0),(105,80)])
R('SPISO',[(99.2,66.05),(99.2,63.6),(98.5,63.6)],(98.5,63.6),[(98.5,63.6),(98.5,84.0),(104.5,84.0),(104.5,78.8)],(104.5,78.8),[(104.5,78.8),(105,78.8)])
R('SPISO3',[(99.6,66.05),(99.6,63.2),(99.5,63.2)],(99.5,63.2),[(99.5,63.2),(99.5,59.0),(103.5,59.0),(103.5,72.8)],(103.5,72.8),[(103.5,72.8),(105,72.8)])
R('SPICLK',[(100.8,66.05),(100.8,62.8),(100.5,62.8)],(100.5,62.8),[(100.5,62.8),(104.0,60.0),(104.5,60.0),(104.5,74.0)],(104.5,74.0),[(104.5,74.0),(105,74)])
R('SPISI',[(101.2,66.05),(101.2,68.4),(102.5,68.4)],(102.5,68.4),[(102.5,68.4),(106.0,68.4),(106.5,75.2)],(106.5,75.2),[(106.5,75.2),(105,75.2)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
