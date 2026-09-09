"""V787: jog PEDET below the endpoint field and center CLKREQ_N between SPI vias."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_ABOVE_SPI_PLACEMENT_V777.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CONTROL_SEPARATED_MID_V787.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for ref,target in {'R2':(109.4,54),'R3':(111,62)}.items():
 f=b.FindFootprintByReference(ref); q=f.FindPadByNumber('1').GetPosition(); f.SetPosition(f.GetPosition()+P(*target)-q)
n=b.FindNet('PEDET'); T(b,n,F,(101.95,70.4),(102.8,70.4)); V(b,n,(102.8,70.4)); T(b,n,B,(102.8,70.4),(102.8,76.5)); T(b,n,B,(102.8,76.5),(108.8,76.5)); T(b,n,B,(108.8,76.5),(108.8,54)); V(b,n,(108.8,54)); T(b,n,F,(108.8,54),(109.4,54))
n=b.FindNet('CLKREQ_N'); T(b,n,F,(101.95,68.4),(105.25,68.4)); V(b,n,(105.25,68.4)); T(b,n,B,(105.25,68.4),(105.25,56)); T(b,n,B,(105.25,56),(110.2,56)); V(b,n,(110.2,56)); T(b,n,F,(110.2,56),(110.2,62)); T(b,n,F,(110.2,62),(111,62))
n=b.FindNet('RTL_3V3'); T(b,n,F,(110.6,54),(112.2,54)); T(b,n,F,(112.2,54),(112.2,62))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
