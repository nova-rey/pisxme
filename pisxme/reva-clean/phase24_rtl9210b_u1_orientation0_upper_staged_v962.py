"""V962: staged upper SPI source escape from the current U1-0 field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V942_U120_CLEANFIELD_V944.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U1_ORIENTATION0_UPPER_STAGED_V962.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
LOCAL={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U1'); a=u.FindPadByNumber('69').GetPosition(); u.SetOrientationDegrees(0); q=u.FindPadByNumber('69').GetPosition(); u.SetPosition(u.GetPosition()+a-q); u2=b.FindFootprintByReference('U2'); u2.SetPosition(u2.GetPosition()+pcbnew.VECTOR2I_MM(20,20))
for item in list(b.GetTracks()):
 if item.GetNetname() in LOCAL: b.RemoveNative(item)
n=b.FindNet('SPISO'); tr(b,n,F,[(101.95,71.2),(103.0,69.0)]); via(b,n,(103.0,69.0)); tr(b,n,B,[(103.0,69.0),(103.0,84.0)])
n=b.FindNet('SPISO3'); tr(b,n,F,[(101.95,71.6),(108.0,71.6),(108.0,70.0)]); via(b,n,(108.0,70.0)); tr(b,n,B,[(108.0,70.0),(108.0,84.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
