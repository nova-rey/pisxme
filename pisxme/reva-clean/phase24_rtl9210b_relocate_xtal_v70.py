"""V70: coherent XTAL/RSET support relocation with U1.60 1V1 escape."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_1V1_TOP25_V63.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_XTAL_RELOCATED_V70.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 for q in list(b.GetTracks()):
  if q.GetNetname() in ('XTAL_IN','XTAL_OUT','RSET'): b.RemoveNative(q)
 # Keep the support components together, outboard of the former U1.60 field.
 for ref,pos in [('Y1',(116.0,82.0)),('C1',(114.0,82.0)),('C2',(118.0,82.0)),('R1',(116.0,85.0))]:
  b.FindFootprintByReference(ref).SetPosition(P(*pos))
 ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT');nr=b.FindNet('RSET');nv=b.FindNet('RTL_1V1')
 # U1.60 now takes the cleared F.Cu corridor and joins existing C4.1.
 tr(b,nv,F,(98.0,73.95),(98.0,74.8));tr(b,nv,F,(98.0,74.8),(112.5,74.8));vi(b,nv,(112.5,74.8));tr(b,nv,B,(112.5,74.8),(113.8,74.8))
 # Crystal paths use distinct B.Cu levels and ordinary transitions.
 tr(b,ni,F,(95.2,73.95),(95.2,75.5));tr(b,ni,F,(95.2,75.5),(94.4,76.0));vi(b,ni,(94.4,76.0));tr(b,ni,B,(94.4,76.0),(113.0,76.0));vi(b,ni,(113.0,76.0));tr(b,ni,F,(113.0,76.0),(115.3,82.0))
 tr(b,no,F,(95.6,73.95),(95.6,77.0));tr(b,no,F,(95.6,77.0),(96.4,77.0));vi(b,no,(96.4,77.0));tr(b,no,B,(96.4,77.0),(114.0,77.0));vi(b,no,(114.0,77.0));tr(b,no,F,(114.0,77.0),(116.7,82.0))
 # RSET drops below the crystal B.Cu paths before reaching the moved resistor.
 tr(b,nr,F,(94.05,73.2),(91.0,78.0));vi(b,nr,(91.0,78.0));tr(b,nr,B,(91.0,78.0),(91.0,80.0));tr(b,nr,B,(91.0,80.0),(114.5,80.0));vi(b,nr,(114.5,80.0));tr(b,nr,F,(114.5,80.0),(114.5,84.0));tr(b,nr,F,(114.5,84.0),(115.4,85.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
