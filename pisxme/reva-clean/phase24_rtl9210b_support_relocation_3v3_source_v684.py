"""V684: connect the RTL_3V3 pull-up source to U1.39."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_CRYSTAL_GND_V683.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_SOURCE_V684.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
t(b,n,F,(90.2,56),(93.2,56));t(b,n,F,(93.2,56),(94,54));v(b,n,(94,54));t(b,n,B,(94,54),(101,54));v(b,n,(101,54));t(b,n,F,(101,54),(101,66.05));t(b,n,F,(101,66.05),(99.6,66.05))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
