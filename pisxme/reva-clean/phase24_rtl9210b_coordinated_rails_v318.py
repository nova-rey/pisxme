"""V318: coordinated RTL rail delivery on the designated In2 power layer."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_COORDINATED_RAILS_V318.kicad_pcb'
F=pcbnew.F_Cu; PWR=pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(p(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def rail(b,name,src,entry,branch,decap):
 n=b.FindNet(name);seg(b,n,F,src,entry);via(b,n,entry);seg(b,n,PWR,entry,branch);seg(b,n,PWR,branch,decap);via(b,n,decap);seg(b,n,F,decap,(decap[0]-1.6,decap[1]))
def main():
 b=pcbnew.LoadBoard(str(BASE))
 rail(b,'RTL_5V',(95.2,58.05),(93.0,58.05),(103.0,57.0),(118.0,61.0))
 rail(b,'RTL_1V1',(94.05,59.2),(92.8,59.2),(105.0,72.5),(106.8,53.0))
 rail(b,'RTL_3V3',(85.7,70.0),(84.0,72.0),(94.0,72.5),(96.4,65.95))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
