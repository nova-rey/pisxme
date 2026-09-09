"""V1304: migrate the complete crystal/RSET pocket on the V1279 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_CRYSTAL_POCKET_MIGRATE_V1304.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def route(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
 if q.GetNetname() in ('RSET','XTAL_IN','XTAL_OUT'): b.RemoveNative(q)
for ref in ('Y1','C1','C2','R1'):
 f=b.FindFootprintByReference(ref); f.SetPosition(f.GetPosition()+P(-20,-10))
nr,ni,no=(b.FindNet(x) for x in ('RSET','XTAL_IN','XTAL_OUT'))
route(b,nr,F,[(94.8,66.05),(92.0,66.05),(92.0,62.0)]); via(b,nr,(92.0,62.0)); route(b,nr,B,[(92.0,62.0),(68.0,62.0),(68.0,55.0)]); via(b,nr,(68.0,55.0)); route(b,nr,F,[(68.0,55.0),(68.0,55.0)])
route(b,ni,F,[(94.05,67.2),(93.4,67.2),(93.4,68.5)]); via(b,ni,(93.4,68.5)); route(b,ni,B,[(93.4,68.5),(60.0,68.5)]); via(b,ni,(60.0,68.5)); route(b,ni,F,[(60.0,68.5),(60.0,52.0),(58.0,52.0),(58.0,49.0)])
route(b,no,F,[(94.05,67.6),(94.5,67.6),(94.5,69.0)]); via(b,no,(94.5,69.0)); route(b,no,B,[(94.5,69.0),(61.0,69.0)]); via(b,no,(61.0,69.0)); route(b,no,F,[(61.0,69.0),(61.0,52.0),(61.0,49.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
