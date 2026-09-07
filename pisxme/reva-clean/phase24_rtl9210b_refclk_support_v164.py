"""V164: separated REFCLK source escapes and J1-side N launch."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_LOWER_1V1_HANDOFF_V160.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_V164.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=.2):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def remove_net(b,name):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
def main():
 b=pcbnew.LoadBoard(str(BASE)); remove_net(b,'XTAL_OUT')
 xt=b.FindNet('XTAL_OUT'); tr(b,xt,F,(95.6,73.95),(94.8,72.2));via(b,xt,(94.8,72.2));tr(b,xt,B,(94.8,72.2),(110.5,72.2));via(b,xt,(110.5,72.2));tr(b,xt,F,(110.5,72.2),(110.5,76.8));tr(b,xt,F,(110.5,76.8),(109.7,75.8));tr(b,xt,F,(109.7,75.8),(111.4,78.0))
 p,n=b.FindNet('REFCLK_P'),b.FindNet('REFCLK_N')
 tr(b,p,F,(98.4,73.95),(98.4,74.4));via(b,p,(98.4,74.4));tr(b,p,B,(98.4,74.4),(137.75,74.4));via(b,p,(137.75,74.4));tr(b,p,F,(137.75,74.4),(137.75,62.725));via(b,p,(137.75,62.725));tr(b,p,F,(137.75,62.725),(137.25,62.725))
 tr(b,n,F,(98.8,73.95),(98.8,73.3));via(b,n,(98.8,73.3));tr(b,n,B,(98.8,73.3),(136.75,73.3));via(b,n,(136.75,62.0));tr(b,n,F,(136.75,62.0),(136.75,62.725))
 # keep the N via transition directly under its connector pad; the vertical
 # J1 sideband field is therefore not entered.
 tr(b,n,B,(136.75,73.3),(136.75,62.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
