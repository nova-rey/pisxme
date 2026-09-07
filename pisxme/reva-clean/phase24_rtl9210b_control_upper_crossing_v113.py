"""V113: cross the inherited upper B.Cu rail only after F.Cu handoff."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U136_RIGHT_ESCAPE_V102.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_UPPER_CROSSING_V113.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.15));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));clk=b.FindNet('CLKREQ_N');per=b.FindNet('PERST_N')
 # CLKREQ: source-side F.Cu, clear the right-field verticals on B.Cu,
 # then return to F.Cu above the existing y=52 rail.
 tr(b,clk,F,(101.95,68.4),(109.0,68.4));via(b,clk,(109.0,68.4));tr(b,clk,B,(109.0,68.4),(109.0,59.5));tr(b,clk,B,(109.0,59.5),(112.0,59.5));tr(b,clk,B,(112.0,59.5),(112.0,53.5));via(b,clk,(112.0,53.5));tr(b,clk,F,(112.0,53.5),(137.5,53.5));tr(b,clk,F,(137.5,53.5),(137.5,70.275));tr(b,clk,F,(137.5,70.275),(136.5,70.275))
 # PERST: separate F.Cu corridor.
 tr(b,per,F,(101.95,68.0),(105.0,68.0));tr(b,per,F,(105.0,68.0),(105.0,67.8));tr(b,per,F,(105.0,67.8),(136.0,67.8));tr(b,per,F,(136.0,67.8),(136.0,70.275))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
