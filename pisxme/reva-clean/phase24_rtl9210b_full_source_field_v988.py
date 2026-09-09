"""V988: full adjacent RTL9210B source-field orthogonal discriminator."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_FULL_SOURCE_FIELD_V988.kicad_pcb'; F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); local={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
for item in list(b.GetTracks()):
 if item.GetNetname() in local: b.RemoveNative(item)
# Horizontal source row at y=66.05: orthogonal exits preserve pad identity and
# stop before any transition.  Adjacent row signals are spaced at the native
# QFN pitch; no synthetic connectivity is introduced.
routes={
 'RTL_1V1':[(98.4,66.05),(98.4,64.0)],
 'SPICS':[(98.8,66.05),(98.8,63.6)],
 'SPISO':[(99.2,66.05),(99.2,63.2)],
 'SPISO3':[(99.6,66.05),(99.6,62.8)],
 'RTL_3V3':[(100.4,66.05),(100.4,62.4)],
 'SPICLK':[(100.8,66.05),(100.8,62.0)],
 'SPISI':[(101.2,66.05),(101.2,61.6)],
 'RTL_5V':[(101.95,66.8),(103.8,66.8)],
}
for name,pts in routes.items(): tr(b,b.FindNet(name),pts)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
