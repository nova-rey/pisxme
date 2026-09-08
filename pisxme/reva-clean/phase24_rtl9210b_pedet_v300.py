"""V300: join the PEDET J1 branch to the corrected U1-side dogleg."""
from pathlib import Path
import pcbnew

HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_ROUTE_V299.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PEDET_ROUTE_V300.kicad_pcb'
F=pcbnew.F_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PEDET');tr(b,n,(109,64.5),(108,64.5));tr(b,n,(108,64.5),(108,62.4));b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
