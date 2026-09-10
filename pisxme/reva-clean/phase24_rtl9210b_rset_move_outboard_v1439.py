"""V1439: move the tiny RSET support footprint outboard and bypass the QFN field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RSET_MOVE_OUTBOARD_V1439.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); r=next(f for f in b.GetFootprints() if f.GetReference()=='R1'); r.SetPosition(r.GetPosition()+P(17,0))
n=b.FindNet('RSET'); assert n
tr(b,n,F,[(94.8,66.05),(96.0,66.05)]); via(b,n,(96.0,66.05)); tr(b,n,B,[(96.0,66.05),(102.0,66.05),(102.0,55.0)]); via(b,n,(102.0,55.0)); tr(b,n,F,[(102.0,55.0),(105.0,55.0),(105.0,65.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
