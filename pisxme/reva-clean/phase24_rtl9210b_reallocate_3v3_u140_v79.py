"""V79: reallocate the local RTL_3V3 escape to test U1.40 RTL_1V1."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_1V1_LEFT50_V75.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_REALLOCATE_3V3_U140_V79.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def key(x):
 a=x.GetStart(); z=x.GetEnd(); return {(round(a.x/1e6,3),round(a.y/1e6,3)),(round(z.x/1e6,3),round(z.y/1e6,3))}
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n3=b.FindNet('RTL_3V3'); n1=b.FindNet('RTL_1V1')
 remove=[{(93.0,65.2),(93.0,68.4)},{(94.8,66.05),(93.0,65.2)},{(93.0,68.4),(92.0,68.4)},{(93.0,68.4),(94.05,68.4)}]
 for x in list(b.GetTracks()):
  if x.GetNetCode()==n3.GetNetCode() and key(x) in remove: b.Remove(x)
 tr(b,n3,F,(94.05,68.4),(93.4,68.4));tr(b,n3,F,(93.4,68.4),(93.4,66.2));tr(b,n3,F,(93.4,66.2),(92.0,66.2));tr(b,n3,F,(92.0,66.2),(92.0,68.4))
 tr(b,n1,F,(94.05,68.8),(92.8,69.0));vi(b,n1,(92.8,69.0));tr(b,n1,B,(92.8,69.0),(92.8,72.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__': main()
