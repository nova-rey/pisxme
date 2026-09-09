"""V799: orientation-180 corridor ordering for PEDET/CLKREQ/PERST."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_PROBE_V712.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_CORRIDOR_ORDER_V799.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for ref,target in {'Y1':(105,60),'C1':(101,60),'C2':(108,60),'R1':(105,56)}.items():
 f=b.FindFootprintByReference(ref); q=f.FindPadByNumber('1').GetPosition(); f.SetPosition(f.GetPosition()+P(*target)-q)
n=b.FindNet('PEDET'); T(b,n,(98.4,66.05),(98.4,76.5)); T(b,n,(98.4,76.5),(89,76.5)); T(b,n,(89,76.5),(89,56))
n=b.FindNet('CLKREQ_N'); T(b,n,(96.4,66.05),(96.4,58)); T(b,n,(96.4,58),(92,58)); T(b,n,(92,58),(92,56))
n=b.FindNet('PERST_N'); T(b,n,(96,66.05),(96,57)); T(b,n,(96,57),(103,57)); T(b,n,(103,57),(103,48)); T(b,n,(103,48),(135,48)); T(b,n,(135,48),(135,69.5)); V(b,n,(135,69.5)); T(b,n,(135,69.5),(136,70.275))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
