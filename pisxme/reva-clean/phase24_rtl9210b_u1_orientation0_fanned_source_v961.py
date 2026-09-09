"""V961: horizontal-first U1-0 SPI source fanout."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V942_U120_CLEANFIELD_V944.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U1_ORIENTATION0_FANNED_SOURCE_V961.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
LOCAL={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U1'); a=u.FindPadByNumber('69').GetPosition(); u.SetOrientationDegrees(0); q=u.FindPadByNumber('69').GetPosition(); u.SetPosition(u.GetPosition()+a-q); u2=b.FindFootprintByReference('U2'); u2.SetPosition(u2.GetPosition()+pcbnew.VECTOR2I_MM(20,20))
for item in list(b.GetTracks()):
 if item.GetNetname() in LOCAL: b.RemoveNative(item)
routes={'SPISO':[(101.95,71.2),(103.0,71.2),(109.0,69.0)],'SPISO3':[(101.95,71.6),(103.5,71.6),(108.0,70.0)],'SPICLK':[(101.95,72.8),(104.0,72.8),(107.0,75.0)],'SPISI':[(101.95,73.2),(104.5,73.2),(106.0,76.0)]}
for name,pts in routes.items():
 n=b.FindNet(name); tr(b,n,pts); via(b,n,pts[-1])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
