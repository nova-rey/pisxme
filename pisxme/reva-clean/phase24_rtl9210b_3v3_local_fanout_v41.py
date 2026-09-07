"""V41: add RTL_3V3 local source/U2 fanout without changing validated SPI."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CORRECT_RAIL_CAPS_V38.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_LOCAL_FANOUT_V41.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
 t(b,n,F,(94.8,66.05),(93.4,66.05));t(b,n,F,(93.4,66.05),(93.4,68.4));t(b,n,F,(93.4,68.4),(94.05,68.4))
 t(b,n,F,(94.05,68.4),(92.8,68.4));v(b,n,(92.8,68.4));t(b,n,B,(92.8,68.4),(92.8,74.8));t(b,n,B,(92.8,74.8),(94.8,74.8));v(b,n,(94.8,74.8));t(b,n,F,(94.8,74.8),(94.8,73.95))
 t(b,n,B,(92.8,74.8),(90.2,79.0));v(b,n,(90.2,79.0));t(b,n,F,(90.2,79.0),(90.2,80.0));t(b,n,F,(84.2,80.0),(84.2,81.0));v(b,n,(84.2,81.0));t(b,n,B,(84.2,81.0),(90.2,81.0));v(b,n,(90.2,81.0));t(b,n,F,(90.2,81.0),(90.2,80.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
