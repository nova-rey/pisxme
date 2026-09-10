"""V1423: XTAL_OUT upper escape around accepted rail geometry."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_RTL5V_U117_FCU_RIGHT_V1415.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALOUT_UPPER_ESCAPE_V1423.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('XTAL_OUT'); assert n
tr(b,n,F,[(94.05,67.6),(96.0,67.6)]); via(b,n,(96.0,67.6)); tr(b,n,B,[(96.0,67.6),(96.0,57.0),(89.0,57.0)]); via(b,n,(89.0,57.0)); tr(b,n,F,[(89.0,57.0),(89.4,59.0),(90.5,59.0),(90.5,60.5),(91.0,62.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
