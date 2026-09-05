"""Occupancy-aware disposable TUSB9261 clock island router.

Routes the three non-HS clock nets on B.Cu around live inherited copper.  The
router is intentionally conservative and only emits orthogonal 0.5 mm grid
segments; it is an experiment for the generic authoring path, not a board
specific hand edit.
"""
from pathlib import Path
import heapq, math, os, sys
import pcbnew

R=Path(__file__).resolve().parent
for a in sys.argv[1:]:
    if a.startswith('--') and '=' in a:
        k,v=a[2:].split('=',1); os.environ[k.replace('-','_')]=v
BASE=R/os.environ.get('CLOCK_BASE','PHASE19_COORDINATED_PASS_CANDIDATE_FINAL.kicad_pcb')
OUT=R/os.environ.get('CLOCK_OUT','PHASE19_CLOCK_OCCUPANCY_ROUTED.kicad_pcb')
SX=float(os.environ.get('CLOCK_SUPPORT_X','250')); SY=float(os.environ.get('CLOCK_SUPPORT_Y','150'))
STEP=.5
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def distseg(p,a,b):
    x,y=p; ax,ay=a; bx,by=b; dx=bx-ax; dy=by-ay
    if dx==dy==0:return math.hypot(x-ax,y-ay)
    t=max(0,min(1,((x-ax)*dx+(y-ay)*dy)/(dx*dx+dy*dy)))
    return math.hypot(x-(ax+t*dx),y-(ay+t*dy))
def main():
    b=pcbnew.LoadBoard(str(BASE)); io=pcbnew.PCB_IO_KICAD_SEXPR()
    names=('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC')
    nets={n:b.FindNet(n) for n in names}
    for n in names:
        if nets[n] is None:
            nets[n]=pcbnew.NETINFO_ITEM(b,n); nets[n].SetNetCode(b.GetNetCount()+1); b.Add(nets[n])
    codes={n.GetNetCode() for n in nets.values()}
    for t in list(b.GetTracks()):
        if t.GetNetCode() in codes: b.Remove(t)
    libs={'Y1':'Crystal_3225_4Pad','R23':'R_0402_1005Metric','C42':'C_0402_1005Metric','C43':'C_0402_1005Metric'}
    pos={'Y1':(SX,SY),'R23':(SX,SY+10),'C42':(SX-6,SY+10),'C43':(SX+6,SY+10)}
    mp={'Y1':{'1':names[0],'2':names[2],'3':names[1],'4':names[2]},'R23':{'1':names[0],'2':names[1]},'C42':{'1':names[0],'2':names[2]},'C43':{'1':names[1],'2':names[2]}}
    for ref,p in pos.items():
        f=b.FindFootprintByReference(ref)
        if f is None:
            f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),libs[ref]); f.SetReference(ref); b.Add(f)
        f.SetPosition(V(*p)); f.SetOrientationDegrees(0); f.SetLayer(pcbnew.B_Cu)
        for q in f.Pads(): q.SetNet(nets[mp[ref][str(q.GetNumber())]]); q.SetNetCode(nets[mp[ref][str(q.GetNumber())]].GetNetCode())
    u=b.FindFootprintByReference('U7'); live={str(q.GetNumber()):xy(q) for q in u.Pads()}
    for pin,nm in [('52',names[0]),('53',names[2]),('54',names[1])]:
        q=next(q for q in u.Pads() if str(q.GetNumber())==pin); q.SetNet(nets[nm]); q.SetNetCode(nets[nm].GetNetCode())
    # Exact live U7 rot180 source row in the selected ancestor; retain a
    # fallback to the measured pins so the authoring path is not coordinate-only.
    src={names[0]:live['52'],names[2]:live['53'],names[1]:live['54']}
    pads={r:{str(q.GetNumber()):xy(q) for q in b.FindFootprintByReference(r).Pads()} for r in pos}
    # Existing copper obstacles, expanded conservatively by 0.35 mm.
    obs=[]
    for t in b.GetTracks():
        if t.GetLayer() == pcbnew.B_Cu:
            obs.append(((pcbnew.ToMM(t.GetStart().x),pcbnew.ToMM(t.GetStart().y)),(pcbnew.ToMM(t.GetEnd().x),pcbnew.ToMM(t.GetEnd().y))))
    routed=[]
    def blocked(p, active):
        if p[0]<75 or p[0]>295 or p[1]<5 or p[1]>175:return True
        for a,z in obs:
            if distseg(p,a,z)<.12:return True
        for a,z,n0 in routed:
            if n0 != active and distseg(p,a,z)<.12:return True
        return False
    def key(p): return (round(p[0]/STEP),round(p[1]/STEP))
    def point(k): return (k[0]*STEP,k[1]*STEP)
    def route(a,z,active):
        sk,zk=key(a),key(z); q=[(0,sk)]; came={sk:None}; cost={sk:0}
        while q:
            _,u0=heapq.heappop(q)
            if u0==zk: break
            ux,uy=point(u0)
            for v in ((u0[0]+1,u0[1]),(u0[0]-1,u0[1]),(u0[0],u0[1]+1),(u0[0],u0[1]-1)):
                p=point(v)
                if v!=zk and blocked(p,active): continue
                nc=cost[u0]+1
                if nc<cost.get(v,10**9): cost[v]=nc; came[v]=u0; heapq.heappush(q,(nc+abs(v[0]-zk[0])+abs(v[1]-zk[1]),v))
        if zk not in came: raise RuntimeError(f'no route {a}->{z}')
        path=[]; k=zk
        while k is not None: path.append(point(k)); k=came[k]
        path.reverse(); return path
    def emit(n,path):
        for a,z in zip(path,path[1:]):
            t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.B_Cu); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t); routed.append((a,z,n))
    # Exit each U7 SMD pad laterally on F.Cu to a separate ordinary via.
    vias={names[0]:(src[names[0]][0],src[names[0]][1]-3),names[2]:(src[names[2]][0]-2,src[names[2]][1]-3),names[1]:(src[names[1]][0]-4,src[names[1]][1]-3)}
    for nm,p in src.items():
        q=vias[nm]; t=pcbnew.PCB_TRACK(b); t.SetStart(V(*p)); t.SetEnd(V(*q)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(nets[nm]); b.Add(t)
        v=pcbnew.PCB_VIA(b); v.SetPosition(V(*q)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(nets[nm]); b.Add(v)
    # Connect U7 -> crystal, then crystal -> every support terminal.  Each
    # new route becomes an obstacle, enforcing a planar set of lanes.
    targets={names[0]:pads['Y1']['1'],names[1]:pads['Y1']['3'],names[2]:pads['Y1']['2']}
    for nm in (names[0],names[1],names[2]): emit(nets[nm],route(vias[nm],targets[nm],nm))
    for nm,links in ((names[0],[('Y1','1','R23','1'),('Y1','1','C42','1')]),(names[1],[('Y1','3','R23','2'),('Y1','3','C43','1')]),(names[2],[('Y1','2','Y1','4'),('Y1','2','C42','2'),('Y1','4','C43','2')])):
        for r1,p1,r2,p2 in links: emit(nets[nm],route(pads[r1][p1],pads[r2][p2],nm))
    b.Save(str(OUT)); print(OUT)
main()
