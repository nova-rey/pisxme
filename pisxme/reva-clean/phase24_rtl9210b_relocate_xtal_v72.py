"""V72: regenerate relocated XTAL/RSET paths with U1.60 support join."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_XTAL_RELOC_DIAG_V71.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_XTAL_RELOCATED_V72.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT');nr=b.FindNet('RSET');nv=b.FindNet('RTL_1V1')
 # U1.60 to existing C4.1 right-side corridor.
 tr(b,nv,B,(112.5,74.8),(113.8,74.8))
 # XTAL_IN: left-side ordinary transition, upper B.Cu spine, new Y1 pad 1.
 tr(b,ni,F,(95.2,73.95),(94.4,72.5));vi(b,ni,(94.4,72.5));tr(b,ni,B,(94.4,72.5),(94.4,50.0));tr(b,ni,F,(94.4,50.0),(119.3,50.0))
 # XTAL_OUT uses a separate upper spine and reaches Y1 pad 2.
 tr(b,no,F,(95.6,73.95),(96.4,72.5));vi(b,no,(96.4,72.5));tr(b,no,B,(96.4,72.5),(96.4,48.0));tr(b,no,F,(96.4,48.0),(120.7,48.0));tr(b,no,F,(120.7,48.0),(120.7,50.0))
 # RSET uses the low perimeter, separated from both crystal spines.
 tr(b,nr,F,(94.05,73.2),(91.0,78.0));vi(b,nr,(91.0,78.0));tr(b,nr,B,(91.0,78.0),(91.0,44.0));tr(b,nr,B,(91.0,44.0),(121.5,44.0));vi(b,nr,(121.5,44.0));tr(b,nr,F,(121.5,44.0),(121.5,54.0));tr(b,nr,F,(121.5,54.0),(119.4,54.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
