"""V176: co-author translated XTAL_OUT and move REFCLK-P left of XTAL_IN."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent; SRC=HERE/'PHASE24_RTL9210B_LOWER_1V1_HANDOFF_V160.kicad_pcb'; BASE=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V174.kicad_pcb'; OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V176.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=.13208
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=W):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def shift(q): return P(q.x/1e6,q.y/1e6-8.)
def copy_xtal_in(dst,src,n):
 for x in src.GetTracks():
  if x.GetNetname()!='XTAL_IN': continue
  pts=[x.GetPosition()] if type(x).__name__=='PCB_VIA' else [x.GetStart(),x.GetEnd()]
  if all(90<=p.x/1e6<=115 and 70<=p.y/1e6<=82 for p in pts):
   if type(x).__name__=='PCB_VIA':
    q=pcbnew.PCB_VIA(dst);q.SetPosition(shift(x.GetPosition()));q.SetWidth(x.GetWidth());q.SetDrill(x.GetDrill());q.SetLayerPair(F,B)
   else:
    q=pcbnew.PCB_TRACK(dst);q.SetStart(shift(x.GetStart()));q.SetEnd(shift(x.GetEnd()));q.SetLayer(x.GetLayer());q.SetWidth(x.GetWidth())
   q.SetNet(n);q.SetNetCode(n.GetNetCode());dst.Add(q)
def remove_net(b,name):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
def main():
 b=pcbnew.LoadBoard(str(BASE));src=pcbnew.LoadBoard(str(SRC));remove_net(b,'REFCLK_P');remove_net(b,'REFCLK_N')
 # Retain XTAL_IN's validated translated geometry; author XTAL_OUT locally.
 copy_xtal_in(b,src,b.FindNet('XTAL_IN'))
 xo=b.FindNet('XTAL_OUT');tr(b,xo,F,(95.6,65.95),(95.6,69.2));via(b,xo,(95.6,69.2));tr(b,xo,B,(95.6,69.2),(110.5,69.2));via(b,xo,(110.5,69.2));tr(b,xo,F,(110.5,69.2),(109.7,67.8));tr(b,xo,F,(109.7,67.8),(111.4,70.0))
 p,n=b.FindNet('REFCLK_P'),b.FindNet('REFCLK_N')
 tr(b,p,F,(98.4,65.95),(98.4,66.55));tr(b,p,F,(98.4,66.55),(98.2,66.8));tr(b,p,F,(98.2,66.8),(93.,67.5));via(b,p,(93.,67.5));tr(b,p,B,(93.,67.5),(93.,60.));tr(b,p,B,(93.,60.),(138.5,60.));via(b,p,(138.5,60.));tr(b,p,F,(138.5,60.),(137.25,62.725))
 tr(b,n,F,(98.8,65.95),(98.8,66.55));tr(b,n,F,(98.8,66.55),(99.,66.8));tr(b,n,F,(99.,66.8),(102.,67.5));via(b,n,(102.,67.5));tr(b,n,B,(102.,67.5),(102.,60.8));tr(b,n,B,(102.,60.8),(136.75,60.8));via(b,n,(136.75,60.8));tr(b,n,F,(136.75,60.8),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
