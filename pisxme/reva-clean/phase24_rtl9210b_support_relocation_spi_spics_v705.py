"""V705: SPICS F/B/F handoff around the retained rail fields."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_U117_V702.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_SPI_SPICS_V705.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPICS')
tr(b,n,F,(101.95,70.8),(102.2,70.8));vi(b,n,(102.2,70.8));tr(b,n,B,(102.2,70.8),(106.0,70.8));vi(b,n,(106.0,70.8));tr(b,n,F,(106.0,70.8),(106.0,57.0));tr(b,n,F,(106.0,57.0),(125.8,57.0));tr(b,n,F,(125.8,57.0),(125.8,58.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
