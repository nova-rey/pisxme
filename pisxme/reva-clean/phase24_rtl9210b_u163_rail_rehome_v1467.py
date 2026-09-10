"""V1467: rehome the U1.63 RTL_1V1 departure on the V1466 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U166_JOIN_RXP_EAST_UP_V1466.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U163_RAIL_REHOME_V1467.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
b=pcbnew.LoadBoard(str(BASE))
def n(s):
 q=b.FindNet(s); assert q is not None; return q
def p(x,y): return pcbnew.VECTOR2I_MM(x,y)
def seg(s,a,z,l):
 q=n(s); t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(s,xy):
 q=n(s); v=pcbnew.PCB_VIA(b); v.SetPosition(p(*xy)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
# Remove only the stale local collector, preserving the remote RTL_1V1 rail.
rail=n('RTL_1V1').GetNetCode()
for item in list(b.GetTracks()):
 if item.GetNetCode()==rail and hasattr(item,'GetStart'):
  a=tuple(round(float(v)/1e6,3) for v in item.GetStart()); z=tuple(round(float(v)/1e6,3) for v in item.GetEnd())
  if {a,z}=={(94.05,70.0),(88.0,70.0)}: b.RemoveNative(item)
# U1.63 is natively at (94.05,71.20).  Exit west, transition at x=91.20,
# and join the existing B.Cu collector at the x=88 vertical rail.
seg('RTL_1V1',(94.05,71.20),(91.20,71.20),F)
seg('RTL_1V1',(91.20,71.20),(91.20,69.80),F)
via('RTL_1V1',(91.20,69.80))
seg('RTL_1V1',(91.20,69.80),(88.0,69.80),B)
seg('RTL_1V1',(88.0,69.80),(88.0,70.0),B)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
