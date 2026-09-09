"""V886: add a deliberate local GND return for relocated support."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V882_RSET_ROUTE_CLEAN_V885.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V885_SUPPORT_GND_RETURN_V886.kicad_pcb'
F=pcbnew.F_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('GND')
tr(b,n,(89.2,62),(90,62));tr(b,n,(92.2,62),(90,62));tr(b,n,(89.2,65),(90,65));tr(b,n,(90,65),(90,62))
q=pcbnew.PCB_VIA(b);q.SetPosition(P(90,62));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
