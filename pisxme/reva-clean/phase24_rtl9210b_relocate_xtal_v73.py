"""V73: regenerate relocated XTAL/RSET with post-transform native endpoints."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_XTAL_RELOC_DIAG_V71.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_XTAL_RELOCATED_V73.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT');nr=b.FindNet('RSET');nv=b.FindNet('RTL_1V1')
 # Finish the U1.60 diagnostic corridor into the existing C4.1 route.
 tr(b,nv,F,(98.0,73.95),(98.0,74.8));tr(b,nv,F,(98.0,74.8),(112.5,74.8));vi(b,nv,(112.5,74.8));tr(b,nv,B,(112.5,74.8),(113.8,74.8))
 # Endpoints are read from the saved V71 transform, not inferred from symbols.
 tr(b,ni,F,(95.2,73.95),(94.4,76.0));vi(b,ni,(94.4,76.0));tr(b,ni,B,(94.4,76.0),(113.0,76.0));vi(b,ni,(113.0,76.0));tr(b,ni,F,(113.0,76.0),(119.3,50.0))
 tr(b,no,F,(95.6,73.95),(96.4,77.0));vi(b,no,(96.4,77.0));tr(b,no,B,(96.4,77.0),(114.0,77.0));vi(b,no,(114.0,77.0));tr(b,no,F,(114.0,77.0),(120.7,50.0))
 tr(b,nr,F,(94.05,73.2),(91.0,78.0));vi(b,nr,(91.0,78.0));tr(b,nr,B,(91.0,78.0),(91.0,44.0));tr(b,nr,B,(91.0,44.0),(121.5,44.0));vi(b,nr,(121.5,44.0));tr(b,nr,F,(121.5,44.0),(121.5,54.0));tr(b,nr,F,(121.5,54.0),(119.4,54.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
