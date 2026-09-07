"""Outboard SPICLK plus SPISI F.Cu handoff for the 90-degree U1 field."""
from pathlib import Path
import pcbnew

HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_90_V15.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_ROTATE_U1_90_MIXED_V21.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 n=b.FindNet('SPISO3'); t(b,n,F,(99.6,66.05),(99.6,61.6));t(b,n,F,(99.6,61.6),(89,61.6));t(b,n,F,(89,61.6),(89,80))
 n=b.FindNet('SPICLK');t(b,n,F,(100.8,66.05),(100.8,63.5));t(b,n,F,(100.8,63.5),(98.8,63.5));v(b,n,(98.8,63.5));t(b,n,B,(98.8,63.5),(87.8,63.5));t(b,n,B,(87.8,63.5),(87.8,78));v(b,n,(87.8,78));t(b,n,F,(87.8,78),(87.8,80))
 n=b.FindNet('SPISI');t(b,n,F,(101.2,66.05),(101.8,64.8));v(b,n,(101.8,64.8));t(b,n,B,(101.8,64.8),(88.4,64.8));v(b,n,(88.4,64.8));t(b,n,F,(88.4,64.8),(86.6,64.8));t(b,n,F,(86.6,64.8),(86.6,80))
 n=b.FindNet('RTL_3V3');t(b,n,F,(100.4,66.05),(100.4,67.0));t(b,n,F,(100.4,67.0),(101.4,67.0));v(b,n,(101.4,67.0));t(b,n,B,(101.4,67.0),(101.4,60.8));t(b,n,B,(101.4,60.8),(110,60.8));t(b,n,B,(110,60.8),(110,68.5));v(b,n,(110,68.5));t(b,n,F,(110,68.5),(110.4,69))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
