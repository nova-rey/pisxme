"""V116: disposable PEDET U1-to-M.2 contact 69 launch."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_UPPER_HOP_V115.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PEDET_J1_V116.kicad_pcb'
F=pcbnew.F_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(pcbnew.FromMM(.15));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PEDET')
 tr(b,n,(101.95,70.4),(104.0,70.4));tr(b,n,(104.0,70.4),(104.0,71.5));tr(b,n,(104.0,71.5),(140.75,71.5));tr(b,n,(140.75,71.5),(140.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
