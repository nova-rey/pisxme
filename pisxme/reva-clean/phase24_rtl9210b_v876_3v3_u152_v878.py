"""V878: left-shift U1.52 RTL_3V3 escape clear of XTAL_IN."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V871_3V3_U134_V876.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V876_3V3_U152_V878.kicad_pcb'
F,L=pcbnew.F_Cu,pcbnew.In2_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,*ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
tr(b,n,F,(94.8,73.95),(93,73.95),(93,76));via(b,n,93,76);tr(b,n,L,(93,76),(93,68.4))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
