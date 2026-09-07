"""Disposable SPI escape trial after 180-degree U1 rotation."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_ROTATE_U1_SPI_V1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 lanes=[('SPISI',(94.05,66.8),(89,66.8),50,115.6),('SPICLK',(94.05,67.2),(89,67.2),51,116.8),('SPISO3',(94.05,68.4),(89,68.4),52,118.0),('SPISO',(94.05,68.8),(89,68.8),53,112.0),('SPICS',(94.05,69.2),(89,69.2),54,110.8)]
 for name,src,esc,row,targetx in lanes:
  n=b.FindNet(name);seg(b,n,F,src,esc);via(b,n,esc);seg(b,n,B,esc,(esc[0],row));seg(b,n,B,(esc[0],row),(targetx,row));seg(b,n,B,(targetx,row),(targetx,74.5));via(b,n,(targetx,74.5));seg(b,n,F,(targetx,74.5),(targetx,76.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
