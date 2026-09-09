"""Minimal native DFM fixture for separated U1.39/U1.40 planar exits."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V661_LOWER_3V3_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_QFN_39_40_CLEAN_ESCAPE_FIXTURE_V666.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def setnet(p,n): p.SetNet(n); p.SetNetCode(n.GetNetCode())
def track(b,n,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(W); setnet(q,n); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
# Retain only the real U1 footprint and two existing local endpoint footprints.
keep={'U1','R2','R3'}
for f in list(b.GetFootprints()):
 if f.GetReference() not in keep: b.RemoveNative(f)
for q in list(b.GetTracks()): b.RemoveNative(q)
for z in list(b.Zones()): b.RemoveNative(z)
u=next(f for f in b.GetFootprints() if f.GetReference()=='U1')
r2=next(f for f in b.GetFootprints() if f.GetReference()=='R2')
r3=next(f for f in b.GetFootprints() if f.GetReference()=='R3')
# Blank unrelated U1 pad net ownership; retain only the two actual test pads.
n33=b.FindNet('RTL_3V3'); n11=b.FindNet('RTL_1V1')
for p in u.Pads(): p.SetNet(None); p.SetNetCode(0)
for f in (r2,r3):
 for p in f.Pads(): p.SetNet(None); p.SetNetCode(0)
# Move by pad-center delta; footprint anchors are not guaranteed to coincide
# with pad 1, so SetPosition(target) would not place the electrical endpoint.
for f, target in ((r2,(80,68.4)), (r3,(80,72.0))):
 f.SetOrientationDegrees(180)
 p=next(x for x in f.Pads() if str(x.GetNumber())=='1')
 f.Move(P(*target)-p.GetPosition())
u39=next(p for p in u.Pads() if str(p.GetNumber())=='39')
u40=next(p for p in u.Pads() if str(p.GetNumber())=='40')
r2p=next(p for p in r2.Pads() if str(p.GetNumber())=='1')
r3p=next(p for p in r3.Pads() if str(p.GetNumber())=='1')
setnet(u39,n33); setnet(r2p,n33); setnet(u40,n11); setnet(r3p,n11)
# Parallel source exits at exactly the production width/clearance contract.
track(b,n33,(94.05,68.4),(80,68.4))
track(b,n11,(94.05,68.8),(87.0,68.8)); track(b,n11,(87.0,68.8),(87.0,72.0)); track(b,n11,(87.0,72.0),(80,72.0))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
