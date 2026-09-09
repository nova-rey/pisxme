"""V1103: coordinated crystal/RSET support-cell relocation from V1092."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_RSET_V1092.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_SUPPORT_V1103.kicad_pcb'
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
# All three support cells move coherently by (+25,+20) mm; local pad geometry stays intact.
delta=P(25,20)
for ref in ('Y1','C1','C2','R1'):
 f=b.FindFootprintByReference(ref); f.SetPosition(f.GetPosition()+delta)
ni,no,nr=(b.FindNet(x) for x in ('XTAL_IN','XTAL_OUT','RSET'))
# QFN side escapes use staggered ordinary vias outside the pad field.
via(b,ni,(93.1,67.2)); tr(b,ni,B,[(93.1,67.2),(93.1,78.5),(113.0,78.5)]); via(b,ni,(113.0,78.5)); tr(b,ni,F,[(113.0,78.5),(113.0,79.0)])
tr(b,ni,B,[(113.0,78.5),(113.0,81.5)]); via(b,ni,(113.0,81.5)); tr(b,ni,F,[(113.0,81.5),(113.0,82.0)])
via(b,no,(92.3,67.6)); tr(b,no,B,[(92.3,67.6),(92.3,77.5),(114.4,77.5)]); via(b,no,(114.4,77.5)); tr(b,no,F,[(114.4,77.5),(114.4,79.0)])
tr(b,no,B,[(114.4,77.5),(116.0,77.5),(116.0,81.5)]); via(b,no,(116.0,81.5)); tr(b,no,F,[(116.0,81.5),(116.0,82.0)])
via(b,nr,(95.6,66.05)); tr(b,nr,B,[(95.6,66.05),(95.6,85.0),(113.0,85.0)]); via(b,nr,(113.0,85.0)); tr(b,nr,F,[(113.0,85.0),(113.0,85.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
