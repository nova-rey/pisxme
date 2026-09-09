"""V783: disposable obstacle-aware F.Cu control routing from V777."""
from pathlib import Path
from heapq import heappush, heappop
import math
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_ABOVE_SPI_PLACEMENT_V777.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CONTROL_ASTAR_V783.kicad_pcb'
F=pcbnew.F_Cu; STEP=0.1; X0,X1=84.0,114.0; Y0,Y1=50.0,85.0
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return (p.x/1e6,p.y/1e6)
def dist_point_seg(px,py,ax,ay,bx,by):
    dx,dy=bx-ax,by-ay
    if dx==dy==0: return math.hypot(px-ax,py-ay)
    t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy)))
    return math.hypot(px-(ax+t*dx),py-(ay+t*dy))
def blocked(b,x,y,net):
    # Conservative electrical clearance for 0.15 mm control traces.
    rr=0.28
    for item in b.GetTracks():
        if item.GetLayer()!=F or item.GetNetname()==net: continue
        a=xy(item.GetStart()); z=xy(item.GetEnd())
        if dist_point_seg(x,y,*a,*z) < rr: return True
    for fp in b.GetFootprints():
        for pad in fp.Pads():
            if pad.GetNetname()==net: continue
            q=xy(pad.GetPosition()); sx,sy=xy(pad.GetSize())
            if abs(x-q[0]) <= sx/2+rr and abs(y-q[1]) <= sy/2+rr: return True
    return False
def node(p): return (round(p[0]/STEP),round(p[1]/STEP))
def coord(n): return (n[0]*STEP,n[1]*STEP)
def astar(b,start,goal,net,extra):
    s=node(start); g=node(goal); blocked_cache={}
    def bad(n):
        if n in blocked_cache: return blocked_cache[n]
        x,y=coord(n)
        v=not (X0<=x<=X1 and Y0<=y<=Y1) or blocked(b,x,y,net) or n in extra
        blocked_cache[n]=v; return v
    openq=[(0,s,None)]; came={}; cost={(s,None):0}; end=None
    while openq:
        _,cur,prev=heappop(openq); state=(cur,prev)
        if cur==g: end=state; break
        x,y=cur
        for nxt in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if bad(nxt): continue
            turn=0.25 if prev is not None and (cur[0]-prev[0],cur[1]-prev[1]) != (nxt[0]-cur[0],nxt[1]-cur[1]) else 0
            ns=(nxt,cur); nc=cost[state]+1+turn
            if nc < cost.get(ns,1e99):
                cost[ns]=nc; came[ns]=state
                h=abs(g[0]-nxt[0])+abs(g[1]-nxt[1])
                heappush(openq,(nc+h,nxt,cur))
    if end is None: raise RuntimeError('no route for '+net)
    path=[]
    while end in came: path.append(coord(end[0])); end=came[end]
    path.append(coord(end[0])); path.reverse(); return path
def add_path(b,n,start,end,path):
    pts=[start]+path[1:-1]+[end]
    # collapse collinear runs
    out=[pts[0]]
    for p in pts[1:]:
        if len(out)>=2:
            a,z=out[-2],out[-1]
            if (z[0]-a[0])*(p[1]-z[1])==(z[1]-a[1])*(p[0]-z[0]): out[-1]=p; continue
        out.append(p)
    for a,z in zip(out,out[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(F); q.SetWidth(pcbnew.FromMM(.15)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
    return out
b=pcbnew.LoadBoard(str(BASE)); extra=set()
for netname,start,end in [('PEDET',(101.95,70.4),(108,60)),('CLKREQ_N',(101.95,68.4),(108,63))]:
    n=b.FindNet(netname); path=astar(b,start,end,netname,extra); out=add_path(b,n,start,end,path)
    extra.update(node(p) for p in out)
    print(netname, len(out), out)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
