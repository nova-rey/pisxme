"""V672: move RSET copper to an interior lower corridor, retaining R1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V35_U2_LEFT_RAILS_5V_PLUS_3V3_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_RSET_INTERIOR_V672.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l)
 q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60))
 q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n)
 q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RSET')
for q in list(b.GetTracks()):
 if q.GetNetname()=='RSET': b.RemoveNative(q)
# U1.51 source to a west interior transition; return below the local field.
t(b,n,F,(94.05,73.2),(91.0,76.0)); v(b,n,(91.0,76.0))
t(b,n,B,(91.0,76.0),(91.0,80.0)); t(b,n,B,(91.0,80.0),(108.4,80.0)); v(b,n,(108.4,80.0))
t(b,n,F,(108.4,80.0),(108.4,81.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
