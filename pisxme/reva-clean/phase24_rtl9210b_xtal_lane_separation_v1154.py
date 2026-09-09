"""V1154: clean source-field base with separated, native XTAL lanes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTALIN_SOURCE_ONLY_V1150.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_XTAL_LANE_SEPARATION_V1154.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return p.x/1e6,p.y/1e6
def pad(b,r,n): return next(p for f in b.GetFootprints() if f.GetReference()==r for p in f.Pads() if p.GetPadName()==n)
def tr(b,c,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNetCode(c); b.Add(q)
def via(b,c,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F,B); q.SetNetCode(c); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); co=b.FindNet('XTAL_OUT').GetNetCode(); ci=b.FindNet('XTAL_IN').GetNetCode()
old=[x for x in list(b.GetTracks()) if x.GetNetCode()==co or x.GetNetCode()==ci]; assert old
for x in old: b.Remove(x)
assert not [x for x in b.GetTracks() if x.GetNetCode() in (co,ci)]
uout=xy(pad(b,'U1','54').GetPosition()); uin=xy(pad(b,'U1','53').GetPosition())
# OUT lower B.Cu lane. Endpoints are native Y1.2 and C2.1 positions.
tr(b,co,F,[uout,(93.4,67.6),(91.5,67.6)]); via(b,co,(91.5,67.6))
tr(b,co,B,[(91.5,67.6),(86.0,68.0),(86.0,58.0)]); via(b,co,(86.0,58.0))
tr(b,co,F,[(86.0,58.0),(89.4,58.0),(89.4,59.0),(90.5,59.0),(90.5,60.5),(91.0,62.0)])
# IN exits to an outer B.Cu lane, avoiding the OUT diagonal and via field.
tr(b,ci,F,[uin,(93.0,67.2),(91.5,66.2),(90.5,66.2)]); via(b,ci,(90.5,66.2))
tr(b,ci,B,[(90.5,66.2),(93.0,66.2),(93.0,75.0),(84.8,75.0),(84.8,62.0)]); via(b,ci,(84.8,62.0))
tr(b,ci,F,[(84.8,62.0),(88.0,62.0),(88.0,59.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT,'removed',len(old),'U1.53',uin,'U1.54',uout)
