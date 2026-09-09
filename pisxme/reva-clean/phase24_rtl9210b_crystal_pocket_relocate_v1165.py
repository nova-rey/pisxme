"""V1165: move the Y1/C1/C2 crystal pocket west and regenerate its nets."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTAL_STAGGERED_V1160.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CRYSTAL_POCKET_RELOCATED_V1165.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,c,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNetCode(c); b.Add(q)
def via(b,c,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F,B); q.SetNetCode(c); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); ni=b.FindNet('XTAL_IN').GetNetCode(); no=b.FindNet('XTAL_OUT').GetNetCode(); ng=b.FindNet('GND').GetNetCode()
old=[x for x in list(b.GetTracks()) if x.GetNetCode() in (ni,no)]; assert len(old)>=10
for x in old: b.Remove(x)
for ref in ('Y1','C1','C2'):
    f=next(f for f in b.GetFootprints() if f.GetReference()==ref); p=f.GetPosition(); f.SetPosition(P(p.x/1e6-10,p.y/1e6))
tr(b,ni,F,[(94.05,67.2),(93.5,67.2),(92.5,66.8)]); via(b,ni,(92.5,66.8)); tr(b,ni,B,[(92.5,66.8),(94.5,66.8),(94.5,75.0),(74.5,75.0),(74.5,62.0)]); via(b,ni,(74.5,62.0)); tr(b,ni,F,[(74.5,62.0),(78.0,62.0),(78.0,59.0)])
tr(b,no,F,[(94.05,67.6),(93.4,67.6),(91.5,67.6)]); via(b,no,(91.5,67.6)); tr(b,no,B,[(91.5,67.6),(80.0,68.0),(80.0,58.0)]); via(b,no,(80.0,58.0)); tr(b,no,F,[(80.0,58.0),(79.4,58.0),(79.4,59.0),(79.4,60.0),(81.0,60.0),(81.0,62.0)])
tr(b,ng,F,[(79.2,62.0),(79.2,63.5)]); via(b,ng,(79.2,63.5)); tr(b,ng,F,[(82.2,62.0),(82.2,63.5)]); via(b,ng,(82.2,63.5))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
