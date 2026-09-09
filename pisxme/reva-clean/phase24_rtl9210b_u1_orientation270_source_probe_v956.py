"""V956: disposable U1-270 source-field probe from clean V944."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V942_U120_CLEANFIELD_V944.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U1_ORIENTATION270_SOURCE_V956.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
LOCAL={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U1'); anchor=u.FindPadByNumber('69').GetPosition(); u.SetOrientationDegrees(270); now=u.FindPadByNumber('69').GetPosition(); u.SetPosition(u.GetPosition()+anchor-now)
for item in list(b.GetTracks()):
    if item.GetNetname() in LOCAL: b.RemoveNative(item)
for name,src,esc in [('SPISI',(94.8,73.95),(94.8,77.0)),('SPICLK',(95.2,73.95),(95.2,78.0)),('SPISO3',(96.4,73.95),(96.4,79.0)),('SPISO',(96.8,73.95),(96.8,80.0))]:
    n=b.FindNet(name); tr(b,n,[src,esc]); via(b,n,esc)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
