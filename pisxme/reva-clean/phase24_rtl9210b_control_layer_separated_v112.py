"""V112: layer-separated CLKREQ upper detour plus F.Cu PERST corridor."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U136_RIGHT_ESCAPE_V102.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_LAYER_SEPARATED_V112.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.15));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));clk=b.FindNet('CLKREQ_N');per=b.FindNet('PERST_N')
 # CLKREQ: F.Cu launch, then upper B.Cu detour above the existing x113.8 field.
 tr(b,clk,F,(101.95,68.4),(106.0,68.4));via(b,clk,(106.0,68.4));tr(b,clk,B,(106.0,68.4),(106.0,66.5));tr(b,clk,B,(106.0,66.5),(112.0,66.5));tr(b,clk,B,(112.0,66.5),(112.0,50.5));tr(b,clk,B,(112.0,50.5),(136.5,50.5));via(b,clk,(136.5,50.5));tr(b,clk,F,(136.5,50.5),(136.5,70.275))
 # PERST remains a separate F.Cu monotonic corridor.
 tr(b,per,F,(101.95,68.0),(105.0,68.0));tr(b,per,F,(105.0,68.0),(105.0,67.8));tr(b,per,F,(105.0,67.8),(136.0,67.8));tr(b,per,F,(136.0,67.8),(136.0,70.275))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
