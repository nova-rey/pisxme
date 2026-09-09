"""V696: connect U1.33 RTL_5V to the local C5 load."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_LOAD_OUTER_V695.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_SOURCE_V696.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_5V')
t(b,n,F,(101.95,67.2),(103.5,67.2));t(b,n,F,(103.5,67.2),(103.5,52.0));v(b,n,(103.5,52.0));t(b,n,B,(103.5,52.0),(126.4,52.0));v(b,n,(126.4,52.0));t(b,n,F,(126.4,52.0),(126.4,51.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
