"""V166: final separated-source trial after V165 F.Cu pad-field failure."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent; BASE=HERE/'PHASE24_RTL9210B_LOWER_1V1_HANDOFF_V160.kicad_pcb'; OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_V166.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return (round(p.x/1e6,3),round(p.y/1e6,3))
def tr(b,n,l,a,z,w=.2):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def rem(b,net,layer,a,z):
 for x in list(b.GetTracks()):
  if x.GetNetname()==net and type(x).__name__=='PCB_TRACK' and x.GetLayer()==layer and (xy(x.GetStart()),xy(x.GetEnd())) in ((a,z),(z,a)): b.RemoveNative(x)
def rv(b,net,a):
 for x in list(b.GetTracks()):
  if x.GetNetname()==net and type(x).__name__=='PCB_VIA' and xy(x.GetPosition())==a:b.RemoveNative(x)
def main():
 b=pcbnew.LoadBoard(str(BASE)); one=b.FindNet('RTL_1V1')
 for l,a,z in [(B,(106.5,77.2),(112.,77.2)),(B,(112.,77.2),(112.,72.8)),(B,(103.,73.8),(107.,73.8)),(B,(94.8,73.8),(103.,73.8)),(B,(94.8,73.8),(94.8,69.5)),(F,(103.,72.8),(103.,73.8)),(F,(106.5,73.8),(107.,73.8)),(F,(112.,72.8),(103.,72.8))]: rem(b,'RTL_1V1',l,a,z)
 for a in ((112.,72.8),(103.,73.8)):rv(b,'RTL_1V1',a)
 tr(b,one,B,(112.,77.2),(112.,69.5))
 for x in list(b.GetTracks()):
  if x.GetNetname()=='XTAL_OUT':b.RemoveNative(x)
 xt=b.FindNet('XTAL_OUT');tr(b,xt,F,(95.6,73.95),(94.8,72.2));via(b,xt,(94.8,72.2));tr(b,xt,B,(94.8,72.2),(110.5,72.2));via(b,xt,(110.5,72.2));tr(b,xt,F,(110.5,72.2),(110.5,76.8));tr(b,xt,F,(110.5,76.8),(109.7,75.8));tr(b,xt,F,(109.7,75.8),(111.4,78.0))
 p,n=b.FindNet('REFCLK_P'),b.FindNet('REFCLK_N')
 tr(b,p,F,(98.4,73.95),(98.4,72.6));via(b,p,(98.4,72.6));tr(b,p,B,(98.4,72.6),(137.75,72.6));via(b,p,(137.75,72.6));tr(b,p,F,(137.75,72.6),(137.75,62.725));tr(b,p,F,(137.75,62.725),(137.25,62.725))
 tr(b,n,F,(98.8,73.95),(98.8,73.3));via(b,n,(98.8,73.3));tr(b,n,B,(98.8,73.3),(136.25,73.3));via(b,n,(136.25,62.0));tr(b,n,F,(136.25,62.0),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
