"""V722: swap SPICS/SPISO vertical corridor assignments."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_SPICS_SPISO_V720.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_SPICS_SPISO_V722.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if q.GetNetname() in ('SPICS','SPISO'):b.RemoveNative(q)
n=b.FindNet('SPICS');path=[(94.05,69.2),(90.0,69.2),(90.0,46.0),(83.3,46.0),(83.3,50.0)]
for a,z in zip(path,path[1:]):tr(b,n,F,a,z)
n=b.FindNet('SPISO');tr(b,n,F,(94.05,68.8),(92.5,68.8));tr(b,n,F,(92.5,68.8),(92.5,64.0));vi(b,n,(92.5,64.0));tr(b,n,B,(92.5,64.0),(92.5,48.0));vi(b,n,(92.5,48.0));tr(b,n,F,(92.5,48.0),(84.5,48.0));tr(b,n,F,(84.5,48.0),(84.5,50.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
