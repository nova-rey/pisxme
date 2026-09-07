"""V162: direct B.Cu 1V1 join plus co-authored REFCLK corridors."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_XTAL_IN_INNER_ENDPOINT_V158.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_V162.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return (round(p.x/1e6,3),round(p.y/1e6,3))
def tr(b,n,l,a,z,w=.2):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));one=b.FindNet('RTL_1V1')
 remove={((112.0,77.2),(112.0,73.8)),((112.0,73.8),(103.0,73.8)),((103.0,72.8),(103.0,73.8))}
 for x in list(b.GetTracks()):
  if x.GetNetname()=='RTL_1V1' and type(x).__name__=='PCB_TRACK':
   pair=(xy(x.GetStart()),xy(x.GetEnd()))
   if pair in remove or pair[::-1] in remove:b.RemoveNative(x)
 for x in list(b.GetTracks()):
  if x.GetNetname()=='RTL_1V1' and type(x).__name__=='PCB_VIA' and xy(x.GetPosition()) in ((112.0,73.8),(103.0,73.8),(112.0,72.8)):b.RemoveNative(x)
 tr(b,one,B,(112.0,77.2),(112.0,69.5))
 p=b.FindNet('REFCLK_P');n=b.FindNet('REFCLK_N')
 tr(b,p,F,(98.4,73.95),(98.4,74.4));tr(b,p,F,(98.4,74.4),(137.75,74.4));via(b,p,(137.75,74.4));tr(b,p,B,(137.75,74.4),(137.75,62.725));via(b,p,(137.75,62.725));tr(b,p,F,(137.75,62.725),(137.25,62.725))
 tr(b,n,F,(98.8,73.95),(98.8,75.0));via(b,n,(98.8,75.0));tr(b,n,B,(98.8,75.0),(104.5,73.5));via(b,n,(104.5,73.5));tr(b,n,F,(104.5,73.5),(136.25,73.5));via(b,n,(136.25,73.5));tr(b,n,B,(136.25,73.5),(136.25,62.0));via(b,n,(136.25,62.0));tr(b,n,F,(136.25,62.0),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
