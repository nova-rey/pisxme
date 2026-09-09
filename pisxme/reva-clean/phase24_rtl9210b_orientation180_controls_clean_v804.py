"""V804: orientation-180 co-moved control fanout with separated PEDET shelf."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_PROBE_V712.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_CONTROLS_CLEAN_V804.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for ref,target in {'Y1':(105,60),'C1':(101,60),'C2':(108,60),'R1':(105,56),'R3':(103,54)}.items():
 f=b.FindFootprintByReference(ref); q=f.FindPadByNumber('1').GetPosition(); f.SetPosition(f.GetPosition()+P(*target)-q)
n=b.FindNet('PEDET'); T(b,n,F,(98.4,66.05),(98.4,52)); T(b,n,F,(98.4,52),(89,52)); T(b,n,F,(89,52),(89,56))
n=b.FindNet('CLKREQ_N'); T(b,n,F,(96.4,66.05),(96.4,58)); T(b,n,F,(96.4,58),(103,58)); T(b,n,F,(103,58),(103,54))
n=b.FindNet('PERST_N'); T(b,n,F,(96,66.05),(96,57)); V(b,n,(96,57)); T(b,n,B,(96,57),(96,46)); T(b,n,B,(96,46),(135,46)); T(b,n,B,(135,46),(135,69.5)); V(b,n,(135,69.5)); T(b,n,F,(135,69.5),(136,70.275))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
