"""V984: orientation-0 RTL/U2 logical-order SPI allocation."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ORIENTATION0_SOURCE_ESCAPE_V981.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ORIENTATION0_MONOTONIC_SPI_V984.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); u2=b.FindFootprintByReference('U2'); a=u2.FindPadByNumber('1').GetPosition(); u2.SetOrientationDegrees(0); q=u2.FindPadByNumber('1').GetPosition(); u2.SetPosition(u2.GetPosition()+a-q)
local={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
for item in list(b.GetTracks()):
 if item.GetNetname() in local: b.RemoveNative(item)
# Source row and U2 orientation-0 endpoint order are both SPICS, SPISO,
# SPISO3, SPICLK, SPISI.  Keep the transition ladder in that order.
data=[('SPICS',(101.95,70.8),(104.5,67.0),(104.6,78.0),(105.0,80.0)),('SPISO',(101.95,71.2),(105.7,68.2),(105.8,78.0),(106.2,80.0)),('SPISO3',(101.95,71.6),(109.3,69.4),(109.4,78.0),(109.8,80.0)),('SPICLK',(101.95,72.8),(110.5,70.6),(110.6,78.0),(111.0,80.0)),('SPISI',(101.95,73.2),(111.7,71.8),(111.8,78.0),(112.2,80.0))]
for name,src,v1,v2,end in data:
 n=b.FindNet(name); tr(b,n,[src,(104.0,src[1]),v1],F); via(b,n,v1); tr(b,n,[v1,(v1[0],78.0),(v2[0],78.0)],B); via(b,n,v2); tr(b,n,[v2,end],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
