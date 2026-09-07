"""V108: separate CLKREQ_N and PERST_N U1-to-J1 corridors."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U136_RIGHT_ESCAPE_V102.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_CLKREQ_PERST_V108.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.15));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def path(b,n,src,via_at,end):
 tr(b,n,F,src,via_at);via(b,n,via_at);tr(b,n,B,via_at,end);tr(b,n,F,end,(end[0],70.275))
def main():
 b=pcbnew.LoadBoard(str(BASE))
 path(b,b.FindNet('CLKREQ_N'),(101.95,68.4),(104.0,67.4),(136.5,67.4))
 path(b,b.FindNet('PERST_N'),(101.95,68.0),(105.0,68.8),(136.0,68.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
