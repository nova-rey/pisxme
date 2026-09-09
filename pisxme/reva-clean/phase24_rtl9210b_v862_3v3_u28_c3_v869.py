"""V869: lift the RTL_3V3 B.Cu jog above the PERST_N corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V860_5V_ADD_U133_V862.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V862_3V3_U28_C3_V869.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,*ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
via(b,n,107.3,71.6);tr(b,n,F,(105,71.6),(107.3,71.6));via(b,n,120.4,49.5)
tr(b,n,B,(107.3,71.6),(107.3,66),(111.5,66),(111.5,48),(120.4,48),(120.4,49.5))
tr(b,n,F,(120.4,49.5),(120.4,51))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
