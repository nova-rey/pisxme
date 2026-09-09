"""V703: first native SPICS channel on the V702 support basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_U117_V702.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_SPI_SPICS_V703.kicad_pcb'
F=pcbnew.F_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPICS')
for a,z in zip([(101.95,70.8),(105.5,70.8),(105.5,57.0),(125.8,57.0),(125.8,58.0)],[(105.5,70.8),(105.5,57.0),(125.8,57.0),(125.8,58.0),(125.8,58.0)]):
 if a!=z: tr(b,n,a,z)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
