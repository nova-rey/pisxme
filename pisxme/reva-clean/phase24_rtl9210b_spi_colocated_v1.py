"""Disposable explicit SPI escape trial after U2 co-location."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_RELOCATION_U2_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SUPPORT_RELOCATION_SPI_V1.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def path(b,name,pts):
 n=b.FindNet(name)
 for a,z in zip(pts,pts[1:]):seg(b,n,a,z)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 # Routes are deliberately explicit and monotonic through the compact island.
 path(b,'SPICS',[(101.95,70.8),(104,70.8),(104,75),(110.8,75),(110.8,76)])
 path(b,'SPISO',[(101.95,71.2),(105,71.2),(105,74.5),(112,74.5),(112,76)])
 path(b,'SPISO3',[(101.95,71.6),(106,71.6),(106,73.5),(118,73.5),(118,76)])
 path(b,'SPICLK',[(101.95,72.8),(107,72.8),(107,75.5),(116.8,75.5),(116.8,76)])
 path(b,'SPISI',[(101.95,73.2),(108,73.2),(108,77),(115.6,77),(115.6,76)])
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
