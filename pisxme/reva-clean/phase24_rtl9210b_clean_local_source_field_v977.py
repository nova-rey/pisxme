"""V977: clean-field source-departure discriminator for the RTL island."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CLEAN_LOCAL_SOURCE_FIELD_V977.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
LOCAL={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
 if item.GetNetname() in LOCAL: b.RemoveNative(item)
routes=[('SPICS',[(98.8,66.05),(97.5,66.05),(97.5,64.5)]),('SPISO',[(99.2,66.05),(99.2,64.5),(98.5,63.5)]),('SPISO3',[(99.6,66.05),(99.6,65.0),(101.5,63.5)]),('SPICLK',[(100.8,66.05),(101.5,65.2)]),('SPISI',[(101.2,66.05),(102.5,66.05)]),('RTL_3V3',[(100.4,66.05),(100.4,65.6),(100.0,64.6)])]
for name,pts in routes:
 n=b.FindNet(name); tr(b,n,pts,F); via(b,n,pts[-1])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
