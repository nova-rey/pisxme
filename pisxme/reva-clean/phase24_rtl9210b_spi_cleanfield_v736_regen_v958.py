"""V958: restore the proven separated-shelf SPI escape from a clean field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V942_U120_CLEANFIELD_V944.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_SPI_CLEANFIELD_V736_REGEN_V958.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
LOCAL={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def vi(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname() in LOCAL: b.RemoveNative(item)
n=b.FindNet('SPICS');
for a,z in [((98.8,66.05),(98.8,63.5)),((104,63.5),(104,82.5)),((104,82.5),(105,82.5)),((105,82.5),(105,80))]: tr(b,n,F if a==(98.8,66.05) else B if a!=(105,82.5) else F,a,z)
vi(b,n,(98.8,63.5)); vi(b,n,(105,82.5))
n=b.FindNet('SPISO'); tr(b,n,F,(99.2,66.05),(99.2,64.5)); tr(b,n,F,(99.2,64.5),(102.5,64.5)); vi(b,n,(102.5,64.5)); tr(b,n,B,(102.5,64.5),(102.5,81.5)); tr(b,n,B,(102.5,81.5),(106.2,81.5)); vi(b,n,(106.2,81.5)); tr(b,n,F,(106.2,81.5),(106.2,78.8))
n=b.FindNet('SPISO3');
for a,z in zip([(99.6,66.05),(99.6,61.5),(112.2,61.5)],[(99.6,61.5),(112.2,61.5),(112.2,72.8)]): tr(b,n,F,a,z)
n=b.FindNet('SPICLK'); tr(b,n,F,(100.8,66.05),(100.8,64.5)); tr(b,n,F,(100.8,64.5),(104,60)); vi(b,n,(104,60)); tr(b,n,B,(104,60),(104.5,60)); tr(b,n,B,(104.5,60),(104.5,74)); vi(b,n,(104.5,74)); tr(b,n,F,(104.5,74),(105,74))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
