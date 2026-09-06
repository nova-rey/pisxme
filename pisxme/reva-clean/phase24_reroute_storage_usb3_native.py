"""Native-pad A* USB3 reroute for the proven storage island."""
from pathlib import Path
from heapq import heappush, heappop
import math, pcbnew
R=Path(__file__).resolve().parent
BASE=R/(__import__('os').environ.get('PISXME_USB3_BASE','PHASE24_MACRO_FRESH_STORAGE_LOCAL_CLEAR2.kicad_pcb'))
OUT=R/(__import__('os').environ.get('PISXME_USB3_OUT','PHASE24_STORAGE_LOCAL_CLEAR2_USB3_ASTAR.kicad_pcb'))
F,B=pcbnew.F_Cu,pcbnew.B_Cu; STEP=.25; W=.15; L=(F,B)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def gr(p): return round(p[0]/STEP),round(p[1]/STEP)
def pt(g): return g[0]*STEP,g[1]*STEP
def pad(b,r,n):
    p=b.FindFootprintByReference(r).FindPadByNumber(str(n))
    if p is None: raise RuntimeError(f'missing {r}.{n}')
    return p
def block(o,l,p,r=.2):
    x,y=gr(p); q=max(1,math.ceil(r/STEP))
    for i in range(-q,q+1):
        for j in range(-q,q+1): o[l].add((x+i,y+j))
def line(o,l,a,z,r=.2):
    ax,ay=gr(a);zx,zy=gr(z);n=max(abs(zx-ax),abs(zy-ay),1);q=max(1,math.ceil(r/STEP))
    for k in range(n+1):
        x=round(ax+(zx-ax)*k/n);y=round(ay+(zy-ay)*k/n)
        for i in range(-q,q+1):
            for j in range(-q,q+1):o[l].add((x+i,y+j))
def occ(b):
    o={F:set(),B:set()}
    for t in b.GetTracks():
        if 'CM5_USB3_' in t.GetNetname(): continue
        if isinstance(t,pcbnew.PCB_VIA):
            p=xy(t.GetPosition());block(o,F,p,.35);block(o,B,p,.35)
        else: line(o,t.GetLayer(),xy(t.GetStart()),xy(t.GetEnd()),.22)
    for f in b.GetFootprints():
        for p in f.Pads():
            s=p.GetSize();r=max(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y))/2+.3
            for l in [x for x in L if p.GetLayerSet().Contains(x)]:block(o,l,xy(p.GetPosition()),r)
    return o
def astar(o,a,z):
    qocc={F:set(o[F]),B:set(o[B])};s=(*gr(a),F);t=(*gr(z),F)
    for l,p in ((F,s),(F,t)):
        for i in range(-8,9):
            for j in range(-8,9):qocc[l].discard((p[0]+i,p[1]+j))
    q=[(0,s)];cost={s:0};prev={s:None}
    while q:
        _,c=heappop(q)
        if c==t:break
        x,y,l=c
        for nx,ny,nl in ((x+1,y,l),(x-1,y,l),(x,y+1,l),(x,y-1,l),(x,y,B if l==F else F)):
            if not (4<=nx<=1100 and 4<=ny<=715):continue
            if (nx,ny) in qocc[nl] and (nx,ny,nl)!=t:continue
            n=(nx,ny,nl);v=cost[c]+1+(28 if nl!=l else 0)
            if v<cost.get(n,10**12):cost[n]=v;prev[n]=c;heappush(q,(v+abs(nx-t[0])+abs(ny-t[1]),n))
    if t not in prev:raise RuntimeError(f'no route {a}->{z}')
    out=[];c=t
    while c is not None:out.append(c);c=prev[c]
    return out[::-1]
def via(b,n,p):
    v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
def emit(b,n,path,o):
    last=None
    for a,z in zip(path,path[1:]):
        if a[2]!=z[2]:p=pt(a[:2]);via(b,n,p);last=None;block(o,F,p,.38);block(o,B,p,.38);continue
        if last is None:last=pt(a[:2])
        e=pt(z[:2]);t=pcbnew.PCB_TRACK(b);t.SetStart(V(*last));t.SetEnd(V(*e));t.SetLayer(a[2]);t.SetWidth(pcbnew.FromMM(W));t.SetNet(n);b.Add(t);line(o,a[2],last,e,.22);last=e
b=pcbnew.LoadBoard(str(BASE))
jobs=[('CM5_USB3_RX_N','128','42'),('CM5_USB3_RX_P','130','43'),('CM5_USB3_TX_N','140','45'),('CM5_USB3_TX_P','142','46')]
# Normalize stale hierarchical aliases on the four J7 source pads to the
# canonical names in the repaired native export before emitting new copper.
for name,jp,_up in jobs:
    n=b.FindNet(name)
    if n is None: raise RuntimeError(f'missing native USB3 net {name}')
    b.FindFootprintByReference('J7').FindPadByNumber(jp).SetNet(n)
# Resolve native terminal coordinates before bulk track mutation; this avoids
# the KiCad 10 Python wrapper invalidating footprint proxies during mutation.
terminals=[(name,xy(pad(b,'J7',jp).GetPosition()),xy(pad(b,'U7',up).GetPosition())) for name,jp,up in jobs]
o=occ(b)
for t in list(b.GetTracks()):
    if 'CM5_USB3_' in t.GetNetname():b.Remove(t)
for name,a,z in terminals:
    n=b.FindNet(name);emit(b,n,astar(o,a,z),o);print(name,a,z)
b.Save(str(OUT));print(OUT)
