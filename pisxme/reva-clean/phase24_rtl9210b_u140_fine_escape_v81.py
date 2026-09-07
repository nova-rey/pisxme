"""V81: test a 0.15-mm pad-aware U1.40 RTL_1V1 escape on V79."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_REALLOCATE_3V3_U140_V79.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U140_FINE_ESCAPE_V81.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.15)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def ends(x):
 a=x.GetStart();z=x.GetEnd();return {(round(a.x/1e6,3),round(a.y/1e6,3)),(round(z.x/1e6,3),round(z.y/1e6,3))}
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
 tracks=list(b.GetTracks())
 for x in tracks:
  if x.GetNetCode()==n.GetNetCode() and ends(x) in [{(94.05,68.8),(92.8,69.0)},{(92.8,69.0),(92.8,72.8)}]: b.Remove(x)
 for v in tracks:
  if type(v).__name__=='PCB_VIA' and v.GetNetCode()==n.GetNetCode() and round(v.GetPosition().x/1e6,3)==92.8 and round(v.GetPosition().y/1e6,3)==69.0: b.Remove(v)
 tr(b,n,F,(94.05,68.8),(92.8,69.0));vi(b,n,(92.8,69.0));tr(b,n,B,(92.8,69.0),(92.8,72.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
