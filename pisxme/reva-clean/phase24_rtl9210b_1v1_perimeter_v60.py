"""V60: native-pad-derived RTL_1V1 perimeter collector candidate."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_3V3_RAIL_JOIN_V52.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_1V1_PERIMETER_V60.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
 # top/right/left edge escapes, with vias outside the QFN pad field
 branches=[((98.4,66.05),(98.4,52.0)),((101.95,67.2),(103.0,67.2)),
           ((94.05,67.2),(92.8,67.2)),((94.05,68.8),(92.8,68.8)),
           ((94.05,72.8),(92.8,72.8))]
 for a,z in branches: tr(b,n,F,a,z);vi(b,n,z)
 # bottom-edge pads exit below the XTAL_IN B.Cu band
 for x in (96.0,98.0,99.2): tr(b,n,F,(x,73.95),(x,76.0));vi(b,n,(x,76.0))
 # C4.1 enters from the right; its via remains clear of C3 and C4.2 GND.
 tr(b,n,F,(113.4,69.0),(113.8,69.0));vi(b,n,(113.8,69.0));tr(b,n,B,(113.8,69.0),(113.8,77.0));tr(b,n,B,(113.8,77.0),(108.5,77.0));tr(b,n,B,(108.5,77.0),(108.5,82.0))
 # perimeter collector at y82, then each via reaches it without crossing XTAL.
 for x,y in [(98.4,52.0),(103.0,67.2),(92.8,67.2),(92.8,68.8),(92.8,72.8),(96.0,76.0),(98.0,76.0),(99.2,76.0)]: tr(b,n,B,(x,y),(x,82.0))
 for x in (92.8,96.0,98.0,99.2,103.0): tr(b,n,B,(x,82.0),(108.5,82.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
