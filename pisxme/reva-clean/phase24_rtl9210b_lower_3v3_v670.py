"""V670: bounded lower RTL_3V3 join on the clean V35 rail basis."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V35_U2_LEFT_RAILS_5V_PLUS_3V3_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_LOWER_3V3_V670.kicad_pcb'
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
# U1.39 to U2.8: upper-west transition, then an independent B.Cu channel.
t(b,n,F,(94.05,68.4),(93.2,67.4)); t(b,n,F,(93.2,67.4),(92.0,66.2)); v(b,n,(92.0,66.2))
t(b,n,B,(92.0,66.2),(82.0,66.2)); t(b,n,B,(82.0,66.2),(82.0,78.0)); v(b,n,(82.0,78.0))
t(b,n,F,(82.0,78.0),(80.2,78.0)); t(b,n,F,(80.2,78.0),(80.2,80.0))
# U1.52 to U2.3: east/lower source escape around the RSET field.
t(b,n,F,(94.8,73.95),(97.0,74.8)); t(b,n,F,(97.0,74.8),(97.0,78.8)); v(b,n,(97.0,78.8))
t(b,n,B,(97.0,78.8),(76.0,78.8)); v(b,n,(76.0,78.8)); t(b,n,F,(76.0,78.8),(74.2,78.8)); t(b,n,F,(74.2,78.8),(74.2,80.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
