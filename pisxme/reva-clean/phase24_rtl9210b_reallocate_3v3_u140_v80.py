"""V80: move the reallocated 3V3 vertical one more pad-field increment left."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_REALLOCATE_3V3_U140_V79.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_REALLOCATE_3V3_U140_V80.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def ends(x):
 a=x.GetStart();z=x.GetEnd();return {(round(a.x/1e6,3),round(a.y/1e6,3)),(round(z.x/1e6,3),round(z.y/1e6,3))}
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
 for x in list(b.GetTracks()):
  if x.GetNetCode()==n.GetNetCode() and ends(x) in [{(93.4,68.4),(93.4,66.2)},{(93.4,68.4),(92.0,66.2)}]: b.Remove(x)
 tr(b,n,F,(93.4,68.4),(93.0,68.4));tr(b,n,F,(93.0,68.4),(93.0,66.2));tr(b,n,F,(93.0,66.2),(92.0,66.2))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
