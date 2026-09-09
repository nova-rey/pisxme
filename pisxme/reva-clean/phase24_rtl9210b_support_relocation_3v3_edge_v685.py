"""V685: escape RTL_3V3 through the QFN outer pad-34 side."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_CRYSTAL_GND_V683.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_EDGE_V685.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
# Separate R2/R3 dogbones avoid the adjacent CLKREQ pad, then use an upper
# B.Cu collector and approach the outer U1.34 rail pad from the right.
t(b,n,F,(90.2,56),(90.2,55));v(b,n,(90.2,55))
t(b,n,F,(93.2,56),(93.2,55));v(b,n,(93.2,55))
t(b,n,B,(90.2,55),(103,55));v(b,n,(103,55));t(b,n,F,(103,55),(103,66.8));t(b,n,F,(103,66.8),(101.95,66.8))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
