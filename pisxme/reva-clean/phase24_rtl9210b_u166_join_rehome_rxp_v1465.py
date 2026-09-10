"""V1465: separate the native RXP transition from RXN and repair its far join."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_U166_JOIN_REHOME_RXP_V1465.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
b=pcbnew.LoadBoard(str(BASE))
def n(s):
    q=b.FindNet(s); assert q is not None; return q
def p(x,y): return pcbnew.VECTOR2I_MM(x,y)
def rm(s):
    c=n(s).GetNetCode()
    for q in list(b.GetTracks()):
        if q.GetNetCode()==c: b.RemoveNative(q)
def seg(s,a,z,l):
    q=n(s); t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(s,xy):
    q=n(s); v=pcbnew.PCB_VIA(b); v.SetPosition(p(*xy)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
# U1.64 is LANE0_RXP at (94.05,71.60); U1.65 is RXN at (94.05,72.00).
# Keep the direct U1.66 GND-to-EP edge join, and send RXP to a distinct
# ordinary-via column, leaving the prior RXN source column untouched.
rm('LANE0_RXP')
seg('LANE0_RXP',(94.05,71.60),(91.80,71.60),F)
seg('LANE0_RXP',(91.80,71.60),(91.80,70.00),F)
via('LANE0_RXP',(91.80,70.00))
seg('LANE0_RXP',(91.80,70.00),(91.80,82.00),B)
via('LANE0_RXP',(91.80,82.00))
seg('LANE0_RXP',(91.80,82.00),(95.00,82.00),F)
via('LANE0_RXP',(95.00,82.00))
seg('GND',(94.05,72.40),(95.60,72.40),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
