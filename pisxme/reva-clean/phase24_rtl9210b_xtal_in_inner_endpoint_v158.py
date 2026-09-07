"""V158: move XTAL_IN transition inward, left of the XTAL_OUT span."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_MOVE_CLKREQ_J1_V156.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_XTAL_IN_INNER_ENDPOINT_V158.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return (round(p.x/1e6,3),round(p.y/1e6,3))
def tr(b,n,l,a,z,w=.2):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('XTAL_IN')
 remove={((107.5,75.0),(108.3,75.8)),((94.4,76.0),(107.5,75.0))}
 for x in list(b.GetTracks()):
  if x.GetNetname()=='XTAL_IN' and type(x).__name__=='PCB_TRACK':
   pair=(xy(x.GetStart()),xy(x.GetEnd()))
   if pair in remove or pair[::-1] in remove:b.RemoveNative(x)
 for x in list(b.GetTracks()):
  if x.GetNetname()=='XTAL_IN' and type(x).__name__=='PCB_VIA' and xy(x.GetPosition())==(107.5,75.0):b.RemoveNative(x)
 tr(b,n,B,(94.4,76.0),(105.5,75.0));via(b,n,(105.5,75.0));tr(b,n,F,(105.5,75.0),(108.3,75.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
