"""V673: add lower RTL_3V3 joins after the clean V672 RSET relocation."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_RSET_INTERIOR_V672.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_LOWER_3V3_V673.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l)
 q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60))
 q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n)
 q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
# Preserve the proven V35 endpoint ordering and use two separated returns.
t(b,n,F,(94.05,68.4),(92.8,67.8)); v(b,n,(92.8,67.8))
t(b,n,B,(92.8,67.8),(80.2,67.8)); v(b,n,(80.2,67.8)); t(b,n,F,(80.2,67.8),(80.2,80.0))
t(b,n,F,(94.8,73.95),(93.2,74.5)); v(b,n,(93.2,74.5))
t(b,n,B,(93.2,74.5),(74.2,74.5)); v(b,n,(74.2,74.5)); t(b,n,F,(74.2,74.5),(74.2,80.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
