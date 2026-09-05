"""Obstacle-aware clock passive fanout on the validated Phase 24 oracle."""
from pathlib import Path
from heapq import heappush, heappop
import math
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CLOCK_ASTAR_NEARWEST.kicad_pcb'
OUT=R/'PHASE24_SUPPORT_ASTAR.kicad_pcb'
STEP=.25

def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def seg(b,n,a,z):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.B_Cu)
    t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(n); b.Add(t)

def main():
    b=pcbnew.LoadBoard(str(BASE)); io=pcbnew.PCB_IO_KICAD_SEXPR()
    names={'XI':'/STORAGE/BRIDGE_XI','XO':'/STORAGE/BRIDGE_XO','VS':'/STORAGE/BRIDGE_VSSOSC'}
    nets={k:b.FindNet(v) for k,v in names.items()}
    libs={'R23':'R_0402_1005Metric','C42':'C_0402_1005Metric','C43':'C_0402_1005Metric'}
    maps={'R23':['XI','XO'],'C42':['XI','VS'],'C43':['XO','VS']}
    placements={'R23':(108,120),'C42':(102,120),'C43':(114,120)}
    fs={}
    for ref,pos in placements.items():
        f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),libs[ref]); f.SetReference(ref); f.SetPosition(V(*pos)); f.SetLayer(pcbnew.B_Cu); b.Add(f); fs[ref]=f
        for p,k in zip(f.Pads(),maps[ref]):
            p.SetNet(nets[k]); p.SetNetCode(nets[k].GetNetCode()); ls=pcbnew.LSET(); ls.AddLayer(pcbnew.B_Cu); p.SetLayerSet(ls)
    y=b.FindFootprintByReference('Y1')
    targets={'XI':xy(P(y,'1')),'XO':xy(P(y,'3')),'VS':xy(P(y,'2'))}
    # Build a conservative B.Cu obstacle grid. Same-net copper is passable;
    # every other-net pad/track is forbidden, with the two endpoints exempted.
    occ=set()
    def mark(ax,bx,ay,by):
        for gx in range(math.floor(ax/STEP),math.ceil(bx/STEP)+1):
            for gy in range(math.floor(ay/STEP),math.ceil(by/STEP)+1): occ.add((gx,gy))
    for t in b.GetTracks():
        if t.GetLayer()!=pcbnew.B_Cu: continue
        if t.GetNetCode() in {n.GetNetCode() for n in nets.values()}: continue
        bb=t.GetBoundingBox(); mark(pcbnew.ToMM(bb.GetX())-.18,pcbnew.ToMM(bb.GetRight())+.18,pcbnew.ToMM(bb.GetY())-.18,pcbnew.ToMM(bb.GetBottom())+.18)
    for f in b.GetFootprints():
        for p in f.Pads():
            if p.GetLayerSet().Contains(pcbnew.B_Cu) and p.GetNetCode() not in {n.GetNetCode() for n in nets.values()}:
                q=xy(p); s=p.GetSize(); mark(q[0]-pcbnew.ToMM(s.x)/2-.18,q[0]+pcbnew.ToMM(s.x)/2+.18,q[1]-pcbnew.ToMM(s.y)/2-.18,q[1]+pcbnew.ToMM(s.y)/2+.18)
    reserved=set()
    def cell(q): return (round(q[0]/STEP),round(q[1]/STEP))
    def route(a,z):
        st=cell(a); goal=cell(z); q=[(0,st)]; prev={st:None}; cost={st:0}
        while q:
            _,u=heappop(q)
            if u==goal: break
            for v in ((u[0]+1,u[1]),(u[0]-1,u[1]),(u[0],u[1]+1),(u[0],u[1]-1)):
                if not (360<=v[0]<=520 and 400<=v[1]<=600): continue
                if v!=goal and (v in occ or v in reserved): continue
                nc=cost[u]+1
                if nc<cost.get(v,10**9): cost[v]=nc; prev[v]=u; heappush(q,(nc+abs(v[0]-goal[0])+abs(v[1]-goal[1]),v))
        if goal not in prev: raise RuntimeError(f'no route {a}->{z}')
        path=[]; u=goal
        while u is not None: path.append(u); u=prev[u]
        return list(reversed(path))
    for ref,f in fs.items():
        for p,k in zip(f.Pads(),maps[ref]):
            a=xy(p); z=targets[k]; path=route(a,z); print(ref,p.GetNumber(),k,len(path))
            for u,v in zip(path,path[1:]):
                seg(b,nets[k],(u[0]*STEP,u[1]*STEP),(v[0]*STEP,v[1]*STEP)); reserved.add(v)
    b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
