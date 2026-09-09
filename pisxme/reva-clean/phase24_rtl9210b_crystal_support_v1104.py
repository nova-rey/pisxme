"""V1104: separated left-side QFN crystal escapes and remote support cell."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_SUPPORT_V1104.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,pts):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if q.GetNetname() in ('XTAL_IN','XTAL_OUT','RSET'): b.RemoveNative(q)
d=P(35,30)
for ref in ('Y1','C1','C2','R1'): b.FindFootprintByReference(ref).SetPosition(b.FindFootprintByReference(ref).GetPosition()+d)
ni,no,nr=(b.FindNet(x) for x in ('XTAL_IN','XTAL_OUT','RSET'))
via(b,ni,(91.4,67.2)); tr(b,ni,B,[(91.4,67.2),(91.4,84.0),(123.0,84.0),(123.0,88.5)]); via(b,ni,(123.0,88.5)); tr(b,ni,F,[(123.0,88.5),(123.0,89.0)])
tr(b,ni,B,[(123.0,84.0),(123.0,91.5)]); via(b,ni,(123.0,91.5)); tr(b,ni,F,[(123.0,91.5),(123.0,92.0)])
via(b,no,(90.4,67.6)); tr(b,no,B,[(90.4,67.6),(90.4,86.0),(126.0,86.0),(126.0,88.5)]); via(b,no,(126.0,88.5)); tr(b,no,F,[(126.0,88.5),(126.0,89.0)])
tr(b,no,B,[(126.0,86.0),(126.0,91.5)]); via(b,no,(126.0,91.5)); tr(b,no,F,[(126.0,91.5),(126.0,92.0)])
via(b,nr,(97.0,66.05)); tr(b,nr,B,[(97.0,66.05),(97.0,97.0),(123.0,97.0)]); via(b,nr,(123.0,97.0)); tr(b,nr,F,[(123.0,97.0),(123.0,95.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
