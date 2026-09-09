"""V797: reordered orientation-180 control fanout discriminator."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_PROBE_V712.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_REORDERED_V797.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
f=b.FindFootprintByReference('R2'); q=f.FindPadByNumber('1').GetPosition(); f.SetPosition(f.GetPosition()+P(87.8,54)-q)
n=b.FindNet('PEDET'); T(b,n,F,(98.4,66.05),(98.4,76.5)); T(b,n,F,(98.4,76.5),(87,76.5)); T(b,n,F,(87,76.5),(87,54)); T(b,n,F,(87,54),(87.8,54))
n=b.FindNet('CLKREQ_N'); T(b,n,F,(96.4,66.05),(96.4,58)); T(b,n,F,(96.4,58),(92,58)); T(b,n,F,(92,58),(92,56))
n=b.FindNet('PERST_N'); T(b,n,F,(96,66.05),(93,66.05)); T(b,n,F,(93,66.05),(93,48)); T(b,n,F,(93,48),(134,48)); T(b,n,F,(134,48),(134,69)); V(b,n,(134,69)); T(b,n,F,(134,69),(136,70.275))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
