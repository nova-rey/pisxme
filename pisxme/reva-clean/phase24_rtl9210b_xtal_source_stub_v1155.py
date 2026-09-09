"""V1155: V1150 source-only proof with XTAL_IN stub above XTAL_OUT."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTALIN_SOURCE_ONLY_V1150.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_XTALIN_SOURCE_STUB_V1155.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def pad(b,r,n): return next(p for f in b.GetFootprints() if f.GetReference()==r for p in f.Pads() if p.GetPadName()==n)
def xy(p): return p.x/1e6,p.y/1e6
def tr(b,c,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNetCode(c); b.Add(q)
def via(b,c,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F,B); q.SetNetCode(c); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); ci=b.FindNet('XTAL_IN').GetNetCode()
old=[x for x in list(b.GetTracks()) if x.GetNetCode()==ci]; assert old
for x in old: b.Remove(x)
assert not [x for x in b.GetTracks() if x.GetNetCode()==ci]
u=xy(pad(b,'U1','53').GetPosition())
tr(b,ci,F,u,(93.0,67.2)); tr(b,ci,F,(93.0,67.2),(90.5,66.8)); via(b,ci,(90.5,66.8))
tr(b,ci,B,(90.5,66.8),(90.5,64.8))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT,'removed',len(old),'U1.53',u)
