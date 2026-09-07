"""V110: keep CLKREQ_N/PERST_N on separated F.Cu corridors."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U136_RIGHT_ESCAPE_V102.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_FCU_MONOTONIC_V110.kicad_pcb'
F=pcbnew.F_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(pcbnew.FromMM(.15));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def path(b,n,points):
 for a,z in zip(points,points[1:]): tr(b,n,a,z)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 path(b,b.FindNet('CLKREQ_N'),[(101.95,68.4),(104.0,68.4),(104.0,67.2),(136.5,67.2),(136.5,70.275)])
 path(b,b.FindNet('PERST_N'),[(101.95,68.0),(105.0,68.0),(105.0,67.8),(136.0,67.8),(136.0,70.275)])
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
