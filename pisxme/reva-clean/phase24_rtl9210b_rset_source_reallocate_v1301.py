"""V1301: reallocate only the RSET source/corridor on the V1279 basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_RSET_SOURCE_REALLOCATE_V1301.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def route(b,n,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RSET')
for q in list(b.GetTracks()):
    if q.GetNetname()=='RSET': b.RemoveNative(q)
route(b,n,F,[(94.8,66.05),(93.2,66.05)]); via(b,n,(93.2,66.05))
route(b,n,B,[(93.2,66.05),(93.2,64.0),(88.0,64.0)]); via(b,n,(88.0,64.0))
route(b,n,F,[(88.0,64.0),(88.0,65.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
