"""V858: RTL_5V source-to-C5 power-plane probe on V857."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V772_PERST_STRAIGHT_RIGHT_V857.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V857_5V_RAIL_PROBE_V858.kicad_pcb'
F,B,L=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.30)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.70)); q.SetDrill(pcbnew.FromMM(.35)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_5V')
tr(b,n,F,[(101.95,66.8),(104.0,66.8)]); via(b,n,104.0,66.8)
via(b,n,126.4,50.0); tr(b,n,L,[(104.0,66.8),(126.4,50.0)])
tr(b,n,F,[(126.4,50.0),(126.4,51.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
