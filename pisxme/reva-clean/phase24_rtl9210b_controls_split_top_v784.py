"""V784: disposable separated mixed-layer control corridors with moved R2/R3."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_ABOVE_SPI_PLACEMENT_V777.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CONTROL_SPLIT_TOP_V784.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z,w=.15):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for ref,target in {'R2':(110,58),'R3':(111,62)}.items():
 f=b.FindFootprintByReference(ref); q=f.FindPadByNumber('1').GetPosition(); f.SetPosition(f.GetPosition()+P(*target)-q)
n=b.FindNet('PEDET'); T(b,n,F,(101.95,70.4),(102.8,70.4)); V(b,n,(102.8,70.4)); T(b,n,B,(102.8,70.4),(102.8,58)); T(b,n,B,(102.8,58),(110,58)); V(b,n,(110,58)); T(b,n,F,(110,58),(110,58))
n=b.FindNet('CLKREQ_N'); T(b,n,F,(101.95,68.4),(102.8,68.4)); V(b,n,(102.8,68.4)); T(b,n,B,(102.8,68.4),(102.8,56)); T(b,n,B,(102.8,56),(111,56)); V(b,n,(111,56)); T(b,n,F,(111,56),(111,62))
n=b.FindNet('RTL_3V3'); T(b,n,F,(111.2,58),(111.2,62))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
