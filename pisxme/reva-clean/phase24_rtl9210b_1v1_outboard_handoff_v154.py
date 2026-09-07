"""V154: move V151's RTL_1V1 handoff outboard of the REFCLK corridor."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RELOCATE_1V1_BELOW_XTAL_V151.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_1V1_OUTBOARD_HANDOFF_V154.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return (round(p.x/1e6,3),round(p.y/1e6,3))
def tr(b,n,l,a,z,w=.15):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
 remove={((106.5,77.2),(106.5,73.8)),((106.5,73.8),(103.0,73.8))}
 for x in list(b.GetTracks()):
  if x.GetNetname()=='RTL_1V1' and type(x).__name__=='PCB_TRACK':
   pair=(xy(x.GetStart()),xy(x.GetEnd()))
   if pair in remove or pair[::-1] in remove:b.RemoveNative(x)
 for x in list(b.GetTracks()):
  if x.GetNetname()=='RTL_1V1' and type(x).__name__=='PCB_VIA' and xy(x.GetPosition())==(106.5,77.2): b.RemoveNative(x)
 tr(b,n,B,(106.5,77.2),(112.0,77.2));via(b,n,(112.0,77.2));tr(b,n,B,(112.0,77.2),(112.0,73.8));via(b,n,(112.0,73.8));tr(b,n,F,(112.0,73.8),(103.0,73.8));via(b,n,(103.0,73.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
