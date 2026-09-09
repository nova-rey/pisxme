"""V697: route RTL_5V around the 1V1 B.Cu barrier."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_LOAD_OUTER_V695.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_OVERPASS_V697.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_5V')
t(b,n,F,(101.95,67.2),(104.0,67.2));t(b,n,F,(104.0,67.2),(104.0,52.0));v(b,n,(104.0,52.0));t(b,n,F,(104.0,52.0),(104.0,50.0));v(b,n,(104.0,50.0));t(b,n,F,(104.0,50.0),(106.0,50.0));v(b,n,(106.0,50.0));t(b,n,B,(106.0,50.0),(126.4,50.0));v(b,n,(126.4,50.0));t(b,n,F,(126.4,50.0),(126.4,51.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
