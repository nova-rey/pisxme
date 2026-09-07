"""V165: remove superseded 1V1 bridge, then use F/B REFCLK corridors."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_LOWER_1V1_HANDOFF_V160.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_V165.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return (round(p.x/1e6,3),round(p.y/1e6,3))
def tr(b,n,l,a,z,w=.2):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def rem(b,net,layer,a,z):
 for x in list(b.GetTracks()):
  if x.GetNetname()!=net or type(x).__name__!='PCB_TRACK' or x.GetLayer()!=layer: continue
  if (xy(x.GetStart()),xy(x.GetEnd())) in ((a,z),(z,a)): b.RemoveNative(x)
def remvia(b,net,a):
 for x in list(b.GetTracks()):
  if x.GetNetname()==net and type(x).__name__=='PCB_VIA' and xy(x.GetPosition())==a:b.RemoveNative(x)
def main():
 b=pcbnew.LoadBoard(str(BASE)); one=b.FindNet('RTL_1V1')
 # The V160 direct B.Cu handoff already joins the lower U1 pad group to the
 # rail. Remove the older parallel bridge that occupied the REFCLK corridor.
 old=[(B,(106.5,77.2),(112.0,77.2)),(B,(112.0,77.2),(112.0,72.8)),
      (B,(103.0,73.8),(107.0,73.8)),(B,(94.8,73.8),(103.0,73.8)),
      (B,(94.8,73.8),(94.8,69.5)),(F,(103.0,72.8),(103.0,73.8)),
      (F,(106.5,73.8),(107.0,73.8)),(F,(112.0,72.8),(103.0,72.8))]
 for layer,a,z in old: rem(b,'RTL_1V1',layer,a,z)
 for a in ((112.0,72.8),(103.0,73.8)): remvia(b,'RTL_1V1',a)
 tr(b,one,B,(112.0,77.2),(112.0,69.5))
 # Re-author XTAL_OUT clear of the exposed pad and new REFCLK launch.
 for x in list(b.GetTracks()):
  if x.GetNetname()=='XTAL_OUT': b.RemoveNative(x)
 xt=b.FindNet('XTAL_OUT');tr(b,xt,F,(95.6,73.95),(94.8,72.2));via(b,xt,(94.8,72.2));tr(b,xt,B,(94.8,72.2),(110.5,72.2));via(b,xt,(110.5,72.2));tr(b,xt,F,(110.5,72.2),(110.5,76.8));tr(b,xt,F,(110.5,76.8),(109.7,75.8));tr(b,xt,F,(109.7,75.8),(111.4,78.0))
 p,n=b.FindNet('REFCLK_P'),b.FindNet('REFCLK_N')
 tr(b,p,F,(98.4,73.95),(98.4,74.4));tr(b,p,F,(98.4,74.4),(137.75,74.4));tr(b,p,F,(137.75,74.4),(137.75,62.725));tr(b,p,F,(137.75,62.725),(137.25,62.725))
 tr(b,n,F,(98.8,73.95),(98.8,73.3));via(b,n,(98.8,73.3));tr(b,n,B,(98.8,73.3),(136.75,73.3));via(b,n,(136.75,62.0));tr(b,n,F,(136.75,62.0),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
