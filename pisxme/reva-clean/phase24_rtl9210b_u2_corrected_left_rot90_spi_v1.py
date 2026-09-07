"""Disposable SPI route against the corrected, rotated U2 footprint."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U2_CORRECTED_LEFT_ROT90_PLACEMENT_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U2_CORRECTED_LEFT_ROT90_SPI_V1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 lanes=[('SPISO3',(94.05,68.4),(93.0,68.4),B,(86.0,73.0)),('SPICLK',(94.05,67.2),(92.4,67.2),F,(86.0,74.2)),('SPISI',(94.05,66.8),(91.8,66.8),B,(86.0,75.4)),('SPISO',(94.05,68.8),(90.8,68.8),F,(86.0,79.0)),('SPICS',(94.05,69.2),(89.8,69.2),B,(86.0,80.2))]
 for name,src,esc,layer,dst in lanes:
  n=b.FindNet(name);s(b,n,F,src,esc);v(b,n,esc);approach=(dst[0]+1.2,dst[1]);s(b,n,layer,esc,approach);v(b,n,approach);s(b,n,F,approach,dst)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
