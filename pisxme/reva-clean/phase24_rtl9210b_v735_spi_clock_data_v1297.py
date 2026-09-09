"""V1297: add rotated-U1 SPISI/SPICLK to the validated V1296 rails."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V735_SOURCE_RAILS_V1296.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V735_SPI_CLOCK_DATA_V1297.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def r(b,n,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); spi=b.FindNet('SPISI'); clk=b.FindNet('SPICLK')
r(b,spi,F,[(101.2,66.05),(101.2,61.0)]); v(b,spi,(101.2,61.0)); r(b,spi,B,[(101.2,61.0),(109.8,61.0),(109.8,80.0)]); v(b,spi,(109.8,80.0))
r(b,clk,F,[(100.8,66.05),(100.8,62.5),(111.0,62.5),(111.0,80.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
