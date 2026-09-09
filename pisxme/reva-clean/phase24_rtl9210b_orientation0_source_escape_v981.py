"""V981: clean-field orientation-0 source-row discriminator."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ORIENTATION0_SOURCE_ESCAPE_V981.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U1'); anchor=u.FindPadByNumber('69').GetPosition(); u.SetOrientationDegrees(0); q=u.FindPadByNumber('69').GetPosition(); u.SetPosition(u.GetPosition()+anchor-q)
local={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
for item in list(b.GetTracks()):
 if item.GetNetname() in local: b.RemoveNative(item)
for name,y in [('SPISI',73.2),('SPICLK',72.8),('RTL_3V3',72.4),('SPISO3',71.6),('SPISO',71.2),('SPICS',70.8)]: tr(b,b.FindNet(name),(101.95,y),(104.0,y))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
