"""V864: outboard RTL_3V3 In2 spine with clear U2 transitions."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V860_5V_ADD_U133_V862.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V862_3V3_BRIDGE_SUPPORT_V864.kicad_pcb'
F,L=pcbnew.F_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
for a,z in [((105,71.6),(112,71.6)),((105,77.6),(112,77.6)),((121.2,75),(130,75)),((121.2,80),(130,80)),((120.4,51),(120.4,48))]:
 tr(b,n,F,a,z); via(b,n,*z)
for a,z in [((112,71.6),(130,71.6)),((130,71.6),(130,80)),((130,71.6),(120.4,48)),((112,77.6),(130,77.6)),((130,77.6),(130,80))]: tr(b,n,L,a,z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
