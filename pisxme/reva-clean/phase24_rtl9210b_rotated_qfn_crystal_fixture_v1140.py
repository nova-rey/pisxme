"""V1140: isolated rotated-U1 crystal/RSET fixture using native pad transforms."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ROTATED_QFN_CRYSTAL_FIXTURE_V1140.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def pos(p): return (p.x/1e6,p.y/1e6)
def pad(board,ref,name):
    f=next(x for x in board.GetFootprints() if x.GetReference()==ref)
    return next(x for x in f.Pads() if x.GetPadName()==name)
def tr(board,net,points):
    for a,z in zip(points,points[1:]):
        q=pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F)
        q.SetWidth(W); q.SetNet(net); q.SetNetCode(net.GetNetCode()); board.Add(q)
source=pcbnew.LoadBoard(str(BASE))
# Preserve the source net codes, then recreate net ownership on the disposable board.
source_codes={n:source.FindNet(n).GetNetCode() for n in ('XTAL_IN','XTAL_OUT','RSET')}
# Build a genuinely isolated board from duplicated native footprints.
b=pcbnew.BOARD()
keep={'U1','Y1','C1','C2','R1'}
for f in source.GetFootprints():
    if f.GetReference() in keep: b.Add(f.Duplicate(False))
nets={n:pcbnew.NETINFO_ITEM(b,n) for n in ('XTAL_IN','XTAL_OUT','RSET','GND')}
for n in nets.values(): b.Add(n)
for f in b.GetFootprints():
    for p in f.Pads():
        if p.GetNetname() in nets: p.SetNet(nets[p.GetNetname()])
u=next(f for f in b.GetFootprints() if f.GetReference()=='U1')
u.SetOrientationDegrees(90)
def xy(ref,name): return pos(pad(b,ref,name).GetPosition())
ni,no,rs=(nets['XTAL_IN'],nets['XTAL_OUT'],nets['RSET'])
ui,uo,ur=xy('U1','53'),xy('U1','54'),xy('U1','51')
# Move support relative to the actual transformed U1 pads, not guessed origins.
targets={'Y1':(ui[0],ui[1]-15.0),'C1':(ui[0],ui[1]-12.0),'C2':(uo[0],uo[1]-12.0),'R1':(ur[0]-6.0,ur[1]-12.0)}
for ref,target in targets.items():
    f=next(f for f in b.GetFootprints() if f.GetReference()==ref)
    current=xy(ref,'1'); d=(target[0]-current[0],target[1]-current[1]); f.Move(P(*d))
ui,uo,ur=xy('U1','53'),xy('U1','54'),xy('U1','51')
yi,yo,c1,c2,r=xy('Y1','1'),xy('Y1','2'),xy('C1','1'),xy('C2','1'),xy('R1','1')
# Native-transformed endpoints are the only source of these route coordinates.
tr(b,ni,[ui,(ui[0],ui[1]-2.0),(yi[0],yi[1]+1.0),yi]); tr(b,ni,[yi,c1])
tr(b,no,[uo,(uo[0],uo[1]-2.0),(yo[0],yo[1]+1.0),yo]); tr(b,no,[yo,c2])
tr(b,rs,[ur,(ur[0]-2.0,ur[1]-1.0),(r[0]+1.0,r[1]),r])
b.Save(str(OUT))
print(OUT); print('U1',ui,uo,ur,'Y1',yi,yo,'C1',c1,'C2',c2,'R1',r)
