"""V1164: rechannel XTAL_IN and U1.55 1V1 around existing support paths."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTAL_STAGGERED_V1160.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_1V1_XTAL_RECHANNEL_V1164.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,c,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNetCode(c); b.Add(q)
def via(b,c,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F,B); q.SetNetCode(c); b.Add(q)
def ep(x):
    if type(x).__name__=='PCB_VIA': return [(x.GetX()/1e6,x.GetY()/1e6)]
    a=x.GetStart(); z=x.GetEnd(); return [(a.x/1e6,a.y/1e6),(z.x/1e6,z.y/1e6)]
b=pcbnew.LoadBoard(str(BASE)); ni=b.FindNet('XTAL_IN').GetNetCode(); n1=b.FindNet('RTL_1V1').GetNetCode()
old=[x for x in list(b.GetTracks()) if x.GetNetCode()==ni]; assert old
for x in old: b.Remove(x)
tr(b,ni,F,[(94.05,67.2),(93.5,67.2),(93.0,67.5),(92.5,68.0)]); via(b,ni,(92.5,68.0)); tr(b,ni,B,[(92.5,68.0),(92.5,75.0),(84.5,75.0),(84.5,62.0)]); via(b,ni,(84.5,62.0)); tr(b,ni,F,[(84.5,62.0),(88.0,62.0),(88.0,59.0)])
tr(b,n1,F,[(94.05,68.0),(92.5,68.4),(91.8,69.0)]); via(b,n1,(91.8,69.0)); tr(b,n1,B,[(91.8,69.0),(96.5,69.0),(96.5,84.0),(126.0,84.0),(126.0,48.0)]); via(b,n1,(126.0,48.0)); tr(b,n1,F,[(126.0,48.0),(123.4,48.0),(123.4,51.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
