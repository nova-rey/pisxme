"""V107: disposable U1-to-J1 control-sideband escape trial."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U136_RIGHT_ESCAPE_V102.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_U1_J1_V107.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.15));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def path(b,n,src,mid,dst):
 tr(b,n,F,src,mid);via(b,n,mid);tr(b,n,B,mid,dst)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 path(b,b.FindNet('CLKREQ_N'),(101.95,68.4),(104.0,68.4),(136.5,68.4));tr(b,b.FindNet('CLKREQ_N'),F,(136.5,68.4),(136.5,70.275))
 path(b,b.FindNet('PERST_N'),(101.95,68.0),(104.0,68.0),(136.0,68.0));tr(b,b.FindNet('PERST_N'),F,(136.0,68.0),(136.0,70.275))
 path(b,b.FindNet('PEDET'),(101.95,70.4),(104.0,71.2),(140.75,71.2));tr(b,b.FindNet('PEDET'),F,(140.75,71.2),(140.75,62.725))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
