"""V718: add an ordinary local GND return for the north-flash SPICS basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_SPICS_V717.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_SPICS_V718.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('GND')
q=pcbnew.PCB_TRACK(b);q.SetStart(P(86.9,50));q.SetEnd(P(86.9,51.0));q.SetLayer(F);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
v=pcbnew.PCB_VIA(b);v.SetPosition(P(86.9,51));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
