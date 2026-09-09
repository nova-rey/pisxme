"""V770: move the crystal GND stitch clear of C2.1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V760_SUPPORT_SIGNALS_V767.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V760_SUPPORT_GROUND_V770.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND')
t(b,n,F,(97.2,80.0),(97.2,80.8)); t(b,n,F,(97.2,80.8),(100.2,80.8)); t(b,n,F,(100.2,80.8),(100.2,80.0)); t(b,n,F,(97.2,80.8),(97.2,83.0)); v(b,n,(98.0,80.8)); t(b,n,B,(98.0,80.8),(98.0,82.5)); v(b,n,(98.0,82.5))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
