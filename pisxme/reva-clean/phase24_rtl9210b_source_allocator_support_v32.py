"""V32: add native-pad XTAL/RSET support to the V31 SPI allocator."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SPI_SOURCE_ALLOCATOR_V31.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SPI_SOURCE_ALLOCATOR_SUPPORT_V32.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 # Each path leaves the native rotated U1 bottom/side pad outward before crossing.
 n=b.FindNet('XTAL_IN');t(b,n,(95.2,73.95),(95.2,76.0));t(b,n,(95.2,76.0),(104.3,76.0));t(b,n,(104.3,76.0),(104.3,72.8));t(b,n,(104.3,72.8),(105.6,75.0))
 n=b.FindNet('XTAL_OUT');t(b,n,(95.6,73.95),(95.6,77.0));t(b,n,(95.6,77.0),(105.7,77.0));t(b,n,(105.7,77.0),(105.7,72.8));t(b,n,(105.7,72.8),(107.4,75.0))
 n=b.FindNet('RSET');t(b,n,(94.05,73.2),(92.5,75.0));t(b,n,(92.5,75.0),(104.4,78.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
