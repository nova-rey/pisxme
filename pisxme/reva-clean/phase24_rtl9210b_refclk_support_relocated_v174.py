"""V174: clean translated support placement, with all superseded local copper scrubbed."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent; BASE=HERE/'PHASE24_RTL9210B_LOWER_1V1_HANDOFF_V160.kicad_pcb'; OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V174.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
DX,DY=0.,-8.; W=.13208
MOVED={'U1','U2','Y1','C1','C2','R1','R2','R3','C3','C4','C5'}
LOCAL={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','RESET_N','PERST_N','SPICS','SPISI','SPISO','SPISO3','SPICLK','REFCLK_P','REFCLK_N'}
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=W):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.6));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for x in list(b.GetTracks()):
  if x.GetNetname() in LOCAL:b.RemoveNative(x)
 for ref in MOVED:
  f=b.FindFootprintByReference(ref)
  if f:
   q=f.GetPosition();f.SetPosition(pcbnew.VECTOR2I(q.x+int(DX*1e6),q.y+int(DY*1e6)))
 p,n=b.FindNet('REFCLK_P'),b.FindNet('REFCLK_N')
 tr(b,p,F,(98.4,65.95),(98.4,66.55));tr(b,p,F,(98.4,66.55),(98.2,66.8));tr(b,p,F,(98.2,66.8),(95.,67.5));via(b,p,(95.,67.5));tr(b,p,B,(95.,67.5),(95.,60.));tr(b,p,B,(95.,60.),(138.5,60.));via(b,p,(138.5,60.));tr(b,p,F,(138.5,60.),(137.25,62.725))
 tr(b,n,F,(98.8,65.95),(98.8,66.55));tr(b,n,F,(98.8,66.55),(99.,66.8));tr(b,n,F,(99.,66.8),(102.,67.5));via(b,n,(102.,67.5));tr(b,n,B,(102.,67.5),(102.,60.8));tr(b,n,B,(102.,60.8),(136.75,60.8));via(b,n,(136.75,60.8));tr(b,n,F,(136.75,60.8),(136.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
