"""V763: separated F/B crystal shelves on the V761 support pocket."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_SUPPORT_PLACEMENT_V761.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_V763.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def ch(b,n,l,p):
 for a,z in zip(p,p[1:]): t(b,n,l,a,z)
b=pcbnew.LoadBoard(str(BASE))
n=b.FindNet('XTAL_IN'); ch(b,n,F,[(95.2,73.95),(95.0,74.4),(94.8,76.5)]); v(b,n,(94.8,76.5)); ch(b,n,B,[(94.8,76.5),(96.0,76.5)]); v(b,n,(96.0,76.5)); ch(b,n,F,[(96.0,76.5),(96.0,77.0),(96.0,80.0)])
n=b.FindNet('XTAL_OUT'); ch(b,n,F,[(95.6,73.95),(95.8,74.4),(96.0,75.5)]); v(b,n,(96.0,75.5)); ch(b,n,B,[(96.0,75.5),(97.4,75.5)]); v(b,n,(97.4,75.5)); ch(b,n,F,[(97.4,75.5),(97.4,77.0),(97.4,78.4),(99.0,80.0)])
n=b.FindNet('RSET'); ch(b,n,F,[(94.05,73.2),(93.4,74.0),(93.4,81.8),(96.0,83.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
