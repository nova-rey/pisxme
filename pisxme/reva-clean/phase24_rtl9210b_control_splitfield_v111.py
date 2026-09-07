"""V111: split control transitions before the RTL_1V1/3V3 right field."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U136_RIGHT_ESCAPE_V102.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SPLITFIELD_V111.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.15));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def path(b,n,src,v,top,end):
 tr(b,n,F,src,v);via(b,n,v);tr(b,n,B,v,top);tr(b,n,B,top,end);tr(b,n,F,end,(end[0],70.275))
def main():
 b=pcbnew.LoadBoard(str(BASE))
 path(b,b.FindNet('CLKREQ_N'),(101.95,68.4),(106.0,68.4),(106.0,66.5),(136.5,66.5))
 path(b,b.FindNet('PERST_N'),(101.95,68.0),(105.0,68.0),(105.0,66.8),(136.0,66.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
