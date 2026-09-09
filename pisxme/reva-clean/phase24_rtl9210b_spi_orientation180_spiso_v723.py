"""V723: SPISO B.Cu endpoint approach with a short U2.2 dogbone."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_SPICS_V718.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_SPISO_V723.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPISO')
tr(b,n,F,(94.05,68.8),(91.5,68.8));tr(b,n,F,(91.5,68.8),(91.5,64.0));vi(b,n,(91.5,64.0));tr(b,n,B,(91.5,64.0),(91.5,51.0));tr(b,n,B,(91.5,51.0),(84.5,51.0));vi(b,n,(84.5,51.0));tr(b,n,F,(84.5,51.0),(84.5,50.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
