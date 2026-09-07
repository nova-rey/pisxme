"""Disposable far-transition SPI source escape for the V4 baseline."""
from pathlib import Path
import pcbnew
BASE=Path("PHASE24_RTL9210B_1V1_CRYSTAL_RSET_STAGED_V4.kicad_pcb")
OUT=Path("PHASE24_RTL9210B_V4_SPI_FAR_SOURCE_V1.kicad_pcb")
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def p(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(p(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def route(b,name,src,esc,spine,target):
 n=b.FindNet(name);s(b,n,F,src,esc);v(b,n,esc);s(b,n,B,esc,spine);s(b,n,B,spine,(target[0],spine[1]));v(b,n,(target[0],spine[1]));s(b,n,F,(target[0],spine[1]),target)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 route(b,"SPICS",(83.95,62.8),(88.0,62.8),(88.0,48.0),(125.8,58.0))
 route(b,"SPISO",(83.95,63.2),(88.5,63.2),(88.5,49.0),(127.0,58.0))
 route(b,"SPISO3",(83.95,63.6),(89.0,63.6),(89.0,50.0),(133.0,58.0))
 route(b,"SPICLK",(83.95,64.8),(89.5,64.8),(89.5,52.0),(131.8,58.0))
 n=b.FindNet("SPISI");s(b,n,F,(83.95,65.2),(90.0,65.2));v(b,n,(90.0,65.2));s(b,n,B,(90.0,65.2),(90.0,70.0));s(b,n,B,(90.0,70.0),(130.6,70.0));v(b,n,(130.6,70.0));s(b,n,F,(130.6,70.0),(130.6,58.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
